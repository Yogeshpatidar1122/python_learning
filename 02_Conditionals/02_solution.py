age=int(input("Enter the age of person: "))
day= "wednesday"

price = 12 if age >= 18 else 8

if day == "wednesday":
    price=price-2
    # price -=2 smae waY TO WRITE 
print("TICKET PRICE FOR YOU IS:",price)