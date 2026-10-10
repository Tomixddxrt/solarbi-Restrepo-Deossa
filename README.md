
* **Integrantes:** 
  * Tomás Restrepo Pulgarín
  * Eduardo Deossa Bohórquez
* **Asignatura:** Inteligencia de Negocios (BI) - Grupo 01
* **Institución:** Institución Universitaria Pascual Bravo

---

## Descripción del Trabajo
Este proyecto implementa una solución integral de Inteligencia de Negocios (Business Intelligence) basada en una arquitectura medallón (*Bronze, Silver y Gold*) para el análisis y monitoreo de un sistema fotovoltaico de energía solar:

1. *Capa Bronze:* Captura de datos crudos simulados de telemetría solar en intervalos de 5 minutos (data/bronze/telemetria.csv).
2. *Capa Silver:* Limpieza de datos automatizada, eliminación de nulos/duplicados, filtrado de rangos operacionales e ingesta en PostgreSQL (silver.lectura_5min).
3. *Capa Gold / DWH:* Agregación diaria de producción de energía (kWh) e indicadores de calidad de datos (dwh.fact_energia_dia).
4. *Visualización:* Tableros analíticos ejecutivos e interactivos en *Power BI* y *Grafana*.

---



1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Tomixddxrt/solarbi-Restrepo-Deossa.git](https://github.com/Tomixddxrt/solarbi-Restrepo-Deossa.git)
   cd solarbi-Restrepo-Deossa

2. **Requisitos Previos**
* Python 3.9 o superior instalado.
* PostgreSQL en ejecución local con una base de datos creada llamada solarbi.
* Power BI Desktop y Grafana instalados.

3. **Tabla de responsabilidades y entregables:**

| Integrante | Responsabilidades | Entregables en Repositorio |
| :--- | :--- | :--- |
| **Tomás Restrepo** | Configuración del repositorio, diseño de esquemas SQL (Silver/Gold), desarrollo del pipeline ETL en Python, automatización de la limpieza de datos y gestión de archivos de las capas Bronze y Silver. | • `sql/esquema.sql`<br>• `etl/run_etl.py`<br>• `etl/simulador.py`<br>• `data/bronze/telemetria.csv`<br>• `data/silver/telemetria_limpia.csv`<br>• `.gitignore` |
| **Eduardo Deossa** | Construcción del reporte ejecutivo interactivo en Power BI con métricas DAX, diseño e integración del tablero de monitoreo en Grafana y consolidación del informe técnico final en PDF. | • `powerbi/dashboard.pbix`<br>• `grafana/dashboard.json`<br>• `docs/Solar BI.pdf` |
