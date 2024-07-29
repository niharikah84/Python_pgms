'''You are given an array A of size N. In one operation you can select any two elements 
from it, add their absolute difference in your score.
Your task is to find and return an integer value, representing the maximum score.
Note:
Assume 1 based indexing
The elements on which operation has been performed cannot be selected again.
Input Specification:
Input1: An integer value N, representing the size of array A
input2: An integer array A
Output Specification:
Return an integer value, representing the maximum score.
Sample Input:
4
1 2 3 4 
Sample Output: 4'''

'''N=int(input())
A=list(map(int,input().split()))
A.sort()
l=len(A)//2
a1,a2=A[0:l],A[l:N+1]
print(a1,a2)
diff=abs(sum(a2)-sum(a1))
print(diff)'''

n=int(input())
arr=list(map(int,input().split()))
arr.sort()
res=[]
start=0
end=-1
while len(arr)>=1:
    res.append(abs(arr[end]-arr[start]))
    arr.pop(start)
    arr.pop(end)
print(sum(res))