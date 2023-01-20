try:
    numbers = []
    num = int(input("Enter the number of test cases: "))

    def next_palindrome(num):
        num = num + 1
        while not is_palindrome(num):
            num += 1
        return num

    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    for i in range(num):
        numb = int(input("Enter the number:\n"))
        numbers.append(numb)

    for i in range(num):
        print(f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])} \n")

except Exception as f:
    print("Please enter numbers only")
