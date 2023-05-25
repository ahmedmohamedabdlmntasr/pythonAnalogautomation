CourseName="javascript beginner"
courseprice=100
name=input("what is your name ,sir?")
isStudent=input("are you a student?")
country=input("what is your country?")




if country=="egypt" or country=="Algeria" or country=="Yamen":
    if isStudent=="yes":
        print(f"hallo {name} the course name is {CourseName} and the course price is {courseprice}\nBecause you are from {country} and is student the price course after discount is {courseprice-95}")
    else:
        print(f"hallo {name} the course name is {CourseName} and the course price is {courseprice}\nBecause you are from {country} the price course after discount is {courseprice-80}")    
elif country=="KSA"  or country=="kuwait" :
    if isStudent=="yes":
        print("hallooooooooooooooooooooooooooooooo")
        print(f"hallo {name} the course name is {CourseName} and the course price is {courseprice}\nBecause you are from {country} and is student the price course after discount is {courseprice-85}")
    else :
        print(f"hallo {name} the course name is {CourseName} and the course price is {courseprice}\nBecause you are from {country} the price course after discount is {courseprice-70}")    
else:
    if isStudent=="yes":
        print(f"hallo {name} the course name is {CourseName} and the course price is {courseprice}\nBecause you are from {country} and is student the price course after discount is {courseprice-70}")
    else:
        print(f"hallo {name} the course name is {CourseName} and the course price is {courseprice}\nBecause you are from {country} the price course after discount is {courseprice-55}")    

#need to debug here 
