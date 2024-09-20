# define class and object  class name must be start with capital letter
class Car:
     def __init__(self,brand,model):   # use self to access item from class like we use this is js
        self.brand = brand
        self.model = model
    
my_car = Car("Hyundai","Creta")  #my_car is obejct which indicate class car
print(my_car.brand)
print(my_car.model)