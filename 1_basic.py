# You can comment a python file by starting the line with a '#')
# Comments can also be placed at the end of a line of code

'''
You can leave a multi-line comment by typing three apostraphe's on either side of a comment.


Like this.

Comments are ignored by the script during execution.
'''

# Variables are defined by creating a name, and assigning the value through an = sign.
number_variable = 2
letter_variable = "a"

# You can print variables or values to the console in various ways
# Printing a raw value such as a 'string'
print("These are how many variables there are:")
# Or printing the variable directly
print(number_variable)
# You can also pass multiple variables/values to the print statement, seperated by a comma
print("This is the value of the Letter Variable:", letter_variable)

# Variables in python aren't 'strictly typed', nor are they constant...
# This means if you assign a number to a variable, you can subsequently overwrite
# That variable, and to any type you want (string to number)
number_variable, letter_variable = letter_variable, number_variable

# Another common way of printing values is to use 'f strings', which is demonstrated below.
print(
    f"Number Variable: {number_variable} \nLetter Variable: {letter_variable}"
)
