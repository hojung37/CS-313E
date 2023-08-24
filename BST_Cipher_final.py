import sys

class Node (object):
    def __init__ (self,data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

    def __str__ (self):
        return str(self.data)


class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = None
        
        #if character is alphabet or space, insert the character to create the tree
        for ch in encrypt_str:
            if ch.isalpha() or ch == ' ':
                self.insert(ch)
        
    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree. 
    def insert (self, ch):
        #using class notes
        new_node = Node(ch)
        if self.root == None:
            self.root = new_node
        
        else:
            curr = self.root
            
            while curr is not None:
                #parent is always above curr when moving
                parent = curr

                #if ch before curr, goes left
                if ch < curr.data :
                    curr = curr.lChild
                
                #if duplicate 
                elif ch == curr.data:
                    return '' 
                
                #if ch after curr, goes right
                else:
                    curr = curr.rChild
                

            if ch < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node 
                



    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.


    def search (self, ch):
    # search for a char and return string containing left (<) and right (>) to reach that char
    # blank if not exist
    # * if char is in root 

        curr = self.root
        added_str = ''
        # blank if not exist
            
        if curr is None:
            return ' '
        else:
        #if character is root of the tree, return * 
            if ch == self.root.data:
                return '*'
        #if character is not root of the tree
            else:
                while ch != curr.data:
                    #print("ch", ch, "added_str", added_str, "curr", curr)
                    #if character is before the data, < 
                    if ch < curr.data:
                        added_str += '<'
                        #print("go left")
                        #if before, goes on the left of the tree
                        curr = curr.lChild 
                    #if character is after the data, > 
                    elif ch > curr.data:
                        added_str += '>'
                        #print("go right")
                        #if after, goes on the right of the tree 
                        curr = curr.rChild 
        
    #return the final str
        #print()
        return added_str



    #while curr is not None and curr.data is not ch:
    #    if ch < curr.data:
    #        curr = curr.lChild
    #    else:
    #        curr = curr.rChild

    #return curr 

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.

    def traverse (self, st): #similar to search but instead looking at st 

        #take in the string of < and > and return the corresponding character
        #return empty if it does not lead to a valid character 

        curr = self.root
        
        #blank if not exist 
        if curr is None:
            return '' 
    
        #exists
        else:
            #make it to a list and if it is a '*' inside that list, do that
            st == st.split()
            #print(curr)
            for string in st:
                #print(string)
                #print(curr)
                
                if curr is None:
                    #print("trig")
                    break
                #if *, it means it is in the root so return self.root.data
                if string == '*':
                    return self.root.data

                #if <, it means that it is on the left (before) 
                elif string == '<':
                    curr = curr.lChild

                #if >, it means that it is on the right (after) 
                elif string == '>':
                    curr = curr.rChild 
                
                

            #return the final self.root.data 
            #print(last_curr)
            if curr is None:
                #print("last curr", last_curr.data)
                return ""
            else:
                #print("curr", curr.data)
                return curr.data




    #check 
    #def inOrder (self, node):
    #    if node:
    #        self.inOrder (node.lChild)
    #        print (node.data, end='')
    #        self.inOrder (node.rChild)





  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
    def encrypt (self, st):

    #take string as input
    #convert to lowercase & return encrypted str
    #ignore digit, punctuation, special char 
    
    #idea; 
    #if the st is alphabet, store and do search 
    #if not alphabet, ignore 

        #convert to lowercase 
        str = st.lower() 
        #print(str)
        full_encr = ''
        
        #similar to how i did in init
        for ch in str:
            #check if the character in str is alphabet or empty string
            if ch.isalpha() or ch == ' ':
                
                #if it is, do search to change the character to < > * 
                to_encr = self.search(ch)
                #print(ch, "\"", to_encr, "\"", counter, " " ,len(str), sep = "")
                #add that to empty string:
                full_encr += to_encr + ("!")

        return full_encr[:-1]




        #if str is True:
            #for i in str:
                #fin_encrypt = self.search(i)






  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
    def decrypt (self, st):
        #split the '!' , since that is not *,<,>
        str = st.split('!')
        full_decr = ''
        
        #take string as input
        #return decrypted

        for exp in str:
            #if <, >, * , do traverse and change to char
            to_decr = self.traverse(exp) 
            full_decr += to_decr

        return full_decr

    




def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()
    #print(encrypt_str)

    # create a Tree object
    the_tree = Tree (encrypt_str)

    #the_tree.inOrder(the_tree.root)

    #print(the_tree.search('u'))


    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print (the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()


  
    # print the decryption
    print (the_tree.decrypt(str_to_decode))
 
if __name__ == "__main__":
    main()
