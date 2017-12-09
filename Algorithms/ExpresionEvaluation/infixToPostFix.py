#PostFixtoInfix.py
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

def postfixToInfix(text):
    expresion = text.split()
    stk = Stack()
    infix =  ""
    
    #iterate throw expresion 
    for token in expresion:
        if isInt(token):
            infix+=token
            infix+=" "
        elif token =="(":
            stk.push(token)
        elif token==")":
            while stk.top()!= "(":
                infix+=stk.pop()
                infix+=" "
            stk.pop()
        elif token in ['+','-','*','/']:
            while (not stk.isEmpty() \
                   and precedence(stk.top())>=precedence(token)):
                infix+=stk.pop()
                infix+=" "
            stk.push(token)
            
    #append the remainded operatprs to expresion , if operator is ( it will be
    #disregarded
    while  not stk.isEmpty() :
        infix+=stk.pop()
        infix+=" "         
    return infix

def main():
    inp=input("Enter the infix expresion:")
    print(postfixToInfix(inp))
    
    
if __name__=="__main__":
    main()
        
            
    