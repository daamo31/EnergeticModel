def process_raw_data(raw_data_path, processed_data_path):
    import pandas as pd
    import os

    # Cargar datos crudos
    raw_data_files = [f for f in os.listdir(raw_data_path) if f.endswith('.csv')]
    data_frames = []

    for file in raw_data_files:
        df = pd.read_csv(os.path.join(raw_data_path, file))
        data_frames.append(df)

    # Concatenar todos los DataFrames
    combined_data = pd.concat(data_frames, ignore_index=True)

    # Limpiar datos (ejemplo: eliminar filas con valores nulos)
    cleaned_data = combined_data.dropna()

    # Guardar datos procesados
    cleaned_data.to_csv(os.path.join(processed_data_path, 'processed_data.csv'), index=False)

def load_processed_data(processed_data_path):
    import pandas as pd

    # Cargar datos procesados
    return pd.read_csv(os.path.join(processed_data_path, 'processed_data.csv'))