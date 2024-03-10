class Car:

    count = 0

    def __init__(self, brand, color, cost, age):
        self.brand = brand
        self.color = color
        self.cost = cost
        self.__age = age
        self.add_auto()

    @classmethod
    def add_auto(cls):
        cls.count += 1

    @staticmethod
    def reserved(point):
        return point > 1

    def greet(self):
        print(f'For sale, {self.get_fullname()}!')

    def get_fullname(self):
        return f'{self.brand} {self.color} {self.cost}'

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age
        print(f'A new age has been set! {self.get_fullname()}')

    def __str__(self):
        return self.get_fullname()


class ElectricCar(Car):
    def __init__(self, brand, color, cost, age, battery):
        super().__init__(brand, color, cost, age)
        self.battery = battery
        self.add_auto()

    def greet(self):
        print(f'Electric car: For sale, {self.get_fullname()}!')


ec1 = ElectricCar('BMW', 'Grey', 85000, 1, 71)
ec2 = ElectricCar('Tesla', 'Grey', 140000, 2, 80)
ec3 = ElectricCar('Nissan', 'Grey', 38000, 4, 50)

ec2.greet()
print(ec1.battery)

auto_1 = Car('BMW', 'Black', 75000, 10)
auto_2 = Car('WV', 'White', 15000, 15)
auto_3 = Car('Kia', 'Red', 35000, 5)

print(Car.reserved(1))
auto_1.greet()
print(auto_1.get_age())
auto_1.set_age(13)
print(auto_1.get_age())
print(ec3.__dict__)
print(ec1.get_age())
ec1.set_age(5)
print(ec1.get_age())
print(Car.count)