"""Exact arithmetic checks of the even-cycle vertex-set Walsh theorem."""
from itertools import permutations
from math import comb, factorial

checks = 0

def check(statement):
    global checks
    assert statement
    checks += 1

def formula(n, k):
    if not n % 2 and k % 2:
        return 0
    return factorial(k) * factorial(n-k) * comb(n//2, k//2)**2

def direct_kernel(n):
    ans = [0] * (1 << n)
    for p in permutations(range(n)):
        seen = 0
        even = 0
        for i in range(n):
            if seen & (1 << i):
                continue
            cycle = []
            j = i
            while not (seen & (1 << j)):
                seen |= 1 << j
                cycle.append(j)
                j = p[j]
            if len(cycle) % 2 == 0:
                for j in cycle:
                    even |= 1 << j
        ans[even] += 1
    return ans

def transform(a, n):
    a = a[:]
    for i in range(n):
        bit = 1 << i
        for mask in range(1 << n):
            if not (mask & bit):
                x, y = a[mask], a[mask | bit]
                a[mask] = x + y
                a[mask | bit] = x - y
    return a

for n in range(1, 9):
    ker = direct_kernel(n)
    check(sum(ker) == factorial(n))
    vals = transform(ker, n)
    for mask, actual in enumerate(vals):
        check(actual == formula(n, mask.bit_count()))
        check(actual >= 0)
    for mask, count in enumerate(ker):
        check(count == 0 if mask.bit_count() % 2 else count > 0)
    check(sum(v != 0 for v in vals) == (2**n if n % 2 else 2**(n-1)))
    positive_vals = [v for v in vals if v]
    check(max(positive_vals) == factorial(n))
    if n % 2:
        check(min(positive_vals) == factorial(n-1))
    else:
        m = n//2
        check(min(positive_vals) == min(formula(n, 2*r) for r in range(m+1)))

# Integer-only all-dimension identity and exact extremizers.
for n in range(1, 201):
    values = [formula(n, k) for k in range(n+1)]
    check(values[0] == values[-1] == factorial(n))
    for k in range(n+1):
        check(values[k] == values[n-k])
        check(0 <= values[k] <= factorial(n))
    if n % 2:
        check(all(v > 0 for v in values))
        check(min(values) == factorial(n-1))
        if n >= 3:
            check([k for k,v in enumerate(values) if v == factorial(n-1)] == [1,n-1])
    else:
        m = n//2
        check(all((v == 0) == bool(k % 2) for k,v in enumerate(values)))
        rmin = [(m//2)] if m % 2 == 0 else [(m-1)//2, (m+1)//2]
        minval = min(v for v in values if v)
        check([k for k,v in enumerate(values) if v == minval] == [2*r for r in rmin])
        for r in range(m):
            left, right = values[2*r], values[2*r+2]
            cmp = (right > left) - (right < left)
            check(cmp == ((2*r+1 > m) - (2*r+1 < m)))
print('PASS:', checks, 'exact checks; n=1..8 independent permutation enumeration, n=1..200 symbolic-spectrum integers')
