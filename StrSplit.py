# Write a program to split a given string on hyphens and display each substring.

# str1 = Emma-is-a-data-scientist

str1 = "Emma-is-a-data-scientist"
after_split = str1.split("-")
for word in after_split:
    if word == "data":
        print("data found")
        break
    else:
        continue
else:
    print("not found")
print(str1.split("-"))
