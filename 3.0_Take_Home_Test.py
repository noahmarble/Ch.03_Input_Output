'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Noah Mable
1. Write a line of code that will print your name.
'''
print("Noah Mable")

'''
2. Write a program that asks someone for their name and then prints their name to the screen?
'''
name = input("what is your name:")
print("my name is: ",name)
'''
3. Predict the ouput of the following lines of code and then test them? Write down your prediction and the output.
print (17/9)        1.88889
print (17//9)       1
print (17%9)        1, actual is 8
'''
print (17/9)
print (17//9)
print (17%9)
'''
4. Write a a program where a user enters a base and height and you print the area of a triangle.
'''
base = int(input("base: "))
height = int(input("height: "))
area= base/2*height
print ("area: ", int(area))
'''
5. Change this program so it works.
A=May the Force be with you!
print(a)
'''
A="May the Force be with you!"
print(A)



'''
6. Write a line of code that will ask the user for the length of a square's
side and then print the area of the square
'''
s=int(input("length of a side: "))
print("area:", s*s)

'''7. Ask a user for the length of radii of an ellipse and then print its area. 
Area=pi*a*b where a and b are the lengths of the major radii.
'''
r=int(input("radii:"))


'''
8. Ask a user for moles, volume and temperature of a gas and print out the pressure. PV=nRT where n is the number of moles, T is the absolute temperature, V is the
volume, and R is the gas constant 8.3144.
'''
V= int(input("volume:"))
n= int(input("number of moles:"))
T= int(input("temp:"))
R=8.3144
print("presure=", int(n*R*T/V))
'''
9. Ask a user for an integer and then print the square root.
'''
import  math
number = int(input("give me a number:"))
answer = (math.sqrt(number))
print("this is the square root of that number:", answer)
'''
10. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma. Ask the user for mass and acceleration
and then print out the Force on one line and "Get it?" on the next.
'''
mass = int(input("May the mass times acceleration be with you!\n\rinput a mass:"))
acceleration = int(input("input an acceleration:"))
force = mass*acceleration
print("your force is:",force, "\n\rGet it?")


