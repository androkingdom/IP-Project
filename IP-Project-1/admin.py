import function

print("+--------------------+")
print("|       SignUp       |")
print("+--------------------+")

UserName1 = input("Enter User Name : ")
UserName = UserName1.replace(" ","")
LoginId = function.LoginId()

if function.AlphaInUserName(UserName) == True:
    if function.unique_(UserName) != False:
        print(f"Your LoginId : {LoginId}")
        with open("user.csv", "at") as file:
            file.write(f"{UserName},{LoginId}\n")
    else:
        print("Enter Another Name !!!")
else:
    print("User Cannot Be Assign")