def solar_generation(irradiance, panel_area, efficiency):
    return irradiance * panel_area * efficiency

def wind_generation(wind_speed, turbine_area, efficiency):
    return 0.5 * efficiency * turbine_area * (wind_speed ** 3)

class Battery:
    def __init__(self, capacity, efficiency):
        self.capacity = capacity
        self.efficiency = efficiency
        self.current_charge = 0

    def charge(self, energy):
        charge_amount = energy * self.efficiency
        if self.current_charge + charge_amount <= self.capacity:
            self.current_charge += charge_amount
        else:
            self.current_charge = self.capacity

    def discharge(self, energy):
        if self.current_charge >= energy:
            self.current_charge -= energy
            return energy
        else:
            discharged_energy = self.current_charge
            self.current_charge = 0
            return discharged_energy

    def get_current_charge(self):
        return self.current_charge