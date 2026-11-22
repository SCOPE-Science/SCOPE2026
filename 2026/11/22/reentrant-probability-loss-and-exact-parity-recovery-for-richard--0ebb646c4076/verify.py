#!/usr/bin/env python3
"""Independent rational-matrix and scalar checks for two-state Richardson Euler."""
from fractions import Fraction as F
import math
import random

def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in (0,1)) for j in (0,1)] for i in (0,1)]

def inverse(A):
    det = A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert det != 0
    return [[A[1][1]/det,-A[0][1]/det],[-A[1][0]/det,A[0][0]/det]]

def power(A, n):
    B = [[F(1),F(0)],[F(0),F(1)]]
    for _ in range(n): B=mm(B,A)
    return B

def r(z):
    return F(2)/(F(1)+z/F(2))**2-F(1)/(F(1)+z)

def matrix_from_formula(a,b,z,n):
    s=a+b; pi=[b/s,a/s]; v=r(z)**n
    return [[(F(1) if i==j else F(0))*v + (F(1)-v)*pi[j] for j in (0,1)] for i in (0,1)]

def from_implicit_steps(a,b,z):
    s=a+b; h=z/s
    Q=[[-a,a],[b,-b]]
    I=[[F(1),F(0)],[F(0),F(1)]]
    Rhalf=inverse([[I[i][j]-h*Q[i][j]/2 for j in (0,1)] for i in (0,1)])
    Rfull=inverse([[I[i][j]-h*Q[i][j] for j in (0,1)] for i in (0,1)])
    H=mm(Rhalf,Rhalf)
    return [[2*H[i][j]-Rfull[i][j] for j in (0,1)] for i in (0,1)]

rng=random.Random(651105)
count=0
for k in range(480):
    a=F(rng.randint(1,30), rng.randint(1,20))
    b=F(rng.randint(1,30), rng.randint(1,20))
    z=F(rng.randint(1,90), rng.randint(1,25))
    T=from_implicit_steps(a,b,z)
    for n in range(1,8):
        P=power(T,n)
        expect=matrix_from_formula(a,b,z,n)
        assert P==expect
        assert all(sum(row)==1 for row in P)
        if n%2==0: assert all(w>=0 for row in P for w in row)
        minpi=min(a,b)/(a+b); signed=r(z)**n
        assert all(w>=0 for row in P for w in row) == (signed >= -minpi/(1-minpi))
        count+=1
# Numeric monotonicity, exact-zero, strict derivative sign, extremum and cusp.
def derivative_num(z): return (z**3-10*z*z-20*z-8)/((z+1)**2*(z+2)**3)
def second_num(z): return -2*(z**4-16*z**3-48*z*z-40*z-8)/((z+1)**3*(z+2)**4)
lo,hi=10.,13.
for _ in range(100):
    mid=(lo+hi)/2
    if mid**3-10*mid**2-20*mid-8<0: lo=mid
    else: hi=mid
zstar=(lo+hi)/2
c=-float(r(F.from_float(zstar)))
mcrit=c/(1+c)
assert 11.75 < zstar < 11.77
assert 0.0348 < mcrit < 0.0349
assert second_num(zstar)>0
assert abs(float(r(F.from_float(2+2*math.sqrt(2)))))<1e-14
# Each off-critical m has two crossings; classify intervals via bisection.
def roots(m):
    assert 0 < m < mcrit
    target=-(m/(1-m))
    cut=2+2*math.sqrt(2)
    lefta,leftb=cut,zstar
    for _ in range(95):
        mid=(lefta+leftb)/2
        if float(r(F.from_float(mid)))>target:lefta=mid
        else:leftb=mid
    righta,rightb=zstar,max(2*zstar,3/m)
    assert float(r(F.from_float(rightb))) > target
    for _ in range(95):
        mid=(righta+rightb)/2
        if float(r(F.from_float(mid)))<target:righta=mid
        else:rightb=mid
    return (lefta+leftb)/2,(righta+rightb)/2
for m in [0.001,0.005,0.01,0.02,0.03,mcrit*0.99999]:
    l,u=roots(m)
    assert 2+2*math.sqrt(2)<l<zstar<u
    for z in [0.01,2, 2+2*math.sqrt(2), l*0.99, (l+zstar)/2, zstar, (zstar+u)/2, u*1.01,2*u]:
        value=m+(1-m)*float(r(F.from_float(z)))
        pred=(l < z < u)
        if abs(z-l)<1e-8 or abs(z-u)<1e-8:continue
        assert (value<0)==pred, (m,z,l,u,value,pred)
K=(1+c)*math.sqrt(2/second_num(zstar))
for delta in [1e-5,1e-6,1e-7,1e-8]:
    l,u=roots(mcrit-delta)
    left=(zstar-l)/math.sqrt(delta)
    right=(u-zstar)/math.sqrt(delta)
    assert abs(left-K)/K<0.05
    assert abs(right-K)/K<0.05
print('PASS: exact 2x2 matrix identities, row sums, parity and positivity: %d cases' % count)
print('PASS: numerical roots / limits / square-root cusp')
print('zstar=%.15f c=%.15f mcrit=%.15f rate_contrast=%.15f K=%.10f'%(zstar,c,mcrit,1/c,K))
