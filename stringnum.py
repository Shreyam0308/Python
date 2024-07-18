l1 = ["January", "February", "March", "April", "May", "June", "Julye", "August", "September", "October", "November", "December"]

value = int(input(f"{l1}\n{list(range(1,13))} \nEnter only number for months value :- "))

if value == 1 or value == 3 or value == 5 or value == 7 or value == 8 or value == 10 or value == 12:
    print("This month has 31 days.")

elif value == 4 or value == 6 or value == 9 or value == 11:
    print("This month has 30 days.")
    
elif value == 2:
    print("This month has 28 / 29 days.")

else:
    print("Enter a valid input")