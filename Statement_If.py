age_str = input("Enter your age: ")
age_int = int(age_str) # Convert string to integer
print(type(age_int)) # Output: <class 'int'>

if age_int >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote yet.")