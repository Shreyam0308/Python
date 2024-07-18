for i in range(1,51):
    if(i%3==0 and i%5==0):
        print(i," Frizzbuzz")
    elif(i%3==0):
        print(i, " Frizz")
    elif(i%5==0):
        print(i," buzz")
    else:
        print(i)