# incapsulation 
# define class and object  class name must be start with capital letter
# use method and self to add brand and model in one line 
class Car:
    def __init__(self,brand,model):   # use self to access item from class like we use this is js
        self.__brand = brand
        self.model = model
        
        # use encapsulation for get brand private it can be used by calling __brand it make private 
    def get_brand(self):
         return self.__brand + " !"
        
    def full_name(self):
         return f"{self.__brand} {self.model}"
        # create new class and use parent class specification along with new class use inheritance 
     
    #  polymorphism is one work with differnt type like car have work on fuel but different types diesel petrol electricity 
    def fuel_type(self):
         return "Diesel or Petrol"
     
     

class ElectricCar(Car):
    def __init__(self,battery_size,brand, model):
        super().__init__(brand ,model)
        self.battery_size = battery_size
        
    def fuel_type(self):
         return "Electric Charge"
    
my_car = Car("Hyundai","Creta")  #my_car is obejct which indicate class car
my_tesla = ElectricCar("Tesla","Model S1","95Kwh")  #my_car is obejct which indicate class car
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
# print(my_tesla.full_name())
# print(my_tesla.get_brand())
print(my_tesla.fuel_type())
print(my_car.fuel_type())
