"""Exact rational checks for the three-block projection family.

Run with Python 3 and the standard library: python check_exact.py.
Finite checks support, but do not replace, the universal proof.
"""
from fractions import Fraction as F
from itertools import product

checks = 0

def verify(ok, label):
    global checks
    assert ok, label
    checks += 1


def matrix(t):
    s = 1 + t + t*t
    x = (1+t)/(2*s)
    y = t/s
    u = (x,x,y)
    a = (F(1),F(1),t)
    P = [[F(i==j) - u[i]*a[j] for j in range(3)] for i in range(3)]
    return s,u,a,P

for denominator in range(1,25):
    for numerator in range(1,denominator+1):
        t=F(numerator,denominator)
        s,u,a,P=matrix(t)
        r=1+t/s
        verify(sum(a[i]*u[i] for i in range(3))==1, 'normalization')
        verify(all(sum(a[i]*P[i][j] for i in range(3))==0 for j in range(3)), 'range')
        verify(all(sum(P[i][k]*P[k][j] for k in range(3))==P[i][j] for i in range(3) for j in range(3)), 'idempotent')
        verify(all(sum(abs(P[i][j]) for i in range(3))==r for j in range(3)), 'sharp primal')
        verify(P[0][0]>0 and P[1][0]<0 and P[2][0]<0, 'first facet')
        verify(P[0][1]<0 and P[1][1]>0 and P[2][1]<0, 'second facet')
        alpha=t*(1+t)/2
        for v1,v2 in product([F(-2),F(-1),F(0),F(1),F(2)], repeat=2):
            v3=(1-v1-v2)/t
            L1=1-v1+v2+v3
            L2=1+v1-v2+v3
            L3=1+t*(v1+v2-v3)
            verify(alpha*(L1+L2)+L3==(2*alpha+1)*r, 'dual certificate')
        if t<1:
            verify((1-t*t)>0, 'strict monotonicity')
        else:
            verify(1-t*t==0, 'endpoint derivative')

print(f'THREE_BLOCK_PROJECTION_RATIONAL_OK {checks}')
