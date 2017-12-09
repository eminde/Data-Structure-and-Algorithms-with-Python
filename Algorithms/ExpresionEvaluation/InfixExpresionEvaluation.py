#Infix Expression Evaluation 
#22 Oct 2017 
#Written By Amin De
#DS & Algorithms With Python

from Stack import Stack

#a list contians operations


#check Whether a token (str) is integer or not
def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
#return the integer value for precedence of an operation
def precedence(operate):
    return {
        '(': 0,
        ')': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }[operate]
    
#given operator and operands calculate the result
def cal(rhs,lhs,operate):
    return {
        '+': lhs+rhs,
        '-': lhs-rhs,
        '*': lhs*rhs,
        '/': lhs/rhs
    }[operate]


def operate(operatorStk,operandStk,operator):
    if operator=="(":
        operatorStk.push(operator)
        return
    while precedence(operator)<= precedence(operatorStk.top()):
    
        topOp=operatorStk.pop()
        if topOp in ['+','-','*','/']:
            operandStk.push(cal(operandStk.pop(),operandStk.pop(),topOp))

        if topOp=="(" and operator==")":
            return
        
    operatorStk.push(operator)
    return
 
                         
    
    
def eval(text):
    expresion = text.split()
    operandStk = Stack()
    operatorStk = Stack()
    operatorStk.push("(")
    
    for token in expresion:
        if isInt(token):
            operandStk.push(int(token))
        else :
            operate(operatorStk,operandStk,token)
            
    operate(operatorStk,operandStk,")")
    return operandStk.pop()


    
def main():
    while True:
        text=input("please enter the infix expresion(enter Q to Exit):")
        if text[0] =='Q' or text[0]=='q':
            return 
        print(text+' = '+str(eval(text)))
    
    
if __name__ =="__main__":
    main()