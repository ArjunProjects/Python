# Arrange string characters such that lowercase letters should come first
# Given str = "PyNaTive"
# Expected output: yaivePNT

def lower_comes_first(act_str):
    low = []
    up = []
    for ch in act_str:
        if ch.islower():
            low.append(ch)
        else:
            up.append(ch)
    return "".join(low + up)


res = lower_comes_first("PyNaTive");
print(res)
