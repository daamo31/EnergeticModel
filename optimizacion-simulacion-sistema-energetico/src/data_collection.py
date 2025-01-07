import requests
import pandas as pd
import os

def download_solar_data(api_url, output_path):
    response = requests.get(api_url)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print(f'Datos solares descargados y guardados en {output_path}')
    else:
        print('Error al descargar datos solares:', response.status_code)

def download_wind_data(api_url, output_path):
    response = requests.get(api_url)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print(f'Datos eólicos descargados y guardados en {output_path}')
    else:
        print('Error al descargar datos eólicos:', response.status_code)

def download_energy_demand_data(api_url, output_path):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        # Procesar los datos JSON y convertirlos en un DataFrame
        records = data['included'][0]['attributes']['values']
        df = pd.DataFrame(records)
        # Guardar el DataFrame en un archivo CSV
        df.to_csv(output_path, index=False)
        print(f'Datos de demanda energética descargados y guardados en {output_path}')
    else:
        print('Error al descargar datos de demanda energética:', response.status_code)

def load_energy_demand_data(file_path):
    return pd.read_csv(file_path)

def main():
    solar_api_url = 'https://power.larc.nasa.gov/api/temporal/hourly/point?start=20100101&end=20221231&latitude=41.66&longitude=-0.88&community=re&parameters=ALLSKY_SFC_SW_DWN&format=json&user=EnergeticHIbrid&header=true&time-standard=lst'
    wind_api_url = 'https://power.larc.nasa.gov/api/temporal/hourly/point?start=20220101&end=20221231&latitude=41.66&longitude=-0.88&community=re&parameters=WS2M&format=json&user=EnergeticHIbrid&header=true&time-standard=lst'
    demand_api_url = "https://apidatos.ree.es/es/datos/demanda/ire-general?start_date=2023-01-01T00:00&end_date=2024-01-01T23:59&time_trunc=day"

    raw_data_dir = os.path.join('..', 'data', 'raw')
    os.makedirs(raw_data_dir, exist_ok=True)

    download_solar_data(solar_api_url, os.path.join(raw_data_dir, 'solar_data.csv'))
    download_wind_data(wind_api_url, os.path.join(raw_data_dir, 'wind_data.csv'))
    download_energy_demand_data(demand_api_url, os.path.join(raw_data_dir, 'demand_data.csv'))

if __name__ == '__main__':
    main()