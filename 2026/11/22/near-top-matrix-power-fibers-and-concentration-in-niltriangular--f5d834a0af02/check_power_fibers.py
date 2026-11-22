"""Independent finite-field checks of near-top power fibers in strict triangular algebras.

Usage: python check_power_fibers.py
No external packages. The claim for all dimensions is proved symbolically, not by the finite tests.
"""
from collections import Counter
from itertools import product
from math import prod


def add(x, y, q):
    return x ^ y if q == 4 else (x + y) % q


def multiply(x, y, q):
    if q == 4:
        z = 0
        for i in range(2):
            if (y >> i) & 1:
                z ^= x << i
        if z & 8:
            z ^= 0b1100
        if z & 4:
            z ^= 0b0111
        return z
    return (x * y) % q


def matrix_power(A, m, q):
    n = len(A)
    Y = [row[:] for row in A]
    for _ in range(m - 1):
        Z = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                v = 0
                for k in range(i + 1, j):
                    v = add(v, multiply(Y[i][k], A[k][j], q), q)
                Z[i][j] = v
        Y = Z
    return (Y[0][m], Y[1][m + 1], Y[0][m + 1])


def formulas(m, q):
    h = m * (m - 1) // 2
    k = h + m - 1
    g = q**k * (q-1)**(m-1)
    c = g * ((m-1)*q + 1)
    z = q**k * (q**(m+2) - (q-1)**m * (q*q + m*q + 1))
    return g, c, z


def check_full(m, q):
    n = m + 2
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    counts = Counter()
    for vals in product(range(q), repeat=len(pairs)):
        A = [[0]*n for _ in range(n)]
        for (i,j), v in zip(pairs, vals):
            A[i][j] = v
        counts[matrix_power(A, m, q)] += 1
    g,c,z = formulas(m,q)
    for a in range(q):
        for b in range(q):
            for d in range(q):
                want = z if a == b == d == 0 else c if a == b == 0 else g
                got = counts[a,b,d]
                assert got == want, ('full',m,q,(a,b,d),got,want)
    assert sum(counts.values()) == q**(n*(n-1)//2)
    print('PASS full matrices',m,q,'total',q**len(pairs),'generic/central/zero',g,c,z)


def check_sparse(m,q):
    # All longer diagonals are invisible to X^m; enumerate independent
    # first- and second-diagonal entries, using field operations only.
    n=m+2
    counts=Counter()
    for vals in product(range(q),repeat=2*m+1):
        A=[[0]*n for _ in range(n)]
        for i in range(m+1):
            A[i][i+1]=vals[i]
        for i in range(m):
            A[i][i+2]=vals[m+1+i]
        counts[matrix_power(A,m,q)]+=1
    unused=n*(n-1)//2-(2*m+1)
    g,c,z=formulas(m,q)
    for a in range(q):
        for b in range(q):
            for d in range(q):
                want = z if a == b == d == 0 else c if a == b == 0 else g
                got = counts[a,b,d]*q**unused
                assert got == want, ('sparse',m,q,(a,b,d),got,want)
    print('PASS sparse diagonals',m,q,'count',q**(2*m+1),'generic/central/zero',g,c,z)


def check_support(m):
    # Zero/nonzero support classification behind the critical nonzero C fiber.
    allowed=[]
    for bits in product((0,1),repeat=m+1):
        p=all(bits[1:m]);
        coeff=any(all(bits[i] for i in range(m+1) if i not in (j,j+1)) for j in range(m))
        if not p and coeff:
            allowed.append(bits)
    assert len(allowed)==2*m-1
    assert sum(sum(1 for v in bits if v==0)==1 for bits in allowed)==m-1
    assert sum(sum(1 for v in bits if v==0)==2 for bits in allowed)==m
    print('PASS support lemma',m,'admissible patterns',len(allowed))

if __name__ == '__main__':
    for m in (2,3,4,5,6,8): check_support(m)
    for m,q in ((2,2),(2,3),(2,4),(3,2),(3,3),(4,2)): check_full(m,q)
    for m,q in ((3,4),(4,3),(5,2),(6,2),(7,2)): check_sparse(m,q)
    print('ALL CHECKS PASSED')
