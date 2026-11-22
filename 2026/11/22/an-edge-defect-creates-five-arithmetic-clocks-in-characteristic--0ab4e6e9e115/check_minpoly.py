"""Finite modular minimal-polynomial and formal cyclotomic checks.

Run: python3 check_minpoly.py
Imports only the standard-library-based check_wave.py included beside this file.
The infinite-domain proof is in RESULT.md; these checks verify its residue table.
"""
from check_wave import graph, eye, matmul


def relation(columns, target):
    """Find coefficients c with sum c[i]*columns[i] = target modulo 3."""
    m = len(target)
    n = len(columns)
    a = [[columns[j][i] % 3 for j in range(n)] + [target[i] % 3]
         for i in range(m)]
    rank = 0
    pivots = []
    for j in range(n):
        pivot = next((r for r in range(rank, m) if a[r][j]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = 1 if a[rank][j] == 1 else 2
        a[rank] = [(z * inv) % 3 for z in a[rank]]
        for r in range(m):
            if r != rank and a[r][j]:
                z = a[r][j]
                a[r] = [(u - z * v) % 3 for u, v in zip(a[r], a[rank])]
        pivots.append(j)
        rank += 1
    if any(row[n] for row in a[rank:]):
        return None
    sol = [0] * n
    for i, j in enumerate(pivots):
        sol[j] = a[i][n]
    return sol


def minimal(a):
    n = len(a)
    powers = [eye(n)]
    for k in range(1, 12):
        powers.append(matmul(powers[-1], a))
        vectors = [[v for row in M for v in row] for M in powers]
        sol = relation(vectors[:-1], [-x for x in vectors[-1]])
        if sol is not None:
            return sol + [1]
    raise AssertionError('degree bound exceeded')


def p_add(f, g):
    a = [0] * max(len(f), len(g))
    for i, v in enumerate(f):
        a[i] += v
    for i, v in enumerate(g):
        a[i] += v
    return trim([z % 3 for z in a])


def p_mul(f, g):
    a = [0] * (len(f) + len(g) - 1)
    for i, u in enumerate(f):
        for j, v in enumerate(g):
            a[i+j] += u*v
    return trim([z % 3 for z in a])


def p_pow(f, n):
    out = [1]
    while n:
        if n & 1:
            out = p_mul(out, f)
        f = p_mul(f, f)
        n >>= 1
    return out


def trim(f):
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    return f


def transform(f):
    d = len(f)-1
    out = [0]
    for i, v in enumerate(f):
        if v:
            term = p_mul([0]*(d-i)+[v], p_pow([1,0,1],i))
            out = p_add(out,term)
    return out


X = [0, 1]
Q = [1, 0, 1]
PHI5 = [1, 1, 1, 1, 1]
PHI10 = [1, 2, 1, 2, 1]
PHI20 = [1, 0, 2, 0, 1, 0, 2, 0, 1]

def expected(a,b):
    if a == b == 2:
        return [1,0,0,0,1], p_mul(PHI5, PHI10)
    i,j = sorted((a%3,b%3))
    poly = {
        (0,0):[0,1,0,1,0,1],
        (0,1):[0,0,0,1,0,1],
        (0,2):[0,2,0,1,0,1],
        (1,1):[0,0,0,1],
        (1,2):[0,0,0,2,0,1],
        (2,2):[0,1,0,0,0,1]
    }[(i,j)]
    factors = {
        (0,0):[Q, p_pow([2,1],4), p_pow([1,1],4)],
        (0,1):[p_pow(Q,3), [1,0,0,0,1]],
        (0,2):[Q, PHI20],
        (1,1):[p_pow(Q,3)],
        (1,2):[p_pow(Q,3),p_pow([2,0,1],2)],
        (2,2):[Q,PHI5,PHI10]
    }[(i,j)]
    prod = [1]
    for f in factors:
        prod = p_mul(prod,f)
    return poly,prod


if __name__=='__main__':
    checks = 0
    for a in range(2,9):
        for b in range(2,9):
            m, temporal = expected(a,b)
            assert minimal(graph(a,b)) == m,(a,b,'adjacency')
            assert transform(m) == temporal,(a,b,'temporal')
            checks += 1
    print('Exact adjacency minimal-polynomial checks:',checks)
    print('Exact transformed temporal polynomial factorizations:',checks)
    print('ALL CHECKS PASSED')
