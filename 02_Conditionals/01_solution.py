age=int(input("Provide age for person: "))

if age < 13:
    print("child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")