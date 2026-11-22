#!/usr/bin/env python3
"""Exact independent integer checks for the two-row binary honeycomb partition function.
Only the Python standard library is required. The theorem is proved analytically.
"""
from itertools import product

T = ((0, 2, 1, 0), (2, 0, 0, 0), (0, 0, 0, 2), (0, 1, 2, 0))

def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4))
                       for j in range(4)) for i in range(4))

def matrix_trace(n):
    A = tuple(tuple(int(i == j) for j in range(4)) for i in range(4))
    for _ in range(n):
        A = mm(A, T)
    return sum(A[i][i] for i in range(4))

def formula(n):
    assert n >= 2
    if n % 2:
        return 8 * 2**n
    return 12 * 2**n + 2 * (6**(n//2) + 2**(n//2))

def transfer_formula(n):
    zero = (16 if n % 2 == 0 else 8) * 2**n
    correction = 4 * 2**n if n % 2 == 0 else 0
    return zero + matrix_trace(n) - correction

def cycles(m, n, dx, dy):
    seen = set()
    out = []
    for x in range(m):
        for y in range(n):
            if (x, y) in seen:
                continue
            c = []
            a = (x, y)
            while a not in seen:
                seen.add(a)
                c.append(a)
                a = ((a[0] + dx) % m, (a[1] + dy) % n)
            out.append(c)
    return out

def independent_direct_count(m, n, width_two=False):
    """Enumerate all local shear fields; solve edge-value cycles independently.
    This is independent of the four-state transfer matrix.
    """
    dirs = ((1,0), (0,1), (-1,1))
    cyc = [cycles(m, n, *d) for d in dirs]
    total = 0
    if width_two:
        assert m == 2
        fields = ([q if x == 0 else -q for x in range(m) for q in s]
                  for s in product((-1,0,1), repeat=n))
    else:
        fields = product((-1,0,1), repeat=m*n)
    for t in fields:
        if sum(t):
            continue
        ways = 1
        for d, cs in enumerate(cyc):
            sign = -1 if d == 1 else 1
            for c in cs:
                nseeds = 0
                for seed in (0, 1):
                    cur = seed
                    ok = True
                    for x, y in c[1:]:
                        cur += sign*t[x*n+y]
                        if cur not in (0,1):
                            ok = False
                            break
                    if ok and cur+sign*t[c[0][0]*n+c[0][1]] == seed:
                        nseeds += 1
                ways *= nseeds
                if not ways:
                    break
            if not ways:
                break
        total += ways
    return total

def run():
    print('direct count vs closed formula and transfer:')
    for n in range(2, 10):
        a = independent_direct_count(2,n,True)
        b = transfer_formula(n)
        c = formula(n)
        assert a == b == c, (n,a,b,c)
        print(n, a, b, c)
    assert independent_direct_count(3,3) == 518
    print('independent 3 by 3 benchmark:', 518)
    for n in range(2, 45):
        assert transfer_formula(n) == formula(n)
    print('all checks passed')

if __name__ == '__main__':
    run()
