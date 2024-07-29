'''Alex is exploring a series and she came across a special series, in which
f(N)=f(N-1)f(N-1)+(N-2)(N-2) mod 47
where f(0) = 1. f(1)=1
Your task is to help Alex find and return an integer value, representing the 
Nth number in this special series.
Input Specification:input1: An integer value N.
Output Specification:
Return an integer value, representing the Nth number in this special.'''

def alex(n):
    if n==0 or n==1:
        return 1
    else:
        return (alex(n-1)*alex(n-1)+(n-2)*(n-2))%47
num=int(input())
print(alex(num))