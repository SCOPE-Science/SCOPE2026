#!/usr/bin/env python3
"""Exact rational examples and numerical checks of mirrored two-strain SIS equilibrium laws.

Requires only Python 3 standard library. Finite checks supplement, not replace, proofs.
"""
from fractions import Fraction as F
from math import sqrt, isclose

checks = 0

def check(cond, msg):
    global checks
    if not cond:
        raise AssertionError(msg)
    checks += 1

def vec_flow(S, i1, i2, a, b, d):
    beta1 = (b, a)
    beta2 = (a, b)
    ds = []
    di1 = []
    di2 = []
    for j in (0, 1):
        k = 1 - j
        ds.append(d*(S[k]-S[j]) - S[j]*(beta1[j]*i1[j] + beta2[j]*i2[j]) + i1[j] + i2[j])
        di1.append(d*(i1[k]-i1[j]) + (beta1[j]*S[j]-1)*i1[j])
        di2.append(d*(i2[k]-i2[j]) + (beta2[j]*S[j]-1)*i2[j])
    return ds, di1, di2

def determinant(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def blocks(a,b,d,s,p,q):
    common11=b*s-1-d-b*p
    common22=a*s-1-d-a*q
    even=((common11,d-b*p),(d-a*q,common22))
    odd=((common11,d+b*p),(d+a*q,common22))
    return even,odd

a,b,d,s,p,q = F(1,2), F(3), F(3,2), F(1,2), F(3,10), F(1,5)
S=(s,s); I1=(p,q); I2=(q,p)
f=vec_flow(S,I1,I2,a,b,d)
for comp in f:
    for entry in comp:
        check(entry==0,"exact equilibrium residual")
check(sum(S)+sum(I1)+sum(I2)==2,"total host mass")
check(a*b*s*s-(a+b)*(1+d)*s+1+2*d==0,"quadratic stationary condition")
check(d*(p-q)==(b*s-1)*p,"Perron first row")
check(d*(p-q)==-(a*s-1)*q,"Perron second row")
check(p>q>0 and s>0,"strict positivity")
Aeven,Aodd=blocks(a,b,d,s,p,q)
check(determinant(Aodd)==F(5,8),"odd determinant")
check(determinant(Aeven)==F(29,8),"even determinant")
check(determinant(Aodd)==d*(p-q)*(b*p/q-a*q/p),"odd determinant formula")
check(determinant(Aeven)==determinant(Aodd)+2*d*(b*p+a*q),"even determinant formula")
for A in (Aeven,Aodd):
    check(A[0][0]+A[1][1]<0,"Hurwitz negative trace")
    check(determinant(A)>0,"Hurwitz positive determinant")

# Detect the loss of positive endemicity at a sharp finite migration cutoff.
a,b = F(1,2), F(5,4)
dc=(b-1)*(1-a)/(2-a-b)
check(dc==F(1,2),"rational cutoff")
for d,expected in [(F(1,8),1),(F(1,2),0),(F(3,4),-1)]:
    # At S=1, trace is negative for these parameters. The determinant
    # has the sign opposite to the Perron eigenvalue, unless zero.
    det=(b-1-d)*(a-1-d)-d*d
    check((det<0)-(det>0)==expected,"invasion threshold sign")

# Positive rational root constructed from selected s; sample a large exact
# family without numerical root-finding error. Verify all 6 equations.
a,b=F(1,2),F(3)
for numerator in range(34,57):
    s=F(numerator,100)
    den=2-(a+b)*s
    if den==0: continue
    d=((a+b)*s-a*b*s*s-1)/den
    if d<=0: continue
    r=d/(1+d-b*s)
    if r<=1: continue
    p=(1-s)*r/(1+r)
    q=(1-s)/(1+r)
    if min(p,q,s)<=0: continue
    f=vec_flow((s,s),(p,q),(q,p),a,b,d)
    for comp in f:
        for val in comp:
            check(val==0,"rational family flow")
    ev,od=blocks(a,b,d,s,p,q)
    check(determinant(ev)>0 and determinant(od)>0,"rational family positive determinants")

# Strong-migration coefficient checked against direct eigenvalue arithmetic.
a,b=0.5,3.0
K=(b-a)**2*(a+b-2)/(4*(a+b)**2)
C=(b-a)*(a+b-2)/(2*(a+b)**2)
for d in [100.0, 1000.0, 10000.0, 100000.0]:
    # small quadratic root evaluated stably as c/(the large root coefficient)
    s=2*(1+2*d)/((a+b)*(1+d)+sqrt((a+b)**2*(1+d)**2-4*a*b*(1+2*d)))
    r=d/(1+d-b*s)
    p=(1-s)*r/(1+r)
    q=(1-s)/(1+r)
    even,odd=blocks(a,b,d,s,p,q)
    tr=odd[0][0]+odd[1][1]
    det=determinant(odd)
    fast=(tr-sqrt(tr*tr-4*det))/2
    slow=det/fast # robust near-zero eigenvalue
    check(slow<0,"slow eigenvalue negative")
    check(abs(d*slow+K)<0.002,"asymptotic slow eigenvalue")
    check(abs(d*(p-q)-C)<0.002,"segregation asymptotic")

print('VERIFY_OK',checks,'exact rational and numeric checks')
