#OOPS Concepts
#DRY concept - Do not Repeat Yourself


'''
class Student:
    course="B.Tech CS"
    passout_12th="S.N.B.P"
    pass

narendra=Student()
sairaj=Student()

narendra.name="Narendra"
narendra.city="Pune"
narendra.subjects=["Graphics","Physics","maths","Environmental Engineering","Communication skills"]

sairaj.name="sairaj"
sairaj.city="Kolhapur"
sairaj.subjects=["Graphics","Physics","maths","Basic Electrical Engineering","Professional skills,","Workshop"]

print(narendra.name,narendra.course,narendra.subjects,narendra.city)
print(sairaj.name,sairaj.course,sairaj.city,sairaj.passout_12th)
'''


'''
class Student:
    course="B.Tech CS"
    passout_12th="S.N.B.P"
    pass

    def printdetails(info):
        return f"Name is {info.name} Course is {info.course} 12th Passout from {info.passout_12th} live in {info.city}"

    
narendra=Student()
sairaj=Student()

narendra.name="Narendra"
narendra.city="Pune"
narendra.subjects=["Graphics","Physics","maths","Environmental Engineering","Communication skills"]

print(narendra.printdetails())
'''


'''
class Student:
    course="B.Tech CS"
    passout_12th="S.N.B.P"
    pass
    def __init__(info,aname,acity,acourse):
        info.name=aname
        info.city=acity
        info.course=acourse

narendra=Student("Narendra","Pune","B.Tech CS")
print(narendra.name)
'''


'''
class Student:
    course="B.Tech CS"
    passout_12th="S.N.B.P"
    
    def __init__(info,aname,acity,acourse):
        info.name=aname
        info.city=acity
        info.course=acourse

    def printdetails(info):
        return f"Name is {info.name} Course is {info.course} 12th Passout from {info.passout_12th} live in {info.city}"
    
    @staticmethod
    def printgood(string):
        null=" "
        print("Good Work "+ string)
        return null
narendra=Student("Narendra","Pune","B.Tech CS")
sairaj=Student("Sairaj","Kolhapur","B.Tech CS")
print(sairaj.course)
print(narendra.name)
print(sairaj.printgood("Narendra"))
'''


'''
#inheritance & single inheritance

class Student:
    course="B.Tech CS"
    passout_12th="S.N.B.P"
    
    def __init__(info,aname,acity,acourse,alanguages):
        info.name=aname
        info.city=acity
        info.course=acourse
        info.languages=alanguages

    def printdetails(info):
        return f"Name is {info.name} Course is {info.course} 12th Passout from {info.passout_12th} live in {info.city}"
    
    @staticmethod
    def printgood(string):
        null=" "
        print("Good Work "+ string)
        return null

narendra=Student("Narendra","Pune","B.Tech CS",["Python","HTML","CSS"])
sairaj=Student("Sairaj","Kolhapur","B.Tech CS",["HTML","CSS"])
saurav=Student("Saurav","delhi","BBA IB",["HTML"])

#inheritance
class Programmer(Student):
    def __init__(info, aname, acity, acourse, alanguages):
        super().__init__(aname, acity, acourse, alanguages)
    def printstu(self):
        return f"The Student is {self.name} Course is {self.course} 12th Passout from {self.passout_12th} live in {self.city} the languages are{self.languages}"
    pass
    print(printstu(saurav))
'''    

'''
#multi Inheritance
class Student:
    course="B.Tech CS"
    passout_12th="S.N.B.P"
    
    def __init__(info,aname,acity,acourse,alanguages):
        info.name=aname
        info.city=acity
        info.course=acourse
        info.languages=alanguages

    def printdetails(info):
        return f"Name is {info.name} Course is {info.course} 12th Passout from {info.passout_12th} live in {info.city}"
    
class player:
    var=5
    no_of_game=2
    def __init__(info, name, game):
        info.name=name
        info.game=game
    def printdetails(info):
        return f"Name is {info.name} the game is {info.game}"

narendra=player("Narendra","Football")
print(narendra.printdetails())

class coolprog(Student,player):
    skill="Trading"
    def print_skill(info):
        print(info.skill)

narendra=coolprog("Narendra","Pune","B.Tech CS",["Python","HTML","CSS"])
print(narendra.printdetails())

print(narendra.var)
narendra.print_skill()
'''


'''
#multi level inheritance
class me:
    level=1
    race="Human"

class son(me):
    level=2
    anatomy="anime"
    def lvl(self):
        return f"My level is {self.level} "
        
class grandson(son):
    level=3
    def lvl(self):
        return f"My level is {self.level} coz I am Strong "

goku=me()
eren=son()
naruto=grandson()

print(naruto.lvl())
print(naruto.race)
print(naruto.anatomy)
'''


#public
#protected  _variable   variables starting with underscore are private variables 
#private  __variable    variables starting with double underscore are protected variables only accessed by sub classes


#POLYMORPHISM - ability to take various forms 
#print(5+6)
#print("5"+"6")

'''
OPPS Concepts
Abstraction 
Encapsulation
Inheritance
Polymophism
'''
#Overriding 
#Super()


'''
#dunder methods - starting and ending with double underscore ex __add__ , __init__ , __truediv__
class Student:
    course="B.Tech CS"
    passout_12th="S.N.B.P"
    
    def __init__(self,aname,acity,afee,alanguages):
        self.name=aname
        self.city=acity
        self.fee=afee
        self.languages=alanguages
    
    def __add__(self, other):
        return self.fee + other.fee

    def __truediv__(self, other):
        return self.fee / other.fee 
    
    def __mul__(self, other):
        return self.fee * other.fee 

narendra=Student("Narendra","Pune",100000,["Python","HTML","CSS"])
sairaj=Student("Sairaj","Kolhapur",30000,["HTML","CSS"])

print( narendra + sairaj)
print( narendra / sairaj)
print( narendra * sairaj)
'''


#abstract base class -used to add compulsory function to parent class that must be used by its child class
from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class rectangle(shape):
    type="Rectangle"
    sides=4

    def __init__(self):
        self.length=10
        self.breadth=14

    def printarea(self):
        return self.length * self.breadth

class square(shape):
    type="Square"
    sides=4

    def __init__(self):
        self.length=20
        
    def printarea(self):
        return self.length*self.length

R_area=rectangle()
S_area=square()
print(R_area.printarea())
print(S_area.printarea())


# Object Introspection

print(type(rectangle()))
print(type(square()))
print(id(rectangle()))
print(id(square()))
print(dir(rectangle()))   # dir give all methods of object

import inspect
print(inspect.getmembers(rectangle()))


# getter , setter , property decorator codewithharry python course video 69












