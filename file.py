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
