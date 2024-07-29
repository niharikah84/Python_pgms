'''You are given a list of integers, and your task is to find the subarray with the maximum sum. 
Write a function or method to solve this problem efficiently and return the maximum sum.
Input:
n: the no of elements in the array
nums (List of integers): A list of integers (1 <= len(nums) <= 10^5)
Sample input:
8
-1 2 3 10 -4 7 2 -5
Sample output:
20
Explanation:
The max subarry sum is 20. The subarray is [2,3,10,-4,7,2]'''

'''
def solve(nums,n):
    currsum=nums[0]
    maxsum=nums[0]
    for num in nums[1:]:
        maxsum=max(num,maxsum+num)
        currsum=max(currsum,maxsum)
    return currsum
n=int(input())
arr=list(map(int,input().split()))
print(solve(arr,n))'''

n=int(input())
arr=list(map(int,input().split()))
max_sum=-float("inf")
present_sum=0
for i in arr:
    present_sum+=i
    max_sum=max(max_sum,present_sum)
    if present_sum<0:
        present_sum=0
print(max_sum)