"""Exact-arithmetic checks for the discrete-affine Poisson GMRES theorem.

Run with Python 3 standard library: python verify.py.
Finite checks supplement, and do not replace, the proof in RESULT.md.
"""
from fractions import Fraction as F


def matvec(x):
    n = len(x)
    return [2*x[j] - (x[j-1] if j else 0) -
            (x[j+1] if j+1 < n else 0) for j in range(n)]


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def rank(columns):
    if not columns:
        return 0
    rows = [list(r) for r in zip(*columns)]
    width = len(columns)
    top = 0
    for j in range(width):
        piv = next((i for i in range(top, len(rows)) if rows[i][j]), None)
        if piv is None:
            continue
        rows[top], rows[piv] = rows[piv], rows[top]
        t = rows[top][j]
        rows[top] = [v/t for v in rows[top]]
        for i in range(top+1, len(rows)):
            t = rows[i][j]
            if t:
                rows[i] = [a-t*b for a, b in zip(rows[i], rows[top])]
        top += 1
        if top == len(rows):
            break
    return top


def linear_solve(a, b):
    n = len(b)
    rows = [list(row)+[val] for row, val in zip(a, b)]
    for j in range(n):
        i = next(i for i in range(j, n) if rows[i][j])
        rows[i], rows[j] = rows[j], rows[i]
        t = rows[j][j]
        rows[j] = [v/t for v in rows[j]]
        for i in range(n):
            if i != j:
                t = rows[i][j]
                if t:
                    rows[i] = [u-t*v for u, v in zip(rows[i], rows[j])]
    return [row[-1] for row in rows]


def residual_squared(b, k):
    if not k:
        return dot(b, b)
    v = matvec(b)
    cols = [v]
    for i in range(1, k):
        v = matvec(v)
        cols.append(v)
    gram = [[dot(x,y) for y in cols] for x in cols]
    rhs = [dot(x,b) for x in cols]
    coefs = linear_solve(gram, rhs)
    residual = [bj - sum((coefs[l]*cols[l][j] for l in range(k)), F(0))
                for j,bj in enumerate(b)]
    return dot(residual, residual)


def predicted(n,L,R,k):
    b = [F(L)+(F(R)-F(L))*F(j,n+1) for j in range(1,n+1)]
    t = F(L*L+R*R)
    interior = sum((b[j-1]**2 for j in range(k+1,n-k+1)), F(0))
    tail = F((R*R-L*L)**2, (n+1)**2)*F(sum(j*j for j in range(1,k+1)),1)/t
    return interior + tail


def run():
    checked = 0
    for n in range(2,13):
        for L,R in ((1,1),(1,-1),(0,1),(2,5),(-3,2)):
            b = [F(L)+(F(R)-F(L))*F(j,n+1) for j in range(1,n+1)]
            for k in range(n//2+1):
                assert residual_squared(b,k) == predicted(n,L,R,k), (n,L,R,k)
                checked += 1
            cols = [b]
            for i in range(1,n):
                cols.append(matvec(cols[-1]))
            expected = ((n+1)//2 if L == R else n//2 if L == -R else n)
            assert rank(cols) == expected, (n,L,R,expected)
            if L == R:
                for k in range((n+1)//2+1):
                    if k < expected:
                        assert residual_squared(b,k) == F(L*L*(n-2*k))
            if L == 0:
                for k in range(n+1):
                    if k<n:
                        expected_norm = F(sum(j*j for j in range(1,n-k+1)),(n+1)**2)
                        assert residual_squared(b,k) == expected_norm
    print(f'VERIFY_OK {checked} exact half-range projections; spectral grades and full constant/ramp profiles')


if __name__ == '__main__':
    run()
