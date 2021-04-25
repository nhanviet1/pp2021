def NoS():
    NoS = int(input("The number of students: "))
    return NoS

DoSI = {}
def getId(id):
    DoSI[id] = [id] 

def SI():
    print("Enter Student Infor")
    name = str(input(" Name : "))
    id = input(" ID : ")
    Birthday = input(" Birthday : ")
    getId(id)
    A = {"name":name,"id":id,"birthday":Birthday}
    return A

#course 
def NoC():
    NoC = int(input("The number of Course: "))
    return NoC    

def CI():
    print("Enter Course Infor")
    name = str(input(" Name : "))
    id = input(" ID : ")
    B = {"name":name,"id":id}
    return B

#show
def ShowS(ListS):
    for i in ListS:
        print(i)
#mainS
ListS = []
amount = NoS()
for i in range (0,amount):
    NS = SI()
    ListS.append(NS)
        
def ShowC(ListC):
    for i in ListC:
        print(i)

#mainC
ListC = []
amountC = NoC()
for i in range (0,amountC):
    NC = CI()
    ListC.append(NC)
    
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
idcheck = input(print("Enter the Mark: ")) 