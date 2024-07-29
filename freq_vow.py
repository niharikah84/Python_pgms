'''Given a string s print the most frequent vowel that is present in the string as a output.
Input Format:
A single line containing the string s.
The input will be read from the STDIN by the candidate
Output Format:
Print a single character which represents the most frequent vowel in the given string.
Example:
Input:
helloworld
Output:
o'''

s=input().lower()
a='aeiou'
dic={}
for char in s:
    if char in a:
        dic[char]=s.count(char)
    else:
        pass
print(max(dic,key=dic.get))