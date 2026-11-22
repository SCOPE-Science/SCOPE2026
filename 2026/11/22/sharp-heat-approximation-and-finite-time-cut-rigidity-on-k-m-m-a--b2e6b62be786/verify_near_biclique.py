"""Finite independent checks for sharp heat approximation on near-balanced bicliques.
Run: python3 verify_near_biclique.py (Python 3 standard library only).
"""
from fractions import Fraction as Q
from itertools import product
import math, random


def weights(a,b,y):
    # rational y = exp(-t) in (0,1)
    W=(1-y**(a+b))/Q(a+b)
    U=(1-y**b-b*W)/a
    V=(1-y**a-a*W)/b
    return U,V,W


def coeff(a,b,y):
    U,V,W=weights(a,b,y)
    if a==b:
        return 2*(U+W)
    if b==a+1:
        return 2*(W+((a-1)*U+a*V)/Q(2*a-1))
    raise ValueError('only a=b and b=a+1')


def cut_value(a,b,p,q,y):
    U,V,W=weights(a,b,y)
    D=b*p+a*q-2*p*q
    if not D:
        return None
    return 2*(W+(p*(a-p)*U+q*(b-q)*V)/D)

for a in range(2,13):
    for b in [a,a+1]:
        for y in [Q(1,2),Q(2,3),Q(3,4),Q(9,10)]:
            c=coeff(a,b,y)
            winners=[]
            for p in range(a+1):
                for q in range(b+1):
                    val=cut_value(a,b,p,q,y)
                    if val is None:continue
                    assert val<=c,(a,b,p,q,y,val,c)
                    if val==c:winners.append((p,q))
            expected = ([(p,p) for p in range(1,a)] if a==b else [(1,1),(a-1,a)])
            assert set(winners)==set(expected),(a,b,y,winners,expected)
print('EXACT_RATIONAL_ALL_CUTS_AND_EQUALITY_CLASS_PASS')


def heat(a,b,t):
    U,V,W=weights(a,b,math.exp(-t))
    N=a+b
    H=[]
    for i in range(N):
        row=[]
        for j in range(N):
            if i<a and j<a:val=1-(a-1)*U-b*W if i==j else U
            elif i>=a and j>=a:val=1-(b-1)*V-a*W if i==j else V
            else:val=W
            row.append(float(val))
        H.append(row)
    return H


def direct_euler_heat(a,b,t,steps=1000):
    # Euler evolution of every basis vector, independent of spectral kernel formulas
    n=a+b
    H=[[float(i==j) for j in range(n)] for i in range(n)]
    dt=t/steps
    for k in range(steps):
        sums_left=[sum(H[j][col] for j in range(a)) for col in range(n)]
        sums_right=[sum(H[j][col] for j in range(a,n)) for col in range(n)]
        for i in range(n):
            if i<a:
                for col in range(n):H[i][col]+=dt*(sums_right[col]-b*H[i][col])
            else:
                for col in range(n):H[i][col]+=dt*(sums_left[col]-a*H[i][col])
    return H

for a,b in [(2,2),(2,3),(3,3),(3,4),(5,5),(5,6)]:
    t=.2
    H=heat(a,b,t)
    R=direct_euler_heat(a,b,t,steps=8000)
    assert max(abs(H[i][j]-R[i][j]) for i in range(a+b) for j in range(a+b))<5e-5
    assert max(abs(sum(row)-1) for row in H)<1e-12
print('INDEPENDENT_HEAT_ODE_AND_ROW_STOCHASTICITY_PASS')

rng=random.Random(20261118)
for a in range(2,10):
    for b in [a,a+1]:
        for t in [.005,.2,1.5]:
            H=heat(a,b,t)
            C=float(coeff(a,b,math.exp(-t)))
            n=a+b
            for trial in range(120):
                f=[rng.uniform(-3,4) for _ in range(n)]
                E=sum(abs(f[i]-f[j]) for i in range(a) for j in range(a,n))
                err=sum(abs(f[i]-sum(H[i][j]*f[j] for j in range(n))) for i in range(n))
                assert err<=C*E+1e-8,(a,b,t,err,C*E)
print('RANDOM_REAL_SIGNAL_TV_L1_CHECKS_PASS',8*2*3*120)
print('ALL_NEAR_BALANCED_BICLIQUE_HEAT_CHECKS_PASS')
