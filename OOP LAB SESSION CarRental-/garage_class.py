class Garage:
    def __init__(self):
        self.vehicle = None

    def setVehicle(self, vehicle_parked):
        # this parks the vehicle in the garage
        self.vehicle = vehicle_parked
        return self.vehicle

    def toString(self):
        return f'Description of the parked vehicle: \n{self.vehicle.toString()}'

