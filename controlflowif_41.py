

courseName="javascript"
price=100
discount=90
name=input("enter your name please:")
country=input("enter your country please:")
if country=="egypt" :
    print(f"hallo {name} the course name is {courseName} and the price is {price}\nBecause you are from {country} the course price is {price-discount}")

elif country=="KSA":
    print(f"hallo {name} the course name is {courseName} and the price is {price}\nBecause you are from {country} the course price is {price-10}")
elif country=="kuwiat":
        print(f"hallo {name} the course name is {courseName} and the price is {price}\nBecause you are from {country} the course price is {price-20}")
else :
         print(f"hallo {name} the course name is {courseName} and the price is {price}\nBecause you are from {country} the course price is {price-50}")


