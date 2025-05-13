import datetime 
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


koha_aktuale = datetime.datetime.now()

print(koha_aktuale)

print("Year:",koha_aktuale.year)
print("Month:",koha_aktuale.month)
print("Day:",koha_aktuale.day)
print("Hour:",koha_aktuale.hour)
print("Minute:",koha_aktuale.minute)
print("Second:",koha_aktuale.second)
print("Mikroseconds:",koha_aktuale.microsecond)
    