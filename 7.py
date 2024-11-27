def max_value(s):
    if len(s) == 1:
        return s[0]
    else:
        return max(s[0], max_value(s[1:len(s)]))
list1 = [10,12,15,14]
print(max_value(list1))
