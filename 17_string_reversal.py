#extended slice syntax
# str[start:stop:step]

trial = "reversal"
new_trial = trial[::-1]

print(new_trial)

# String_reverse 2
def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:])+str[0]

str="reversal"
reverse = string_reverse(str)
print(reverse)