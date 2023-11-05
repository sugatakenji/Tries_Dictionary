#Testando a estrutura de Tries
#Criando a classe dos nodes desse arvore
import pickle
from parserXML import *
class TrieNode:
    #Constructor
    def __init__(self):
        self.child = [None for _ in range(26)]
        #Conta quantas palavras est'ao associadas a este node
        self.wordCount = 0
        self.meaning = ""

    def nNodes(self):
        nNodes = 0
        for c in self.child:
            if c != None:
                nNodes += 1
        return nNodes
        

def insertKey(root, key, meaning):

    currentNode = root
    #Iterando atraves do tamanho da string.
    #ord(c) - ord('a') retorna a posicao do da letra c enre 0 - 26.
    for c in key:
        if currentNode.child[ord(c) - ord('a')] == None:
            newNode = TrieNode()
            currentNode.child[ord(c) - ord('a')] = newNode
        currentNode = currentNode.child[ord(c) - ord('a')]
    
    #O ultimo node possui o worldcount = 1, o que serve para demarcar uma palavra
    currentNode.wordCount += 1
    currentNode.meaning = meaning

def searchKey(root, key):

    currentNode = root

    for c in key:
        if currentNode.child[ord(c) - ord('a')] == None:
            return False
        currentNode = currentNode.child[ord(c) - ord('a')]
    if currentNode.wordCount >= 1:
        return True, currentNode.meaning
    return False

def serialize(root, filename):
        with open(filename, 'wb') as file:
            pickle.dump(root, file)


#node is the root node of tree or subtree
#level is de depth of the node. Root node of tree have depth equal to 0
def printNode(node, level):
    global f
    n = 0 #The index of childNode 
    nNode = node.nNodes()#The number of childNumber order
    #Verifica quantos nodes tem. IMportante para ver se colocar vigula no colchete de fechamento 
    for c in node.child:
        if c != None:
            
            letter = chr(ord('a')+n) #Turn the index in a representive letter
            print((level * "    ")+('"'+letter+'"'+': ' + '{')+" ")
            f.write((level * "    ")+('"'+letter+'"'+': ' + '{')+" "+"\n")
            #Print meanig 
            if (c.meaning != "") and (c.nNodes() >> 0):
                print((level + 1) * "    "+"\"meaning\" : \""+c.meaning+"\",")
                f.write((level + 1) * "    "+"\"meaning\" : \""+c.meaning+"\","+"\n")
            elif c.meaning != "":
                print((level + 1) * "    "+"\"meaning\" : \""+c.meaning+"\"")
                f.write((level + 1) * "    "+"\"meaning\" : \""+c.meaning+"\"\n")

            printNode(c, level + 1) # Now, print the child nodes of this node
            
            #Fecha colchetes do objeto.
            nNode -= 1
            if nNode > 0:
                print(level * "    " + "},")
                f.write(level * "    " + "},"+"\n") 
            else:
                print(level * "    " + "}")
                f.write(level * "    " + "}"+"\n")
        n += 1
    

if __name__ == "__main__":
    global f
    f = open("b.json", "x")
    f.write("{\n")
    dictB = dictXML()
    rootNode = TrieNode()
    valid = True
    for word in dictB:
        valid = True
        for c in word[0]:
            c = c.lower()
            if ((ord(c) - ord('a')) > 26)  or ((ord(c) - ord('a')) < 0):
                valid = False
                print(c)
                print(ord(c) - ord('a'))
        if valid:
            print("foi")
            insertKey(rootNode, word[0].lower(), word[1])
        
    printNode(rootNode, 0)
    f.write("}")
