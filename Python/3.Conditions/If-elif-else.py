'''
    If statement conditions

    If-else conditional statement is used in Python when a situation leads to two conditions and one of them should hold true.
    Python relies on indentation to define scope in the code
'''

'''
    Syntax:

    if (condition):
        code1
    elif (condition):
        code2
    else:
        code3
'''

# Example
print("Example 1")

a = 35
b = 20
if b > a:
    print("b is greater than a")
elif a > b:
    print("a is greater than b")
else:
    print("Both are Equal")




'''
    One Line Syntax

    # [on_true] if [expression] else [on_false]
'''

# Short Hand Example
print("\nExample 2")

a = 20
b = 35
print("A is greater") if a > b else print("B is greater")




'''
    and , or keywords

    Used to combine conditional statements

'''

# And Example
print("\nExample 3")

a = 200
b = 33
c = 500
if a > b and c > a:
    print("And is used when Both statements are true")



# Or Example
print("\nExample 4")

a = 200
b = 33
c = 500
if a > b or a > c:
    print("or is used when At least one of the conditions is True")





'''
    Nested IF 

    if statements inside if statements

'''

# Example
print("\nExample 5")

x = 41
if x > 10:
  print("Above ten," , end=" ")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")