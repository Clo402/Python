#Assigning Different Variables
Name="Penguin"
Age=11
Is_student=True
Weight=38.5
#Printing Different Vaiables and their Data Type
print("Name:",Name)
print("Age:",Age)
print("Data Type for Age is:",type(Age))
print("Is_student:",Is_student)
print("Data type for Is_Student is:",type(Is_student))
print("Weight:",Weight)
print("Data typr for Weight is",type(Weight))
#Type casting to convert the datatype of variables
print("\n After Type Casting...")
Age=str(Age)
print(Age)
print("Data type for Age is:",type(Age))
Weight=int(Weight)
print(Weight)
print("Data type for Weight is:",type(Weight))