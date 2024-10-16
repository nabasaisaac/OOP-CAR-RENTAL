from vehicle_class import Vehicle


class Truck(Vehicle):
    def __init__(self, color: str, has_trailer: bool=False):
        super().__init__(color)
        self.has_trailer = has_trailer

    def toString(self):
        return f'The car is {self.getColor()}\nHas trailer: {self.has_trailer}'


if __name__ == '__main__':
    # creating object of truck class
    truck = Truck('Blue', False)
    # printing the truck info
    truck_info = truck.toString()
    print(truck_info)