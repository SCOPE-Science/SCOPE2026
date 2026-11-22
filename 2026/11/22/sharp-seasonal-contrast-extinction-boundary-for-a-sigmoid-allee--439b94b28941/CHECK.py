#!/usr/bin/env python3
"""Exact-arithmetic diagnostic checks for the two-season sigmoid Allee theorem.
No external packages or input data are required. Finite checks complement the proof.
"""
from fractions import Fraction as F
from math import sqrt, acosh, log

checks = 0

def certify(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)


def Fmap(r, x):
    return r*x*x/(1+x*x)


def two_year(a, b, x):
    return Fmap(b, Fmap(a, x))


def Q(a,b,x):
    return (1+a*a)*x**4-b*a*a*x**3+2*x*x+1


def H(a,b):
    return 27*a**4*b**4-288*a*a*b*b-256*(a*a+b*b+1)


def det_bareiss(matrix):
    """Exact integer determinant by fraction-free elimination with row swaps."""
    m=[list(map(int,row)) for row in matrix]
    n=len(m)
    if n==1:return m[0][0]
    sign=1
    prev=1
    for k in range(n-1):
        if m[k][k]==0:
            j=next((j for j in range(k+1,n) if m[j][k]),None)
            if j is None:return 0
            m[k],m[j]=m[j],m[k]
            sign=-sign
        pivot=m[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=m[i][j]*pivot-m[i][k]*m[k][j]
                if num%prev!=0:raise ArithmeticError('Bareiss divisibility')
                m[i][j]=num//prev
            m[i][k]=0
        prev=pivot
    return sign*m[n-1][n-1]


def resultant_quartic_derivative(a,b):
    aa=int(a);bb=int(b)
    c4=1+aa*aa; c3=-bb*aa*aa; c2=2
    f=[c4,c3,c2,0,1]
    g=[4*c4,3*c3,2*c2,0]
    rows=[]
    for shift in range(3):rows.append([0]*shift+f+[0]*(2-shift))
    for shift in range(4):rows.append([0]*shift+g+[0]*(3-shift))
    return det_bareiss(rows)

# The signed stroboscopic displacement identity holds exactly.
for a in [F(1,4),F(1,2),F(1),F(2),F(3),F(7)]:
    for b in [F(1,3),F(1),F(2),F(5),F(36)]:
        for x in [F(1,8),F(1,2),F(1),F(3,2),F(4),F(10)]:
            denom=(1+x*x)**2+a*a*x**4
            certify((two_year(a,b,x)-x)*denom == -x*Q(a,b,x), 'stroboscopic identity')
            certify(0 < two_year(a,b,x) <= b, 'bounded map')

# The quartic discriminant identity is verified by exact Sylvester determinants.
for a in range(1,9):
    for b in range(1,9):
        res=resultant_quartic_derivative(a,b)
        c4=1+a*a
        certify(res == c4*(-a**4*H(a,b)), 'quartic resultant / discriminant')

# Exact contrast witnesses at the same product ab=9.
certify(H(F(1),F(9)) == 132571, 'moderate seasonal contrast')
certify(H(F(1,4),F(36)) == -178229, 'extreme seasonal contrast')
certify(H(F(2),F(2)) == 0, 'critical homogeneous')
certify(H(F(3),F(3)) == 148955, 'supercritical homogeneous')
certify(Q(F(2),F(2),F(1)) == 0, 'tangency location')
certify(two_year(F(2),F(2),F(1)) == 1, 'critical population')

# Numeric check of the sharp seasonal-contrast boundary (not a proof).
for gg in [2.1,2.5,3,4,5]:
    cc=(27*gg**8-288*gg**4-256)/(512*gg**2)
    certify(cc>1,'supercritical arcosh argument')
    th=0.5*acosh(cc)
    def h(theta):return H(gg*__import__('math').exp(theta),gg*__import__('math').exp(-theta))
    certify(h(0)>0 and h(th*.8)>0 and h(th*1.2)<0,'critical contrast sign')
    certify(abs(h(th)) < 1e-7*max(1,abs(h(0))), 'critical contrast equation')

print('PASS:',checks,'exact and numerical diagnostic assertions')
