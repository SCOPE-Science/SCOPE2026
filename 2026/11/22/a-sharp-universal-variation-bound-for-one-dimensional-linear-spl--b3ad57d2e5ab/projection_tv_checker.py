"""Exact rational spot checks for one-dimensional continuous P1 L2 projection in BV.
The infinite-dimensional and all-grid assertions are proved analytically elsewhere.
"""
from fractions import Fraction as F
from itertools import product

def project(h, cells=None, jump=None):
    n=len(h)+1
    M=[[F(0) for _ in range(n)] for _ in range(n)]
    b=[F(0) for _ in range(n)]
    for i,H in enumerate(h):
        M[i][i]+=H/F(3); M[i+1][i+1]+=H/F(3)
        M[i][i+1]+=H/F(6); M[i+1][i]+=H/F(6)
        if cells is not None:
            b[i]+=H*cells[i]/2; b[i+1]+=H*cells[i]/2
    if jump is not None:
        k,u=jump
        for i,H in enumerate(h):
            if i>k:
                b[i]+=H/F(2); b[i+1]+=H/F(2)
            elif i==k:
                b[i]+=H*(1-u)**2/F(2)
                b[i+1]+=H*(1-u*u)/F(2)
    for i in range(n):
        pivot=M[i][i]
        for j in range(i+1,n):
            if not M[j][i]: continue
            mult=M[j][i]/pivot
            for q in range(i,n): M[j][q]-=mult*M[i][q]
            b[j]-=mult*b[i]
    x=[F(0)]*n
    for i in range(n-1,-1,-1):
        x[i]=(b[i]-sum(M[i][j]*x[j] for j in range(i+1,n)))/M[i][i]
    return x

def variation(x):return sum((abs(x[i+1]-x[i]) for i in range(len(x)-1)),F(0))

checks=0
for nc in range(1,6):
    for lengths in product([F(1),F(2),F(5)],repeat=nc):
        for k in range(nc):
            for u in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
                y=project(lengths,jump=(k,u))
                assert variation(y)<=3,(lengths,k,u,y)
                checks+=1
print('ALL_EXACT_STEP_VARIATION_BOUNDS_PASS', checks)

checks2=0
for nc in range(2,7):
    for lengths in product([F(1),F(3)],repeat=nc):
        for cells in product([F(-1),F(0),F(2)],repeat=nc):
            v=variation(cells)
            if v:
                assert variation(project(lengths,cells=cells))<=3*v
                checks2+=1
print('ALL_EXACT_PIECEWISE_CONSTANT_BV_BOUNDS_PASS',checks2)

for m in range(1,8):
    e=F(1,1000)
    lengths=[e**j for j in range(m,0,-1)]+[F(1)]+[e**j for j in range(1,m+1)]
    gain=variation(project(lengths,jump=(m,F(1,2))))
    limiting=F(3)-F(3,2)*F(1,2)**m
    assert gain<3
    assert abs(gain-limiting)< F(1,100), (m,gain,limiting)
    print('GEOMETRIC_SHARPNESS',m, 'gain',round(float(gain),12),'limit',round(float(limiting),12))
print('ALL_CONTINUOUS_LINEAR_SPLINE_BV_TESTS_PASS')
