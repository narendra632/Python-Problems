"""name=("narendra","sairaj","saurav","anuj","salman")

print(len(name))

name.append("asif")
name.insert(2,"Nitin")
name.remove("Nitin")
name.pop()
print(name)

percent=(100,990,80,70,60,50,40,30,20,10,)

print(percent)

a=1
b=2
a,b=b,a
print(b)"""




'''dictionery = {"narendra":{"c1":"python","c2":"c#"},"sairaj":"javascript","saurav":"html","anuj":"php","salman":"c++"}
#print(dictionery["narendra"]["c1"])
#print(dictionery["sairaj"])
#dictionery["asif"] = "typescript"   # to insert value
#del dictionery["salman"]            # to delete a value
#dictionery.update({"narendra":{"c2":"css"}})
#print(dictionery.get("narendra"))
#print(dictionery.keys())
#print(dictionery.items())
#print(dictionery.values())

name1 = input("enter the name :")
print(dictionery[name1])

info=input("Enter Name :")
if info=="narendra":
    print(dictionery.get("narendra"))
elif info=="sairaj":
    print(dictionery.get("sairaj"))
elif info=="saurav":
    print(dictionery.get("saurav"))
elif info=="anuj":
    print(dictionery.get("anuj"))
elif info=="salman":
    print(dictionery.get("salman"))
else:
    print("name not exist in dictionery")'''

#set = {0,1,2,3,4}
#set.add(5)
#print(max(set))
#set.remove(3)
#print(set)

'''print("What is your Age?")

age=int(input("your age :"))

if  age>18 and age<99:
    print("You are elligible to drive")
elif age==18:
    print("please confirm your licence")
elif age>99:
    print("you are allready dead")
elif age<0:
    print("you are not born yet")
else:
    print("you are not elligible to drive")'''

'''name = [["narendra", 1], ["sairaj",2], ["saurav",3], ["anuj",4], ["salman",5]]
dict1= dict(name)
for item in dict1.items():
    print(item)'''

'''list2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

for item in list2:
    if item>4 and item<15:
        print(item , " hi")'''


'''i = 0
while (True):
    if i < 5 :
        i 
        continue
    print(i )
    if (i==5):
        break
    i = i + 2

num1=int(input())
num2=int(input())

if num1 is not num2:
    print("numbers are not equal")'''


'''def func1(a, b):
    """This function add the value of a and b \n"""
    print("addding a and b\n",a+b)
add=func1(1, 2)
print(func1.__doc__)
print(func1)'''

'''print("Enter num 1")
num1=input()
print("enter a num 2")
num2=input()

try:
    print("The sum of two numbers is",
            int(num1)+int(num2))
except Exception as e:
    print(e)

print(("Hi I am Narendra "))'''


#lamda function
'''plus= lambda x, y: x+y
print(plus(11111,11111))'''

'''
import random
random_number= random.randint(-10,10)
print(random_number)

if random_number==7:
    print("you won the lottery")
else:
    print("try again")

list=["Narendra","Sairaj","Saurav","anuj","Salman","Asif"]
choice=random.choice(list)
print(choice)
'''
'''
#args used to add multiple values in existing functions
def exampleARGs(*args):
    for item in args:
        print(item)

list=["Narendra","Sairaj","Saurav","anuj","Salman","Asif"]

exampleARGs(list)
'''
'''
import flask
print(flask.__path__)

import sys
print(sys.path)

import introduceMe
print(introduceMe.gotdate())
'''
'''
list=["Narendra","Sairaj","Saurav","anuj","Salman","Asif"]

#for item in list:
#    print(item, "and", end=" ")

a=" and ".join(list)
print(a)
'''
'''
list1=[1,3,5,6,8,10]
square=list(map(lambda num: num*num,list1))
print(square)
'''
'''
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def greater(num):
    return num>5

greaterthan5=list(filter(greater, list1))
print(greaterthan5)
'''
'''
from functools import reduce
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
num=reduce(lambda x,y:x*y,list1)
print(num)
'''
'''
def execution(execute):
    def executing():
        print("Executing NoW")
        execute()
        print("Executed")
    return executing

@execution

def myinfo():
    print("I am Narendra Singh Rathore")
#myinfo=execution(myinfo)

myinfo()
'''

'''
def add():
    print("hello world")

def bata():
    add()

bata()
'''

query=input("quit or exit: ")
if "quit" in query or "exit" in query:
    print(" good bye sir, shellbee is being turned off")
    exit()
else:
    print("try again")