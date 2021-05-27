s1 = input("enter first string:")
s2 = input("enter second string:")
i = 0
j = 0
output = ''
while i < len(s1) or j < len(s2):
    output = output+s1[i]+s2[j]
    i = i+1
    j = j+1
print(output)