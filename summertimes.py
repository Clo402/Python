#Summer Times
print("What is the temprature where you are?")
temp=int(input("Your temprature (in Celcius):"))
if (temp<=10 and temp>=100):
    print("You should where a big, thick jacket with gloves, earmuffs, and more cozy apparel!`")
elif (temp>=10 and temp<=20):
    print("You should where a nice warm jacket and boots!")
elif (temp>20 and temp<=30):
    print("You should where a t-shirt, shorts, and sneakers!")
elif (temp>30):
    print("Your should where a t-shirt, shorts, flip-flops, and a lot of sunscreen!")