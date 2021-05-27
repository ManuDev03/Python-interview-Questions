s = input("enter a alphanumeric :")
alphabets = []
digits = []

for ch in s :
    if ch.isalpha():
        alphabets.append(ch)
    else :
        digits.append(ch)
output = ''.join(sorted(alphabets) + sorted(digits))
print(output)
