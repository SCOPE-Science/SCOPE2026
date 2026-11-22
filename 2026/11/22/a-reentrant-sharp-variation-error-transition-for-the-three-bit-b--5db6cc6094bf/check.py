#!/usr/bin/env python3
"""Exact rational and independent state-space checks for the three-bit threshold theorem."""
from fractions import Fraction as Q
from math import comb

tests=0

def ck(v, description):
    global tests
    tests+=1
    if not v:
        raise AssertionError(description)

def spectral(p,r):
    v=p*(1-p)
    a1=(3*v*(1-p)**4,3*v*v*(1-p)**2,v**3)
    a2=(12*v**3,3*v*v*(1-2*p)**2,4*v**3)
    a3=(3*v*p**4,3*v*v*p**2,v**3)
    w=((1-r)**2,(1-r*r)**2,(1-r**3)**2)
    return tuple(sum(a[i]*w[i] for i in range(3)) for a in (a1,a2,a3))

def B(p,r):
    return 3*p*p+2*p-1+p*p*((1+r+r*r)**2-(2-3*p)/(1-p)*(1+r)**2)

def br(p,r):
    a=(2-3*p)/(1-p)
    return 2*p*p*((1+r+r*r)*(1+2*r)-a*(1+r))

def matrix_errors(p,r):
    # Given k current ones: retained-or-refreshed success a; new success b from zeros.
    a=r+(1-r)*p
    b=(1-r)*p
    mat=[]
    for k in range(4):
        row=[]
        for target in range(4):
            prob=Q(0)
            for i in range(k+1):
                j=target-i
                if 0<=j<=3-k:
                    prob+=comb(k,i)*a**i*(1-a)**(k-i)*comb(3-k,j)*b**j*(1-b)**(3-k-j)
            row.append(prob)
        ck(sum(row)==1,'row stochastic')
        mat.append(row)
    masses=[comb(3,k)*p**k*(1-p)**(3-k) for k in range(4)]
    ck(sum(masses)==1,'stationary masses normalized')
    for target in range(4):
        ck(sum(masses[k]*mat[k][target] for k in range(4))==masses[target], 'stationarity')
    return tuple(sum(masses[k]*((Q(int(k>=j))-sum(mat[k][l]*int(l>=j) for l in range(4)))**2) for k in range(4)) for j in (1,2,3))

for den in (5,7,11):
    for a in range(1,den):
        p=Q(a,den)
        for b in range(den):
            r=Q(b,den)
            vals=matrix_errors(p,r)
            f=spectral(p,r)
            ck(vals==f,'independent matrix/Fourier norm mismatch')
            ck(f[1]-f[0]==3*p*(1-p)**3*(1-r)**2*B(p,r),'quartic factorization')
            rev=spectral(1-p,r)
            ck(vals==(rev[2],rev[1],rev[0]),'spin reflection')
            if p<Q(1,2):
                ck(f[0]>f[2],'rare-count threshold dominance')
            if p==Q(1,2):
                ck(f[1]>f[0] and f[0]==f[2],'balanced case')

p=Q(87,250)
ck(B(p,Q(0))>0,'reentry: left positive')
ck(B(p,Q(1,5))<0,'reentry: middle negative')
ck(B(p,Q(1))>0,'reentry: right positive')
ck(B(p,Q(0))==Q(28997,10187500),'left sign exact')
ck(B(p,Q(1,5))==-Q(16202602,1591796875),'middle sign exact')
ck(B(p,Q(1))==Q(8944,20375),'right sign exact')

# Simple independent float localization check: the proof of uniqueness is analytic.
def bisect_root(g,a,b,steps=100):
    va=g(a)
    for _ in range(steps):
        m=(a+b)/2
        if (g(m)>0)==(va>0):
            a=m;va=g(m)
        else:b=m
    return (a+b)/2

def minimum_r(x):
    return bisect_root(lambda t: float(br(x,t)),0.0,1.0)

def minB(x):
    return float(B(x,minimum_r(x)))

pc=bisect_root(minB,0.35,0.351)
rc=minimum_r(pc)
ck(abs(pc-0.3504779118934075)<2e-13,'critical p numerical enclosure')
ck(abs(rc-0.2054909532402524)<2e-13,'critical rho numerical enclosure')
for x in (0.348,0.349,0.350):
    rmin=minimum_r(x)
    ck(minB(x)<0 and float(B(x,0.0))>0 and float(B(x,1.0))>0,'double-switch window')
    left=bisect_root(lambda rr: float(B(x,rr)),0.0,rmin)
    right=bisect_root(lambda rr: float(B(x,rr)),rmin,1.0)
    ck(0<left<rmin<right<1,'root ordering')
print(f'PASS {tests} exact-rational and numerical assertions; pc~{pc:.15f}, rho_c~{rc:.15f}')
