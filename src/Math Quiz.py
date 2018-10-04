# Michael Trinh
# CS 3750
# Python Program : Math Quiz

import random, math

# list of operators and expression
listOperators = ['+','-','x','/','**']
# mathematical expression
expression = ''

# gets the mathematical expression in list form
def getExpression(listOperators):
    # list output of expression
    listExpression = []
    # number of operands in expression, more than 2 operands adds complication
    # in calculating expression from string 
    operands = 2
    # create an expression in list form using a loop
    for num in range(0,operands):
        # add operand to the list
        listExpression.append(random.randint(0,10))
        # add an operator after all operands except last one
        if(num != (operands-1)):
            listExpression.append(random.choice(listOperators))
    return listExpression        
# end getExpression

# prints the question
def printQuestion(list, expression):
    # converts the expression from list form to string form
    for element in list:
        expression += str(element)
    # prints question    
    print('What is ' + expression + ' ?')
# end printQuestion

printQuestion(getExpression(listOperators), expression)

