#!/usr/bin/env python3
"""Exact cyclotomic verifier for four-subspace spectra of a F_9 harmonic fusion frame.

Only Python's standard library is used. All Fourier and characteristic-polynomial
arithmetic is in Z[X]/(Phi_24), Phi_24 = X^8 - X^4 + 1.
"""
from itertools import combinations
from fractions import Fraction
from math import comb

P = 3
ELEMENTS = [(a, b) for a in range(3) for b in range(3)]
ZERO = (0, 0)
ONE = (1, 0)
GEN = (1, 1)  # primitive element of F_3[t]/(t^2+1)

def add(x, y):
    return ((x[0] + y[0]) % 3, (x[1] + y[1]) % 3)

def neg(x):
    return ((-x[0]) % 3, (-x[1]) % 3)

def sub(x, y):
    return add(x, neg(y))

def mul(x, y):
    return ((x[0] * y[0] + 2*x[1]*y[1]) % 3,
            (x[0] * y[1] + x[1]*y[0]) % 3)

def power(x, n):
    ans = ONE
    for _ in range(n):
        ans = mul(ans, x)
    return ans

NONZERO = [x for x in ELEMENTS if x != ZERO]
assert len({power(GEN, i) for i in range(8)}) == 8
LOG = {power(GEN, i): i for i in range(8)}
assert len(LOG) == 8 and power(GEN, 4) == neg(ONE)

def trace(x):
    return (2*x[0]) % 3

Z = (0,) * 8
I = (1,) + (0,) * 7

def radd(x, y):
    return tuple(a+b for a,b in zip(x,y))

def rneg(x):
    return tuple(-a for a in x)

def rscale(x, k):
    return tuple(k*a for a in x)

def rmul(x, y):
    c = [0] * 15
    for i, a in enumerate(x):
        if a:
            for j, b in enumerate(y):
                if b:
                    c[i+j] += a*b
    # x^8 = x^4 - 1, reduce high degrees in decreasing order.
    for d in range(14,7,-1):
        z = c[d]
        c[d] = 0
        c[d-4] += z
        c[d-8] -= z
    return tuple(c[:8])

ROOTS = [I]
X = (0,1,0,0,0,0,0,0)
for i in range(1,24):
    ROOTS.append(rmul(ROOTS[-1], X))
assert rmul(ROOTS[8], radd(ROOTS[8], I)) == rneg(I)  # zeta_3^2+zeta_3+1=0
assert ROOTS[12] == rneg(I) and rmul(ROOTS[3], ROOTS[3]) == ROOTS[6]

def gram(S, character_exponent):
    """Raw 8 by 8 Gram of [psi(ax),chi(a)psi(ax)] at the four x in S."""
    idx = [(g,r) for g in S for r in (0,1)]
    ans = []
    for g,r in idx:
        row = []
        for h,s in idx:
            v = Z
            for a in NONZERO:
                phase = (8 * trace(mul(a,sub(h,g))) + 3*character_exponent*LOG[a]*(s-r)) % 24
                v = radd(v, ROOTS[phase])
            row.append(v)
        ans.append(row)
    for i in range(8):
        assert ans[i][i] == rscale(I,8)
    return ans

def mm(A, B):
    n = len(A)
    return [[sum_ring(rmul(A[i][k],B[k][j]) for k in range(n))
             for j in range(n)] for i in range(n)]

def sum_ring(xs):
    a = Z
    for b in xs:
        a = radd(a,b)
    return a

def characteristic(A):
    """Newton trace identities, monic coefficients descending, exactly in Q(zeta_24)."""
    n=len(A)
    traces=[]
    current=A
    for k in range(1,n+1):
        traces.append(sum_ring(current[i][i] for i in range(n)))
        if k<n:
            current=mm(current,A)
    coeffs=[I]
    for m in range(1,n+1):
        s=sum_ring(rmul(coeffs[m-j],traces[j-1]) for j in range(1,m+1))
        assert all(z%m==0 for z in s), (m,s)
        coeffs.append(tuple(-z//m for z in s))
    return coeffs

def poly_square(ascending_desc_coeffs):
    c=ascending_desc_coeffs
    return [sum(c[i]*c[k-i] for i in range(max(0,k-4),min(4,k)+1))
            for k in range(9)]

def orbit(S):
    return {tuple(sorted(add(mul(c,x),b) for x in S))
            for b in ELEMENTS for c in NONZERO}

# Four-root isolating intervals are simple finite rational sign certificates.
QUARTICS = {
    72: ([1,-32,324,-1134,972],[(125,100,126,100),(486,100,488,100),
                                    (1012,100,1013,100),(1575,100,1576,100)]),
    18: ([1,-32,324,-1080,972],[(142,100,144,100),(380,100,381,100),
                                    (1256,100,1258,100),(1419,100,1420,100)]),
    36: ([1,-32,324,-1080,486],[(52,100,54,100),(575,100,577,100),
                                   (1040,100,1041,100),(1530,100,1532,100)]),
}

def eval_poly(c,x):
    v=Fraction(0)
    for a in c:
        v=v*x+a
    return v

def run():
    unseen = set(combinations(ELEMENTS,4))
    classes=[]
    while unseen:
        S=min(unseen)
        O=orbit(S)
        assert O <= unseen
        unseen -= O
        classes.append((S,len(O),O))
    assert len(classes)==3 and sum(len(O) for _,_,O in classes)==comb(9,4)
    assert {n for _,n,_ in classes} == {18,36,72}
    assert len(set.union(*(O for _,_,O in classes))) == 126
    for S,n,O in classes:
        c, intervals=QUARTICS[n]
        for exponent in (1,3,5,7):
            assert characteristic(gram(S, exponent)) == [rscale(I,a) for a in poly_square(c)]
        for u,v,w,z in intervals:
            left,right=Fraction(u,v),Fraction(w,z)
            assert left<right and eval_poly(c,left)*eval_poly(c,right)<0
        print('orbit_size',n,'representative',S,'quartic',c,'isolating_intervals',intervals)
    # Certify that the first root for the worst class is smaller than the others.
    assert QUARTICS[36][1][0][2] * QUARTICS[72][1][0][1] < QUARTICS[72][1][0][0] * QUARTICS[36][1][0][3]
    assert QUARTICS[36][1][0][2] * QUARTICS[18][1][0][1] < QUARTICS[18][1][0][0] * QUARTICS[36][1][0][3]
    print('PASS: 4 odd characters, 126 four-subset spectra each, exact characteristic polynomial squares, positive full rank, and sharp worst orbit of size 36')

if __name__ == '__main__':
    run()
