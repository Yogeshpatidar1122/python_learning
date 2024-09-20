password =input("Enter Your password: ")
if len(password)<6:
    strength = "Weak"
elif len(password)<=10:
    strength = "Medium"
elif len(password)>10:
    strength = "Strong"
print("Your password is :",strength)