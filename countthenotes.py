#Taking the total amount as input from user
amount=int(input("Please Enter Amount for Withdrawl in Dollars:"))
#Calculating the number of notes of different denominatiors
note1=amount//100
note2=amount//10
note3=amount//1
print("Notes of $100:",note1)
print("Notes of $10", note2)
print("Notes of$1",note3)