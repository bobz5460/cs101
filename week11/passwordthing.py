password = "aBadpa$$word"
numtries = 5
for i in range(numtries, 0, -1):
    passguess = input("Enter your password: \n")
    if passguess == password:
        print("Welcome!")
        exit()
    else:
        print(f"Incorrect. You have {i-1} tries left.")
print(f"{numtries} incorrect password attempts. Goodbye!")
