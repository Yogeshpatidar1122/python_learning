# add a class variable to car that keeps track of created car 
# incapsulation 
# define class and object  class name must be start with capital letter
# use method and self to add brand and model in one line 
class Car:
    total_car = 0
    def __init__(self,brand,model):   # use self to access item from class like we use this is js
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
        
        # use encapsulation for get brand private it can be used by calling __brand it make private 
    def get_brand(self):
         return self.__brand + " !"
        
    def full_name(self):
         return f"{self.__brand} {self.__model}"
        # create new class and use parent class specification along with new class use inheritance 
     
    #  polymorphism is one work with differnt type like car have work on fuel but different types diesel petrol electricity 
    def fuel_type(self):
         return "Diesel or Petrol"
     
    # staticmethod are decorator which is used for that method are accesed by only class or not by class instance 
    @staticmethod
    def general_description():
        return "car are means of transport"
      
    @property
    def model(self):
        return self.__model
        
class ElectricCar(Car):
    def __init__(self,battery_size,brand, model):
        super().__init__(brand ,model)
        self.battery_size = battery_size
        
    def fuel_type(self):
         return "Electric Charge"
    
creta = Car("Hyundai","Creta")  #my_car is obejct which indicate class car
safari = Car("Tata","Safari")  #my_car is obejct which indicate class car
# property decorator 
# safari.model="harrier"
print(safari.model)
my_tesla = ElectricCar("Tesla","Model S1","95Kwh")  #my_car is obejct which indicate class car
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
# print(my_tesla.full_name())
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())
# print(creta.fuel_type())
# print(Car.total_car)
# staticmethod general definition can be accessed by only car class not by object

# print(creta.general_description()) not accessed by this object 
# print(Car.general_description())

# isinstance
print(isinstance(safari,Car))
print(isinstance(safari,ElectricCar))

print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))
