name = "Noha Shehab"
# this a comment
"1- get the len of the string "
print(len(name))

"2- get access to the part of the string "
print(name[6])
print(name[2:7])  # get chars from 2 to 6

print(name[-1])

"3- count number of chars in a string "
print(name.count('a'))

"4- get index of a char in a string ? "
print(name.index("h"))  ## get the index of the first occurrence of the char in the string

########################### functions you can with the string
" string interpolation "
fname = 'Noha '
midname = 'Abdelhady '
lname = 'Shehab'

"concat the string"
# fullname = fname + midname + midname + lname
# print(fullname)


fullname = fname + midname*2 + lname
print(fullname)

"6- captilize"
msg = "i lives in cairo "
print(msg.capitalize())
print(msg.upper())
print(msg.lower())

"6- check if the string upper or lower"
instructorname = "NOHA"
print(instructorname.islower())
print(instructorname.isupper())

"7- check value in the string .... "
"----- check if the value numeric or not "
year = '2022'
print(year.isdigit())

name = 'nohaaa'
print(name.isalpha())  # chek if the string contains only alphas from a-z

mystr = '                       '
print(mystr.isspace())

"8- replacement "

# sentence = "My name is Noha, I works at iti"
# # replace o ---> 0
#
# sentence = sentence.replace("o", "0")  # replace string with another string
# print(sentence)
#
# # a === > @
#
# print(sentence.replace("a", '@'))
#
# print(sentence.replace("e", "4"))

"9- format "

info = "Ahmed lives in {0} and studies at {1}"
print(info.format("Cairo", "iti"))
print(info.format("Alex", 'MUST'))

info = "Ahmed lives in {cityname} and studies at {uni_name}"

print(info.format(uni_name="Engineering", cityname="Alex"))



############

username = input("please enter your name ,,,, : ")  # input must return with string
print(username)
if username.isdigit():
    username = int(username)
else:
    print("---- not allowed ? ---- ")







