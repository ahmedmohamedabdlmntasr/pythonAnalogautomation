# Name=input("what\'s your name?").strip().capitalize
# emial=input("what\'s you email?").strip
# theUserName=emial[:emial.index("@")]
# thecompanyDomain=emial[emial.index("@")+1:]
# print(f"your name is {Name}\nyour emial is{emial} \nyour your name is {theUserName}\nyour website is {thecompanyDomain}")



InputUser=input("what is your name ,sir?").strip().capitalize()
email=input("what is your email,sir?")

# print(email[0:email.index("@")])

userName=email[0:email.index("@")]
companyName=email[email.index("@")+1:]

print(f"your user name is {userName} \nyour company name is {companyName}")

