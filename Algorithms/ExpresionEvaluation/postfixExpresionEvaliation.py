#postfixExpresionEvaliation.py
#23 Oct 2017
#Written By Amin De
#DS and Algorithms with Dr.Mahdevar

from Stack import Stack

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

def eval(text):
    expresion = text.split()
    stk = Stack()
    
    for token in expresion:
        if isInt(token):
            stk.push(token)
        if token in "+/-*":
            stk.push(cal(int(stk.pop()),int(stk.pop()),token))
           
    return stk.pop()

def main():
    inp=input("Enter the postfix expresion:")
    print(eval(inp))
    
    
if __name__=="__main__":
    main()