from types import MethodType
from variableClass import *
from errorClass import *

def output(lineNum):
    if line[leftParInd+1]=='"':
        remain=line[leftParInd+2::]
        if remain.count('"')==1 and ((remain[len(remain)-2]==')' and remain[len(remain)-1]==';') or (remain[len(remain)-3]==')' and remain[len(remain)-2]==';' and remain[len(remain)-1]=='\n')):
            rightQuoteInd=remain.find('"')
            print(remain[0:rightQuoteInd])
        else:
            error="Syntax Error on line "+str(lineNum)
            print(error)


def varCheck(line):
    if line.count('=')==1:
        return line[0:line.index('=')]

def funcs(line,varFunc,lineNum):
    leftParInd=line.index('(')

    if line[0:leftParInd]=="output":
        if varFunc==True:
            error="Error on line "+str(lineNum)+":\n    "+line[0:leftParInd]+"() does not have a return value and thus cannot be considered a value for a variable."
            print(error)
            return error
        else:
            output(lineNum)
    else:
        error="Error on line "+str(lineNum)+":\n    "+line[0:leftParInd]+"() is not a valid function."
        print(error)
        return error
    

with open('code.txt', 'r') as f:
    lines=f.readlines()
    i=0

    vars=[]

    for line in lines:
        if (line[len(line)-1]=='\n' and line[len(line)-2]==';') or (line[len(line)-1]==';'):
            #Sees if function
            leftParInd=line.find('(')
            if leftParInd!=-1:
                #Checks if variable
                varSub=varCheck(line[0:leftParInd])
                try:
                    variable=variable(varSub,funcs(line[(len(varSub)+1)::],True,i))
                    vars.append(variable)
                    if isinstance(variable.getValue,MethodType):
                        break
                except:
                    funcs(line,False,i)
        i+=1
