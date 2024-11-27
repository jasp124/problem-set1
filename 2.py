def recursive_power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / recursive_power(base, -exp)

    else:
        return base * recursive_power(base, exp - 1)


result = recursive_power(2, 3)  
print(result)