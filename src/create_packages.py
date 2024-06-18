import os
import json
from frictionless import Package, Resource, Schema, Field

def create_frictionless_package(csv_path, json_path, output_path):
    # Cargar el JSON de metadatos
    with open(json_path) as json_file:
        metadata = json.load(json_file)

    # Crear los campos del esquema a partir de los metadatos
    fields = []
    for column in metadata["Database"]["Columns"]:
        fields.append(Field(name=column["ColumnName"], type="string", description=column["Description"]))

    schema = Schema(fields=fields)

    # Crear el recurso (archivo CSV)
    resource = Resource(path=csv_path, schema=schema)

    # Crear el paquete de datos
    package = Package(resources=[resource])

    # Añadir metadatos adicionales si existen
    package.name = metadata.get("Database", {}).get("Name", "default_name")
    package.title = metadata.get("Database", {}).get("TableName", "default_title")
    package.description = "Paquete de datos generado a partir de archivos CSV y JSON de República Dominicana."

    # Guardar el paquete de datos en un archivo 'datapackage.json'
    package.to_json(output_path)
    print(f"Paquete de datos creado exitosamente y guardado en '{output_path}'.")

def main():
    base_dir = "data"
    for dataset_dir in os.listdir(base_dir):
        dataset_path = os.path.join(base_dir, dataset_dir)
        if os.path.isdir(dataset_path):
            csv_files = [f for f in os.listdir(dataset_path) if f.endswith('.csv')]
            json_files = [f for f in os.listdir(dataset_path) if f.endswith('.json')]
            for csv_file, json_file in zip(csv_files, json_files):
                csv_path = os.path.join(dataset_path, csv_file)
                json_path = os.path.join(dataset_path, json_file)
                output_path = os.path.join(dataset_path, 'datapackage.json')
                create_frictionless_package(csv_path, json_path, output_path)

if __name__ == "__main__":
    main()
