import pandas as pd
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_file(file_path):
    try:
        print(f"Procesando archivo: {file_path}")
        df = pd.read_csv(file_path, on_bad_lines='skip', delimiter=';')
        # Filtrar los datos de Aragón
        df_aragon = df[df['CCAA'].str.contains('Aragón', case=False, na=False)]
        return df_aragon
    except Exception as e:
        print(f"Error al procesar el archivo {file_path}: {e}")
        return None

def process_raw_data(raw_data_path, processed_data_path):
    # Cargar datos crudos
    raw_data_files = [os.path.join(raw_data_path, f) for f in os.listdir(raw_data_path) if f.endswith('.csv')]
    data_frames = []

    print("Procesando archivos...")

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(process_file, file): file for file in raw_data_files}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Procesando archivos", unit="archivo"):
            result = future.result()
            if result is not None:
                data_frames.append(result)

    # Concatenar todos los DataFrames
    try:
        combined_data = pd.concat(data_frames, ignore_index=True)
    except Exception as e:
        print(f"Error al concatenar los DataFrames: {e}")
        return

    # Limpiar datos (ejemplo: eliminar filas con valores nulos)
    cleaned_data = combined_data.dropna()

    # Guardar datos procesados
    try:
        cleaned_data.to_csv(os.path.join(processed_data_path, 'processed_data.csv'), index=False)
        print(f'Datos procesados guardados en {os.path.join(processed_data_path, "processed_data.csv")}')
    except Exception as e:
        print(f"Error al guardar los datos procesados: {e}")

def load_processed_data(processed_data_path):
    # Cargar datos procesados
    return pd.read_csv(os.path.join(processed_data_path, 'processed_data.csv'))

def main():
    raw_data_path = os.path.join('..', 'data', 'raw')
    processed_data_path = os.path.join('..', 'data', 'processed')
    os.makedirs(processed_data_path, exist_ok=True)
    
    process_raw_data(raw_data_path, processed_data_path)

if __name__ == '__main__':
    main()