
#Write a python program to find area of triangle?

a = int(input("Enter the Length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))
# using the heron's formula to calculate the semi perimeter.
s = (a+b+c)/2
# calculate the area of the triangle
Area =  (s*(s-a)*(s-b)*(s-c)**0.5)
print("The area of the triangle is %0.2f" %Area)
