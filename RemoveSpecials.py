# Remove special symbols / punctuation from a string
import  re
str1 = "/*Jon is @developer & musician"

res = ""
for st in str1:
    if st.isdigit() or st.isalpha():
        res += st
    else:
        continue
print(res)

#Approach2
# res = re.sub(r'[^\w\s]', "", str1)
# print(res)