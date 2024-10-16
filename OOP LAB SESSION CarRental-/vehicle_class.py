"""
NAME: NABASA ISAAC
COURSE: BSCS
REG NO: M23B23/043
ACCESS NO: B22448
"""

# creating class vehicle
class Vehicle:
    def __init__(self, color: str):
        self.color = color

    # defining get color method
    def getColor(self):
        return self.color

    def toString(self):
        return f'The car is {self.getColor()}'


if __name__ == '__main__':
    # creating the vehicle object
    vehicle = Vehicle('red')
    # printing the vehicle color
    vehicle_color = vehicle.toString()
    print(vehicle_color)
