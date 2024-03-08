import time
# make timer work
print("jambo!")
uname = input("yourname")
ustring = input("") or "noustring"
x = int(input("testinputx"))
y = int(input("testinputy"))
print (x , y)
print (x*y)
print (type(x))
print (id(y))
print ("end")
print (ustring)
time.sleep(5)
print (uname)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

j = int(input("j"))
print(thislist[j])

import tkinter
top = tkinter.Tk()

input("press enter to continue")
