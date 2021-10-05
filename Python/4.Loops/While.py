'''
    Python Loops
    
    While Loop - It is used to execute a block of statements repeatedly until a given a condition is satisfied.
'''

'''
    Syntax:

    while expression:
        statement(s)
'''

# Example
print("Example 1")

count = 0
while (count < 3):
	count += 1
	print("Hello World!!!")



'''
    Single Line Syntax

    while expression: statement
'''

# Example
print("\nExample 2")

count = 0
while (count < 3): count += 1; print("Hello World!!!")     # infinite loop




'''
    Nested While Loops

    while loop inside a while Loop
'''

'''
    Syntax

    while expression:
        while expression:
            statement(s)
        statement(s)
'''


# Example Pattern Print
print("\nExample 3")

i = 1
while i <= 5 :
    j = 1
    while j <= i:
        print("*", end = " ")
        j += 1
    print()
    i += 1