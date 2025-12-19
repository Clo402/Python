#Take marks as input from user
print("Enter marks obtained in four subjects")
math=int(input("Math:"))
science=int(input("Science:"))
reading=int(input("Reading:"))
hindi=int(input("Hindi:"))
#Let's calculate the percentage of the marks
sum=math+science+reading+hindi
print("Sum of Math, Science, Reading and Hindi")
perc=(sum/400)*100
print("Percentage Mark=")
print(perc)