

def tellage():
    try:
        age=int(input("Enter your age or year of Birth : "))
        if (age<=0 or age>2022):
            print("You are not born yet")

        elif (age>0 and age<100):
            age= 2022-age
            print(f"You will be 100 year old, in the year {age+100}")

        elif (age>=1922 and age<=2022):
            age= 2022-(2022-age)
            print(f"You will be 100 year old, in the year {age+100}")

        elif (age>=100 and age<200):
            print("You are allredy 100. Are you still Alive!!")

        elif (age<1922):
            age= 2022-(2022-age)
            print(f"You were 100 year old in the year {age+100} AD. Man How are you still alive")
    
    except Exception as f:
        print("Please Enter a date or year!! --",f)
        tellage()

    while(True):
        again=input("Press c to continue e to exit ")
        if again=="c":
            tellage()
        elif again=="e":
            exit()
        elif again not in ["c","e"]:
            print("Wrong input")
            continue
tellage()
        



