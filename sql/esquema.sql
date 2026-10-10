-- Creación de esquemas
CREATE SCHEMA IF NOT EXISTS silver;
CREATE SCHEMA IF NOT EXISTS dwh;

-- Tabla Silver (Lecturas cada 5 min)
CREATE TABLE IF NOT EXISTS silver.lectura_5min (
    ts TIMESTAMP PRIMARY KEY,
    dispositivo_id INT,
    p_ac_kw NUMERIC,
    irradiancia_wm2 NUMERIC,
    temp_modulo_c NUMERIC
);

-- Tabla DWH (Resumen de energía diaria)
CREATE TABLE IF NOT EXISTS dwh.fact_energia_dia (
    fecha DATE PRIMARY KEY,
    dispositivo_id INT,
    energia_kwh NUMERIC,
    pct_datos_validos NUMERIC
);