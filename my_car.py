from cars import Car, ElectricCar

my_gti = Car('volkswagen', 'gti', '2018')
print(my_gti.get_descriptive_name())

my_gti.odometer_reading = 16
my_gti.read_odometer()

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()

