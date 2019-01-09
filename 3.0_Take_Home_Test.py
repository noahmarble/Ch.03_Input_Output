'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Noah Mable



1. Write a line of code that will print your name.
'''
print("noah mable")

'''
2. How do you enter a comment in a program?

'''
#this is a comment

'''
3. What is the ouput of the following lines of code?
print (2/3)
print (2//3)
0.66666666666666
0
'''


'''
4. Write a line of code that creates a variable called pi and sets it to an
appropriate value.

'''
pi = 3.14

'''
5. Why does this code not work?
A=22
print(a)
a is not defined
'''



'''
6. All of the variable names below can be used. But which of these is the best?
a
A
Area
AREA
area
areaOfRectangle
AreaOfRectangle         this it describes the variable well and is consistant capitolization
'''


'''
7. Which of these variables names are not allowed in Python?
apple
Apple
APPLE
Apple2
1Apple                  this
account number          this
account_number
account.number          this
accountNumber
account#                this
'''



'''
8. Why does this code not work?

print(a)
a=45
a is defined after it is asked to print
'''



'''
9. Write a line of code that will ask the user for the length of a square's
side and store the result in a variable. Make sure to convert the value
to an integer.
'''
side = int(input("length of a square: "))

'''
10. Write a line of code that prints the area of the square, using the
number the user typed in that you stored in question 9.
'''
print("area of a sqaure: ",side*side)


'''11. Do the same as in questions 9 and 10, but with the formula for the
area of an ellipse. Area=pi*a*b where a and b are the lengths of the major radii.
'''
radious1 = int(input("lenth of a radious: "))
radious2 = int(input("lenth of another radious: "))
area = pi*radious1*radious2
print("area of an elipse given the previous radiouses: ",area)


'''
12. Do the same as in questions 9 and 10, but with a formula to find
the pressure of a gas. PV=nRT where n is the number of moles, T is the absolute temperature, V is the
volume, and R is the gas constant 8.3144.
'''
volume = int(input("volume: "))
numberofmoles = int(input("number of moles: "))
R = 8.3144
absolutetempreture = int(input("absolute tempreture: "))
pressure = (numberofmoles*R*absolutetempreture)/volume
print("pressure is: ",pressure)
'''
13. Explain the mistake in this code:

pi = float(3.14)
the float is unessasary
'''



'''
14. Assume radius has been defined. This code runs, but isn't very good. Explain the mistake in the following code:

x=3.14
pi=x
area=pi*radius**2
you can just set pi to 3.14
'''


'''
Assuming x and y are already defined, this code runs. But
something isn't quite right. Explain the mistake in the following code:

a=((x)*(y))
you can simpily use a = x*y
'''


'''
16. Explain the mistake in the following code:

radius = input(float("Enter the radius:"))
you need to float the input not the string, should be like this
radius = float(input("Enter the radius:"))
'''


