# define class and object  class name must be start with capital letter
# use method and self to add brand and model in one line 
class Car:
     def __init__(self,brand,model):   # use self to access item from class like we use this is js
        self.brand = brand
        self.model = model
        
     def full_name(self):
         return f"{self.brand} {self.model}"
        # create new class and use parent class specification along with new class use inheritance 
class ElectricCar(Car):
    def __init__(self,battery_size,brand, model):
        super().__init__(brand ,model)
        self.battery_size = battery_size
    
# my_car = Car("Hyundai","Creta")  #my_car is obejct which indicate class car
electricCar = ElectricCar("Tesla","Model S1","95Kwh")  #my_car is obejct which indicate class car
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
print(electricCar.full_name())
