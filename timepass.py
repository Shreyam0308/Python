unique = ["@","$","#"]
count = 0
while(count!=1):
    password = input(f"Password should be minimum 8 and maximum 16 character\nPassword should contain atleast 1 {unique} character\nPassword contain atleast one number\nEnter a password :- ")
    if (len(password) > 5 or len(password) < 17) and ("@" in password or "$" in password or "#" in password):
        for i in password:
            if i.isdigit():
                count = 1
                break
        if count == 1:
            print(f"Now {password} is your password")
        else:
            print("Re generate Password")
    else:
        print("Re generate Password")