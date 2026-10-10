
* **Integrantes:** 
  * Tomás Restrepo Pulgarín
  * Eduardo Deossa Bohórquez
* **Asignatura:** Inteligencia de Negocios (BI) - Grupo 01
* **Institución:** Institución Universitaria Pascual Bravo

---


Para el monitoreo y análisis de telemetría de paneles solares fotovoltaicos. Incluye la ingesta de datos crudos (Bronze), procesamiento y limpieza en Python (Silver), modelado dimensional en PostgreSQL (Gold/DWH), y visualizaciones operativas y de negocio en Grafana y Power BI.

---



1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Tomixddxrt/solarbi-Restrepo-Deossa.git](https://github.com/Tomixddxrt/solarbi-Restrepo-Deossa.git)
   cd solarbi-Restrepo-Deossa

2. **Tabla de responsabilidades y entregables:**

| Integrante | Responsabilidades | Entregables en Repositorio |
| :--- | :--- | :--- |
| **Tomás Restrepo** | Configuración del repositorio, diseño de esquemas SQL (Silver/Gold), desarrollo del pipeline ETL en Python, automatización de la limpieza de datos y gestión de archivos de las capas Bronze y Silver. | • `sql/esquema.sql`<br>• `etl/run_etl.py`<br>• `etl/simulador.py`<br>• `data/bronze/telemetria.csv`<br>• `data/silver/telemetria_limpia.csv`<br>• `.gitignore` |
| **Eduardo Deossa** | Construcción del reporte ejecutivo interactivo en Power BI con métricas DAX, diseño e integración del tablero de monitoreo en Grafana y consolidación del informe técnico final en PDF. | • `powerbi/dashboard.pbix`<br>• `grafana/dashboard.json`<br>• `docs/Solar BI.pdf` |
