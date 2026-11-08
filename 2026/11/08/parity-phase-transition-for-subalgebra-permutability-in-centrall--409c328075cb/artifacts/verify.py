"""Standalone exact finite-field verification of subalgebra-permutability counts.

Uses row-reduced subspace enumeration and direct Lie-bracket rank tests;
it does not classify subalgebras using the symbolic proof.
No third-party packages are required.
"""
from itertools import combinations, product


class Field:
    def __init__(self, q):
        assert q in (2, 3, 4, 5)
        self.q = q
        if q == 4:
            self.add = lambda x, y: x ^ y
            self.neg = lambda x: x
            def mult(x, y):
                a, b = x & 1, (x >> 1) & 1
                c, d = y & 1, (y >> 1) & 1
                # t^2 = t + 1 in GF(2)[t]/(t^2+t+1).
                return ((a*c + b*d) & 1) | (((a*d+b*c+b*d) & 1) << 1)
            self.mul = mult
        else:
            self.add = lambda x, y: (x+y) % q
            self.neg = lambda x: (-x) % q
            self.mul = lambda x, y: (x*y) % q
        self.inv = {x: next(y for y in range(1, q) if self.mul(x, y) == 1)
                    for x in range(1, q)}

    def sub(self, a, b):
        return self.add(a, self.neg(b))


def rank(vectors, n, f):
    if not vectors:
        return 0
    rows = [list(row) for row in vectors]
    k = 0
    for j in range(n):
        pivot = next((i for i in range(k, len(rows)) if rows[i][j] != 0), None)
        if pivot is None:
            continue
        rows[k], rows[pivot] = rows[pivot], rows[k]
        inv = f.inv[rows[k][j]]
        rows[k] = [f.mul(inv, a) for a in rows[k]]
        for i in range(len(rows)):
            if i == k or rows[i][j] == 0:
                continue
            scale = rows[i][j]
            rows[i] = [f.sub(a, f.mul(scale, b)) for a, b in zip(rows[i], rows[k])]
        k += 1
        if k == len(rows):
            break
    return k


def subspaces(n, q):
    for d in range(n+1):
        for pivots in combinations(range(n), d):
            cells = [(i, j) for i in range(d) for j in range(pivots[i]+1, n)
                     if j not in pivots]
            for vals in product(range(q), repeat=len(cells)):
                a = [[int(j == pivots[i]) for j in range(n)] for i in range(d)]
                for (i, j), v in zip(cells, vals):
                    a[i][j] = v
                yield tuple(tuple(row) for row in a)


def bracket(x, y, f):
    z = [0] * len(x)
    z[1] = f.sub(f.mul(x[0], y[1]), f.mul(x[1], y[0]))
    return tuple(z)


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    num = 1
    den = 1
    for i in range(k):
        num *= q**(n-i)-1
        den *= q**(k-i)-1
    return num//den


def formulas(r, q):
    count_G = lambda n: sum(gaussian(n, u, q) for u in range(n+1))
    total = 2*count_G(r+1) - count_G(r) + q*sum(
        gaussian(r, u, q)*q**(r-u) for u in range(r+1))
    bc = cc = 0
    for u in range(r+1):
        for v in range(r+1):
            for t in range(max(0, u+v-r), min(u, v)+1):
                joint = (gaussian(r,u,q)*gaussian(u,t,q)*gaussian(r-u,v-t,q)
                         *q**((u-t)*(v-t)))
                bc += joint*(q**(u-t)-1)*q**(r-v+1)
                cc += joint*(q**(2*r-u-v)-q**(r-t))
    return total, 2*bc + q*(q-1)*cc


def direct(r, q):
    f = Field(q)
    n = r+2
    good = []
    n_spaces = 0
    for rows in subspaces(n,q):
        n_spaces += 1
        brackets = [bracket(x,y,f) for x,y in combinations(rows,2)]
        if rank(list(rows)+brackets,n,f) == len(rows):
            good.append(rows)
    bad = 0
    for i,a in enumerate(good):
        for j in range(i,len(good)):
            b=good[j]
            rs=list(a)+list(b)
            d=rank(rs,n,f)
            isbad=any(rank(rs+[bracket(x,y,f)],n,f)!=d for x in a for y in b)
            if isbad:
                bad += 1 if i==j else 2
    return len(good), bad, n_spaces


def main():
    cases=((0,2),(1,2),(1,3),(1,4),(1,5),(2,2),(2,3),(2,4),(3,2))
    examined=0
    for r,q in cases:
        observed=direct(r,q)
        theory=formulas(r,q)
        assert observed[:2] == theory, (r,q,observed,theory)
        examined += observed[2]
        print('PASS', 'central_dim',r,'field',q,'subalgebras',theory[0],
              'ordered_nonpermuting_pairs',theory[1], 'all_subspaces',observed[2])
    assert formulas(1, 2) == (14,12)
    assert formulas(2, 3) == (116,2880)
    print('VERIFY_OK cases=',len(cases),'subspaces_examined=',examined)

if __name__ == '__main__':
    main()
