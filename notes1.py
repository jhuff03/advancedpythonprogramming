import random

# Functions and Scope
# First --> Don't drop all the good programming habits you have from java
#           So don't use globals when instead you should be passing parameters
# You should keep your functions seperate from other code

"""
Don't do this....

Code
code

function

code
code
"""


"""
Do this instead

function
function

code
code

"""


def exampleFunction( a , b ):
    return a + b

def arrayMod( a ):
    a[0] = 10


c = exampleFunction( 2 , 3 )
print( c )

d = [ 3 , 5 , 8 ]   #note lists you surround with [ ] not { }
print( d )
arrayMod( d )
print( d )


"""
Whats the difference between an Array and List?
- To use an Array, you must import NumPy package
- Arrays can only store the same data type
- Arrays need to be declared
- Arrays are great for storing data more efficiently
- Arrays are great for numerical operations

    Such as I can divide the whole array by a number with a single operation

Lists - effectively you can think of them as ArrayLists from Java
- We will be using Lists to do all our work
- You are welcome to use Arrays, but I am not going to focus on teaching them


Tuples - we wont use, but what are they?
- They are a collection which is unchangeable once created
- Indicate tubles by using ( ) instead of [ ]


"""

arr = []
for i in range( 10 ):
    arr.append( random.randint( 1 , 10 ) )
print( arr )

# accessing individual data is the same, with the exception of
# negative indexing
# -1   --> access last data
# -2   --> access second to last data

print( arr[0] )
print( arr[-2] )


# you can access group of data using ranges
print( arr[2:4] )  # 2 - 3

# looping over lists is like for each

for element in arr:
    print( element )

# to access indexes
for i in range( len(arr) ):
    print("index=",i,"element=",arr[i])