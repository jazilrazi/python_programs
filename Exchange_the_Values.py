# Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable

#                                      if the values is given

value_one = 10
value_two = 20
print("Value one Before Exchange",value_one)
print("Value two Before Exchange",value_two)

value_one = value_one + value_two
value_two = value_one - value_two
value_one = value_one - value_two

print("Value one After Exchange",value_one)
print("Value two After Exchange",value_two)

#                                   if the values is not given

value_1 = int(input("enter the number:"))
value_2 = int(input("enter the number:"))

value_1 = value_1 + value_2
value_2 = value_1 - value_2
value_1 = value_1 - value_2

print("Value one After Exchange",value_1)
print("Value two After Exchange",value_2)