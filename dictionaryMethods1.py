user={
    "name":"ahmed",
    "age" :23,
    "location":"tenth of ramadan"

}
print(user)
user2=user.copy()
user.clear()
print(user)
print(user2)
user2["gender"]="male"
print(user2)
user2.update({"department":"engineering"})
print(user2)
print("-"*40)
print(user2.keys())
print(user2.values())
