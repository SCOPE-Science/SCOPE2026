"""Check centralizer-rank polynomials for finite unicyclic radical-square-zero quiver algebras.
Uses the multiplication table, not the incidence-matrix proof formula.
"""
from itertools import product
from collections import Counter
from math import comb


def plus(a, b, q):
    return a ^ b if q == 4 else (a + b) % q


def minus(a, b, q):
    return a ^ b if q == 4 else (a - b) % q


def times(a, b, q):
    if q != 4:
        return a * b % q
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7  # alpha^2 = alpha+1
    return result


def inverse(a, q):
    return next(x for x in range(1, q) if times(a, x, q) == 1)


def rank(rows, q):
    a = [list(r) for r in rows]
    if not a:
        return 0
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        u = inverse(a[r][j], q)
        a[r] = [times(u, v, q) for v in a[r]]
        for i in range(len(a)):
            if i != r and a[i][j]:
                u = a[i][j]
                a[i] = [minus(v, times(u, w, q), q) for v, w in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def multiplication_table(n, arrows):
    dim = n + len(arrows)
    t = [[None] * dim for _ in range(dim)]
    for i in range(n):
        t[i][i] = i
    for j, (source, target) in enumerate(arrows):
        t[source][n+j] = n+j
        t[n+j][target] = n+j
    return t


def algebra_product(a, b, table, q):
    n = len(a)
    out = [0]*n
    for i, ai in enumerate(a):
        if not ai:
            continue
        for j, bj in enumerate(b):
            if bj and table[i][j] is not None:
                k = table[i][j]
                out[k] = plus(out[k], times(ai, bj, q), q)
    return out


def exact_counts(q, n, arrows):
    table = multiplication_table(n, arrows)
    dim = len(table)
    basis = [tuple(int(i == j) for i in range(dim)) for j in range(dim)]
    count = Counter()
    for v in product(range(q), repeat=dim):
        mat = [[0]*dim for _ in range(dim)]
        for j, e in enumerate(basis):
            left = algebra_product(v, e, table, q)
            right = algebra_product(e, v, table, q)
            for i in range(dim):
                mat[i][j] = minus(left[i], right[i], q)
        count[rank(mat, q)] += 1
    return count


def convolution(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def formula(q, n, cycle_length):
    c = cycle_length
    base = [comb(c,r)*((q*q-1)**r+(q-1)*(-1)**r) for r in range(c+1)]
    base[c-1] += q*(q-1)**c
    base[c] -= q*(q-1)**c
    branch = [comb(n-c,r)*(q*q-1)**r for r in range(n-c+1)]
    return Counter(dict(enumerate(convolution(base, branch))))


def run():
    cases = [
        (2,3,[(0,1),(1,2),(2,0)],3),
        (2,3,[(1,0),(2,1),(0,2)],3),
        (3,3,[(0,1),(1,2),(2,0)],3),
        (4,3,[(0,1),(1,2),(2,0)],3),
        (2,4,[(0,1),(1,2),(2,0),(0,3)],3),
        (2,4,[(1,0),(2,1),(2,0),(3,0)],3),
        (3,4,[(0,1),(1,2),(2,0),(0,3)],3),
        (2,4,[(0,1),(1,2),(2,3),(3,0)],4),
        (3,4,[(0,1),(1,2),(2,3),(3,0)],4),
        (2,5,[(0,1),(1,2),(2,0),(0,3),(3,4)],3),
        (2,5,[(0,1),(1,2),(2,0),(0,3),(0,4)],3),
        (2,5,[(0,1),(1,2),(2,3),(3,0),(1,4)],4),
        (2,5,[(0,1),(1,2),(2,3),(3,4),(4,0)],5)
    ]
    for q,n,arrows,c in cases:
        got=exact_counts(q,n,arrows)
        want=formula(q,n,c)
        assert got==want, (q,n,arrows,got,want)
        assert sum(got.values()) == q**(2*n)
        assert got[0]==q
        assert got[1]==q*(q-1)*((q+1)*n-q*c)
    print('VERIFY_OK_UNICYCLIC', len(cases))

if __name__=='__main__':
    run()
