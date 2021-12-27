f = open("newFile.txt", "r")
t = f.read()
print(t)
f.close()

a = open("file.txt", "r")
c = a.read()
print(c)
a.close()