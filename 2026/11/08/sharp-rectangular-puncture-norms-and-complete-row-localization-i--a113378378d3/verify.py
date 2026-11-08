"""Exact checks for the punctured rectangular bilinear Walsh norm theorem.
Run: python3 verify.py. Only Python's standard library is required.
"""
from fractions import Fraction as F
from itertools import product
import random

def moments(m, n, a):
    assert a[m-1][n-1] == 0
    B = sum(v*v for row in a for v in row)
    fourth_self = sum(v**4 for row in a for v in row)
    rectangles = sum(a[i][j]*a[i][l]*a[k][j]*a[k][l]
                     for i in range(m) for k in range(i+1,m)
                     for j in range(n) for l in range(j+1,n))
    return B, 3*B*B - 2*fourth_self + 24*rectangles

def exhaustive_fourth(m, n, a):
    total = 0
    for xs in product((-1,1), repeat=m):
        for ys in product((-1,1), repeat=n):
            value = sum(a[i][j]*xs[i]*ys[j]
                        for i in range(m) for j in range(n))
            total += value**4
    return F(total, 2**(m+n))

def model(a,b,p,q,r):
    return (F(3) + F(6*(a-1)*(b-1)-2,a*b)*p*p
            -F(2,a)*q*q-F(2,b)*r*r
            + F(12*(a-1),a)*p*q + F(12*(b-1),b)*p*r)

def certificate(a,b,p,q,r):
    assert a>=b+1 and b>=1 and p+q+r==1 and min(p,q,r)>=0
    C=F(3*a-2,a)*F(3*b+1,b+1)
    popt=F(3*a*b-2*b,(3*a-2)*(b+1))-F(3*a-2*b,(3*a-2)*(b+1))*r
    A=F(2*(3*a-2)*(b+1),a*b)
    L=F(4*(3*a-3*b-1),a*(b+1))
    h=a-b
    N=(21*b-6)*h*h+(27*b*b-17*b-2)*h+6*b**3-5*b*b
    assert L>0 and N>0
    H=F(2*N,a*b*(3*a-2)*(b+1))
    deficit=A*(p-popt)**2 + L*r*(1-r) + H*r*r
    assert C - model(a,b,p,q,r) == deficit, (a,b,p,q,r)
    assert deficit >= 0
    return C

random.seed(70042)
enumerated=0
for m in range(3,7):
    for n in range(2,m):
        a,b=m-1,n-1
        C=F(3*a-2,a)*F(3*b+1,b+1)
        # Model sharpness: an undamaged complete (m-1) x n rectangle.
        witness=[[1 if i<m-1 else 0 for j in range(n)] for i in range(m)]
        B,M4=moments(m,n,witness)
        assert F(M4,B*B)==C
        for _ in range(18):
            arr=[[random.randint(-2,2) if (i,j)!=(m-1,n-1) else 0
                   for j in range(n)] for i in range(m)]
            B,M4=moments(m,n,arr)
            assert F(M4)==exhaustive_fourth(m,n,arr)
            if B: assert F(M4,B*B) <= C
            enumerated+=1
print('EXACT_SIGN_ENUMERATION_MOMENT_IDENTITY_OK',enumerated)

certificate_tests=0
for b in range(1,31):
    for a in (b+1,b+2,b+4,2*b+7,5*b+31):
        for _ in range(18):
            x=[F(random.randint(0,30),30) for _ in range(3)]
            if sum(x)==0: continue
            p,q,r=(v/sum(x) for v in x)
            certificate(a,b,p,q,r)
            certificate_tests+=1
        p=F(b,b+1);q=F(1,b+1);r=F(0)
        assert model(a,b,p,q,r)==certificate(a,b,p,q,r)
print('EXACT_NONNEGATIVE_GLOBAL_BLOCK_CERTIFICATE_OK',certificate_tests)

for a in range(2,50):
    for b in range(1,a):
        h=a-b
        N1=21*a*a*b-6*a*a-15*a*b*b-5*a*b-2*a+6*b*b+2*b
        N2=(21*b-6)*h*h+(27*b*b-17*b-2)*h+6*b**3-5*b*b
        assert N1==N2 and N2>0
print('UNIVERSAL_POSITIVITY_POLYNOMIAL_IDENTITY_DIAGNOSTICS_OK')
print('ALL_RECTANGULAR_RADEMACHER_NORM_CHECKS_PASSED')
