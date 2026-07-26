# Python Program to Calculate the Average of Numbers in a Given List

#                                   if the valuse is given
number = [5,64,5,78,5,4,33,5,64,4,]
large = max(number)
print("largest number is :",large) 



#                                  if tha values is not given
numbers = []
count = int(input ("how many numbers:"))
for i in range(count):
    num = int(input("enter the numbers:"))
    numbers.append(num)
largest = max(numbers)  
print("largest number is :",largest)


