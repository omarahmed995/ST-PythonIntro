username=input("please enter your name :")
print("the name is ", username ,"the length of letters is :")
print(len(username))
print("the number of o is",username.count('o'))
if len(username) >=6 :
 print(username[6])
else:
    print("no char at index 6")


r = float(input("Enter Radius of Circle: "))
circumference = 2 * 3.14 * r
area = (r**2)*3.14
print("Area = ", area)
print("Circumference of a Circle ", circumference)


length = float(input("Please Enter the Length of a Triangle: "))
height = float(input("Please Enter the Width of a Triangle: "))
area = length * height
print("The Area of a Rectangle using", length, "and", height, " = ", area)

firstname=input("enter first name :")
lastname=input("enter last name :")
fullname="{} {}".format(firstname,lastname)
print(fullname.capitalize())





