"""Exact-rational finite checks for a fixed-positive-definite-coupling matrix map.
The infinite-time statement is proved in RESULT.md; finite checks corroborate only.
"""
from fractions import Fraction as Q
import random

Z=Q(0); O=Q(1)
I=((O,Z),(Z,O))

def mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in (0,1)) for j in (0,1)) for i in (0,1))
def tr(A): return tuple(tuple(A[j][i] for j in (0,1)) for i in (0,1))
def minus(A,B): return tuple(tuple(A[i][j]-B[i][j] for j in (0,1)) for i in (0,1))
def scl(c,A):return tuple(tuple(c*A[i][j] for j in (0,1)) for i in (0,1))
def psd(A):return A[0][1]==A[1][0] and A[0][0]>=0 and A[1][1]>=0 and A[0][0]*A[1][1]>=A[0][1]**2
def F(B,H):return mul(mul(B,mul(H,minus(I,H))),tr(B))

r=random.Random(37118)
checks=0
for t in (Q(1,5),Q(1,4),Q(2,5)):
    Bd=((Q(2),Z),(Z,t))
    Bs=((Z,Q(2)),(t,Z))
    A=((Q(4),Z),(Z,t*t))
    assert mul(Bd,tr(Bd))==mul(Bs,tr(Bs))==A; checks+=1
    assert mul(Bs,Bs)==scl(2*t,I);checks+=1
    q=(2*t)**2
    for j in range(15):
        a,b,c,d=[r.randrange(-4,5) for _ in range(4)]
        M=((Q(a),Q(b)),(Q(c),Q(d)))
        P=mul(tr(M),M)
        denom=P[0][0]+P[1][1]+1
        H0=scl(1/denom,P)
        assert psd(H0) and psd(minus(I,H0)); checks+=2
        H=H0
        for n in range(12):
            assert psd(H) and psd(minus(I,H));checks+=2
            if n%2==0:
                assert psd(minus(scl(q**(n//2),H0),H));checks+=1
            H=F(Bs,H)
        assert psd(H);checks+=1
    for x in (Q(1,7),Q(1,3),Q(1,4),Q(2,5)):
        H=((x,Z),(Z,Z))
        for k in range(12):
            assert H[0][1]==H[1][0]==H[1][1]==0;checks+=1
            H=F(Bd,H)
            x=4*x*(1-x)
            assert H[0][0]==x;checks+=1
print('FIXED_PD_COUPLING_EXACT_OK',checks)
