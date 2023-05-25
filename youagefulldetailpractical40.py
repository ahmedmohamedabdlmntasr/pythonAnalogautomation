Age=int(input("Enter your age ,please:"))
months=Age*12
weeks=months*4
days=months*30
hours=days*24
minustes=hours*60
seconds=minustes*60


print(f"you lived for {Age} years ")
print(f"you lived or {months} months")
print(f"you lived or {weeks:,} weeks")
print(f"you lived or {days:,} days")
print(f"you lived or {hours:,} hours")
print(f"you lived or {minustes:,} minutes")
print(f"you lived or {seconds:,} seconds")