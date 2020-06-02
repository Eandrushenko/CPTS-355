# ------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opStack = [5, 4, 3, 2, 1, 3, 4]

#debug function for testing

debug_level = 0

def debug(*s):
    if debug_level > 0:
        print(s)

# now define functions to push and pop values on the opstack according to your
# decision about which end should be the hot end. Recall that `pass` in Python is
# a no-op: replace it with your code.

def opPop():
    if len(opStack) > 0:
        x = opStack[-1]
        del opStack[-1]
        return x
    else:
        debug("Error: opPop -Operand stack is empty")

def opPush(value):
    opStack.append(value)

# Remeber that there is a Postscript operator called "pop" so we choose
# different names for these functions


# ------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations

dictStack = []

# now define functions to push and pop dictionaries on the dictstack, to define
# name, and to lookup a name

def dictPop():
    if len(dictStack) > 0:
        dictStack.pop(len(dictStack) - 1)
    else:
        debug("Error: dictPop - Operand stack is empty")

# dictPop pops the top dictionary from he sictionary stack

def dictPush(d):
    if isinstance(d, dict):
        dictStack.append(d)
    else:
        opPush(d)
        debug("Error : dictPush - Expecting a dictionary on the top of the dictStack")

# dictPush pushes a new dictionary to the dictstack. Note that, your interpreter
# will call dictPush only when Postscript "begin" operator is called. "begin"
# should pop the empty dictionary from the opstack and push it onto the dictstack
# by calling dictPush. You may either pass this dictionary (which you popped from
# opstack) to dictPush as a parameter or just simply push a new empty dictionary
# in dictPush.

def define(name, value):
    if (len(dictStack) > 0):
        dictStack[-1][name] = value
    else:
        newDict = {}
        newDict[name] = value
        dictStack.append(newDict)

# add name: value to the top dictionary in the dictionary stack. (Keep the '/' in
# name when you add it to the top dictionary) Your psDef function should pop the
# name and value from the operand stack and call the "define" function.

def lookup(name):
    for d in reversed(dictStack):
        if d.get('/'+name, None) != None:
            return d.get('/'+name, 0)
    return None

# return the value assocaited with name
# What is your design decision about what to do when there is no definition for
# name?

def add():
    if (len(opStack) > 1):
        op1 = opPop()
        op2 = opPop()
        if ((isinstance(op1, int) or isinstance(op1,float)) and (isinstance(op2, int) or isinstance(op2,float))):
            opPush(op1+op2)
        else:
            debug("Error: add - One or more argument types are invalid")
    else:
        debug("Error : add - Expecting at least two arguments")


def sub():
    if (len(opStack) > 1):
        op1 = opPop()
        op2 = opPop()
        if ((isinstance(op1, int) or isinstance(op1,float)) and (isinstance(op2, int) or isinstance(op2,float))):
            opPush(op2-op1)
        else:
            debug("Error: sub - One or more argument types are invalid")
    else:
        debug("Error : sub - Expecting at least two arguments")
        
def mul():
    if (len(opStack) > 1):
        op1 = opPop()
        op2 = opPop()
        if ((isinstance(op1, int) or isinstance(op1,float)) and (isinstance(op2, int) or isinstance(op2,float))):
            opPush(op2*op1)
        else:
            debug("Error: mul - One or more argument types are invalid")
    else:
        debug("Error : mul - Expecting at least two arguments")

def div():
    if (len(opStack) > 1):
        op1 = opPop()
        op2 = opPop()
        if op1 != 0:
            if ((isinstance(op1, int) or isinstance(op1,float)) and (isinstance(op2, int) or isinstance(op2,float))):
                opPush(op2/op1)
            else:
                debug("Error: div - div or more argument types are invalid")
        else:
            debug("Error: div - Diving by zero is not allowed")
    else:
        debug("Error : div - Expecting at least two arguments")

def eq():
    if (len(opStack) > 1):
        op1 = opPop()
        op2 = opPop()
        if ((isinstance(op1, int) or isinstance(op1,float)) and (isinstance(op2, int) or isinstance(op2,float))):
            if op1 == op2:
                opPush(True)
            else:
                opPush(False)
        else:
            debug("Error: eq - One or more argument types are invalid")
    else:
        debug("Error : eq - Expecting at least two arguments")

def lt():
    if (len(opStack) > 1):
        op1 = opPop()
        op2 = opPop()
        if ((isinstance(op1, int) or isinstance(op1,float)) and (isinstance(op2, int) or isinstance(op2,float))):
            if op2 < op1:
                opPush(True)
            else:
                opPush(False)
        else:
            debug("Error: lt - One or more argument types are invalid")
    else:
        debug("Error : lt - Expecting at least two arguments")
        
def gt():
    if (len(opStack) > 1):
        op1 = opPop()
        op2 = opPop()
        if ((isinstance(op1, int) or isinstance(op1,float)) and (isinstance(op2, int) or isinstance(op2,float))):
            if op2 > op1:
                opPush(True)
            else:
                opPush(False)
        else:
            debug("Error: gt - One or more argument types are invalid")
    else:
        debug("Error : gt - Expecting at least two arguments")
        
# ------------------------- 15% -------------------------------------
# Arithmetic and comparison operators:   define all the arithmetic and
# comparison operators here -- add, sub, mul, div, eq, lt, gt
# Make sure to check the operand stack has the correct number of parameters and
# types of the parameters are correct.

def length():
    if (len(opStack) > 0):
        op1 = opPop()
        if (isinstance(op1, str)):
            opPush(len(op1))
        else:
            debug("Error : length - invalid type, argument type must be a string")
    else:
        debug("Error : length - Expecting at least one argument")

def get():
    if (len(opStack) > 1):
        value = opPop()
        op1 = opPop()
        if (value >= 0 and (isinstance(value, int))):
            if (isinstance(op1, str)):
                if (len(op1) >= value):
                    opPush(ord(op1[value]))
                else:
                    debug("Error : get - index must be less than or equal to string length")
            else:
                debug("Error : get - invalid type, argument type must be a string")
        else:
            debug("Error : get - index must a nonnegative integer")
    else:
        debug("Error : get - Expecting at least two arguments")

def getinterval():
    if (len(opStack) > 2):
        end = opPop()
        start = opPop()
        op1 = opPop()
        if (isinstance(op1, str)):
            if ((start >= 0) and (isinstance(start, int)) and (isinstance(end, int)) and (end > start) and (end <= len(op1))):
                op2 = op1[start:end]
                opPush(op2)
            else:
                debug("Error : getinterval - indexes are invalid")
        else:
            debug("Error : getinterval - invalid type, expected a string")
    else:
        debug("Error: getinterval - Expectingat least three arguments")
                
# ------------------------- 15% -------------------------------------
# String operators: define the string operators length, get, getinterval

def psAnd():
    if (len(opStack) > 1):
        op1 = opPop()
        op2 = opPop()
        if ((isinstance(op1, bool)) and (isinstance(op2, bool))):
            opPush(op1 and op2)
        else:
            debug("Error : psAnd - invalid type, must be boolean")
    else:
        debug("Error : psAnd - Expected at least 2 arguments")

def psOr():
    if (len(opStack) > 1):
        op1 = opPop()
        op2 = opPop()
        if ((isinstance(op1, bool)) and (isinstance(op2, bool))):
            opPush(op1 or op2)
        else:
            debug("Error : psOr - invalid type, must be boolean")
    else:
        debug("Error : psOr - Expected at least 2 arguments")

def psNot():
    if (len(opStack) > 0):
        op1 = opPop()
        if (isinstance(op1, bool)):
            opPush(not op1)
        else:
            debug("Error : psNot - invalid type, must be boolean")
    else:
        debug("Error : psNot - Expected at least 1 argument")



# ------------------------- 15% -------------------------------------
# Boolean operators: define the boolean operators psAnd, psOr, psNot;
# Remember that these take boolean operands only. Anything else is an error

def dup():
    if (len(opStack) > 0):
        opPush(opStack[-1])
    else:
        debug("Error : dup - Operand stack is empty")

def exch():
    if (len(opStack) > 1):
        op1 = opStack[-1]
        opStack[-1] = opStack[-2]
        opStack[-2] = op1
    else:
        debug("Error : exch - Expecting at least two arguments")

def pop():
    if len(opStack) > 0:
        x = opStack[-1]
        del opStack[-1]
        print(x)
    else:
        debug("Error: pop -Operand stack is empty")
        

def roll():
    if (len(opStack) > 3):
        rollset = []
        n = opPop() 
        m = opPop()
#wasn't able to finish
        

def copy():
    if len(opStack) > 1:
        op1 = opPop()
        if (op1 <= len(opStack) + 1):
            copylist = []
            while (op1 > 0):
                copylist.append(opPop())
                op1 = op1 - 1
            copylist.reverse()
            opStack.extend(copylist)
            opStack.extend(copylist)
        else:
            debug("Error : copy - Argument exceeds size of stack")
    else:
        debug("Error : copy - Expected at least 2 argument")

def clear():
    opStack[:] = []

def stack():
    print(opStack)

# ------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators: dup, exch, pop, roll,
# copy, clear, stack

def psDict():
    newDict = {}
    dictPush(newDict)

def begin():
    if len(opStack) > 0:
        op1 = opPop()
        if (isinstance(op1, dict)):
            dictPush(op1)
        else:
            debug("Error: begin - invalid type, must be dictionary")
    else:
        debug("Error: begin - opStack is empty")

def end():
    if len(dictStack) > 0:
        op1 = dictStack.pop(len(dictStack) - 1)
    else:
        debug("Error: end - Dictionary stack is empty")

def psDef():
    if len(opStack) > 1:
        value = opPop()
        name = opPop()
        if (isinstance(name, str)):
            define(name, value)
        else:
            debug("Error: psDef - invalid name argument")
    else:
        debug("Error: psDef - not enough arguments")


# ------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the functions for the def operator psDef because def is reserved in
# Python.
# Note: the psDef operator will pop the value and name from the opstack and call your own d
# call your own "define" operator (pass those values as parameters). Note that
# psDef() wont have any parameters.
    
def testAdd():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3: return False
    return True
def testSub():
    opPush(5)
    opPush(1)
    sub()
    if opPop() != 4: return False
    return True
def testMul():
    opPush(5)
    opPush(3)
    mul()
    if opPop() != 15: return False
    return True
def testDiv():
    opPush(4)
    opPush(2)
    div()
    if opPop() != 2: return False
    return True
def testEq():
    opPush(5)
    opPush(5)
    eq()
    if opPop() != True: return False
    return True
def testLt():
    opPush(3)
    opPush(5)
    lt()
    if opPop() != True: return False
    return True
def testGt():
    opPush(7)
    opPush(5)
    gt()
    if opPop() != True: return False
    return True
def testLength():
    opPush("cpts355")
    length()
    if opPop() != 7: return False
    return True
def testGet():
    opPush("cpts355")
    opPush(2)
    get()
    if opPop() != 116: return False
    return True
def testGetinterval():
    opPush("cpts355")
    opPush(0)
    opPush(3)
    getinterval()
    if opPop() != "cpt": return False
    return True
def testPsAnd():
    opPush(True)
    opPush(True)
    psAnd()
    if opPop() != True: return False
    return True
def testPsOr():
    opPush(True)
    opPush(False)
    psOr()
    if opPop() != True: return False
    return True
def testPsNot():
    opPush(True)
    psNot()
    if opPop() != False: return False
    return True
def testDup():
    opPush(7)
    dup()
    if opPop() != 7: return False
    return True
def testExch():
    opPush(7)
    opPush(9)
    exch()
    if opPop() != 7: return False
    return True
def testPop():
    opPush(21)
    pop()
    if opPop() == 21: return False
    return True
def testCopyandClear():
    opPush(25)
    clear()
    if opPop() == 25: return False
    opPush(5)
    opPush(6)
    opPush(2)
    copy()
    if opStack != [5, 6, 5, 6]: return False
    clear()
    return True
def testPsDict():
    psDict()
    if len(dictStack) == 0: return False
    end()
    return True
def testBeginandEnd():
    opPush({'test' : 404})
    begin()
    if dictStack[0] == None : return False
    end()
    if dictPop() == {'test' : 404}: return False
    return True
def testPsDef():
    opPush("\n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3: return False
    return True
def testDefineandLookup():
    define('\test',5)
    lookup('test')
    if lookup("test") == None: return False
    return True
    
    
    
# Test Functions

if __name__ == '__main__':
    testCases = [('add', testAdd), ('sub', testSub), ('mul', testMul), ('div', testDiv), ('eq', testEq), ('lt', testLt), ('gr', testGt), ('length', testLength), ('get', testGet),
                 ('getinterval', testGetinterval), ('psAnd', testPsAnd), ('or', testPsOr), ('not', testPsNot), ('dup', testDup), ('exch', testExch), ('pop', testPop),
                 ('Copy and Clear', testCopyandClear), ('psDict', testPsDict), ('begin and end', testBeginandEnd), ('psDef', testPsDef), ('define and lookup', testDefineandLookup)]
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        print('Some tests failed', failedTests)
        print('Additionally, roll was not implemented')
    else:
        print('All tests OK')


