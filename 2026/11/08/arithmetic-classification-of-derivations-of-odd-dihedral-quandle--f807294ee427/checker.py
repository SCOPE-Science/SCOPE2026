"""Independent finite-field tests of the dihedral quandle-algebra derivation theorem.

Usage: python checker.py
Requires Python 3 and NumPy.  Not a substitute for the general proof.
"""
from math import gcd
import numpy as np


def rank_prime(matrix, p):
    a = np.array(matrix, dtype=np.int64) % p
    m, n = a.shape
    r = 0
    for col in range(n):
        matches = np.flatnonzero(a[r:, col])
        if len(matches) == 0:
            continue
        j = r + int(matches[0])
        a[[r, j]] = a[[j, r]]
        a[r] = a[r] * pow(int(a[r, col]), -1, p) % p
        piv = a[r].copy()
        rows = np.flatnonzero(a[r + 1:, col]) + r + 1
        if len(rows):
            a[rows] = (a[rows] - a[rows, col, None] * piv) % p
        r += 1
        if r == m:
            break
    return r


def full_derivation_dimension(n, p):
    """Unrestricted n-by-n matrix unknowns; all n^3 Leibniz equations."""
    mat = np.zeros((n**3, n*n), dtype=np.int64)
    row = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mat[row, ((2*j-i) % n)*n + k] += 1
                mat[row, i*n + ((2*j-k) % n)] -= 1
                mat[row, j*n + (((k+i)*pow(2, -1, n)) % n)] -= 1
                row += 1
    return n*n - rank_prime(mat, p)


def orbit_vectors(n, p):
    """Construct coefficient vectors using only doubling/sign compatibility."""
    unseen = set(range(1, n))
    vecs = []
    while unseen:
        u = min(unseen)
        orb = set()
        for sign in [1, -1]:
            v = sign*u % n
            while v not in orb:
                orb.add(v)
                v = 2*v % n
        unseen -= orb
        d = 1
        v = 2*u % n
        while v != u:
            v = 2*v % n
            d += 1
        halfway = pow(2, d//2, n) == n-1 if d % 2 == 0 else False
        if halfway:
            good = (pow(2, d//2, p)+1) % p == 0
        else:
            good = (pow(2, d, p)-1) % p == 0
        if not good:
            continue
        c = [0]*n
        for s in [1, -1]:
            v = s*u % n
            for j in range(d):
                c[v] = (s * pow(2, -j, p)) % p
                v = 2*v % n
        assert len(orb) in (d,2*d)
        vecs.append(c)
    return vecs


def direct_leibniz(n, p, c):
    """Check actual D(e_i e_j)=D(e_i)e_j+e_iD(e_j) coefficientwise."""
    for i in range(n):
        for j in range(n):
            lhs = [(2*j-i+u)%n for u in range(n)]
            rhs1 = [(2*j-i-u)%n for u in range(n)]
            rhs2 = [(2*(j+u)-i)%n for u in range(n)]
            vals = [0]*n
            for u in range(n):
                vals[lhs[u]] += c[u]
                vals[rhs1[u]] -= c[u]
                vals[rhs2[u]] -= c[u]
            if any(v%p for v in vals):
                return False
    return True


def check():
    pairs = [(n,p) for n in (3,5,7,9,11,13) for p in (2,3,5,7,11,13) if n%p]
    for n,p in pairs:
        vecs = orbit_vectors(n,p) if p!=2 else []
        dim = full_derivation_dimension(n,p)
        assert dim == len(vecs), (n,p,dim,len(vecs))
        assert all(direct_leibniz(n,p,c) for c in vecs)
    examples = [(11,3,1),(13,5,1),(23,89,1),(15,7,0)]
    for n,p,expected in examples:
        if n%p:
            vv = orbit_vectors(n,p)
            assert len(vv) == expected, (n,p,len(vv),expected)
            assert all(direct_leibniz(n,p,c) for c in vv)
    print('VERIFY_OK rank_cases=%d orbit_examples=%d' % (len(pairs),len(examples)))


if __name__ == '__main__':
    check()
