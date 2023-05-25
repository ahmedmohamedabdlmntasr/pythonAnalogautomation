country=input("enter your country ,please:")
age=int(input("enter your age ,please:"))

if country=="egypt":
    print("wheater is fine")
elif country=="KSA" :
    print("wheater is so hot")
else :
    print("country is not on the list")

print("you are allowed to watch" if age>14 else "you are not allowed to watch")
