#!/usr/bin/env python3
"""Exact sign certificate for 11th-root positive trigonometric quadrature.
Standard library only. No floating-point operation enters accepted signs.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import factorial

P=11
SCALE=10**12


def atan_partial(x, n=15):
    return sum(((-1)**k*x**(2*k+1)/Q(2*k+1) for k in range(n)), Q(0))

# Machin: pi = 16 arctan(1/5) - 4 arctan(1/239).
PI0=16*atan_partial(Q(1,5))-4*atan_partial(Q(1,239))
PIERR=16*Q(1, 31*5**31)+4*Q(1, 31*239**31)
assert PIERR<Q(1,10**20)


def trig_approx(k):
    j=k if k<=5 else k-11
    theta=Q(2*j,11)*PI0
    assert abs(theta)<3
    cosine=sum(((-1)**t*theta**(2*t)/Q(factorial(2*t)) for t in range(18)),Q(0))
    sine=sum(((-1)**t*theta**(2*t+1)/Q(factorial(2*t+1)) for t in range(18)),Q(0))
    # Each rational Taylor approximation differs from the true value by
    # < 3**36/36! + (10/11)*PIERR < 1e-20.
    assert Q(3**36,factorial(36))+PIERR<Q(1,10**20)
    assert Q(3**37,factorial(37))+PIERR<Q(1,10**20)
    return (cosine.numerator*SCALE//cosine.denominator,
            sine.numerator*SCALE//sine.denominator)

TRIG=[trig_approx(j) for j in range(P)]


def det(a):
    a=[row[:] for row in a];n=len(a);sgn=1;prev=1
    for k in range(n-1):
        if a[k][k]==0:
            ix=next((i for i in range(k+1,n) if a[i][k]),None)
            if ix is None:return 0
            a[k],a[ix]=a[ix],a[k];sgn=-sgn
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*pivot-a[i][k]*a[k][j]
                assert z%prev==0
                a[i][j]=z//prev
            a[i][k]=0
        prev=pivot
    return sgn*a[-1][-1]


def matrix(S):
    rows=[[SCALE]*len(S)]
    for k in range(1,4):
        rows.append([TRIG[(k*j)%11][0] for j in S])
        rows.append([TRIG[(k*j)%11][1] for j in S])
    return rows


def canonical_gaps(S):
    # A cyclic translation preserves gaps, and reflection reverses them.
    gaps=tuple((S[(i+1)%7]-S[i])%P for i in range(7))
    return min([gaps[i:]+gaps[:i] for i in range(7)]+
               [gaps[::-1][i:]+gaps[::-1][:i] for i in range(7)])


def signatures(S):
    A=matrix(S)
    D=det(A)
    # Entrywise error < (1e-12+1e-20) < 2e-12. For a 7x7 determinant,
    # the Leibniz formula bounds error by 7!*7*(2e-12)*(1+2e-12)^6 < 1e-7.
    # Hence |det(approx)|>1e-3 certifies its exact sign.
    assert abs(D)*1000>SCALE**7
    tests=[]
    for j in range(7):
        Aj=[r[:] for r in A]
        for i in range(7):Aj[i][j]=(SCALE if i==0 else 0)
        Dj=det(Aj)
        assert abs(Dj)*1000>SCALE**7
        tests.append(1 if D*Dj>0 else -1)
    return tests


def main():
    orbits={}
    for S in combinations(range(P),7):
        key=canonical_gaps(S)
        if key not in orbits:orbits[key]=[]
        orbits[key].append(S)
    assert len(orbits)==20 and sum(map(len,orbits.values()))==330
    good=[]
    for gaps,ss in sorted(orbits.items()):
        signs=signatures(ss[0])
        pos=all(x==1 for x in signs)
        if pos:good.append((gaps,len(ss),ss[0],signs))
        print('GAP',gaps,'ORBIT',len(ss),'POSITIVE',pos,'SIGNS',tuple(signs))
    assert len(good)==3 and sum(t[1] for t in good)==33
    assert [x[0] for x in good]==[
        (1,1,1,2,2,2,2),
        (1,1,2,2,1,2,2),
        (1,2,1,2,1,2,2)]
    assert all(t[1]==11 for t in good)
    # The positive classes are precisely the reflection-fixed classes
    # having no gap larger than two (a directly checkable consequence).
    for gap,ss in orbits.items():
        reflection=any({(a-x)%11 for x in ss[0]}==set(ss[0]) for a in range(11))
        expected=reflection and max(gap)<=2
        assert expected==(gap in [g[0] for g in good])
    print('CERTIFIED_11TH_ROOT_SEVEN_NODE_CLASSIFICATION_PASSED')

if __name__=='__main__':main()
