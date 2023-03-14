
#Write a program to count occurrences of all characters within a string

#create an empty dictionary to store the result. character is the key, and the count is the value
#Iterate each character from a string s1 using a loop
#In the body of a loop, use the count() function to find how many times a current character appeared in a string
#Add key-value pair in a dictionary

st = "Apple"
char_dic = dict()
for ch in st:
    cnt = st.count(ch)
    char_dic[ch] = cnt
print(char_dic)




