#!/usr/bin/env python3
"""Exact mod-19 certificate for nonsymmetric Euler exponents of 9-color components.

Only Python's standard library is needed. All operations are in F_19 and
truncated formal series. References: Bilgici, arXiv:2611.24516v1,
Theorems 2.3 and 3.2 and Question 2 (Section 8).
"""
from itertools import combinations_with_replacement
from math import comb

MOD = 19
YDEG = 19
QDEG = 19 * YDEG + 18


def multiply(f, g, bound=YDEG):
    h = [0] * (bound + 1)
    for i in range(min(len(f), bound + 1)):
        for j in range(min(len(g), bound + 1 - i)):
            h[i + j] = (h[i + j] + f[i] * g[j]) % MOD
    return h


def inverse(f, bound=YDEG):
    assert f[0] % MOD
    g = [0] * (bound + 1)
    g[0] = pow(f[0], -1, MOD)
    for n in range(1, bound + 1):
        g[n] = -g[0] * sum(f[k] * g[n-k] for k in range(1, n+1)) % MOD
    return g


def theta_factors():
    out = {}
    for a in range(10):
        f = [1] + [0] * YDEG
        roots = [19] if a == 0 else [a, 19 - a]
        for v in roots:
            for j in range(v, YDEG + 1, 19):
                for n in range(YDEG, j - 1, -1):
                    f[n] = (f[n] - f[n-j]) % MOD
        out[a] = f
    return out


def nine_colored_partitions():
    # 9 independent colors of every allowed part size, with unlimited repetition.
    p = [0] * (QDEG + 1)
    p[0] = 1
    for part in range(1, QDEG + 1):
        for color in range(9):
            for n in range(part, QDEG + 1):
                p[n] = (p[n] + p[n-part]) % MOD
    return p


def euler_exponents(unit):
    """Return unique exponents e_1,...,e_18 modulo 19, from yH'/H."""
    assert unit[0] == 1
    inv = inverse(unit, 18)
    yp = [0] * 19
    for n in range(1, 19):
        yp[n] = n * unit[n] % MOD
    log = multiply(yp, inv, 18)
    ex = [0] * 19
    for n in range(1, 19):
        preceding = sum(d * ex[d] for d in range(1,n) if n % d == 0)
        ex[n] = (-log[n] - preceding) * pow(n, -1, MOD) % MOD
    # Exact reconstruction by finite product, independently of log derivative.
    h = [1] + [0] * 18
    for n in range(1,19):
        factor = [0] * 19
        for k in range(0, 19//n+1):
            if k*n > 18: break
            factor[n*k] = ((-1)**k * comb(ex[n],k)) % MOD
        h = multiply(h, factor, 18)
    assert h == unit[:19], 'Euler-factor reconstruction mismatch'
    return ex


def source_dissection(factors):
    """Independent Theorem 2.3 computation of 19 two-quartic components."""
    b = [[0] * (YDEG + 1) for _ in range(19)]
    for a in range(1,10):
        for z in range(a+1,10):
            epsilon = (3*a*a + 3*z*z - 19*a - 57*z + 300)//2
            shift,r = divmod(epsilon, 19)
            coef = -3 * (-1)**(a+z) * a*z * (z*z-a*a)
            product = [1] + [0]*YDEG
            for j in (a,z,min(a+z,19-a-z),z-a):
                product = multiply(product, factors[j])
            for n in range(YDEG+1-shift):
                b[r][n+shift] = (b[r][n+shift] + coef * product[n]) % MOD
    return b


# Reported exact certificate (r, initial y-order, leading coefficient,
# first Euler exponent, eighteenth Euler exponent).
EXPECTED = [
    (0,0,1,15,4), (1,0,9,14,15), (2,0,16,14,4),
    (3,0,8,15,15), (4,0,9,4,1), (5,0,10,0,15),
    (6,1,15,1,0), (7,0,6,1,2), (8,0,6,0,1),
    (9,0,7,0,9), (10,0,9,16,11), (11,0,9,4,7),
    (12,0,13,14,9), (13,1,3,0,8), (14,0,7,0,12),
    (15,0,15,0,1), (16,0,18,6,3), (18,0,14,4,0)
]


def main():
    p = nine_colored_partitions()
    factors = theta_factors()
    d = [1]+[0]*YDEG
    for j in range(1,10):
        d = multiply(d, factors[j])
    d_over_p0 = multiply(d, inverse(factors[0]))
    by_partition = []
    for r in range(19):
        phi = [p[r+19*n] for n in range(YDEG+1)]
        by_partition.append(multiply(phi, d_over_p0))
    by_source = source_dissection(factors)
    assert by_partition == by_source, 'Independent series identities disagree'
    assert by_partition[17] == [0]*(YDEG+1)

    records=[]
    for r in range(19):
        if r == 17: continue
        b=by_partition[r]
        s=next(i for i,v in enumerate(b) if v)
        c=b[s]
        assert s<=1, (r,s)
        unit=[v*pow(c,-1,MOD)%MOD for v in b[s:s+19]]
        assert len(unit)==19
        e=euler_exponents(unit)
        records.append((r,s,c,e[1],e[18]))
        assert (e[1]!=e[18]) or (e[2]!=e[17]), r
        if r==3:
            assert (e[1],e[18],e[2],e[17])==(15,15,10,18)

    assert records==EXPECTED, (records,EXPECTED)
    # A smaller direct quartic census corroborates the stronger unrestricted result.
    products=[]
    for tup in combinations_with_replacement(range(10),4):
        product=[1]+[0]*YDEG
        for a in tup: product=multiply(product,factors[a])
        products.append(product)
    assert len(products)==715
    for r in range(19):
        if r==17: continue
        b=by_partition[r]
        s=next(i for i,v in enumerate(b) if v)
        unit=[v*pow(b[s],-1,MOD)%MOD for v in b[s:]]
        assert all(unit[:len(product)]!=product[:len(unit)] for product in products)
    print('PASS: 19 dissection components agree by independent colored-partition and Winquist methods.')
    print('PASS: 18 normalized nonzero components each violate a paired Euler-exponent constraint.')
    print('PASS: all 715 four-factor products excluded for each nonzero component.')
    print('r,order,leading,e1,e18')
    for record in records: print(*record,sep=',')
    print('Exceptional r=3: e2=10, e17=18 (mod 19).')

if __name__ == '__main__': main()
