from vehicle_class import Vehicle


class Car(Vehicle):
    def __init__(self, color: str, is_winter_tires: bool = False):
        super().__init__(color)
        self.is_winter_tires = is_winter_tires

    def toString(self):
        return f'The car is {self.getColor()}\nHas winter tires: {self.is_winter_tires}'


if __name__ == '__main__':
    # Creating car object
    my_car = Car('red', True)

    # printing the car information
    car_info = my_car.toString()
    print(car_info)