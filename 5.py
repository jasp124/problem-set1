def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]    #1: removes first letter
                                               #  [0] adds the first letter at the end

print(reverse_string("Hello World!"))
print("Hello World!"[::-1])
