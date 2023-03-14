st = "pynative"
# first approach with slicing
print(st[::-1])

#second approach with reversed() function
res = "".join(reversed(st))
print(res)