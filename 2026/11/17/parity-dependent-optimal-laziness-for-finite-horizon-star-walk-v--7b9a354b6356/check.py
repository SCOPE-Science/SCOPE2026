"""Exact-rational checks for finite-horizon edge variation of lazy star walks.
Run: python check.py. No external dependencies are required.
"""
from fractions import Fraction as F
from random import Random
from math import isclose


def p_step(values, alpha):
    k = len(values)-1
    center = values[0]
    avg = sum(values[1:], F(0))/k
    return [alpha*center+(1-alpha)*avg] + [alpha*z+(1-alpha)*center for z in values[1:]]


def p_power(values, alpha, m):
    for _ in range(m):
        values = p_step(values,alpha)
    return values


def variation(values):
    return sum((abs(x-values[0]) for x in values[1:]), F(0))


def closed_norm(k,m,alpha):
    if k==1:
        return abs(2*alpha-1)**m
    a=alpha**m
    b=(2*alpha-1)**m
    return max(abs(b), (2*(k-1)*a-(k-2)*b)/k)


def edge_column_norm(k,m,alpha):
    base=[F(0)]*(k+1)
    base[1]=F(1)
    return variation(p_power(base,alpha,m))


r=Random(841269)
checks=0
for k in range(1,13):
    for m in range(1,15):
        for j in range(26):
            alpha=F(j,25)
            n1=closed_norm(k,m,alpha)
            n2=edge_column_norm(k,m,alpha)
            assert n1==n2,(k,m,alpha,n1,n2)
            checks+=1
print('EXACT_DIRECT_STAR_EDGE_COLUMN_EQUALITY_PASSED',checks)

checked=0
for k in range(1,13):
    for m in range(1,10):
        for _ in range(19):
            alpha=F(r.randrange(0,41),40)
            x=[F(r.randrange(-15,16),r.randrange(1,10)) for _ in range(k+1)]
            if variation(x):
                assert variation(p_power(x,alpha,m))<=closed_norm(k,m,alpha)*variation(x)
                checked+=1
print('EXACT_ARBITRARY_SIGNED_INPUT_VARIATION_BOUNDS_PASSED',checked)

count=0
for k in range(2,27):
    a=F(1,3)
    for m in range(2,20,2):
        x=[F(r.randrange(-8,9),7) for _ in range(k+1)]
        y=p_power(x,a,m)
        # At even horizons, all edge differences equal 3^{-m} times the input differences.
        for i in range(1,k+1):
            assert y[i]-y[0]==(x[i]-x[0])/3**m
            count+=1
print('EVEN_HORIZON_UNIVERSAL_EDGE_SCALAR_IDENTITY_PASSED',count)

for k in range(2,32):
    for m in range(1,20,2):
        if m==1:
            alpha=1/(k+1)
        elif k<=3:
            alpha=1/(2+(k-1)**(1/m))
        else:
            alpha=1/(2+((k-1)/(k-2))**(1/(m-1)))
        val=float(closed_norm(k,m,alpha))
        for j in range(1001):
            x=j/1000
            check=float(closed_norm(k,m,x))
            assert check>=val-5e-12,(k,m,alpha,val,x,check)
print('ODD_HORIZON_ANALYTIC_MINIMIZERS_BEAT_FINE_GRID_PASSED',30*10*1001)

print('ALL_LAZY_STAR_VARIATION_DIAGNOSTICS_PASSED')
