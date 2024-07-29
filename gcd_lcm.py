'''Given two numbers a and b. Find the GCD and LCM of and d.
Input:
* Two positive integers a and b (1 <=a, b <=1000)
Output:
For GCD function, an integer representing the GCD of a 'and b
For LCM function, an integer representing the LCM of a and b
Sample Input:
12 18
Output:
6
36'''

a,b=list(map(int,input().split()))
def gcd(a,b):
    while b:
      a,b=b,a%b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)
print(gcd(a,b))
print(lcm(a,b))