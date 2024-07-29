'''You are given an array A of N integers. The array A can be divided into two parts: the 
first part consists of the first 'i' elements of A (where ranges from 1 to N), and the 
second part consists of the last (N-i) elements of A
Your task is to find and return a new array named result of the same size as A, where 
each element of result[i] represents the absolute difference between the sum of the 
elements in the first part of A and the sum of the elements in the second part of A
Note: For i= N,N-i=0.So, consider the sum of last N-i integers as 0 in this case
Input Specifications:
input1: An integer value representing the size of the array A.
input2: An integer array A.
Output Specification:

Return a new integer array named result of the same size as A, where each element of 
result[i) represents the absolute difference between the sum of the elements in the 
first part A and the sum of the elements in the second part of A
Sample Input:
5
1 2 3 4 5
Sample Output:
[13, 9, 3, 5, 15]'''

res=[]
n=int(input())
arr=list(map(int,input().split()))
for i in range(1,n+1):
    arr1,arr2=arr[0:i],arr[i:n+1]
    diff=abs(sum(arr1)-sum(arr2))
    res.append(diff)
print(res)