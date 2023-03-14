# Calculate the sum and average of the digits present in a string
# Given str1 = "PYnative29@#8496"
# Output Sum is: 38 Average is  6.333333333333333

import re

def cal_sum_avg(str):
    total = 0
    count = 0
    for c in str:
        if c.isdigit():
            total = total+int(c)
            count = count+1
        else:
            continue
    return total/count


#print(cal_sum_avg("PYnative29@#8496"))

# another approach with regular expressions
str1 = "PYnative29@#8496"

digits = [int(num) for num in re.findall(r"\d", str1)]
alphas = [str(ch) for ch in re.findall(r'[a-zA-Z]+', str1)]
print(alphas)
total = sum(digits)
avg = total/len(digits)

print(f"sum is {total} and avg is {avg}")
