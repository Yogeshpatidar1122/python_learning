fruit =str(input('Enter the fruit name: '))
color =str(input('Enter the color: '))
if fruit=='Banana':
    if color=='Green':
        print ("Unripe")
    elif color =='Yellow':
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
    else:
        print("Give the suitable fruit")