#  File: ExpressionTree.py

#  Description: Create expression tree and calculate and also get prefix and postfix expression

#  Student Name: hojung kim

#  Student UT EID: hk25322

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 11/7

#  Date Last Modified: 11/8

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        #node = Node()
        #starting from the root, call it "current node"
        self.root = Node()
        curr_node = self.root
        #split the expression 
        split_expr = expr.split()
        
        #stack to create the tree 
        empty_stack = Stack()
        tree = Tree() 

    
    #string broke into tokens [left parenthesis, right parenthesis, operator, operand]
    #left- new expression
    #right- ending expression 
        operands = [0,1,2,3,4,5,6,7,8,9]
        operators = ['+','-','%','*','**','/','//']
      
        #token in the expression
        for curr_token in split_expr:
            #if curr_token is left parenthesis, 
            if curr_token == '(':
                #add a new node as the left child of curr_node
                curr_node.lChild = Node()
                #push curr_node on the stack
                empty_stack.push(curr_node)
                #make curr_node equal to left child
                curr_node = curr_node.lChild 

            #if curr_token is operator, (like +,-,*)
            elif curr_token in operators:
                #set curr_node's data value to the operator
                curr_node.data = curr_token
                #push curr_node on the stack
                empty_stack.push(curr_node) 
                #add a new node as the right child of curr_node 
                curr_node.rChild = Node() 
                #make curr_node equal to right child 
                curr_node = curr_node.rChild

            #if curr_token is operand, (like 1,2,3)
            #elif curr_token in operands:
                #set curr_node's data to the operand
            #    curr_node.data = curr_token 
                #make curr_node equal to parent by popping the stack
            #    curr_node = empty_stack.pop ()
                 


            #if curr_token is a right parenthesis,
            elif curr_token == ')': 
                #make curr_node equal to the parent node by popping the stack if it's not empty 
                if empty_stack.is_empty is not False: 
                    curr_node = empty_stack.pop() 

            else:
                #set curr_node's data to the operand
                curr_node.data = curr_token 
                #make curr_node equal to parent by popping the stack
                curr_node = empty_stack.pop()

    # this function should evaluate the tree's expression
    
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        operands = [0,1,2,3,4,5,6,7,8,9]
        operators = ['+','-','%','*','**','/','//']


        if aNode == '+':
            return self.evaluate (aNode.lChild) + self.evaluate (aNode.rChild)

        elif aNode == '-':
            return self.evaluate (aNode.lChild) - self.evaluate (aNode.rChild)

        elif aNode == '/':
            return self.evaluate (aNode.lChild) % self.evaluate (aNode.rChild)
        
        elif aNode== '//':
            return self.evaluate (aNode.lChild) * self.evaluate (aNode.rChild)

        elif aNode == '%':
            return self.evaluate (aNode.lChild) - self.evaluate (aNode.rChild)

        elif aNode == '**':
            return self.evaluate (aNode.lChild) % self.evaluate (aNode.rChild)
        
        elif aNode== '*':
            return self.evaluate (aNode.lChild) * self.evaluate (aNode.rChild)


        #professor told me to do it recursively instead
        #so similar to what I did but recursively
        if aNode is not None:
            #traversing left child
            l_chi = (self.evaluate(aNode.lChild))
            #traversing right child
            r_chi = (self.evaluate(aNode.rChild))
            #calculate, has to be changed to a string
            node = eval(str(l_chi)+str(aNode.data)+str(r_chi))
            #change to float to fit format
            return float(node)
        else:
            return " "

        

    
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        #from lecture notes
        s = "" 
        if aNode is not None:
            s = str(aNode.data) + " "
            #print (aNode.data, end = " ")
            s += self.pre_order(aNode.lChild)
            s += self.pre_order(aNode.rChild)
        return s

        

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        #from lecture notes
        if aNode is not None:
            self.post_order (aNode.lChild)
            self.post_order (aNode.rChild)
            print (aNode.data, end = " ")
            

# you should NOT need to touch main, everything should be handled for you
#professor helped with debugging and he helped with touching main 
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
    tree = Tree()
    tree.create_tree(expr)


    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())
    

    # get the postfix version of the expression and print
    print("Postfix Expression: ", end = "")
    tree.post_order(tree.root)
    print()
    #print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()