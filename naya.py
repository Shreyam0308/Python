lis = [(10,20,30),(40,50,60),(70,80,90)]
num = int(input("Enter a number :- "))
start = 0
for i in lis:
    l = list(i)
    l[-1] = num
    list2 = tuple(l)
    list[start] = list2
    start+=1
print(lis)