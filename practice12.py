# 12. Debugging the program.Finding errors in program

# a= input("value")
# b = a/2
# print(a,b)



# operand (/) should be suitable for 'int' not 'str'
# if we write,                  a= input("value")      here, the int is not actually defined.
# TYpeError : saying "unsupported operand type(s) for /: 'str' and 'int' "
 
# instead it should be code as, a= int(input("value"))

a= int(input("value"))
b = a/2
print(a,b)
