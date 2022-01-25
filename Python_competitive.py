# Python competitive coding solutions (Hacker Rank) 
""" 1. Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given scores. Store them in a list and find the score of the runner-up """

arr= [2, 3, 6, 6, 5]
first = max(arr)
last= min(arr)
uniq= []


for i in arr:
    if i not in uniq:
        uniq.append(i)
for i in range(len(uniq)):
    for j in range(len(uniq)-1):
        if uniq[j]>uniq[j+1]:
            uniq[j],uniq[j+1]= uniq[j+1],uniq[j]
n= len(uniq)
runner_up= uniq[n-2]
print("The unsorted list of scores are:", arr)
print("The sorted list of scores are:", uniq)
print("Score of the first position is: ", first)
print("Score of the runner-up is: ", runner_up)

Output: 
        The unsorted list of scores are: [2, 3, 6, 6, 5]
        The sorted list of scores are: [2, 3, 5, 6]
        Score of the first position is:  6
        Score of the runner-up is:  5

