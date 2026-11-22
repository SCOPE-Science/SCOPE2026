#!/usr/bin/env python3
"""Independent direct finite-level checks for consecutive even-power sums.

Only uses Python's integer arithmetic.  This is finite corroboration,
not a substitute for the symbolic theorem.
"""
from fractions import Fraction
from math import isqrt


def formula(p, k):
    assert p >= 3 and p % 2 and k >= 1
    chi = 1 if p % 4 == 1 else -1
    eta = (1 + chi) // 2
    R = (p - 4 - chi) // 4
    Z = 1 + sum((p - 1) * p ** (k - 2*j - 1) // 2
                for j in range(1, (k - 1) // 2 + 1))
    H = (p - 1) * p ** (k - 1) // 2 + Z
    J = H + (p - 1) * (R * p ** (k - 1) + (1 + eta) * Z)
    return H, Z, R, J


def direct(p, k):
    mod = p ** k
    period = p ** (k + 1)
    squares = {x*x % mod for x in range(mod)}
    s = 0
    histogram = [0, 0, 0, 0]  # both, first only, second only, neither
    marg = [0] * mod
    for n in range(period):
        first = s in squares
        nxt = (s + pow(n + 1, p - 1, mod)) % mod
        second = nxt in squares
        if first and second:
            histogram[0] += 1
        elif first:
            histogram[1] += 1
        elif second:
            histogram[2] += 1
        else:
            histogram[3] += 1
        marg[s] += 1
        s = nxt
    H, Z, R, J = formula(p, k)
    expected = [J, p*H-J, p*H-J, period-2*p*H+J]
    assert histogram == expected, (p, k, histogram, expected)
    assert all(m == p for m in marg), (p, k, min(marg), max(marg))
    assert s == 0, ('period', p, k, s)
    return period, histogram


def branch_isometries(p, k):
    # F_r(t) is bijective modulo p^k for every r modulo p.
    mod = p**k
    for r in range(p):
        value = sum(pow(i, p-1, mod) for i in range(1, r+1)) % mod
        # Scan n=r+pt without raising huge powers.
        hits = set()
        for t in range(mod):
            hits.add(value)
            for i in range(r+p*t+1, r+p*(t+1)+1):
                value = (value + pow(i, p-1, mod)) % mod
        assert len(hits) == mod, (p, k, r, len(hits))
    return p*mod


def density(p):
    chi = 1 if p % 4 == 1 else -1
    R = (p - 4 - chi) // 4
    eta = (1+chi)//2
    mu = Fraction(p, 2*(p+1))
    delta = Fraction(p-1,p) * (
        Fraction(R,p) + Fraction(1+eta,2*p*(p+1))) + mu/p
    covariance = delta - mu*mu
    assert (covariance > 0) == (p % 4 == 3)
    return str(mu), str(delta), str(covariance)


def main():
    cases = [(p,k) for p,ks in {
        3:[1,2,3,4,5], 5:[1,2,3,4], 7:[1,2,3,4],
        11:[1,2,3], 13:[1,2,3], 17:[1,2], 19:[1,2]
    }.items() for k in ks]
    total = 0
    for p,k in cases:
        n,_ = direct(p,k)
        total += n
    for p,k in [(3,4),(5,3),(7,2),(11,2)]:
        branch_isometries(p,k)
    for p in [3,5,7,11,13,17,19,23,29,31,37,41,43]:
        density(p)
    print('PASS: exact four-cell table, p-to-one marginals and full periods')
    print('prime-power cases:',len(cases),'indices directly checked:',total)
    print('PASS: branch bijections for p=3,k=4;5,3;7,2;11,2')
    print('PASS: covariance sign for 13 odd primes')
    for p in [3,5,7,11,13]:
        print('density',p,*density(p))

if __name__ == '__main__':
    main()
