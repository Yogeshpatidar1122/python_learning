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
        

class Battery :
    def battery_info(self):
        return "battery"

class Engine:
    def engine_info(self):
        return "Crdi engine"

class ElectricCars(Battery,Engine ,Car):
     pass
 
my_tesla_new = ElectricCars("Tesla" , "Model S2")
print(my_tesla_new.engine_info())
print(my_tesla_new.battery_info())
