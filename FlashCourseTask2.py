
def confession(name):
    while True:
        answer = input('%s, Do you confess? Yes or No?:' %(name))
        answer = answer.lower()
        if answer == 'yes' or answer == 'no':
            break
        else:
            print('Give me the damn answer!')
    return answer

def quesionLoop():

    while True:
        prisoner1 = input('What is your name?')
        result1 = confession(prisoner1)
        print('His answer is: %s' %(result1))

        prisoner2 = input('And what is your name?')
        result2 = confession(prisoner2)
        print('His answer is: %s' %(result2))

        judgeP1 = ''
        judgeP2 = ''
        if result1 == 'yes' and result2 == 'yes':
            judgeP1 = '10 Years'
            judgeP2 = '10 Years'
        elif result1 == 'yes' and result2 == 'no':
            judgeP1 = '1 Year'
            judgeP2 = '10 Years'
        elif result1 == 'no' and result2 == 'yes':
            judgeP1 = '10 Year'
            judgeP2 = '1 Years'
        else:
            judgeP1 = '3 Year'
            judgeP2 = '3 Years'          
        
        print('The final result is:',prisoner1,judgeP1,prisoner2,judgeP2)

        res = input('Exit? Yes or No:').lower()
        if res == 'yes':
            break



quesionLoop()





