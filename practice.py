with open("practice.txt","w") as f:
    f.write("Hi everyone")
with open("practice.txt","a") as f:
    f.write("\nwe are learning file I/O")
with open("practice.txt","a") as f:
    f.write("\nusing python")
with open("practice.txt",'a') as f:
    f.write("\nI like programming in Python")
with open("practice.txt","r") as f:
    data=f.read()
    print(data)


#or alternative
def check_for_word():
     with open("practice.txt","w") as f:
          f.write("Hi everyone\nwe are learning file I/O\nusing python\nI like programming in python")

     with open("practice.txt","r") as f:
          data=f.read()
          new_data=data.replace("python","Java")
          print(new_data)
     with open("practice.txt","w") as f:
          f.write(new_data)
          word="learning"
     with open("practice.txt","r") as f:
          data=f.read()
          if(data.find(word)!=-1):
               print("Found")
          else:
               print("Not found")
check_for_word()


def check_for_line():
     word="learning"
     data=True
     line_no=1
     with open("practice.txt","r") as f:
          while data:
               data=f.readline()
               if(word in data):
                    print(line_no)
                    return
               line_no+=1
     return -1         
check_for_line() 
count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if data[i] == ",":
            if num: 
                number = int(num)
                print(number)
                if number % 2 == 0:
                    count += 1
            num = ""
        else:
            num += data[i]
print("Even count =", count)

#alternate way

count=0
with open("practice.txt","r") as f:
     data=f.read()
     nums=data.split(",")
     for val in nums:
          if(int(val)%2==0):
               count+=1
print(count)