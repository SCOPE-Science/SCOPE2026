#!/usr/bin/env python3
"""Reproducible algebraic and numerical checks for a sharp BV norm formula.
This standalone checker is not a substitute for the infinite-sequence proof.
"""
from fractions import Fraction as F
from math import sqrt
import random

# Cubic-Hermite derivative in the local coordinate t.
def basis(t):
    return (6*t*(1-t), 3*t*t-4*t+1, 3*t*t-2*t)

def integrate_abs_quad(c0,c1,c2):
    # polynomial q(t)=c0+c1*t+c2*t^2; returns integral |q| on [0,1].
    roots=[]
    if abs(c2)>1e-12:
        disc=c1*c1-4*c2*c0
        if disc>0:
            roots=[(-c1-sqrt(disc))/(2*c2),(-c1+sqrt(disc))/(2*c2)]
    elif abs(c1)>1e-12:
        roots=[-c0/c1]
    cuts=[0.]+sorted(set(r for r in roots if 0<r<1))+[1.]
    prim=lambda t:c0*t+c1*t*t/2+c2*t*t*t/3
    return sum(abs(prim(b)-prim(a)) for a,b in zip(cuts,cuts[1:]))

def steffen(a,b,ha,hb):
    if a*b<=0:return 0.
    p=(hb*a+ha*b)/(ha+hb)
    return (1 if a>0 else -1)*min(2*abs(a),2*abs(b),abs(p))

def slopes(h,s):
    return [0.]+[steffen(s[i-1],s[i],h[i-1],h[i]) for i in range(1,len(s))]+[0.]

def tv(h,s,t):
    m=slopes(h,s)
    return sum(h[i]*integrate_abs_quad(m[i],6*s[i]-4*m[i]-2*m[i+1],-6*s[i]+3*m[i]+3*m[i+1]) for i in range(len(s)))

def theoretical(h):
    return max(1+16*(h[i-1]+h[i+1])/(27*h[i]) for i in range(1,len(h)-1))

# Exact Hermite polynomial coefficient and integral checks, with rational arithmetic.
# A(t) = 0+6t-6t², B(t) = 1-4t+3t², C(t) = 0-2t+3t².
A=(F(0),F(6),F(-6));B=(F(1),F(-4),F(3));C=(F(0),F(-2),F(3))
int_poly=lambda p,t:p[0]*t+p[1]*t*t/2+p[2]*t*t*t/3
assert int_poly(A,F(1))==1 and int_poly(B,F(1))==0 and int_poly(C,F(1))==0
assert int_poly(B,F(1,3))*2==F(8,27)
assert -int_poly(C,F(2,3))*2==F(8,27)
add=lambda *ps:tuple(sum(p[j] for p in ps) for j in range(3))
scale=lambda a,p:tuple(a*v for v in p)
assert add(A,scale(2,B))==(2,-2,0)    # 2(1-t)
assert add(A,scale(2,C))==(0,2,0)     # 2t
assert add(A,scale(2,B),scale(2,C))==(2,-6,6)  # >= 1/2 on [0,1]
# A(t)=6t(1-t)>=0; hence all four corners and their convex hull are >=0.
print('EXACT_BASIS_INTEGRALS_AND_FOUR_CORNER_IDENTITIES_PASS 8/27')

# WITNESS: h[-1],h[0],h[+1]=2,1,3; two inputs differ in a single secant.
h=[1.,1.,2.,1.,3.,1.,1.]
s=[0.,0.,1000.,1.,1000.,0.,0.]
t=s.copy();t[3]+=0.25
ms,mt=slopes(h,s),slopes(h,t)
assert abs(mt[3]-ms[3]-0.5)<1e-10 and abs(mt[4]-ms[4]-0.5)<1e-10
q=[a-b for a,b in zip(t,s)]
# For pairwise differences, Hermite derivative uses differences of both secants and slopes.
dm=[a-b for a,b in zip(mt,ms)]
pair_var=sum(h[i]*integrate_abs_quad(dm[i],6*q[i]-4*dm[i]-2*dm[i+1],-6*q[i]+3*dm[i]+3*dm[i+1]) for i in range(len(s)))
K=1+F(16,27)*(F(2)+F(3))/F(1)
assert K==F(107,27)
assert abs(pair_var/(h[3]*q[3])-float(K))<1e-11
print('EXACT_WITNESS_COEFFICIENT_PASS 107/27')

rng=random.Random(20261114)
for trial in range(2500):
    n=rng.randint(6,16)
    h=[2**rng.uniform(-3,3) for _ in range(n)]
    s=[0.]*n; t=[0.]*n
    for i in range(1,n-1):
        s[i]=rng.uniform(-5,5)
        t[i]=s[i]+rng.uniform(-2,2)
    dm=[a-b for a,b in zip(slopes(h,t),slopes(h,s))]
    diff=[a-b for a,b in zip(t,s)]
    V=sum(h[i]*abs(diff[i]) for i in range(n))
    L=sum(h[i]*integrate_abs_quad(dm[i],6*diff[i]-4*dm[i]-2*dm[i+1],-6*diff[i]+3*dm[i]+3*dm[i+1]) for i in range(n))
    assert L<=theoretical(h)*V+1e-7*(1+V), (trial,L,theoretical(h)*V)
    assert abs(tv(h,s,t)-sum(h[i]*abs(s[i]) for i in range(n)))<1e-7
print('NONUNIFORM_RANDOM_TWO_INPUT_AND_ONE_INPUT_BV_CHECKS_PASS 2500')
print('ALL_STEFFEN_NONUNIFORM_CHECKS_PASS')
