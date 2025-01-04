# simulation.py

import numpy as np
import pandas as pd
import random

class EnergySimulation:
    def __init__(self, solar_data, wind_data, demand_data):
        self.solar_data = solar_data
        self.wind_data = wind_data
        self.demand_data = demand_data

    def simulate(self, num_days):
        results = []
        for day in range(num_days):
            solar_generation = self._simulate_solar_generation()
            wind_generation = self._simulate_wind_generation()
            demand = self._simulate_demand()
            results.append({
                'day': day,
                'solar_generation': solar_generation,
                'wind_generation': wind_generation,
                'demand': demand,
                'net_generation': solar_generation + wind_generation - demand
            })
        return pd.DataFrame(results)

    def _simulate_solar_generation(self):
        return random.uniform(0, max(self.solar_data))

    def _simulate_wind_generation(self):
        return random.uniform(0, max(self.wind_data))

    def _simulate_demand(self):
        return random.uniform(0, max(self.demand_data))

# Ejemplo de uso:
# solar_data = pd.read_csv('data/processed/solar_data.csv')
# wind_data = pd.read_csv('data/processed/wind_data.csv')
# demand_data = pd.read_csv('data/processed/demand_data.csv')
# simulation = EnergySimulation(solar_data['generation'].values, wind_data['generation'].values, demand_data['demand'].values)
# results = simulation.simulate(num_days=30)
# print(results)