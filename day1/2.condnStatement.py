age=int(input("Enter the age : "))
gender=input("Enter Gender: ")
if (age>=18 and (gender=='male' or gender=='female')):
    print("Eligible")
else:
    print("Not Eligible")