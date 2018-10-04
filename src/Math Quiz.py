# Michael Trinh
# CS 3750
# Python Program : Math Quiz
#   A simple math quiz game where you answer each question until you get one wrong

import random

# GLOBAL VARIABLES: list of operators and expression
listOperators = ['+','-','*','/']
expression = None

# gets the mathematical expression in list form
def getExpressionInList(listOperators):
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

# convert the list to string
def getExpression(listEx):
    # mathematical expression
    expression = ''
    # converts the expression from list form to string form
    for element in listEx:
        expression += str(element)
    return expression
# end getExpression

# prints the math question
def printQuestion(expression):
    # prints question    
    print('What is ' + expression + ' ?')
# end printQuestion    

# returns the position of the operator in the expression
def getOperator(listOp, expression):
    # operator not in expression returns -1
    operatorPosition = -1
    for operator in listOp:
        operatorPosition = expression.find(operator)
        if(operatorPosition != -1):
            return operatorPosition
    return operatorPosition    
# end getOperator

# calculates the answer for the expression
def getAnswer(expression):
    print(expression)
    print(getOperator(listOperators, expression))
# end getAnswer    

# set our global expression variable to getExpression return value
expression = getExpression(getExpressionInList(listOperators))
# prints the mathquestion
printQuestion(expression)
getAnswer(expression)
