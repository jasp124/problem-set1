def is_prime(n, i=2):
    if n <= 2:
        if n == 2:
            return True
        return False
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)


print(is_prime(19))