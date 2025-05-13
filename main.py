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

koha_aktuale1 = datetime.datetime.now().date()

print(koha_aktuale1)

koha_aktuale2 = datetime.datetime.now().time()

print(koha_aktuale2)

data=datetime.date(2024,5,12)
print(data)
time=datetime.time(12,23,44,23415)
print(time)

duration=datetime.timedelta(days=5 ,hours=3)

new_Day=koha_aktuale + duration

print(new_Day)

bday=datetime.timedelta(days=7302)

bday1=koha_aktuale1 - bday

print(bday1)



koha2 = datetime.timedelta(days=100)
data2 = datetime.datetime.now()  # or any datetime object
future_date = data2 + koha2
future_date1 = data2 - koha2

with open(file_path, "w") as file:
    file.write("Koha: " + str(future_date))
with open(file_path, "w") as file:
    file.write("Koha: " + str(future_date1))




with open(file_path,"r")as file:
    content=file.read()
    print(content)