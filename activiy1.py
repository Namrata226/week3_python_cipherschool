#object
a=5
isinstance(a,object) # ---> True
a+4
isinstance(a,int) # ---> True

def func(): # ---> This statement creates a value and store it in the variable func
    pass
isinstance(func,object) # ---> True

class A:
    name="jatin"
    marks=50

type(A) # ---> Datatype is type for this variable
A=5
type(A) # ---> int  

class A:
    def __call__(self):
        print("You called me")

a=A()
type(a) # __main__.A
a() # You called me

b=A.__call__()
b=A()

def func():
    print("Hello") # ---> Hello
func()
func.__call__() # ---> Hello

def say_hi(self):
    print(self.name)
    self.name="anonymous"

for i in range(5):
    print(i)
#Even for for loop there is dunders

a={"name":"Jatin"}
# a{"name"} --->'Jatin'
a.__getitem__("name") # --->'Jatin'

class Exponent:
    def __init__(self,n):
        self.n=n
    def __getitem__(self,x):
        return x**self.n
e=Exponent(3)
e[6] # --->216

class A:
    name="Jatin"
    def __init__(self,n):
        self.n=n
a=A(2)
a.name # --->"Jatin"
a.n # ---> 2


class Dog:
    kind='canine'
    def __init__(self,name):
        self.name=name
a=Dog("Maxx")
a.name # ---> 'Maxx'
a.kind # ---> 'canine'


class Dog:
    tricks=[]
    def __init__(self,name):
        self.name=name
    def add_tricks(self,trick):
        self.tricks.append(trick)
d1=Dog("Maxx")

d1.add_tricks("fetch")
d1.add_tricks("talk")
d1.tricks # ['fetch','talk']
d2=Dog("Bella")
d2.tricks # ['fetch','talk']

# a=[]
# b=a
# b.append(1)
#Ultimately we are appending on a
 103  
class20-Inheritance, MRO and Iteration Protocol-CipherSchools.py
@@ -0,0 +1,103 @@
class A:
    def __init__(self,x):
        self.x=x
class B(A):
    def __init__(self,x,y):
        print("B init executed")

abc=B()

#Python doesn't have a concept of overloading
class A:
    def __init__(self):
        print("A init executed")
class B(A):
    def __init__(self,x,y):
        print("B init executed")
#By design python doesn't have polymorphic functions
#It will replace it by attributes
#init is not a constructor

'''
If we want to call parent class we use super()
'''
class A:
    def __init__(self):
        print("A init executed")
class B(A):
    def __init__(self,x,y):
        print("B init executed")
        super().__init__()
abc=B()

""" MRO  - Method Resolution Order """
class A:
    pass
class B(A): #class B extend from A
    pass
class C(B):
    x=5
class D(A):
    x=10
class E(C,D): #class B extend from C and D
    pass
e=E()
print(e.x) #5

class A:
    x=5
class B(A): #class B extend from A
    pass
class C(B):
    x=5
class D(A):
    x=10
class E(C,D): #class B extend from C and D
    pass
e=E()
print(e.x) #10

# E.mro() --->[__main__.E,__main__.C,__main__.B,__main__.D,__main__.A,object]

"""
RULES:
    DFS---> If there is a loop, solve branches differently
"""

""" ITERATION PROTOCAL """
'''
For any object to be an iterable, it should have 2 dunders
__iter__ ---> return an iterators which helps me iterate over this iterator
__next__ 
'''
a=range(5)
it=a.__iter__()
it.__next__() #0
it.__next__() #1
it.__next__() #2
it.__next__() #3
it.__next__() #4
'''
Stop the iteration
'''

class myrange:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return myrange_iterator(self)
class myrange_iterator:
    def __init__(self,myrange):
        self.myrange=myrange
        self.i=0
    def __next__(self):
        ret=self.i
        self.i+=1
        if ret>=self.myrange.n:
            raise StopIteration
        return ret

a=myrange(5)
it=iter(a)
next(it)

 91  
class21-Concept of Generators-CipherSchools.py
@@ -0,0 +1,91 @@
""" Generators """
# a=[]
#     for i in range(1,100):
#         a.append(i==2)
#     for x in a:
#         print(x)

def generate_squares(n):
    return [i**2 for i in range(1,n)]
for x in generate_squares(100):
    print(x)
"""
The thing is that it is doing eager loading
first calculating then storing
"""

#Lazy Loading
'''
We use yeild keyword for lazy loading
'''

def generate_squares(n):
    for i in range(1,n):
        yield i**2

""" whatever value is infront of it , it will give away the control to the parent toexecute the code of its own"""

for i in generate_squares(100000000000):
    print(i)
#calculating single square at a time and giving away the control to the for loop
#yield uses iteration protocol
#iteration protocol is such a beautiful API

def func():
    print("start")
    yield 1
    print("yielded 1")
    yield 2
    print("yielded 2")
it=iter(func())
next(it)

print("Hello")
for i in range(100000000000):
    pass
print("World")

def func():
    for i in range(10000000000000):
        pass
    print("ended")

from time import sleep
def func():
    print("start")
    yield
    sleep(5)
    print("ended")

print("hello")
it=iter(func())
next(it)
print("world")
next(it)


def generate_squares(n):
    for i in range(1,n):
        yield i**2
a=generate_squares(10)
print(type(a)) #generator

########################################################################
a=(i**2 for i in range(10)) #It is a generator which returns a generator
'''
There is no tuple comprehension in python
'''
for i in a:
    print(i)
'''Generator is nothing but an iterator'''

a=generate_squares(10)
next(a)

a=(i**2 for i in range(10))
print(iter(a))
print(a)

a=(i**2 for i in range(10))
print(next(a))
print(next(a))
0 comments on commit 718c159
@Namrata226
 
Add heading textAdd bold text, <Ctrl+b>Add italic text, <Ctrl+i>
Add a quote, <Ctrl+Shift+.>Add code, <Ctrl+e>Add a link, <Ctrl+k>
Add a bulleted list, <Ctrl+Shift+8>Add a numbered list, <Ctrl+Shift+7>Add a task list, <Ctrl+Shift+l>
Directly mention a user or team
Reference an issue, pull request, or discussion
Add saved reply
Leave a comment
No file chosen
Attach files by dragging & dropping, selecting or pasting them.
Styling with Markdown is supported
 
