# 17: Find words with both alphabets and numbers

str1 = "Emma25 is Data scientist50 and AI Expert"

res = str1.split(" ")
s = []
for item in res:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        s.append(item)

for rs in s:
    print(rs)
