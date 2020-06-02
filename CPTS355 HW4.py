def make_ttable(s1, s2):
    D = {}
    counter = 0
    while (counter < len(s1)):
        D[s1[counter]] = s2[counter]
        counter += 1
    return D
    pass
def trans(ttable, s):
    result = ""
    for c in s:
        if c in ttable:
            result += (ttable[c])
        else:
            result += c
    return result
    pass
def testtrans():
    ttable = make_ttable("abc", "xyz")
    revttable = make_ttable("xyz", "abc")
    if trans(ttable, "Now I know my abc's") != "Now I know my xyz's":
        return False
    if trans(revttable, trans(ttable,"Now I know my abc's")) != "Now I know mb abc's":
        return False
    if trans(ttable,'') != '':
         return False
    if trans(make_ttable('',''), "abc") != 'abc':
        return False
    return True
    


gColors = {"scapolite" : "yellow" , "helidor" : "yellow" , "topaz" : "blue" ,
           "zircon" : "blue" , "moonstone" : "blue" , "garnet" : "red" ,
           "aquamarine" : "blue" , "emerald" : "green" , "ruby" : "red" , "beryl" : "red"}

sColors = {"Pepsi" : "black" , "Coca-Cola" : "black" , "Mountain Dew" : "green" ,
           "Sprite" : "clear" , "Dr. Pepper" : "black" , "Sierra Mist" : "clear"}

cColors = {"WSU" : "red" , "UW" : "purple" , "WWU" : "blue" ,
           "EWU" : "red" , "CWU" : "red" , "OU" : "green" ,
           "OSU" : "orange" , "Gonzaga" : "blue" , "USC" : "red"}
           
def gemsbyColor(GemTable):
    result = {}
    for gem in GemTable.keys():
        result[GemTable[gem]] = []
    for color in GemTable.keys():
        result[GemTable[color]].append(color)
    return result
def testgems():
    if gemsbyColor(gColors) != {'blue': ['aquamarine', 'zircon', 'moonstone', 'topaz'], 'red': ['beryl', 'garnet', 'ruby'], 'green': ['emerald'], 'yellow': ['scapolite', 'helidor']}:
        return False
    if gemsbyColor(sColors) != {'black': ['Coca-Cola', 'Pepsi', 'Dr. Pepper'], 'green': ['Mountain Dew'], 'clear': ['Sierra Mist', 'Sprite']}:
        return False
    if gemsbyColor(cColors) != {'red': ['WSU', 'CWU', 'USC', 'EWU'], 'purple': ['UW'], 'green': ['OU'], 'blue': ['WWU', 'Gonzaga'], 'orange': ['OSU']}:
        return False
    return True


def histo1(S):
    D = {}
    L = []
    for c in S:
        D[c] = D.get(c, 0) + 1
    D.pop(" ", None)
    for c in D.keys():
        L.append((c, D[c]))
    L.sort()
    (L.sort(key=lambda tup: tup[1]))
    return L
def histo2(S):
    L = []
    S = S.replace(' ', '')
    L = [(c, S.count(c)) for c in S]
    M = set(L)
    L = list(M)
    L.sort()
    (L.sort(key=lambda tup: tup[1]))
    return L
def testhisto():
    if histo1("Cpts355 --- Assign1") != [('1', 1), ('3', 1), ('A', 1), ('C', 1), ('g', 1), ('i', 1), ('n', 1), ('p', 1), ('t', 1), ('5', 2), ('-', 3), ('s', 3)]:
        return False
    if histo2("Cpts355 --- Assign1") != [('1', 1), ('3', 1), ('A', 1), ('C', 1), ('g', 1), ('i', 1), ('n', 1), ('p', 1), ('t', 1), ('5', 2), ('-', 3), ('s', 3)]:
        return False
    if histo1("pizza") != histo2("pizza"):
        return False
    return True


funDict = {"add": lambda x,y: (x+y),
           "concat3": lambda a,b,c: (a+","+b+","+c),
           "mod2": lambda n: (n % 2)}

def execute(funDict, fun, args):
    operation = funDict[fun]
    if len(args) == 1:
        return operation(args[0])
    elif len(args) == 2:
        return operation(args[0], args[1])
    else:
        return operation(args[0], args[1], args[2])
def testexecute():
    if execute(funDict, "add", [1, 2]) != 3:
        return False
    if execute(funDict, "concat3", ["Hey", "it", "works!"]) != "Hey,it,works!":
        return False
    if execute(funDict, "mod2", [40]) != 0:
        return False
    return True
        
    
if __name__ == '__main__':
    passedMsg = "%s passed"
    failedMsg = "%s failed"
    if testtrans():
        print ( passedMsg % 'testtrans' )
    else:
        print ( failedMsg % 'testtrans' )
    if testgems():
        print ( passedMsg % 'testgems' )
    else:
        print ( failedMsg % 'testgems' ) 
    if testhisto():
        print ( passedMsg % 'testhisto' )
    else:
        print ( failedMsg % 'testhisto' )
    if testexecute():
        print ( passedMsg % 'testexecute' )
    else:
        print ( failedMsg % 'testexecute' ) 







