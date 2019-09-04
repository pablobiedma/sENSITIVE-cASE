# for debugging intentions


text = input("Please enter your text: \n")
print("************ To swap case enter 1")
print("***To make all lower case enter 2")
print("***To make all upper case enter 3")
choice = input("\nPlease make a choice: \n")

if choice == "1":
    result = str.swapcase(text)
    print(result)

elif choice == "2":
    result = text.lower()
    print(result)

elif choice == "3":
    result = text.upper()
    print(result)
else:
    print("Error, please enter a valid action.")
