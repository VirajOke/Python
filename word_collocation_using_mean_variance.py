""" This Pyhton program aims to identify if the two words in a set of sentences are 
fixed collocation, flexible collocation or not a collocation using mean and variance method"""

import re
import math
from nltk.tokenize import word_tokenize

def difference(main_list,key_1,key_2):
    diff= []
    temp= []
    num1= 0
    num2= 0
    mu=0
    list_1= []
    for item in main_list:
        for string in item:
            list_1= word_tokenize(string)  
            n= len(list_1)
            #End of string splitting 
            for i in range(len(list_1)):
                for j in range(len(list_1)): 
                    if list_1[i]==key_1[0]:
                        num1= i
                    elif list_1[j]==key_2[0]:
                        num2= j
        x= num1-num2 
        diff.append(abs(x))
        diff_len= len(diff)
        #formula for collocation
        mu= sum(diff)/diff_len
        for i in range(diff_len):
            p= abs(diff[i]- mu)
            x = math.pow(p,2)
            temp.append(x)   
        s= math.sqrt(sum(temp)/diff_len)
    
    if s>0 and mu !=0:
        print("It is a flexible collocation.")
    elif s==0:
        print("It is a fixed collocation.")
    else:
        print("It is not a collocation.")
    return print("The value of µ is:",mu,"\n","The value of S is:",s)
    
main_list= []
n= int(input())
for i in range(0,n):
    aa= [input()] 
    main_list.append(aa)
key1= int(input())
key2= input()

difference(main_list,key1,key2)

"""
Input values used for the example:
main_list= [["knocked on the door"],['knocked at the door'],["knocked on John's door."],['knocked on the metal front door']]
key1= ['knocked']
key2= ['door']

Output:
It is a flexible collocation.
The value of µ is: 4.0 
 The value of S is: 1.2909944487358056
 """
