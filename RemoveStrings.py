import re

# Approach1
str1 = 'I am 25 years and 10 months old'
res = ""
for st in str1:
    if st.isdigit():
        res += st
    else:
        continue

print(res)

# Approach2
# s = "".join(item for item in str1 if item.isdigit())
# print(s)
