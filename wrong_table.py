import random

def wrongmul(number):
    wrong=random.randint(0,9)
    table=[i * number for i in range(1,11)]
    table[wrong] = table[wrong]+random.randint(0,5)
    return table

def correctmul(table,number):
    for i in range(1, 11):
        if table[i-1] != i*number:
            return i - 1
    return None

try:
    number=int(input("Enter the number : "))
    mytable=wrongmul(number)
    print(mytable)
    wrongindex= correctmul(mytable,number)
    print(f"table is wrong at {wrongindex}")

except Exception as f:
    print("Enter numbers only ")