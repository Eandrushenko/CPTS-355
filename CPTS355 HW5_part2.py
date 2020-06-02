print("----------------------------------- PART 1 --------------------------------")

# ------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opStack = [5, 4, 3, 2, 1, 3, 4]

# debug function for testing

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
        if ((isinstance(op1, int) or isinstance(op1, float)) and (isinstance(op2, int) or isinstance(op2, float))):
            opPush(op1 + op2)
        else:
            debug("Error: add - One or more argument types are invalid")
    else:
        debug("Error : add - Expecting at least two arguments")


def sub():
    if (len(opStack) > 1):
        op1 = opPop()
        op2 = opPop()
        if ((isinstance(op1, int) or isinstance(op1, float)) and (isinstance(op2, int) or isinstance(op2, float))):
            opPush(op2 - op1)
        else:
            debug("Error: sub - One or more argument types are invalid")
    else:
        debug("Error : sub - Expecting at least two arguments")


def mul():
    if (len(opStack) > 1):
        op1 = opPop()
        op2 = opPop()
        if ((isinstance(op1, int) or isinstance(op1, float)) and (isinstance(op2, int) or isinstance(op2, float))):
            opPush(op2 * op1)
        else:
            debug("Error: mul - One or more argument types are invalid")
    else:
        debug("Error : mul - Expecting at least two arguments")


def div():
    if (len(opStack) > 1):
        op1 = opPop()
        op2 = opPop()
        if op1 != 0:
            if ((isinstance(op1, int) or isinstance(op1, float)) and (isinstance(op2, int) or isinstance(op2, float))):
                opPush(op2 / op1)
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
        if ((isinstance(op1, int) or isinstance(op1, float)) and (isinstance(op2, int) or isinstance(op2, float))):
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
        if ((isinstance(op1, int) or isinstance(op1, float)) and (isinstance(op2, int) or isinstance(op2, float))):
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
        if ((isinstance(op1, int) or isinstance(op1, float)) and (isinstance(op2, int) or isinstance(op2, float))):
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
            opPush(len(op1[1:-1]))
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
                if ((len(op1)-2) >= value):
                    opPush(ord(op1[1:][value]))
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
            if ((start >= 0) and (isinstance(start, int)) and (isinstance(end, int)) and (end <= (len(op1)-2))):
                op2 = op1[1:][start:start+end]
                opPush('('+op2+')')
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
    rollAmount = opPop()
    rollElements = opPop()
    if rollAmount <= len(opStack):
        tempStack = opStack[len(opStack) - rollElements:]
        for i in range(rollElements):
            opPop()
        if rollAmount < 0:
            for number in range(abs(rollAmount)):
                temp = tempStack[0]
                tempStack.append(temp)
                tempStack.remove(temp)
        else:
            for number in range(rollAmount):
                temp = tempStack.pop()
                tempStack.insert(0, temp)
        for everything in range(len(tempStack)):
            opPush(tempStack[everything])
    else:
        print("Error; not enough operands in operator stack to roll")


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
    opPop()
    newDict = {}
    opPush(newDict)


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

#------- Assignment5 - Part A Tests--------------
def testDefine():
    define("/n1", 4)
    if lookup("n1") != 4:
        return False
    return True

def testLookup():
    opPush("/n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False
    return True

#Arithmatic operator tests
def testAdd():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    return True

def testSub():
    opPush(10)
    opPush(4.5)
    sub()
    if opPop() != 5.5:
        return False
    return True

def testMul():
    opPush(2)
    opPush(4.5)
    mul()
    if opPop() != 9:
        return False
    return True

def testDiv():
    opPush(10)
    opPush(4)
    div()
    if opPop() != 2.5:
        return False
    return True

def testEq():
    opPush(6)
    opPush(6)
    eq()
    if opPop() != True:
        return False
    return True

def testLt():
    opPush(3)
    opPush(6)
    lt()
    if opPop() != True:
        return False
    return True

def testGt():
    opPush(3)
    opPush(6)
    gt()
    if opPop() != False:
        return False
    return True

#String operator tests
def testLength():
    opPush("(CptS355)")
    length()
    if opPop() != 7:
        return False
    return True

def testGet():
    opPush("(CptS355)")
    opPush(3)
    get()
    if opPop() != 83:
        return False
    return True

def testGetinterval():
    opPush("(CptS355)")
    opPush(4)
    opPush(3)
    getinterval()
    if opPop() != '(355)':
        return False
    return True

#boolean operator tests
def testPsAnd():
    opPush(True)
    opPush(False)
    psAnd()
    if opPop() != False:
        return False
    return True

def testPsOr():
    opPush(True)
    opPush(False)
    psOr()
    if opPop() != True:
        return False
    return True

def testPsNot():
    opPush(True)
    psNot()
    if opPop() != False:
        return False
    return True

#stack manipulation functions
def testDup():
    opPush(10)
    dup()
    if opPop()!=opPop():
        return False
    return True

def testExch():
    opPush(10)
    opPush("/x")
    exch()
    if opPop()!=10 and opPop()!="/x":
        return False
    return True

def testPop():
    l1 = len(opStack)
    opPush(10)
    pop()
    l2= len(opStack)
    if l1!=l2:
        return False
    return True

def testRoll():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(4)
    opPush(-3)
    roll()
    if opPop()==4 and opPop()==3 and opPop()==2 and opPop()==5 and opPop()==1:
        return True
    return False

def testRoll2():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(6)
    opPush(4)
    opPush(-1)
    roll()
    if opPop()==3 and opPop()==6 and opPop()==5 and opPop()==4 and opPop()==2 and opPop()==1:
        return True
    return False

def testCopy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    copy()
    if opPop()!=5 and opPop()!=4 and opPop()!=5 and opPop()!=4 and opPop()!=3 and opPop()!=2:
        return False
    return True

def testClear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opStack)!=0:
        return False
    return True

#dictionary stack operators
def testDict():
    opPush(1)
    psDict()
    if opPop()!={}:
        return False
    return True

def testBeginEnd():
    opPush("/x")
    opPush(3)
    psDef()
    opPush({})
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x")!=3:
        return False
    return True

def testpsDef():
    opPush("/x")
    opPush(10)
    psDef()
    if lookup("x")!=10:
        return False
    return True

def testpsDef2():
    opPush("/x")
    opPush(10)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("x")!=10:
        end()
        return False
    end()
    return True


def main_partA():
    testCases = [('define',testDefine),('lookup',testLookup),('add', testAdd), ('sub', testSub),('mul', testMul),('div', testDiv),  ('eq', testEq), \
                 ('lt', testLt),  ('gt', testGt),('length', testLength),('get', testGet), ('getinterval', testGetinterval), \
                 ('psAnd', testPsAnd), ('psOr', testPsOr), ('psNot', testPsNot),  \
                 ('dup', testDup), ('exch', testExch), ('pop', testPop), ('roll', testRoll), ('copy', testCopy), \
                ('clear', testClear), ('dict', testDict), ('begin', testBeginEnd), ('psDef', testpsDef), ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests != []:
        return ('Some tests failed', failedTests)
    else:
        return ('All tests OK')



if __name__ == '__main__':
    print(main_partA())

opStack.clear()
dictStack.clear()
# ------------------------------- PART 2 ------------------------------
# For tokenizing we'll use the “re” package for Regular Expressions
print("----------------------------------- PART 2 --------------------------------")

import re


def tokenize(s):
    return re.findall("/?[a-zA-Z()][a-zA-Z0-9_()]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)


# See what tokenize does
print(tokenize(
    """
    (facto) dup length /n exch def
    /fact {
    0 dict begin
    /n exch def
    n 2 lt
    { 1}
    {n 1 sub fact n mul }
    ifelse
    end
    } def
    n fact stack
    """))


# The it argument is an iterator that returns left or right parenthesis characters.
# The sequence of characters returned by the iterator should represent a string of properly nested
# parentheses pairs, from which the leading '(' has already been removed. If the
# parentheses are not properly nested, return False.

def find(it, k):
    v = ''
    for c in it:
        if c == k:
            print(v)
            return it
        v = v + c
    return None


def groupMatching(it):
    res = ['{']
    for c in it:
        if c == ')':
            res.append(')')
            return res
        else:
            # note how we use a recurseive call to group the inner
            # matching parenthesis string and append it as a whole
            # to the list we are constructing.
            # Also note how we've already seen the leading '(' of this
            # inner group and consumed it from the iterator.
            res.append(groupMatching(it))
        return False


# function to turn a string of properly nested parenthese
# into a list of properly nested lists.

def group(s):
    if s[0] == '(':
        return groupMatching(iter(s[1:]))
    else:
        return False  # If it starts with ')' it is not properly nested


group('(()(()))')  # will return ['(', ['(', ')'], ['(', ['(', ')'], ')'], ')'] print(c)


# Write your parsing code here; it takes a list of tokens producted by tokenize
# and returns a code array; Of course you may create additional functions to help you
# write parse()

def parseMatching(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c == '{':
            res.append(parseMatching(it))
        else:
            if c.isnumeric() == True:
                c = int(c)
            elif c[0] == '-':
                c = int(c)
            elif c.upper() == 'TRUE':
                c = True
            elif c.upper() == 'FALSE':
                c = False
            res.append(c)
    return False


def parse(s):
    res = []
    it = iter(s)
    for c in it:
        if c == '}':
            return False
        elif c == '{':
            res.append(parseMatching(it))
        else:
            if c.isnumeric() == True:
                c = int(c)
            elif c[0] == '-':
                c = int(c)
            elif c.upper() == 'TRUE':
                c = True
            elif c.upper() == 'FALSE':
                c = False
            res.append(c)
    return res


def psif():
    if (len(opStack) > 1):
        op1 = opPop()
        op2 = opPop()
        if (isinstance(op2, bool)):
            if op2 == True:
                interpretSPS(op1)
        else:
            debug("Error: psif - One or more argument types are invalid")
    else:
        debug("Error : psif - Expecting at least two arguments")


def psifelse():
    if (len(opStack) > 2):
        op1 = opPop()
        op2 = opPop()
        op3 = opPop()
        if (isinstance(op3, bool)):
            if op3 == True:
                interpretSPS(op2)
            else:
                interpretSPS(op1)
        else:
            debug("Error: psifelse - One or more argument types are invalid")
    else:
        debug("Error : psifelse - Expecting at least three arguments")


# Write the necessary code here; again write
# auxiliary functions if you need them. This will probably be the largest
# function of the whole project, but it will have a very regular and obvious
# structure if you've followed the plan of the assignment.

def interpretSPS(code):  # code is a code array
    for t in code:
        if (isinstance(t, int)) or (isinstance(t, bool)):
            opPush(t)
        elif t[0] == '/':
            opPush(t)
        elif t[0] == '(':
            opPush(t)
        elif (isinstance(t, list)):
            opPush(t)
        elif t == 'add':
            add()
        elif t == 'sub':
            sub()
        elif t == 'mul':
            mul()
        elif t == 'div':
            div()
        elif t == 'eq':
            eq()
        elif t == 'lt':
            lt()
        elif t == 'gt':
            gt()
        elif t == 'roll':
            roll()
        elif t == 'length':
            length()
        elif t == 'get':
            get()
        elif t == 'getinterval':
            getinterval()
        elif t == 'and':
            psAnd()
        elif t == 'or':
            psOr()
        elif t == 'not':
            psNot()
        elif t == 'dup':
            dup()
        elif t == 'exch':
            exch()
        elif t == 'pop':
            pop()
        elif t == 'copy':
            copy()
        elif t == 'clear':
            clear()
        elif t == 'dict':
            psDict()
        elif t == 'begin':
            begin()
        elif t == 'end':
            end()
        elif t == 'def':
            psDef()
        elif t == 'define':
            define()
        elif t == 'lookup':
            lookup()
        elif t == 'if':
            psif()
        elif t == 'ifelse':
            psifelse()
        elif t == 'stack':
            stack()
        elif t == 'begin':
            begin()
        elif t == 'end':
            end()
        elif (isinstance(t, str)):
            u = lookup(t)
            if (isinstance(u, list)):
                interpretSPS(u)
            elif (not (isinstance(u, list))):
                opPush(u)
        else:
            debug("Error : interpretSPS - unexpected value")


# Copy this to your HW2_part2.py file>
def interpreter(s):  # s is a string
    interpretSPS(parse(tokenize(s)))


# --------------------------testing----------------------------------------------

print('\n')

input1 = """
/square {
dup mul
} def
(square)
4 square
dup 16 eq true and
{(pass)} {(fail)} ifelse stack"""

input2 = """
(facto) dup length /n exch def
/fact {
0 dict begin
/n exch def
n 2 lt
{1}
{n 1 sub fact n mul }
ifelse
end
} def
n fact stack
"""

input3 = """
/lt6 {6 lt} def
1 2 3 4 5 6 4 -3 roll
dup dup lt6 exch 3 gt and {mul mul} if
stack
"""

input4 = """
(CptS355_HW5) 4 3 getinterval
(355) eq
{(You_are_in_CptS355)} if
stack
"""

input5 = """ 1 dup add
5 mul true false or
{(this_test_should_pass)} stack
"""


def token_test1(input1):
    if tokenize(input1) == ['/square', '{', 'dup', 'mul', '}', 'def', '(square)', '4', 'square', 'dup', '16', 'eq',
                            'true', 'and', '{', '(pass)', '}', '{', '(fail)', '}', 'ifelse', 'stack']:
        print("Tokenize passed test 1")
    else:
        print("Tokenize failed test 1")


def token_test2(input2):
    if tokenize(input2) == ['(facto)', 'dup', 'length', '/n', 'exch', 'def', '/fact', '{', '0', 'dict', 'begin', '/n',
                            'exch', 'def', 'n', '2', 'lt', '{', '1', '}', '{', 'n', '1', 'sub', 'fact', 'n', 'mul', '}',
                            'ifelse', 'end', '}', 'def', 'n', 'fact', 'stack']:
        print("Tokenize passed test 2")
    else:
        print("Tokenize failed test 2")


def token_test3(input3):
    if tokenize(input3) == ['/lt6', '{', '6', 'lt', '}', 'def', '1', '2', '3', '4', '5', '6', '4', '-3', 'roll', 'dup',
                            'dup', 'lt6', 'exch', '3', 'gt', 'and', '{', 'mul', 'mul', '}', 'if', 'stack']:
        print("Tokenize passed test 3")
    else:
        print("Tokenize failed test 3")


def token_test4(input4):
    if tokenize(input4) == ['(CptS355_HW5)', '4', '3', 'getinterval', '(355)', 'eq', '{', '(You_are_in_CptS355)', '}',
                            'if', 'stack']:
        print("Tokenize passed test 4")
    else:
        print("Tokenize failed test 4")


def token_test5(input5):
    if tokenize(input5) == ['1', 'dup', 'add', '5', 'mul', 'true', 'false', 'or', '{', '(this_test_should_pass)', '}', 'stack']:
        print("Tokenize passed test 5")
    else:
        print("Tokenize failed test 5")


def parse_test1(input1):
    if parse(tokenize(input1)) == ['/square', ['dup', 'mul'], 'def', '(square)', 4, 'square', 'dup', 16, 'eq', True,
                                   'and', ['(pass)'], ['(fail)'], 'ifelse', 'stack']:
        print("Parse passed test 1")
    else:
        print("Parse failed test 1")


def parse_test2(input2):
    if parse(tokenize(input2)) == ['(facto)', 'dup', 'length', '/n', 'exch', 'def', '/fact',
                                   [0, 'dict', 'begin', '/n', 'exch', 'def', 'n', 2, 'lt', [1],
                                    ['n', 1, 'sub', 'fact', 'n', 'mul'], 'ifelse', 'end'], 'def', 'n', 'fact', 'stack']:
        print("Parse passed test 2")
    else:
        print("Parse failed test 2")


def parse_test3(input3):
    if parse(tokenize(input3)) == ['/lt6', [6, 'lt'], 'def', 1, 2, 3, 4, 5, 6, 4, -3, 'roll', 'dup', 'dup', 'lt6',
                                   'exch', 3, 'gt', 'and', ['mul', 'mul'], 'if', 'stack']:
        print("Parse passed test 3")
    else:
        print("Parse failed test 3")


def parse_test4(input4):
    if parse(tokenize(input4)) == ['(CptS355_HW5)', 4, 3, 'getinterval', '(355)', 'eq', ['(You_are_in_CptS355)'], 'if',
                                   'stack']:
        print("Parse passed test 4")
    else:
        print("Parse failed test 4")


def parse_test5(input5):
    if parse(tokenize(input5)) == [1, 'dup', 'add', 5, 'mul', True, False, 'or', ['(this_test_should_pass)'], 'stack']:
        print("Parse passed test 5")
    else:
        print("Parse failed test 5")


def interpreter_test1(input1):
    clear()
    print (interpreter(input1))
    if opStack == ['(square)', 16, '(pass)']:
        print("Interpeter passed test 1")
    else:
        print("Interpreter failed test 1")
    print('\n')


def interpreter_test2(input2):
    clear()
    interpreter(input2)
    if opStack == ['(facto)', 120]:
        print("Interpeter passed test 2")
    else:
        print("Interpreter failed test 2")
    print('\n')


def interpreter_test3(input3):
    clear()
    interpreter(input3)
    if opStack == [1, 2, 6, 60]:
        print("Interpeter passed test 3")
    else:
        print("Interpreter failed test 3")
    print('\n')


def interpreter_test4(input4):
    clear()
    interpreter(input4)
    if opStack == [['(You_are_in_CptS355)']]:
        print("Interpeter passed test 4")
    else:
        print("Interpreter failed test 4")
    print('\n')


def interpreter_test5(input5):
    clear()
    interpreter(input5)
    if opStack == [10, True, ['(this_test_should_pass)']]:
        print("Interpeter passed test 5")
    else:
        print("Interpreter failed test 5")
    print('\n')




token_test1(input1)
token_test2(input2)
token_test3(input3)
token_test4(input4)
token_test5(input5)
print('\n')
parse_test1(input1)
parse_test2(input2)
parse_test3(input3)
parse_test4(input4)
parse_test5(input5)
print('\n')
interpreter_test1(input1)
interpreter_test2(input2)
interpreter_test3(input3)
interpreter_test4(input4)
interpreter_test5(input5)

opStack.clear()
dictStack.clear()









