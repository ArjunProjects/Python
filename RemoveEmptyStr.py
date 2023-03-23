# Remove empty strings from a list of strings
#given  str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# output = ['Emma', 'Jon', 'Kelly', 'Eric']


str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# create an empty list to store strings whose length is greater than zero
str_after_removing_empty_str = []

# approach 1
for st in str_list:
    if st:
        str_after_removing_empty_str.append(st)

print(str_after_removing_empty_str)

# approach 2
new_str = list(filter(None, str_list))
print(new_str)
