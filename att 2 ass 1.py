#TANAYA SAWAJI
"""
assignment 1 : Find the area of the circle
"""

CONSTANT_PI = 3.14
radius = float(input("enter the radius of the circle :"))
area = CONSTANT_PI * radius**2 


print("the area of the circle is :", area)
print("End of the program")

print("part TWO")

filename=input("Write the file name :")
f_exts=filename.split(".")
print("the extension of the file is :" + repr(f_exts[-1]))

print("the end")