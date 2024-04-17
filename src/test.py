class Vehicle():
    def __init__(self, name=None, color=None, mpg=None):
        self.name = name
        self.color = color
        self.mpg = mpg

    def __repr__(self):
        return f'This car is {self.name}, the color is {self.color} and the mpg is {self.mpg}'

class Truck(Vehicle):
    def __init__(self, name=None, color=None, mpg=None, bed_lenght=None):
        self.bed_length = bed_lenght
        super().__init__(name, color, mpg)
    
    def print_bed_length(self):
        return f'The bed length of this truck is {self.bed_length}sqft and color {self.color}'
