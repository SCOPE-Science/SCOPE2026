"""Direct finite check of two-base palindromes and exact length counts.

No external dependencies. The theorem is proved independently of this finite check.
"""
from math import ceil

def digits(n, b):
    z = []
    while n:
        z.append(n % b)
        n //= b
    return z

def pal(n, b):
    a = digits(n, b)
    return bool(a) and a == a[::-1]

def formula(b, k, m, s):
    return (b-1) * b**((s-1)//2 + (s+1)//2 * ((m+1)//2-1))

def blocks_condition(n, b, k, m, s):
    q = b**k
    blocks = []
    for _ in range(m):
        value = n % q
        n //= q
        blocks.append(digits_fixed(value, b, k))
    return (n == 0 and blocks[-1][s-1] != 0 and
            all(all(t == 0 for t in z[s:]) for z in blocks) and
            blocks == blocks[::-1] and
            all(z[:s] == z[:s][::-1] for z in blocks))

def digits_fixed(n,b,k):
    z = []
    for _ in range(k):
        z.append(n%b)
        n //= b
    return z

bin_checks = 0
integers_checked = 0
for b in (2,3,4):
    for k in range(2,6):
        for m in range(1,6):
            for s in range(1,k+1):
                low = b**(k*(m-1)+s-1)
                high = b**(k*(m-1)+s)
                if high > 250000:
                    continue
                actual = 0
                for n in range(low, high):
                    present = pal(n,b) and pal(n,b**k)
                    assert present == blocks_condition(n,b,k,m,s), (b,k,m,s,n)
                    actual += present
                expected = formula(b,k,m,s)
                assert actual == expected, (b,k,m,s,actual,expected)
                bin_checks += 1
                integers_checked += high-low
                M = m
                cumulative_formula = sum(formula(b,k,j,t) for j in range(1,M+1) for t in range(1,k+1))
                # Direct partial cumulative check at B^(M) requires available upper bound.
                if b**(k*M) <= 250000:
                    direct_total = sum(pal(z,b) and pal(z,b**k) for z in range(1,b**(k*M)))
                    assert direct_total == cumulative_formula
print(f'VERIFY_OK: {bin_checks} exact length bins and {integers_checked} direct integer tests')
