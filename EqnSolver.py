#   Initializing the code by asking how many unknowns. Currently 1 and 2 unknowns are supported.
#
#   After that the code asks you if the solutions can be equal if there are 2 unknowns. This is
#   done because when it was being tested, an equation was given   (x**y = y**x)   . Obviously 
#   if x = y, the equation would be true. But I wanted the non-equal solutoins. So the "Can solutions
#   be equal?" was implemented.
#
#   Then the code asks you the LHS(Left Hand Side) and the RHS(Right Hand Side). Now there are a few
#   restrictions here.
#   1.   The unknowns must be "x" and "y".
#   2.   x^y is not supported, instead x**y is supported.
#   3.   Non-integer solutions are not supported.
#   4.   As I am really stupid and could not come up with a good technique to solve equation,
#        I ended up iterating through all possible values for the unknowns/variables to get
#        solution(s). And also, I set the range of iterating from -100 to 100. This will be
#        Improved in shaa allah.
#
#   An important thing is that at the last, after you have given the LHS and the RHS, the code
#   will ask you a weird "thing". Write 1 for normal output, Write 2 for output in list etc.
#   Let me tell you what the normal output is. So, if your equation is x**2 = 4, and if you input
#   1 at the last, the output will be something like-
#
#   >>> The unknown is: 2   (N.B.: For some reason it does not output -2, which is also a solution.)
#
#   And if you input 2 at the last, the output will be something like-
#
#   >>> [2]
#   If you input 3 at last-
#
#   >>> {1 : 2}
#
#   Inputing 4 at last will result in bot the list and dictionary being outputted at the same time-
#
#   >>> [2]
#   >>> {1 : 2}
#
#
#   Feel free to change/develop this code and let me know if you find any bug or have any questions
#   or have a better idea through tanvirsalehin2988@gmail.com


import math

def initialize():
    unknowns = int(input("How many unknowns: " ))
    if unknowns == 2:
        equal = input("Can the unknowns be equal?   y/n"
                    "\n==> ")
    else:
        equal = "y"
        
    lhs = input("Write the LHS:\n")
    rhs = input("Write the RHS:\n")
    
    return unknowns, equal, lhs, rhs

unknowns, equal, lhs, rhs = initialize()

def styleAssign(style):
    pstyle = 1
    if style == 2:
        pstyle = 2
    elif style == 3:
        pstyle = 3
    elif style == 4:
        pstyle = 4
    elif style == 1:
        pstyle = 1
    else:
        pstyle = 1
        
    return pstyle

def solPrinter(pstyle, List, Dict):
    if pstyle == 2:
        print(List)
    elif pstyle == 3:
        print(Dict)
    elif pstyle == 4:
        print(List)
        print(Dict)

def solveForOne(lhs, rhs, List, Dict, StyleName, solnum):
    for x in range(-100, 1000):
        try:
            if evaluate(lhs, x) == evaluate(rhs, x):
                List.append(x)
                solnum += 1
                Dict[solnum] = x
                if StyleName == 1:
                	print("The unknown is: ", x)
        except ZeroDivisionError:
            continue

def solveForTwo(lhs, rhs, List, Dict, StyleName, solnum, equal=True):
    for x in range(-100, 100):
            for y in range(-100, 100):
                if x == y:
                    if not equal:
                        continue
                try:
                    if evaluate(lhs, x, y) == evaluate(rhs, x, y):
                        solnum += 1
                        li = [x, y]
                        List.append(li)
                        Dict[x] = y
                        if StyleName == 1:
                            print("The unknowns are: ", x, y)
                except ZeroDivisionError:
                    continue

def convertLiToStr(List):
	string = ''
	for element in List:
		string += str(element)
	return string

def convertStrToLi(string):
    list1=[]
    list1[:0]=string
    return list1

def evaluate(exp, a=0, b=0, c=0):
	exp1 = exp
	exp1 = convertStrToLi(exp1)
	for element in range(len(exp1)):
		if exp1[element] == 'x':
			exp1[element] = a
		elif exp1[element] == 'y':
			exp1[element] = b
		elif exp1[element] == 'z':
			exp1[element] = c
	exp1 = convertLiToStr(exp1)
	exp1 = eval(exp1)
	return exp1


def solve(lhs, rhs, Unknowns, equal = True, style = 1):
    print("Solving for the equation with ", Unknowns, " unknown(s):\n", lhs, "=", rhs)
    Solutions = []
    SolutionDict = {}
    
    pstyle = styleAssign(style)
    
    if Unknowns == 1:
        a = 0
        solveForOne(lhs, rhs, Solutions, SolutionDict, pstyle, a)
        solPrinter(pstyle, Solutions, SolutionDict)
        return Solutions, SolutionDict
        print("Sorry!")
            
                
    elif Unknowns == 2:
        a = 0
        solveForTwo(lhs, rhs, Solutions, SolutionDict, pstyle, a, equal)
        solPrinter(pstyle, Solutions, SolutionDict)
        return Solutions, SolutionDict
        print("Sorry!")


run = True
while run:
    outputStyle = int(input("Write 1 for normal output."
                        "\nWrite 2 for Output in List."
                        "\nWrite 3 for output in Dictionary."
                        "\nWrite 4 for output in both Dictionary and List."
                        "\n"
                        "\n==> "))
    if equal == "y":
        if outputStyle == 1:
            solve(lhs, rhs, unknowns, True, 1)
            run = False
        elif outputStyle == 2:
            a, b = solve(lhs, rhs, unknowns, True, 2)
            run = False
        elif outputStyle == 3:
            a, b = solve(lhs, rhs, unknowns, True, 3)
            run = False
        elif outputStyle == 4:
            a, b = solve(lhs, rhs, unknowns, True, 4)
            run = False
        else:
            print("The input to see the style of output has to be a positive integer among 1, 2, 3, 4."
                  "\n")
            
    elif equal == "n":
        if outputStyle == 1:
            solve(lhs, rhs, unknowns, False, 1)
            run = False
        elif outputStyle == 2:
            a, b = solve(lhs, rhs, unknowns, False, 2)
            run = False
        elif outputStyle == 3:
            a, b = solve(lhs, rhs, unknowns, False, 3)
            run = False
        elif outputStyle == 4:
            a, b = solve(lhs, rhs, unknowns, False, 4)
            run = False
        else:
            print("The input to see the style of output has to be a positive integer among 1, 2, 3, 4.")

