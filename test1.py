import os



print("sample file commands")

print("directory list:")
dlist = os.listdir()
print(dlist)
print("---")

filename = input("filename?")
fo = open(filename, "a+")
addtext = input("addtext")
addtext = addtext + "\n"
fo.write(addtext)
fo.close()
fo = open(filename, "r")
newdoc = fo.read()
print (newdoc)
input("press enter to continue")

# windows path
# c:\Users\james.foley\Documents\CSStest\python>
# cd \Users\james.foley\Documents\CSStest\python