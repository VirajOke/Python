""" For, Nested IF and Function example """

def solution(numbers,pivot):
    for i in range(len(numbers)):
        if numbers[i]== 0:
            numbers[i]=0
        elif numbers[i]>0 and pivot>0 or numbers[i]<0 and pivot<0:
            numbers[i]= 1
        else:
            numbers[i]= -1
    return numbers
    
numbers = [6,-5,0]
pivot= 2
solution(numbers,pivot)

# Output: [1, -1, 0]
