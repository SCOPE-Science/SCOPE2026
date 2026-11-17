"""Exact finite relation certificates for cyclic directed path homology.

No external packages are required. This verifies the small torsion block
and absence of unintended short relations in illustrative block counts.
The uniform statement additionally uses the arithmetic proof in RESULT.md.
"""
from collections import defaultdict
from itertools import combinations
from math import gcd

T = (0, 1, 9, 10, 13, 15, 17, 20)


def rows(S):
    groups = defaultdict(list)
    for i, a in enumerate(S):
        for j in range(i, len(S)):
            b = S[j]
            v = [0] * len(S)
            v[i] += 1
            v[j] += 1
            groups[a + b].append(((i, j), v))
    R, signatures = [], []
    for sm, pairs in sorted(groups.items()):
        if sm in S:
            v = pairs[0][1][:]
            v[S.index(sm)] -= 1
            R.append(v)
            signatures.append(('triangle', sm, pairs[0][0]))
        for pair, v in pairs[1:]:
            R.append([x-y for x,y in zip(pairs[0][1], v)])
            signatures.append(('collision', sm, pairs[0][0], pair))
    return R, signatures


def determinant(matrix):
    """Fraction-free Bareiss determinant of a square integer matrix."""
    n = len(matrix)
    A = [list(map(int, r)) for r in matrix]
    if n == 0:
        return 1
    sign, prev = 1, 1
    for k in range(n-1):
        if A[k][k] == 0:
            p = next((p for p in range(k+1,n) if A[p][k]),None)
            if p is None:
                return 0
            A[k],A[p] = A[p],A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num = pivot*A[i][j] - A[i][k]*A[k][j]
                assert num % prev == 0
                A[i][j] = num // prev
        for i in range(k+1,n):
            A[i][k] = 0
        prev = pivot
    return sign*A[n-1][n-1]


def minor_gcd(M, d):
    nr,nc = len(M),len(M[0])
    g = 0
    for rr in combinations(range(nr),d):
        for cc in combinations(range(nc),d):
            g = gcd(g,abs(determinant([[M[i][j] for j in cc] for i in rr])))
            if g == 1:
                return g
    return g


def steps(r):
    return (1,) + tuple(2*100**(r+i)+2*100**i*t
                        for i in range(r) for t in T)


def main():
    # Only equal-sum relations, excluding the formal zero as a graph step.
    groups = defaultdict(list)
    for i,a in enumerate(T):
        for j in range(i,len(T)):
            b=T[j]
            v=[0]*8; v[i]+=1; v[j]+=1
            groups[a+b].append(v)
    M = [[x-y for x,y in zip(g[0],v)] for g in groups.values() for v in g[1:]]
    assert len(M)==6
    g5, g6 = minor_gcd(M,5),minor_gcd(M,6)
    assert (g5,g6)==(1,2)
    print('eight-point block: six relations; gcd of 5-minors =',g5,
          '; gcd of 6-minors =',g6)
    print('Smith invariants: 1,1,1,1,1,2; free rank 2')
    for r in range(1,6):
        S=steps(r); R, signatures=rows(S)
        assert len(S)==1+8*r
        assert all(x[0]=='collision' for x in signatures)
        assert len(R)==6*r
        for record in signatures:
            _, sm, pair1, pair2 = record
            bi={(i-1)//8 for pair in (pair1,pair2) for i in pair}
            assert len(bi)==1, (r,record)
        assert len(set(S))==len(S)
        print('r =',r,'number of steps =',len(S),
              'number of relation rows =',len(R),
              'free H1 rank =',1+2*r,'order-two factors =',r,
              'least modulus =',2*max(S)+1)
    print('All exact finite certificates passed.')

if __name__=='__main__':
    main()
