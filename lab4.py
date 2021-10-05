import random

array = []
for x in range(10): #create random array of length 10 with random numbers 1-20
    array.append(random.randint(1, 20))

total = 0
for x in array: #add up all numbers in an array
    total += x
mean = total / len(array) #calculate mean

smallest = 21
for x in array: #iterate through array
    if x < smallest: #find smallest
        smallest = x
index = array.index(smallest)
print("The array is: ", array, "\nThe mean of the array is: ", mean, "\nThe smallest element in the array is: ", smallest, " and the index is: ", index)

#----------------------------------------------------------------

input = int(input("Please input an int: "))
numbers = []
print(input)

while input != 0: #iterate through the number by division
    numbers.append(int(input % 10))
    input -= input %10
    input /= 10
numbers.reverse()
print (numbers)

#----------------------------------------------------------------

array1 = []
array2 = []

for x in range(10): #create two random arrays of length 10 with random numbers 1-20
    array1.append(random.randint(1, 20))
    array2.append(random.randint(1, 20))

array1.sort()
array2.sort()

print("Array 1: ", array1)
print("Array 2: ", array2)

array3 = []
leng = len(array1) + len(array2)
while len(array3) != leng: #While the array is not filled...
    if(len(array2) != 0 and len(array1) != 0 and array1[0] <= array2[0]): #make sure that neither of the arrays are empty and check which array has the smallest number
        array3.append(array1[0])
        array1.pop(0)
    elif(len(array1) != 0 and len(array2) != 0 and array1[0] > array2[0]): #make sure that neither of the arrays are empty and check which array has the smallest number
        array3.append(array2[0])
        array2.pop(0)
    elif(len(array1) == 0): #array 1 is empty, fill from array 2
        array3.append(array2[0])
        array2.pop(0)
    elif (len(array2) == 0): #array 2 is empty, fill from array 1
        array3.append(array1[0])
        array1.pop(0)
print("Final array: ", array3)