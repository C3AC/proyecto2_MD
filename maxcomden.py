def mcd(n, m):
    if n == m or m == 0:
        return n
    m, n = n % m, m
    return mcd(n, m)
