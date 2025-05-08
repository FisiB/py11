file_path="C:/Users/Student/Desktop/py11/leximi.txt"
path=open(file_path,"r")
content=path.read()
print(content)
with open(file_path,"r")as file:
    content=file.read()
    print(content)

with open(file_path,"r")as file:
    line1=file.readline()
    print(line1)

with open(file_path, "w")as file:
    file.write("Hello World")

with open(file_path,"r")as file:
    file.seek(1)
    data=file.read()
    print(data)

    