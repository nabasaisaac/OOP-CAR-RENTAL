class Customer:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
    # using dunder method __str__ to return customer information

    def __str__(self):
        return f'Customer Information: \nName: {self.name}\nAddress: {self.address}'


if __name__ == '__main__':
    # Creating customer class object
    customer1 = Customer('NABASA ISAAC', 'MUKONO')
    # Printing customer information
    print(customer1)

