year = int(input("Enter a Year :- "))
month = int(input("Enter a Month :- "))
date = int(input("Enter a date :- "))

if date in range(1,32) and month in range(1,13):
        if year%400==0 or year%4:
            if month == 2:
                if date in range(1,29):
                    date+=1
                    print(date,"-",month,"-",year)
                else:
                    date = 1
                    month+=1
                    print(date,"-",month,"-",year)
            elif month in [1,3,5,7,8,10]:
                if date in range(1,30):
                    date+=1
                    print(date,"-",month,"-",year)
                else:
                    date = 1
                    month+=1
                    print(date,"-",month,"-",year)
            elif month == 12:
                if date in range(1,31):
                    date+=1
                    print(date,"-",month,"-",year)
                else:
                    date = 1
                    month = 1
                    year += 1
                    print(date,"-",month,"-",year)
            else:
                if date in range(1,29):
                    date+=1
                    print(date,"-",month,"-",year)
                else:
                    date = 1
                    month+=1
                    print(date,"-",month,"-",year)
        if year%100==0:
            if month == 2:
                if date in range(1,27):
                    date+=1
                    print(date,"-",month,"-",year)
                else:
                    date = 1
                    month+=1
                    print(date,"-",month,"-",year)
            elif month in [1,3,5,7,8,10]:
                if date in range(1,30):
                    date+=1
                    print(date,"-",month,"-",year)
                else:
                    date = 1
                    month+=1
                    print(date,"-",month,"-",year)
            elif month == 12:
                if date in range(1,31):
                    date+=1
                    print(date,"-",month,"-",year)
                else:
                    date = 1
                    month = 1
                    year += 1
                    print(date,"-",month,"-",year)
            else:
                if date in range(1,29):
                    date+=1
                    print(date,"-",month,"-",year)
                else:
                    date = 1
                    month+=1
                    print(date,"-",month,"-",year)
else:
    print("Enter a valid input")