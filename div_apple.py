def divapple():
    try:
        apples=int(input("Enter the number of Apples "))
        mn=int(input("Enter the minimum number to check "))
        mx=int(input("Enter the maximum number to check "))
        if mn > mx+1:
                print("mn value can't be greater than mx value. enter Again")
                divapple()
        for i in range(mn,mx+1):
            
            if apples%i==0:
                print(f"{i} is divisor of {apples}")
            else:
                print(f"{i} is not a divisor of {apples}")

    except Exception as f:
        print("Please enter numbers only   ----    ")
        divapple()

divapple()