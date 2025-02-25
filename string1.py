#string programing 
#types of string 
print("Hello word !")
print('hello word !')
print("""This is my car , 
i'm from Lower dir maidan ,
i'm a student of computer science !""")
# accessing of character 
name="python"
print(name[0])
print(name[1])
print(name[2])
# slicing the string 
taxt="python from youtub !"
print(taxt[0:6])
# string concatenation 
str1="Hello"
str2="word"
result=str1+" "+str2
print(result)
# length of string 
taxt="python"
print(len(taxt))
# Metheds of strings 
# Lower 
text="HELLO"
print(text.lower())
# upper 
text="hello"
print(text.upper())
#removes space from first of the line now here is it . 
# strip
text="  hello hello  python"
print(text.strip())
# replace 
text="hello world"
print(text.replace("world","python"))
# split 
text="hello world"
print(text.split())
# string formating 
name = "Taj ul islam"
age  = 21
print(f"My name is {name}, my age is {age}")
#escape charactes 
#\n new line 
#\t Tab 
#\\ backslash
#\" double quote
print(" ")
name="hello\npython"
name1="hello\tpython"
name2="hello \\ python"
name3="hello \" python"
print(name)
print(name1)
print(name2)
print(name3)
# checking substrins 
text = "hello world "
print("d"in text)
#string immutability 
# blow both programes give me errer .
name="taj ul islam "
name5=name[0]="T"
print(name5)

name="taj ul islam "
name[0]="T"
print(name[0])

