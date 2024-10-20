# Emmanuel Cruz Adrian Garcia

# Oct 19, 2024

print("Daily Routine:")
print("1. Wake up")
print("2. Eat Breakfast")
print("3. Learn Python")
print("4. Working on homework")
print("5. Going on a run")
print("6. Eat dinner")
print("7. Go to bed")
print("0. Exit")

while True:
    w = input("Please enter your answer (0-7): ")
    
    if w == "1":
        print("Getting out of bed.")
    elif w == "2":
        print("Enjoy your breakfast!")
    elif w == "3":
        print("Time to learn Python.")
    elif w == "4":
        print("Let's get started on that homework!")
    elif w == "5":
        print("Don't forget to stretch before your run.")
    elif w == "6":
        print("Dinner is ready!")
    elif w == "7":
        print("Time to rest. Good night!")
    elif w == "0":
        print("Exiting the program. Have a nice day!")
        break
    else:
        print("Invalid option. Please enter a number between 0 and 7.")

