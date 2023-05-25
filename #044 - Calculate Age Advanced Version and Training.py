print("#"*80)
print("you can enter the unit with the full name or the first letter")
print("#"*80)
age=int(input("enter your age ,please:"))
unit=input("enter your unit (months,years,days):").strip().lower()

months=age*12
days=months*30
hours=days*24





if unit=="months" or unit=="m":
    print(f"your age in months is {months,}")
elif unit=="years" or unit=="y":
    print(f"your age in years is {age}")
elif unit=="days" or unit=="y":
    print(f"your age in days is {days:,}")
else:
    print("your choice is not correct:)")




