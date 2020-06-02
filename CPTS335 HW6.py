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
    if isinstance(d, tuple):
        dictStack.append(d)
    else:
        opPush(d)
        debug("Error : dictPush - Expecting a tuple on the top of the dictStack")


# dictPush pushes a new dictionary to the dictstack. Note that, your interpreter
# will call dictPush only when Postscript "begin" operator is called. "begin"
# should pop the empty dictionary from the opstack and push it onto the dictstack
# by calling dictPush. You may either pass this dictionary (which you popped from
# opstack) to dictPush as a parameter or just simply push a new empty dictionary
# in dictPush.

def define(name, value):    
    if (len(dictStack) == 0):
        newDict = (0, {})
        newDict[1][name] = value
        dictPush(newDict)
    else:
        topDict = dictStack[len(dictStack)-1]
        topDict[1][name] = value

# add name: value to the top dictionary in the dictionary stack. (Keep the '/' in
# name when you add it to the top dictionary) Your psDef function should pop the
# name and value from the operand stack and call the "define" function.

def lookup(token):
    found = findstaticlink('/'+token,len(dictStack)-1)
    return dictStack[found][1]['/'+token]


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
        debug("Error; not enough operands in operator stack to roll")


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


def printDict(scope):
    if (scope.upper() == "STATIC" or scope.upper() == "S"):
        while len(dictStackholder) > 0:
            index = len(dictStackholder)-1
            link = dictStackholder[-1][0]
            print('----',index,'----',link,'----',sep='')
            for i in dictStackholder[-1][1]:
                print(i,'', dictStackholder[-1][1][i])
            del dictStackholder[-1]
    else:
        while len(dictStack) > 0:
            index = len(dictStack)-1
            link = dictStack[-1][0]
            print('----',index,'----',link,'----',sep='')
            for i in dictStack[-1][1]:
                print(i,'', dictStack[-1][1][i])
            del dictStack[-1]
    print('==============')


def stack(scope):
    if (scope.upper() == "STATIC" or scope.upper() == "S"):
        print("Static")
        print('==============')
        for i in reversed(opStack):
            print(i)
        print('==============')
        printDict(scope)
    else:
        print("Dynamic")
        print('==============')
        for i in reversed(opStack):
            print(i)
        print('==============')
        printDict(scope)
        


# ------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators: dup, exch, pop, roll,
# copy, clear, stack

def psDict():
    dictPop()
    dictPush()

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

# ------------------------------- PART 2 ------------------------------
# For tokenizing we'll use the “re” package for Regular Expressions

import re


def tokenize(s):
    return re.findall("/?[a-zA-Z()][a-zA-Z0-9_()]*|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)


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

dictStackholder = []

def interpretSPS(code, scope):  # code is a code array
    if (scope.upper() == "STATIC" or scope.upper() == "S"):
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
                stack(scope)
            elif t == 'begin':
                begin()
            elif t == 'end':
                end()
            elif (isinstance(t, str)):
                u = lookup(t)
                if (isinstance(u, list)):
                    dictStackholder.append(dictStack[-1])
                    dictPush((findstaticlink(t, len(dictStack)-1), {}))
                    interpretSPS(u, scope)
                elif (not (isinstance(u, list))):
                    opPush(u)
                else:
                    debug("Error : interpretSPS - unexpected value")           
        dictPop()
    else:
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
                stack(scope)
            elif t == 'begin':
                begin()
            elif t == 'end':
                end()
            elif (isinstance(t, str)):
                u = lookup(t)
                if (isinstance(u, list)):
                    interpretSPS(u, scope)
                elif (not (isinstance(u, list))):
                    opPush(u)
            else:
                debug("Error : interpretSPS - unexpected value")

# Copy this to your HW2_part2.py file>
def interpreter(s, scope):  # s is a string
    interpretSPS(parse(tokenize(s)), scope)

clear()
# ------------------------------- PART 3 ------------------------------
# For tokenizing we'll use the “re” package for Regular Expressions
print("----------------------------------- PART 3 --------------------------------")


def findstaticlink (token,ind): 
    if token in dictStack[ind][1]:
        return ind
    else:
        if (ind != 0):
            return findstaticlink(token,dictStack[ind][0])
        else:
            return 0


input1 = """
/x 4 def
/g { x stack } def
/f { /x 7 def g } def
f
"""

input2 = """
/m 50 def
/n 100 def
/egg1 {/m 25 def n} def
/chic {
/n 1 def
/egg2 { n } def
m n
egg1
egg2
stack } def
n
chic
"""

input3 = """
/x 10 def
/A { x } def
/C { /x 40 def A stack } def
/B { /x 30 def /A { x } def C } def
B
"""

def HW6():
    interpreter(input1, 's')
    opStack.clear()
    dictStack.clear()
    print('')
    interpreter(input1, 'd')
    opStack.clear()
    dictStack.clear()
    print('')
    interpreter(input2, 's')
    opStack.clear()
    dictStack.clear()
    print('')
    interpreter(input2, 'd')
    opStack.clear()
    dictStack.clear()
    print('')
    interpreter(input3, 's')
    opStack.clear()
    dictStack.clear()
    print('')
    interpreter(input3, 'd')
    opStack.clear()
    dictStack.clear()
    print('')

#Prints the test cases from Assignment 6
HW6()

# dictPush(d, index) - tuple, findstaticlink(token) - returns the index
# define, lookup(token, scope) - static follow links, dynamic follow order
# make a function that prints type, opstack, dictstack
# psDict



