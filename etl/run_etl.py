import os
import pandas as pd
from sqlalchemy import create_engine, text

# Ajusta tu contraseña aquí si es diferente
DB_URI = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:03dejulio@localhost:5432/solarbi")

def run_pipeline():
    # 1. Generar archivo Bronze
    os.system("py etl/simulador.py")
    
    # 2. Limpieza de datos
    df_raw = pd.read_csv("data/bronze/telemetria.csv")
    total_leidas = len(df_raw)
    
    dup_count = df_raw.duplicated().sum()
    df = df_raw.drop_duplicates()
    
    df['p_ac_kw'] = pd.to_numeric(df['p_ac_kw'], errors='coerce')
    df['irradiancia_wm2'] = pd.to_numeric(df['irradiancia_wm2'], errors='coerce')
    null_count = df['p_ac_kw'].isna().sum() + df['irradiancia_wm2'].isna().sum()
    df = df.dropna(subset=['p_ac_kw', 'irradiancia_wm2'])
    
    range_count = ((df['p_ac_kw'] < 0) | (df['irradiancia_wm2'] < 0)).sum()
    df_clean = df[(df['p_ac_kw'] >= 0) & (df['irradiancia_wm2'] >= 0)].copy()
    
    total_validas = len(df_clean)
    pct_validos = round((total_validas / total_leidas) * 100, 2)
    
    print("=== REPORTE DE CALIDAD DE DATOS ===")
    print(f"Filas leídas: {total_leidas}")
    print(f"Rechazadas por duplicados: {dup_count}")
    print(f"Rechazadas por nulos/faltantes: {null_count}")
    print(f"Rechazadas por rango fuera de norma: {range_count}")
    print(f"Filas válidas: {total_validas}")
    print(f"Porcentaje de datos válidos: {pct_validos}%")
    
    # Energía por intervalo de 5 min
    df_clean['ts'] = pd.to_datetime(df_clean['ts'])
    df_clean['energia_intervalo_kwh'] = df_clean['p_ac_kw'] * (5.0 / 60.0)
    
    # Exportar datos limpios a la capa Silver (CSV)
    os.makedirs("data/silver", exist_ok=True)
    df_clean.to_csv("data/silver/telemetria_limpia.csv", index=False)
    print("✅ Archivo data/silver/telemetria_limpia.csv generado exitosamente.")
    
    # 3. Carga en PostgreSQL (Silver y Gold)
    engine = create_engine(DB_URI)
    
    query_silver = "INSERT INTO silver.lectura_5min (ts, dispositivo_id, p_ac_kw, irradiancia_wm2, temp_modulo_c, energia_intervalo_kwh) VALUES (:ts, :disp, :p_ac, :irr, :temp, :e_int) ON CONFLICT (ts) DO UPDATE SET p_ac_kw = EXCLUDED.p_ac_kw, irradiancia_wm2 = EXCLUDED.irradiancia_wm2, temp_modulo_c = EXCLUDED.temp_modulo_c, energia_intervalo_kwh = EXCLUDED.energia_intervalo_kwh;"
    
    with engine.begin() as conn:
        for _, row in df_clean.iterrows():
            conn.execute(text(query_silver), {
                'ts': row['ts'], 'disp': int(row['dispositivo_id']), 'p_ac': float(row['p_ac_kw']),
                'irr': float(row['irradiancia_wm2']), 'temp': float(row['temp_modulo_c']),
                'e_int': float(row['energia_intervalo_kwh'])
            })
            
    df_clean['fecha'] = df_clean['ts'].dt.date
    df_gold = df_clean.groupby(['fecha', 'dispositivo_id']).agg(
        energia_kwh=('energia_intervalo_kwh', 'sum')
    ).reset_index()
    df_gold['pct_datos_validos'] = pct_validos
    
    query_gold = "INSERT INTO dwh.fact_energia_dia (fecha, dispositivo_id, energia_kwh, pct_datos_validos) VALUES (:fecha, :disp, :e_kwh, :pct) ON CONFLICT (fecha, dispositivo_id) DO UPDATE SET energia_kwh = EXCLUDED.energia_kwh, pct_datos_validos = EXCLUDED.pct_datos_validos;"
    
    with engine.begin() as conn:
        for _, row in df_gold.iterrows():
            conn.execute(text(query_gold), {
                'fecha': row['fecha'], 'disp': int(row['dispositivo_id']),
                'e_kwh': float(row['energia_kwh']), 'pct': float(row['pct_datos_validos'])
            })
    print("Pipeline ETL completado exitosamente.")

if __name__ == "__main__":
    run_pipeline()