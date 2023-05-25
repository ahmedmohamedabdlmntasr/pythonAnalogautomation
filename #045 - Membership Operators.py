s="ahmed mohamed abdlmntaser"
print("ahmed" in s)

print("abdl" in s)



DiscountCountries=["egypt" , "tunisia" , "bahrain" , "ghana","algeria","syria"]
richcountries=["europe","brazil","usa"]

country=input("enter your country please:")
if country in DiscountCountries:
    print(f"you have a good discount beacuse you are in {country}")
elif country in richcountries:
    print(f"you have no discount because you are from {country}")
else:
    print("your country in not in the list")