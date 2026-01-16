print("Enter a number (Numerator): ")
numn=int(input())
print("Enter a number (Denominator): ")
numb=int(input())
if numn%numb==0:
    print("\n" +str(numn) + " is divisible by " + str(numb))   
else:
    print("\n" +str(numn) + " is not divisible by " + str(numb))