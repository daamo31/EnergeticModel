# Proyecto: Optimización y Simulación de un Sistema Energético Híbrido

## Objetivo del Proyecto
Diseñar un modelo para simular y optimizar un sistema energético híbrido (solar fotovoltaico, eólico y almacenamiento en baterías) para satisfacer la demanda de energía en una región específica, minimizando costos y emisiones de carbono.

## Estructura del Proyecto
El proyecto está organizado en los siguientes directorios y archivos:

- **data/**: Contiene los datos utilizados en el proyecto.
  - **raw/**: Datos crudos descargados de las APIs.
  - **processed/**: Datos procesados listos para el análisis y modelado.

- **notebooks/**: Cuadernos de Jupyter para análisis y modelado.
  - **data_analysis.ipynb**: Recolección y análisis de datos.
  - **modeling.ipynb**: Modelado matemático del sistema energético.
  - **optimization.ipynb**: Optimización del sistema energético.

- **src/**: Código fuente del proyecto.
  - **data_collection.py**: Funciones para conectarse a las APIs y descargar datos.
  - **data_processing.py**: Funciones para procesar y limpiar los datos.
  - **energy_modeling.py**: Implementación de las ecuaciones de generación y almacenamiento de energía.
  - **optimization.py**: Formulación y resolución del problema de optimización.
  - **simulation.py**: Modelado de diferentes escenarios de generación y consumo.
  - **visualization.py**: Funciones para crear visualizaciones interactivas y dashboards.

- **requirements.txt**: Lista de dependencias del proyecto.

- **README.md**: Documentación del proyecto.

- **.gitignore**: Archivos y directorios que deben ser ignorados por Git.

## Cómo Ejecutar el Proyecto
1. Clona el repositorio en tu máquina local.
2. Instala las dependencias listadas en `requirements.txt` utilizando pip.
3. Ejecuta los cuadernos de Jupyter en el orden indicado para realizar el análisis, modelado y optimización del sistema energético.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas colaborar, por favor abre un issue o un pull request.

## Licencia
Este proyecto está bajo la licencia MIT.