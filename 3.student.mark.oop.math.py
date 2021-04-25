import math
#function
def NoS():
    NoS = int(input("The number of students: "))
    return NoS
def NoC():
    global NoC
    NoC = int(input("The number of course: "))
    return NoC
DoSI = {}
def getId(id):
    DoSI[id] = [id]
    
def ShowS(ListS):
    for i in ListS:
        print(i)
        
def ShowC(ListC):
    for i in ListC:
        print(i)
              
class student():
    def __init__(lmeow, name, id, birthday):
        lmeow.name = name
        lmeow.id = id
        lmeow.birthday = birthday
    
    #set
    def setName(LmeowS, name):
        LmeowS.name = name
    def setId(LmeowS, id):
        LmeowS.id = id
    def setBirthday(LmeowS, birthday):
        LmeowS.birthday = birthday
        
    #get
    def getName(LmeowX):
        return name
    def getId(LmeowX):
        return id
    def getBirthday(LmeowX):
        return birthday
    
        
class course():
    def __init__(lmeow, name, id):
        lmeow.name = name
        lmeow.id = id
    
    #set
    def setName(LmeowS, name):
        LmeowS.name = name
    def setId(LmeowS, id):
        LmeowS.id = id
        
    #get
    def getName(LmeowX):
        return name
    def getId(LmeowX):
        return id



#makinglist

    
#main
ListS = []
ListC = []

amountS = NoS()
for i in range (0, amountS):
    print("enter the student's info " + str(i + 1))
    name = input("Name: ")
    id = input("ID: ")
    getId(id)
    birthday = input("birthday: ")
    Lmeow = student(name, id, birthday)
    X = (Lmeow.getName(), Lmeow.getId(), Lmeow.getBirthday())
    ListS.append(X)
    
amountC = NoC()
for i in range (0, amountC):
    print("enter the course's info " + str(i + 1))
    name = input("Name: ")
    id = input("ID: ")
    Lmeow = course(name, id)
    Y = (Lmeow.getName(), Lmeow.getId())
    ListC.append(Y)
print("List of students: " )  
ShowS(ListS)
print("List of courses: " )
ShowC(ListC)
print(DoSI)
#markpart...
idcheck = input(print("Enter the ID: ")) 
while True:
    if idcheck not in DoSI:
        idcheck = input(print("Enter the ID again: "))
    else:
        break
def blyat(Mark):
    M4rk = math.floor(Mark)
    print("mark = " + str(M4rk))
print("Enter the Mark: ")
Mark = input()
Mark = float(Mark)
blyat(Mark)

'''def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

print("The average is", cal_average(Mark))'''