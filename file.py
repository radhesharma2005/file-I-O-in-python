#Python can be used for perform operations on file.(read and write)
#Types of files
# 1)text files :- .txt, .docx, .log etc
# 2)Binary files :-.mp4, .mov, .png, .jpeg etc
 # SYNTAX of file
# We have to open a file before reading or writing in file
#  f=open("filename","mode")

# filenmae : - sample.txt ,demo.docx
# mode : - r :- read , w:- write

# f.read():- to read only function from file
# f.close():- to close the file

f = open("C:/Users/sharm/Desktop/radhe.txt", "r")
data=f.read()
print(data)
print(type(data))
f = open("C:/Users/sharm/Desktop/radhe.txt", "r")
line1=f.readline()
print(line1)
f.close()
#READING a file

# data=f.read()  #read entire file
# data=f.readline()  #read one line at a time
 #data =f.read(5)   # reads only 5 letters


#Writing in File 

#f=open("demo.txt","w")    #overwrites data in file
#f.write("this is a new line")

#f=open("demo.txt","a")      #append line in file or adds newline in file
#f.write("this is a new line")


f = open("C:/Users/sharm/Desktop/radhe.txt", "w")
f.write("I am learning python")
f = open("C:/Users/sharm/Desktop/radhe.txt", "a")
f.write("\nI am learning java")
f=open("C:/Users/sharm/Desktop/radhe.txt","r")
content=f.read()
print(content)

#lets understand the concept of r+,w+
# r+ :- overwrite the data from the start, in this we can read and the write the data too. (read+overwrite)
#       pointer is at start) , no  truncate 
#Example 
f=open("C:/Users/sharm/Desktop/radhe.txt","r+")
f.write("This is a sample text file.")
print(f.read())
f.close()

#w+ :- used for reading and writing the data from start but the data is fully truncated (empty and start the new content)
f=open("C:/Users/sharm/Desktop/radhe.txt","w+")
#f.write("This is a sample text file.")
print(f.read())
f.write("Radheshyam Sharma")
f.close()

#a+ :- The stream is positioned at the end of the file (read+append) , no truncate ,pointer at the end.

f=open("C:/Users/sharm/Desktop/radhe.txt","a+")
#f.write("This is a sample text file.")
print(f.read())
f.write("Radheshyam Sharma")
f.close()

# With Syntax
with open("C:/Users/sharm/Desktop/radhe.txt","r") as f:
    data=f.read()
    print(data)
with open("C:/Users/sharm/Desktop/radhe.txt","w") as f:
    f.write("New Data filling.")

#Deleting a file
#using a module or a built in library in python 

# import os
# os.remove(filename)  ......Syntax for deleting

import os
with open("Sample.txt","w") as f:
    f.write("Hello")
os.remove("Sample.txt")

