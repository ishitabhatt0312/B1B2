#!/usr/bin/env python
# coding: utf-8

# Submitted by : Ishita Bhatt (590016198)
# ASSIGNMENT 1

# In[ ]:


Question 1 : write a python scripts that print your name, course name, and the python version you are using also execute the script from the command line and include a screenshot of the output


# In[1]:


import platform
# putting the value
name = "ISHITA BHATT"
course = "MCA with specialization in Cyber Threat Intelligence "

print("Name:", name)
print("Course:", course)
print("Python Version:", platform.python_version())


# In[ ]:


Question : Write a python program that takes user first name and last name as input and print them in reverse order with a space between them


# In[3]:


# first we need to ask the input from the user
first_name = input("Enter your first name ")
last_name = input("Enter your last name ")

# Printing the names in reverse order with a space in between
print(last_name + " " + first_name)


# In[ ]:


Question : Use at least two string methods and explain their purpose in the comments in python


# In[5]:


# I,will take the above code of first_name and last_name , in that i will use two methods of string

# 1  .string_variableName.upper()-> this method  convert the entire string to uppercase

first_name=first_name.upper()
last_name=last_name.upper()

# 2 Second i will use REPLACE method, removing spaces within name)
first_name = first_name.replace(" ", "")
last_name = last_name.replace(" ", "")

# Printing the names in reverse order with a space in between
print(last_name + " " + first_name)


# In[ ]:


Question 1 : Write a python program that takes an input numbers from the users, convert it to different numeric data types(integers,float,and complex),and displays the converted values


# In[7]:


I am taking the input from the user , which is in string format so that i can convert easily to different data type
user_input = input("Enter a number ")

# converting the user_input to different data type
integer_value = int(float(user_input))  
float_value = float(user_input)        
complex_value = complex(user_input)  

# printing 
print("Integer Value", integer_value)
print("Float Value", float_value)
print("Complex Value", complex_value#)


# In[9]:


# taking user input of length and width
length=int(input("Enter the length of rectangle-> "))
width=int(input("Enter the width of rectangle-> "))
area= length*width
print(area)


# In[11]:


# we will using format string method in python for the above code
# taking user input of length and width
length=int(input("Enter the length of rectangle-> "))
width=int(input("Enter the width of rectangle-> "))
area= length*width
print(f"The area of rectangle is {area:.2f}")


# In[13]:


# Taking user input for three numbers
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number "))
num3 = int(input("Enter the third number"))

# Calculate the average
calculate_average = (num1 + num2 + num3) / 3

# Print the average using % formatting 
print(f"The average of the three numbers is: %.2f" % calculate_average)


# In[ ]:


Write a python program that ask the user for a number and determine whether it is postive,negative or zero


# In[15]:


# user input 
number = float(input("Enter a number: "))

# checking if the number is positive, negative, or zero
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")


# In[ ]:


Implement a loop that continues to ask the user for a number until they enter exit
use break to exit the loop and continue to prompt for a new number if the input is not exits


# In[17]:


# Loop to asking again and again from the user
while True:
    user_input = input("Enter a number (or type 'exit' to quit) ")

    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break

    # Try to convert the input to a float
    # we will use exception handling , bcoz user can also different input
    try:
        number = float(user_input)
        
        # checking 
        if number > 0:
            print("The number is positive.")
        elif number < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
    except ValueError:
        print("Please enter a valid number or 'exit' to quit.")


# In[ ]:


Create a python script that takes two number as input and print whether both numbers are even or odd or one of each using relational and logical operators


# In[19]:


# user input 
num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))

# Checking  if both numbers are even or odd
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd")
else:
    print("One number is even and the other is odd")


# In[23]:


# user input 
number = int(input("Enter an integer "))

# Initialize variables for binary, octal, and hexadecimal representations
binary = ""
octal = ""
hexadecimal = ""

# Calculate binary representation using bitwise operators
for i in range(31, -1, -1):  # Assuming 32 bits for the integer
    # Check if the ith bit is set
    if number & (1 << i):
        binary += "1"
    else:
        binary += "0"

# Remove leading zeros for binary representation
binary = binary.lstrip("0") or "0"

# Calculate octal representation using bitwise operators
temp_number = number
while temp_number > 0:
    octal_digit = temp_number & 7  # Get the last three bits
    octal = str(octal_digit) + octal
    temp_number >>= 3  # Right shift by 3 to move to the next group of bits

# If the input number is 0, ensure the octal representation is "0"
if not octal:
    octal = "0"
# Calculate hexadecimal representation using bitwise operators
temp_number = number
while temp_number > 0:
    hex_digit = temp_number & 15  # Get the last four bits
    # Convert to hexadecimal character
    if hex_digit < 10:
        hexadecimal = str(hex_digit) + hexadecimal
    else:
        hexadecimal = chr(ord('A') + hex_digit - 10) + hexadecimal_representation
    temp_number >>= 4  # Right shift by 4 to move to the next group of bits

# If the input number is 0, ensure the hexadecimal representation is "0"
if not hexadecimal:
    hexadecimal = "0"

# Print the results
print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadecimal}")


# In[ ]:




