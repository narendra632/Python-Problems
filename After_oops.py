'''
# Iterable   - iter() __iter__()  
# Iterator   -__next__()
# generators

n= "I Am Narendra Singh Rathore"
itrator= iter(n)

print(itrator.__next__())
print(itrator.__next__())
print(itrator.__next__())
print(itrator.__next__())
print(itrator.__next__())
print(itrator.__next__())
'''

'''
# Comprehension

# 1. List Comprehensions
#Classic Example
table3=[]
for i in range(33):
    if i%3==0:
        table3.append(i)
print(table3)

#Comprehension example 
table3=[i for i in range(33)]
print(table3)
table3=[i for i in range(33) if i%3==0]   #with condition 
print(table3)
print(type(table3))

# 2. Dictionery Comprehensions
#Classic Example 
dict={1:"one",2:"two",3:"three"}
print(dict)

#Comprehension example
dict={i:f"item{i}" for i in range(1,11) if i%2==0}
print(dict)
dict={value:key for key,value in dict.items()}
print(dict)
print(type(dict))

# 3. set Comprehension
#Classic Example
names={"Narendra","Sairaj","saurav","Anuj","Salman"}
print(names)
print(type(names))

#Comprehension Example
names={name for name in ["Narendra","Sairaj","saurav","Anuj","Salman"]}
print(names)
print(type(names))


# 4. Generator Comprehension
evens= (i for i in range(100) if 1%2==0)
for item in evens:
    print(item)
print(type(evens))
'''

'''
names=["Narendra","Sairaj","saurav","Anuj","Salman"]

for item in names:
    if item=="Rohit":
        print("Hello " +item)
        break
else:
    print("You are not Narendra")
'''


'''
#function Cashing(Cache)
import time
from functools import lru_cache

no_of_cache=int(input("Enter "))
@lru_cache(maxsize=no_of_cache)

def timer_loop(n):
    time.sleep(n)
    return n

n=int(input("Enter the time amount  "))


print("Timer now running")
timer_loop(n)
print(f"ran for {n} seconds, running again")
timer_loop(n+2)
timer_loop(n+2)
timer_loop(n+2)
print(f"again ran for {n} seconds running again")
timer_loop(n+3)
timer_loop(n+3)
timer_loop(n+3)
print(f"again ran for {n} seconds running again")
timer_loop(n)
print(f"again ran for {n} seconds running again")
timer_loop(n)
print(f"again ran for {n} seconds running again")
timer_loop(n)
print(f"Finally ended in {n} seconds")
'''

'''
try:
    f1=open("GuessTheNumber.py")
except Exception as f:
    print("File not Opened",f)
#else will run if except is not running
else:
    print("Game File opened")
finally:
    f2=open("introduceMe.py")

print("introduceMe.py File opened")
print("Can you see second file ?")

x=input("y or n\n")
if x=="y":
    print("OK please continue")
else:
    print("Sorry for inconvinience")

f1.close
f2.close
'''

'''
import os

print(os.getcwd())

os.chdir("E://")
print(os.getcwd())

os.rename("movies","Movies")
print(os.listdir())

print(os.path.exists("C://"))
'''

'''
import requests
get and post 
'''

'''
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
speak("Hi, I am a Devil, of my World")
'''

'''
import json
from optparse import Values

data='{"name1":"Narendra","name2":"Sairaj","name3":"Saurav"}'

parsed=json.loads(data)
print(parsed["name1"])
print(type(parsed))

data2={"marks":[89,98,69],"values":True}
jsdump=json.dumps(data2)
print(jsdump)
'''

'''
import pickle
'''

'''
import re

mystr = "PS C Users Ashapura Desktop Python> python -u c Users Ashapura Desktop\Python\After_oops.py"


patt = re.compile(r'.Ashapura')
matches=patt.finditer(mystr)

for match in matches:
    print(match)
'''

'''
a=[5,6,"34"]
b=[5,6,"34"]
a == b
print(b is a)
print(b == a)
'''

'''
import argparse
import sys

def calc(args):
    if args.o=="add":
        return args.x + args.y
    elif args.o=="sub":
        return args.x - args.y
    elif args.o=="mul":
        return args.x * args.y
    elif args.o=="div":
        return args.x / args.y
    else:
        return "Something went wrong"
    
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float,default=1.0, help="Enter First number or  Please contact Me")

    parser = argparse.ArgumentParser()
    parser.add_argument('--y', type=float,default=3.0, help="Enter Second number or Please contact Me")

    parser = argparse.ArgumentParser()
    parser.add_argument('--y', type=float,default=3.0, help="Enter Second number or Please contact Me")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
'''

'''
import requests
import pickle

data=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
#print(data)

l1=data.split("\n")
#print(l1)

l2= [item.split(",") for item in l1]
#print(l2)

with open("myiris.pkl", "wb") as f:
    pickle.dump(l2,f)
'''
'''
import pickle
with open("myiris.pkl","rb") as f:
    print(pickle.load(f))
'''


































































