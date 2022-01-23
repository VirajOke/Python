#Hacker rank challenge solution 1
# list comprehension python

def funct(x,y,z,n):
    list2= [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    return print(list2)
    
x= int(input())
y= int(input())
z= int(input())
n= int(input())
funct(x,y,z,n)

# when X= 1, y=1, z=1, n=2
# Output: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]] 
