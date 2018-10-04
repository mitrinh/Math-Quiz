# Michael Trinh
# CS 3750
# Python Program : Math Quiz
# A simple math quiz game where you answer each question until you get one wrong

import random, time

# GLOBAL VARIABLES: list of operators, list of expressions, expression
#                   score, correct, difficulty, again
listOperators = ['+','-','*','/']
listExpression = []
expression = None
score = 0
correct = True
difficulty = None
retry = True

# gets the mathematical expression in list form
def getExpressionInList(listOperators, difficulty):
    # list output of expression
    listExpression = []
    # number of operands in expression, more than 2 operands adds complication
    # in calculating expression from string 
    operands = 2
    # create an expression in list form using a loop
    for num in range(0,operands):
        # add operand to the list
        listExpression.append(random.randint(1,difficulty))
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

# returns the math question
def getQuestion(expression):
    # returns question    
    return ('What is ' + expression + ' ? ')
# end getQuestion    

# returns the answer for the expression
def getAnswer(listEx):
    # calculates the answer depending on the operator
    if(listEx[1] == '+'):
        return listEx[0] + listEx[2];
    elif(listEx[1] == '-'):
        return listEx[0] - listEx[2];
    elif(listEx[1] == '*'):
        return listEx[0] * listEx[2];
    else:
        return listEx[0] / listEx[2];
# end getAnswer

# asks user to select the difficulty
def getDifficulty():
    # uses input for user to pick difficulty
    difficulty = input('Select Difficulty: easy, normal, hard ')
    # hard difficulty = 1000 range
    if (difficulty == 'hard'):
        return 1000
    # normal difficulty = 100 range
    elif (difficulty == 'normal'):
        return 100
    # (default) easy difficulty = 10 range
    return 10
# end getDifficulty

# main: quiz
# loop used to iterate many tries
while(retry):
    # updates difficulty
    difficulty = getDifficulty();
    # starts quiz
    print('Starting quiz...')
    print('REMINDER: irrational numbers are rounded to 15 decimal places after the decimal')
    # used for multiple iterations
    correct = True
    # keeps going until you get a question wrong
    while(correct):
        # updates listExpression
        listExpression = getExpressionInList(listOperators, difficulty)
        # updates expression
        expression = getExpression(listExpression)
        # prints math question and allow input for answer and puts it in int form
        myAnswer = float(input(getQuestion(expression)))
        # updates correct answer
        answer = getAnswer(listExpression)
        # if question is wrong stop test and give score
        if(myAnswer != answer):
            # prints correct answer then score
            correct = False
            print('INCORRECT: The answer was ' + str(answer) + '!')
            time.sleep(1)
            print('You got ' + str(score) + ' questions right!')
            # asks if you want to try quiz again
            retry = input('Try again? y or n ')
            if retry == 'y':
                retry = True
            else:
                retry = False
        # else if question is right, keep going and increment score    
        else:
            print('CORRECT!')
            score += 1
    # end quiz
