dict = {
    'Name' : "Shreyam",
    'Field' : "BE",
    'Branch' : "CSE(AIML)"
}

# print(dict.get('Name', 'Not Find'))
# print(dict.get('Mobile No.', 'Not Find'))
d2 = {
    'none' : None,
    'Lets play' : 'cricket',
}
dict['Year'] = 2
dict.update(d2)
# print(dict)

for i,j in dict.items():
    print(i,"\t",j)