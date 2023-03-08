"""
2_types.py
--------

This the 'doc-string' for the module 2_types.py.

When you assign a value to a variable, python is able to immediately identify
what type the variable is, and assigns it to a CLASS of that type, exposing
the variable to various methods that allow you to manipulate the value
contained within the variable.

"""

# Here, we assign a string to a variable. As a result, we have instant access
# to various methods contained within the 'String' class, including the ability
# to capitalise the first letter of the string.

THIS_IS_A_STRING = "a"
print(THIS_IS_A_STRING.capitalize())

###############################################################################
# Uncomment line 39 below and try and run the program again.                  #
#                                                                             #
# Python throws an error. Let's disect the error:                             #
#                                                                             #
# 1 - Traceback (most recent call last):                                      #
# 2 -   File "2_types.py", line 39, in <module>                               #
# 3 -     print(this_is_a_number.capitalize())                                #
# 4 - AttributeError: 'int' object has no attribute 'capitalize'              #
#                                                                             #
# 1: This is the start of the error, where the error has been traced to.      #
# 2: This is the file and the line of the error (in this case, line 39)       #
# 3: This is the exact line of code which the error has been traced back to.  #
# 4: This is the type of error (AttributeError), and a an explanation         #
# In this instance, it's telling you an integer (1) can't be capitalized.     #
###############################################################################

THIS_IS_A_NUMBER = 1
# print(THIS_IS_A_NUMBER.capitalize())

###############################################################################
# You can also manipulate variables through other means such as addition      #
# and subtraction. This can be done through multiple variables, or variables  #
# and explicit values                                                         #
###############################################################################

# INTEGERS
print(THIS_IS_A_NUMBER + 2)
THIS_IS_ALSO_A_NUMBER = 3
COMBINED_NUMBER = THIS_IS_A_NUMBER + THIS_IS_ALSO_A_NUMBER
print(COMBINED_NUMBER)

# STRINGS
print(THIS_IS_A_STRING + "b")
THIS_IS_ALSO_A_STRING = "bracadabra"
COMBINED_STRING = THIS_IS_A_STRING + THIS_IS_ALSO_A_STRING
print(COMBINED_STRING)

###############################################################################
# The most basic types are strings and variables, but we also have lists,     #
# sets, and dictionaries in python. They all have their intended purpose,     #
# which we can cover off in more detail later, but here are some examples.    #
# Similar to strings and integers python packages the types in their relative #
# classes to give you out-of-the box functionality depending on the type of   #
# the variable                                                                #
###############################################################################

# LISTS
LIST_1 = [1, 2]
LIST_2 = [3, 4]
print(f"Combined list: {LIST_1 + LIST_2}")

# You can locate items in a list via its index
# Indexes in python start from 0 (the first position)
# Below we use the in-built list method (.index) to find a value's index

print(f"The index of the number 3 is: {(LIST_1 + LIST_2).index(3)}")

# And then below we use the index to retrieve that value from the list
print((LIST_1 + LIST_2)[2])

# As you can see above, I'm combining the two lists and wrapping that
# In circular brackets. The results contained within the () are essentially
# a new variable, and you can utilise this as if it were its own named
# variable. This is the equivalent to the below:
LIST_3 = LIST_1 + LIST_2
print(LIST_3[2])


# You can nest lists, which means the a list can contain a list.
# Also note that lists are not type sensitive, which means they
# can contain any type as values within the list.

NESTED_LIST = [1, "a", [2, "b"]]
print(
    f'''
-----------------------------------------------------------
This is the combined list: {NESTED_LIST}
The third item in this list is a list: {NESTED_LIST[2]}
The the second item in that list is : {NESTED_LIST[2][1]}
-----------------------------------------------------------
'''
)

# DICTIONARY
# dict_1 = {"hello": "Hello"}
# dict_2 = {"goodbye": "Goodbye"}
# print(dict_1 + dict_2)
