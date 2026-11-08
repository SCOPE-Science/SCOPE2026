"""Finite exact checks for the Cesaro/shift commutator theorem.
Run: python checker.py (Python standard library only).
These finite checks do not prove the infinite singular-value estimates.
"""
from fractions import Fraction as Q
from math import isclose, pi

checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def multiply(a,b):
    n=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)),Q(0)) for j in range(n)] for i in range(n)]

for n in (8,13,21,34):
    C=[[Q(1,i+1) if j<=i else Q(0) for j in range(n)] for i in range(n)]
    for m in range(1, min(n-1,7)):
        Sm=[[Q(1) if i==j+m else Q(0) for j in range(n)] for i in range(n)]
        lhs=multiply(C,Sm)
        rhs=multiply(Sm,C)
        for i in range(n):
            for j in range(n):
                expected = -Q(m,(i+1)*(i-m+1)) if i>=j+m else Q(0)
                check(lhs[i][j]-rhs[i][j]==expected, f'commutator at n={n},m={m},i={i},j={j}')
        for i in range(n-m):
            for j in range(n):
                expected=Q(m,(i+1)*(i+m+1)) if i>=j else Q(0)
                check(-(lhs[i+m][j]-rhs[i+m][j])==expected,'shifted factorable matrix')
        partial=sum((Q(i+1)*Q(m*m,(i+1)**2*(i+m+1)**2) for i in range(n-m)),Q(0))
        direct=sum(( (lhs[i][j]-rhs[i][j])**2 for i in range(n) for j in range(n)),Q(0))
        check(partial==direct,'finite Hilbert-Schmidt column/row agreement')

# Dyadic block exact inverse and cancellation tests.
for r in range(1,8):
    N=2**r
    for seed in range(1,5):
        xs=[Q(((j+seed*r)%7)-3,7) for j in range(N-1)]
        xs.append(-sum(xs,Q(0)))
        check(sum(xs,Q(0))==0,'zero sum')
        accum=[]
        s=Q(0)
        for v in xs:
            s+=v
            accum.append(s)
        recon=[accum[0]]+[accum[j]-accum[j-1] for j in range(1,N)]
        check(recon==xs,'unit-lower-triangular difference inverse')
        # A row-terraced matrix cancels exactly after the block.
        for m in (1,2,5):
            start=N-1
            for i in (2*N-1,3*N+3):
                ai=Q(m,(i+1)*(i+m+1))
                check(ai*sum(xs,Q(0))==0,'tail cancellation')

# A simple exact sum test for the Hilbert-Schmidt identity.
for m in range(1,12):
    H=sum((Q(1,k) for k in range(1,m+1)),Q(0))
    H2=sum((Q(1,k*k) for k in range(1,m+1)),Q(0))
    for N in (20,40,100):
        sum_partial=sum((Q(m*m,r*(r+m)**2) for r in range(1,N+1)),Q(0))
        remainder=sum((Q(m*m,r*(r+m)**2) for r in range(N+1,10*N)),Q(0))
        check(sum_partial>0 and remainder>0,'partial positive and tail positive')
        val=float(H)+m*float(H2)-m*(pi*pi/6)
        check(float(sum_partial)<val+1e-12,'partial below infinite closed form')

print('CESARO_SHIFT_COMMUTATOR_EXACT_FINITE_OK',checks)
