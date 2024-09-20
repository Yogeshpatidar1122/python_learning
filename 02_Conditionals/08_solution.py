species = str(input("Enter the species (Dog/Cat): "))
age = int(input("Enter age: "))

if species == 'Dog':
    if age < 2:
        print("Puppy food")
    else:
        print("Senior dog food")

elif species == 'Cat':
    if age < 5:
        print("Adult cat food")
    else:
        print("Senior cat food")

else:
    print("Sorry, we only recommend food for dogs and cats.")
