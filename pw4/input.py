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