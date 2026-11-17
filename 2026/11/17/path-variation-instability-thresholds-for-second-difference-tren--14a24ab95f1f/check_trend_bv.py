"""Exact rational audit for path-variation sensitivity of second-difference trend filtering.
Run: python3 check_trend_bv.py. Uses only the Python standard library.
"""
from fractions import Fraction as Q
from itertools import combinations


def transpose(A):
    return [list(row) for row in zip(*A)] if A else []


def multiply(A, B):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*B)] for row in A]


def invert(A):
    n = len(A)
    R = [[Q(v) for v in row] + [Q(i == j) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next((r for r in range(c, n) if R[r][c]), None)
        assert p is not None, 'unexpected rank deficiency'
        R[c], R[p] = R[p], R[c]
        t = R[c][c]
        R[c] = [v/t for v in R[c]]
        for r in range(n):
            if r != c:
                t = R[r][c]
                R[r] = [u-t*v for u, v in zip(R[r], R[c])]
    return [row[n:] for row in R]


def matvec(A, v):
    return [sum(a*b for a, b in zip(row, v)) for row in A]


def projector(n, active_rows):
    D = []
    for j in active_rows:
        row = [Q(0)]*n
        row[j:j+3] = [Q(1),Q(-2),Q(1)]
        D.append(row)
    if not D:
        return [[Q(i==j) for j in range(n)] for i in range(n)]
    gram = multiply(D, transpose(D))
    correction = multiply(multiply(transpose(D), invert(gram)), D)
    return [[Q(i == j)-correction[i][j] for j in range(n)] for i in range(n)]


def variation(v):
    return sum(abs(v[i+1]-v[i]) for i in range(len(v)-1))


def exhaustive(n):
    best=Q(0); extremizers=[]
    for mask in range(1 << max(0,n-2)):
        F=tuple(j for j in range(n-2) if mask>>j&1)
        P=projector(n,F)
        assert all(sum(row)==1 for row in P)
        for j in range(1,n):
            cut=[Q(int(i>=j)) for i in range(n)]
            norm=variation(matvec(P,cut))
            if norm>best:
                best=norm; extremizers=[(F,j)]
            elif norm==best:
                extremizers.append((F,j))
    return best,extremizers


def full_affine_lower(n):
    j=n//2
    cut=[Q(int(i>=j)) for i in range(n)]
    P=projector(n,range(n-2))
    obtained=variation(matvec(P,cut))
    formula=Q(6*j*(n-j),n*(n+1))
    assert obtained==formula
    return obtained


def explicit_four_site_witness():
    # At lambda=1, a=(0,0,1,1), b=0.
    a=[Q(0),Q(0),Q(1),Q(1)]
    fit=matvec(projector(4,(0,1)),a)
    assert fit==[Q(-1,10),Q(3,10),Q(7,10),Q(11,10)]
    D=[[Q(1),Q(-2),Q(1),Q(0)],[Q(0),Q(1),Q(-2),Q(1)]]
    dual=matvec(invert(multiply(D,transpose(D))),matvec(D,a))
    assert dual==[Q(1,10),Q(-1,10)]
    assert max(map(abs,dual))<1 and matvec(D,fit)==[0,0]
    assert variation(fit)/variation(a)==Q(6,5)


def main():
    expected={2:Q(1),3:Q(1),4:Q(6,5),5:Q(4,3),6:Q(7,5),7:Q(28,19),8:Q(11,7)}
    for n in range(2,9):
        value,ex=exhaustive(n)
        assert value==expected[n], (n,value)
        print('EXACT_ACTIVE_FACES n=',n,'constant=',value,'attainers=',len(ex))
    for n in range(4,26):
        assert full_affine_lower(n)>1
    explicit_four_site_witness()
    print('ALL_TREND_BV_EXACT_CHECKS_PASS')

if __name__=='__main__': main()
