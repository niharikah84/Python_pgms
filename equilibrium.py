'''You are given an array A of N integers. An equilibrium position is a position where the 
sum of all integers on its left is equal to the sum of all integers on its right in the array 
A. Print the index of the equilibrium position.
Note:For any given array there is only a single equilibrium position, if no equilibrium 
position is found then print "NOT FOUND" without quotes.
The array is 1 indexed.
Input Format:
The input consists of two lines:
The first line contains an integer denoting N.
The second line contains N space-separated integers denoting the elements of the 
array A.
Input will be read from the STDIN by the candidate
Output Format:
Print the index of the equilibrium position. If no index is found, print "NOT FOUND"
Sample Input
5
2 4 3 2 7
Sample Output
3'''

n=int(input())
arr=list(map(int,input().split()))
flag=True
for i in range(1,n+1):
    if sum(arr[:i+1])==sum(arr[i+1:]):
        flag=False
        print(i+1)
        break
if flag:
    print("Not found")