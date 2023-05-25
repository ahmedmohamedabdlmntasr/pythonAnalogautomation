subscriptionList=["ahmed", "mona", "mohamed", "ashraf","rahma","suze"]


name=input("enter your name ,please:")

#neeeeeeeeeeeeeeeeeeeed debugginggignignignignignigng
if name in subscriptionList:
    print(f"your name is in subscription list.")
    choice=input("update or remove:")
    if choice=="update" or choice=="u" :
        theNewName=input("enter the new name:")
        print(f"the new name is {theNewName}")
        subscriptionList[subscriptionList.index(name)]=theNewName
        print("the name had been updated")
        print(subscriptionList)

    elif choice=="remove" or choice=="r":
        subscriptionList[subscriptionList.index(name)]={}
        print("the name had beed deleted")
        print(subscriptionList)
    else:
        print("your choive is not corret ,please try again")




else:
    print("your name is not in subscription list")
    choice3=input("add or not:")
    if choice3=="add" or choice3== "a":
        subscriptionList.append(name)
        print("the name had beed added welcome on board")
        print(subscriptionList)
    elif choice3=="not" or choice3=="n":
        print("ok thanks for your time ")
    else:
        print("your choice is not correct ,try again later.")




