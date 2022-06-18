#Q1.
#Take input from the user for the string they want to reverse
inp_string = input("Enter the string you want to reverse.\n")

#Reverse the string using string operation
output = inp_string[::-1]

#Print the output
print(output)

#Q2.
print("Program prints all Numbers in a Range Divisible by a Given Number.")

"""Take the range by asking the user for two numbers
that will be the starting and end points for the range"""

start_range = int(input("Enter starting number of range\n"))
end_range = int(input("Enter ending number of range\n"))

#User enters the number for which they want to check divisibilty for
divisibe_number = int(input("Enter number for which you want to check divisibilty\n"))


#Use for loop to print numbers in a range divisible by given Number.

for number in range(start_range, end_range):
    if number % divisibe_number == 0:
        print(number)

#Q3.
#First we check if the sides of the triangle make a triangle

#User inputs three sides

side1 = int(input("Enter length 1\n"))
side2 = int(input("Enter length 2\n"))
side3 = int(input("Enter length 3\n"))

a = side1 + side2
b = side2 + side3
c = side1 + side3


#If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle.
#Checking for this condition
check_1 = a > side3
check_2 = b > side1
check_3 = c > side2

#Checking if the three conditions are true or false

triangle_check = str(check_1 & check_2 & check_3)

#Use Heron's formula if the sides form a triangle
s = round((side1 + side2 + side3) / 2)
ar_square = s * (s - side1) * (s - side2) * (s - side3)


if triangle_check == "True":
    area = (ar_square) ** (1/2)
    #Round off the result for a more understandable output
    area_print = round(area)
    #Print the area if sides form a triangle
    print("Area of the triangle is", area_print, "square units")

else:
    print("These sides do not form a triangle.")

#Q4.
#Use string formatting to print the required output
string = "*"

"""Starting with n = 5, we make a for loop for a number in range n,
since we want nested for loop, we make another loop inside in which the range
is the number (whose earlier range was defined as n)
Using string formatting to print the required output"""
n = 5
for number in range(n):
    for nested_no in range(number):
        print(string, end=" ")
    print(" ")    


for number in range(n , 0, -1):
    for nested_no in range(number):
        print(string, end=" ")
    print(" ")    

#Q5.
st = 'A'
for i in range(int(input(Enter number of rows: ))):
    for j in range(i+1):
        print(st, end="")
        if st == 'Z':
            st = 'A'
        else:
            st = chr(ord(st) + 1)
    print()

#Q6.
"""Take the range by asking the user for two numbers
that will be the starting and end points for the range"""

start_range = int(input("Enter start of range:\n"))
end_range = int(input("Enter end of range:\n"))


#Create three cases for if numbers are starting from 0, 1, or some other number

""" Divide the numbers by the numbers preceding them,
if they are divisible, they are not prime.
So, everytime a number is divisible, increase the value of a variable,
if the variable remains zero, the number is prime """


print("Prime numbers in the range are:")
#Since we know 0 and 1 are not prime, we start from 2.
if start_range == 0:
    for number in range(start_range + 2, end_range+1):
        check = 0
        for divide_check in range(2, number):
            if number % divide_check == 0:
                check += 1
        if check == 0:
             print(number)
    
elif start_range == 1:
    for number in range(start_range + 1, end_range+1):
        check = 0
        for divide_check in range(2, number):
            if number % divide_check == 0:
                check += 1
        if check == 0:
             print(number)
    
else:
    for number in range(start_range , end_range+1):
        check = 0
        for divide_check in range(2, number):
            if number % divide_check == 0:
                check += 1
        if check == 0:
            print(number)

#Q7.
#Take range from 1 to 500.
#Then use if else with and operator to print the numbers divisible by 7 and 11.

print("Numbers which are multiple of 7 and divisible by 11 in the range 1-500 are:")
for number in range(1, 500):
   if number % 7 == 0 and number % 11 == 0:
       print(number)

#Q8.
#Take 10 integers as input from user.

int_1 = int(input("1st integer: "))
int_2 = int(input("2nd integer: "))
int_3 = int(input("3rd integer: "))
int_4 = int(input("4th integer: "))
int_5 = int(input("5th integer: "))
int_6 = int(input("6th integer: "))
int_7 = int(input("7th integer: "))
int_8 = int(input("8th integer: "))
int_9 = int(input("9th integer: "))
int_10 = int(input("10th integer: "))

#Make a list of the integers, so that it is easier to traverse them for operations in loop
integer_list = [int_1, int_2, int_3, int_4, int_5, int_6, int_7, int_8, int_9, int_10]

#Applying simple if else statements to print required outputs

#Part (a)
print("Positive numbers are:")
for number in integer_list:
    if number > 0:
        print(number)

#Part (b)
print("Negative numbers are:")
for number in integer_list:
    if number < 0:
        print(number)

#Part (c)
print("Odd numbers are:")
for number in integer_list:
    if number % 2 != 0:
        print(number)

#Part (d)
print("Even numbers are:")
for number in integer_list:
    if number % 2 == 0:
        print(number)

#Part (e)
""" Assign number of occurances of an integer to a corresponding
variable and print the same."""
"""If an integer is repeating, we do not need to count it again, so
we will use if statements to print only if the integer is unique"""

count_1 = integer_list.count(int_1)
count_2 = integer_list.count(int_2)
count_3 = integer_list.count(int_3)
count_4 = integer_list.count(int_4)
count_5 = integer_list.count(int_5)
count_6 = integer_list.count(int_6)
count_7 = integer_list.count(int_7)
count_8 = integer_list.count(int_8)
count_9 = integer_list.count(int_9)
count_10 = integer_list.count(int_10)



print(int_1, "occurs", count_1, "times") 


if int_2 != int_1:
    print(int_2, "occurs", count_2, "times")
    
    
if int_3 != int_1 and int_3 != int_2:
    print(int_3, "occurs", count_3, "times")
    
    
if int_4 != int_1 and int_4 != int_2 and int_4 != int_3:
    print(int_4, "occurs", count_4, "times")
    
    
if int_5 != int_1 and int_5 != int_2 and int_5 != int_3 and int_5 != int_4:
    print(int_5, "occurs", count_5, "times")

    
if int_6 != int_1 and int_6 != int_2 and int_6 != int_3 and int_6 != int_4 and int_6 != int_5:
    print(int_6, "occurs", count_6, "times")
 
    
if int_7 != int_1 and int_7 != int_2 and int_7 != int_3 and int_7 != int_4 and int_7 != int_5 and int_7 != int_6:
    print(int_7, "occurs", count_7, "times")
    
    
if int_8 != int_1 and int_8 != int_2 and int_8 != int_3 and int_8 != int_4 and int_8 != int_5 and int_8 != int_6 and int_8 != int_7:
    print(int_8, "occurs", count_8, "times")
    
    
if int_9 != int_1 and int_9 != int_2 and int_9 != int_3 and int_9 != int_4 and int_9 != int_5 and int_9 != int_6 and int_9 != int_7 and int_9 != int_8:
    print(int_9, "occurs", count_9, "times")
    
    
if int_10 != int_1 and int_10 != int_2 and int_10 != int_3 and int_10 != int_4 and int_10 != int_5 and int_10 != int_6 and int_10 != int_7 and int_10 != int_8 and int_10 != int_9:
    print(int_10, "occurs", count_10, "times")

#Q9.
#Define an empty list
word_list = []
#Ask user for number of elements
number_of_words = int(input("How many words do you want in the list? "))


#Add words to the list
for count in range(0, number_of_words):
  word_list.append(input("Enter Word: "))

#ask the user for the word they want they want to count the number of occurrences

word_check = input("Which word do you want to check number of occurances for?: ")
no_of_occurance = word_list.count(word_check)


print(word_check, "occurs", no_of_occurance, "times in list")

            
        


