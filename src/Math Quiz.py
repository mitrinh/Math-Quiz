# Michael Trinh
# CS 3750
# Python Program

import random

# list of operations and expression
listOperations = ['+','-','x','/']
listExpression = None

# gets the mathematical expression in list form
def getExpression(listOperations):
    # number of operands here, at least 2
    operands = 2
    print('Starting Test...')
    # create an expression in list form using a loop
    for num in range(0,operands):
        # add operand to the list
        listExpression.append(random.randint(1,10))
        # add an operator after all operands except last one
        if(num != (operands-1)):
            listExpression.append(listOperations)
# end getExpression

# prints the question
def printQuestion(list):
    for element in list:
        if(element == list[0]):
            expression = element
        else:
            expression += element
    print('What is ' + expression + ' ?')
# end pringQuestion

getExpression(listOperations)
printQuestion(listExpression)
