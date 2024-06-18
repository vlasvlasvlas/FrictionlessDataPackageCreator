# Frictionless Data Package Creator

Este proyecto crea paquetes de datos de Frictionless a partir de múltiples archivos JSON de metadatos y archivos CSV de datos. Está diseñado para ser escalable y manejar múltiples conjuntos de datos, permitiendo añadir fácilmente nuevos archivos CSV y JSON de metadatos.

## Estructura del Proyecto

```plaintext
frictionless_data_project/
│
├── data/
│   ├── dataset1/
│   │   ├── data.csv
│   │   └── metadata.json
│   ├── dataset2/
│   │   ├── data.csv
│   │   └── metadata.json
│   └── ...
│
├── src/
│   ├── create_packages.py
│
├── .gitignore
├── .env.example
├── README.md
├── requirements.txt
└── setup.py
```

## Instrucciones

### Configuración del Entorno Virtual

Se recomienda utilizar un entorno virtual para gestionar las dependencias del proyecto. Para crear y activar un entorno virtual, sigue estos pasos:

1. Crea un entorno virtual:

   ```bash
   python -m venv env
   ```

2. Activa el entorno virtual:

   - En Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - En macOS y Linux:

     ```bash
     source env/bin/activate
     ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

### Uso de Variables de Entorno

Utiliza un archivo `.env` para gestionar las variables de entorno. Puedes copiar el archivo de ejemplo `.env.example` y renombrarlo a `.env`:

```bash
cp .env.example .env
```

### Ejecución del Script

1. Coloca tus archivos CSV y JSON de metadatos en subdirectorios dentro del directorio `data`.
   - Cada conjunto de datos debe tener su propio subdirectorio.
   - El archivo CSV debe llamarse `data.csv`.
   - El archivo JSON de metadatos debe llamarse `metadata.json`.

2. Ejecuta el script para crear los paquetes de datos:

   ```bash
   python src/create_packages.py
   ```

   Esto generará un archivo `datapackage.json` en cada subdirectorio del conjunto de datos.

## Ejemplo de Uso

1. Supón que tienes los siguientes archivos:

   ```plaintext
   data/
   ├── dataset1/
   │   ├── data.csv
   │   └── metadata.json
   ├── dataset2/
   │   ├── data.csv
   │   └── metadata.json
   ```

2. Ejecuta el script:

   ```bash
   python src/create_packages.py
   ```

3. Esto generará los archivos `datapackage.json` en cada subdirectorio:

   ```plaintext
   data/
   ├── dataset1/
   │   ├── data.csv
   │   ├── metadata.json
   │   └── datapackage.json
   ├── dataset2/
   │   ├── data.csv
   │   ├── metadata.json
   │   └── datapackage.json
   ```

## Configuración del Proyecto

El archivo `setup.py` está configurado para instalar el proyecto como un paquete de Python, si es necesario.

```python
from setuptools import setup, find_packages

setup(
    name='frictionless_data_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'frictionless',
    ],
    entry_points={
        'console_scripts': [
            'create-package=src.create_packages:main',
        ],
    },
)
```

## .gitignore

El archivo `.gitignore` está configurado para ignorar archivos generados y temporales.

```plaintext
__pycache__/
*.pyc
data/**/datapackage.json
.env
```

## .env.example

Proporciona un ejemplo de archivo `.env` para gestionar variables de entorno.

```plaintext
# Añade tus variables de entorno aquí
# Por ejemplo:
# DATABASE_URL=postgres://user:password@localhost:5432/mydatabase
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request en GitHub para discutir cualquier cambio que te gustaría realizar.

## Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT. Consulta el archivo LICENSE para más detalles.

---

Para más información sobre Frictionless Data, visita [este enlace](https://frictionlessdata.io/introduction/).

¡Gracias por usar Frictionless Data Package Creator! Si tienes alguna pregunta o problema, no dudes en abrir un issue en el repositorio de GitHub.
