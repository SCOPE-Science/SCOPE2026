#!/usr/bin/env python3
"""Independent finite tests of a Dombos partition congruence and ideal-count law."""
from math import isqrt

LIMIT = 300

def factor(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def chi24(d):
    if d % 2 == 0 or d % 3 == 0:
        return 0
    return 1 if d % 24 in (1, 5, 7, 11) else -1

def divisor_char_sum(m):
    return sum(chi24(d) for d in range(1, m+1) if m % d == 0)

def prime_criterion(m):
    f = factor(m)
    a = f.pop(3, 0)
    odds = [p for p,e in f.items() if e % 2]
    if len(odds) != 1:
        return False
    p = odds[0]
    return f[p] % 4 == 1 and p % 24 == (5 if a % 2 == 0 else 7)

def reps(m):
    c = 0
    for x in range(1, isqrt(m//2)+1, 2):
        y2, rem = divmod(m-2*x*x, 3)
        if rem == 0 and y2 > 0:
            y = isqrt(y2)
            if y % 2 and y*y == y2:
                c += 1
    return c

def main():
    total = 6*(LIMIT-1)+4
    dp = [0]*(total+1)
    dp[0] = 1
    for k in range(1, total+1):
        if k % 4 == 0 or k % 6 in (1,5):
            for v in range(k, total+1):
                dp[v] = (dp[v]+dp[v-k]) % 4
    twos = 0
    for n in range(LIMIT):
        m = 8*n+5
        lhs = dp[6*n+4]
        ideal = divisor_char_sum(m)
        theta = reps(m)
        criterion = prime_criterion(m)
        assert lhs == ideal % 4 == (2*theta)%4, (n,lhs,ideal,theta)
        assert (lhs == 2) == criterion, (n,lhs,criterion)
        twos += criterion
    print('DOMBOS_QUADRATIC_CHARACTER_OK', LIMIT, twos)
if __name__ == '__main__':
    main()
