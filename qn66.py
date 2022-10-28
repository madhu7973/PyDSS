def get_last_digit(n):
    """Returns the last digit of n."""
    n = str(n)
    return int(n[len(n)-1])
n = get_last_digit(12.34)
print(n)