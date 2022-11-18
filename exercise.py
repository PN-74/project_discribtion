#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Exercise 1: Create a function in Python
 Exercise 2: Create a function with variable length of arguments
 Exercise 3: Return multiple values from a function
 Exercise 4: Create a function with a default argument
 Exercise 5: Create an inner function to calculate the addition in
the following way
 Exercise 6: Create a recursive function
 Exercise 7: Assign a different name to function and call it through
the new name
 Exercise 8: Generate a Python list of all the even numbers
between 4 to 30
 Exercise 9: Find the largest item from a given list


# In[ ]:


# Create a function in Python
#calling function

def my_function():
    print("my name is pooja")
    
my_function()


# In[ ]:


#Arguments
def my_function(Fname,lastname):
    print("Name of person:",Fname,lastname)
    
my_function("Pooja","Nawale")

    


# In[ ]:


# Create a function with variable length of arguments

# there are 2 types of variable length arguments in python

## Non_keyword arguments denoted as (*args)
## keyworded arguments is denoted as (**kwargs)

def my_function(*args):
    num= 5
    for i in args:
        num = num*i
        
    print("finalresult:",num)
    
my_function(1,9,5)


# In[ ]:


def my_function(*name):
    print("name of person:",name)
    
my_function("Pooja","Sahil")


# In[ ]:


def my_function(**kwargs):
    for key, value in kwargs.items():
        print(kwargs)
    
my_function(firstname="Pooja",lastname="Nawale")
my_function(firstname="Sahil",lastname="sharma")


# In[ ]:


## Return multiple values from a function
   
def my_function(x):
   return 10*x
print(my_function(2))
print(my_function(3))


# In[ ]:


def my_function():
    mul = 12*2
    Add = 12+2
    return mul,Add
result=my_function()
print("Multiplication and Addition:",result)


# In[ ]:


##Create a function with a default argument
   
def user_input(country = "India"):
   print(country + " Is My Country. ")
   
user_input("Landon")
user_input("Maxico")
user_input()


# In[ ]:


#Create an inner function to calculate the addition in following way

def outer_fun():
    add=12+12 
    return add
    def inner_fun():
        add=10+10
        return add
    inner_fun()
    
outer_fun()


# In[ ]:


##Create a recursive function

def count(n):
    print(n)
    if n == 0:
        return
    else:
        count(n-1)
count(5)


# In[ ]:


def fibonacci(n):
    
    if n == 1:
        return 1
    else:
        return n * fibonacci(n-1)
    
fibonacci(4)
        


# In[ ]:


## Assign a different name to function and call it through the new name
 
def my_function(x,y):
    addition= x+y
    return addition
user_input=my_function(12,12)
print("Addition of two numbers:",user_input)


# In[3]:


## Generate a Python list of all the even numbers between 4 to 30
a=4
b=30
li=[]
for i in list(range(a,b+1)):
    li.append(i)
even_num = list(filter(lambda x: x%2==0,li)) 
print(even_num)


# In[4]:


## Find the largest item from a given list
lis=[12, 34, 56, 3, 100, 12]
print("largest no in list: ",max(lis))


# In[ ]:




