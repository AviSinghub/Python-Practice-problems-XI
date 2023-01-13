# 10. Finding errors in program. Debugging 

# val = input("Enter a value:")
# nval= val + 3
# print(nval)

# we get an error if we don't place 'int' at the variable container. in Ln1
# TypeError: can only concatenate str (not "int") to str

val = int(input("Enter a value:"))
nval= val + 3
print(nval)

