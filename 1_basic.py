'''
1_basic.py
--------

This the 'doc-string' for the module 1_basic.py.

Doc-strings can be found at the top of a module, or at the top line of a
function, class, or method.

Doc-strings are used to 'peek' into modules/functions when importing and
using them in other files.
'''

# You can comment a python file by starting the line with a '#')
# Comments can also be placed at the end of a line of code

# Variables are created by defining a name and assigning a value.
NUMBER_VARIABLE = 2
LETTER_VARIABLE = "a"

# You can print variables or values to the console in various ways
# Printing a raw value such as a 'string'
print("These are how many variables there are:")
# Or printing the variable directly
print(NUMBER_VARIABLE)
# You can also pass multiple comma separated values to a print statement
print("This is the value of the Letter Variable:", LETTER_VARIABLE)

# Variables in python aren't 'strictly typed', nor are they constant...
# This means if you assign a number to a variable, you can overwrite
# That variable, and to any type you want (string to number)
NUMBER_VARIABLE, LETTER_VARIABLE = LETTER_VARIABLE, NUMBER_VARIABLE

# Another common way of printing values is to use 'f strings':
print(
    f"Number Variable: {NUMBER_VARIABLE} \nLetter Variable: {LETTER_VARIABLE}"
)

# You can also comment out lines of code (which prevents execution) by
# starting the line with a #

# print("This has been commented out")

#############################################################
# To run this file, type 'python 1_basic.py' in the terminal.#
#############################################################
