

'''while(True):
    inpi=int(input("type a number\n"))
    if inpi > 100:
        print(" congrates the number is greater than 100\n")
        break
    elif inpi < 0:
        print("number is less than zero\n")
        continue
    else:
        print("try again")
        continue'''

'''print("Lets print stars\n")
num = int(input("How many Star rows you want to print\n"))
print("what order you want")
pattern=input("enter 1 for acending order, 0 for decending order\n")
if pattern=="1":
    for i in range(0,num+1):
        print("*"*int(i))
if pattern=="0":
    for i in range(num,0,-1):
        print("*"*int(i))'''


'''
#recursive recursion
def factorial(n):
    fac=1
    for i in range(n):
        fac= fac * (i + 1)
    return fac
    
number=int(input("Enter your number\n"))
print(factorial(number))'''


'''
#iterative recursion
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number=int(input("Enter your number\n"))
print(fibonacci(number))'''


'''
import time
initial=time.time()

k=0
while(k<3):
    print("While loop ran in ")
    k+=1
    time.sleep(1)
print(time.time() - initial,"second")

initial2=time.time()

for i in range(3):
    print("For loop ran in")
    time.sleep(2)
print(time.time() - initial2,"second")

localtime= time.asctime(time.localtime(time.time()))
print(localtime)
'''

'''
import wikipedia
tell=input("for search  ")
results= wikipedia.summary(tell)


if tell in results:
    print(results)
'''

'''
import webbrowser
webbrowser.open("google.com")
'''



'''
import datetime
strTime = datetime.datetime.now().strftime("%H;%M:%S")
print(f"Sir, the time is {strTime}")
'''

'''
import os
vscode= "E:\\VS Code\Microsoft VS Code\\Code.exe"
os.startfile(vscode)
'''

'''
import smtplib
def sendEmail(to, content):
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("mrperfectth7@gmail.com", "#your password")    
    server.sendmail("mrperfectth7@gmail.com", to, content)
    server.close    

try:
    print("What should I say")
    content=input("Enter text: ")
    to = "mrperfectth7@gmail.com"
    sendEmail(to, content)
    print("Email has been sent")
except Exception as e:
    print(e)
    print("Sorry sir, I was unable to send the Email")
'''

'''
import random
import os
movie_dir="D:\\Movies\\MARVEL Movies"
movie= os.listdir(movie_dir)
surprise=random.choice(movie)
os.startfile(os.path.join(movie_dir, surprise))
'''
import datetime
strTime = datetime.datetime.now().strftime("%H:%M:%S")
print(strTime)
