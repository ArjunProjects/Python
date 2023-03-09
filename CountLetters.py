#  Count all letters, digits, and special symbols from a given string
# str1 = "P@#yn26at^&i5ve"

def count_letters(act_str):
    digits = 0
    alpha = 0
    spl = 0
    for ch in act_str:
        if ch.isalpha():
            alpha += 1
        elif ch.isdigit():
            digits += 1
        else:
            spl += 1
    return f" letters = {alpha}\n digits = {digits}\n specials = {spl} "


res = count_letters("P@#yn26at^&i5ve")
print(res)
