'''
    Python Loops
    
    for Loop - It is used for sequential traversal
'''

'''
    Syntax:

    for iterator_var in sequence:
        statements(s)
'''


# Example
print("Example 1")

for i in range(0, 4):   # range(start, stop+1)
	print(i)





'''
    Single Line Syntax

    for iterator_var in sequence: statements(s)
'''

# Example
print("\nExample 2")

for i in range(3): print(i) # In range -> by Default start = 0

# Example
print("\nExample 3")

print([i**2 for i in range(4)])




'''
    Nested For Loops

    for loop inside a for Loop
'''

'''
    Syntax

    for element in sequence 
        for element in sequence:
            body of inner for loop
        body of outer for loop
'''

# Example Pattern Print
print("\nExample 4")

rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')