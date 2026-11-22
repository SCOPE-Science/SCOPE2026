#!/usr/bin/env python3
"""Standalone exact-arithmetic and numerical cross-checks for a two-scale corridor theorem."""
from fractions import Fraction as F
from math import log, sqrt

def q1(u): return u*u-96*u+2500
def q2(u): return u*u+102*u+22201
def H(u): return 10*u**3-351*u*u-4259*u+81852
def P(u): return -10*u**3+683*u*u-8009*u+10900

def bisect(f,a,b,steps=80):
    assert f(a)*f(b)<0
    for _ in range(steps):
        m=(a+b)/2
        if f(a)*f(m)>0: a=m
        else: b=m
    return (a+b)/2

def cost(x,L=14):
    return (log((1+x*x)*(1+(L-x)**2))
           +9*log((1+(x/10)**2)*(1+((L-x)/10)**2)))/10

def dcost(x,L=14):
    return sum((w*2*(x/(l*l+x*x)-(L-x)/(l*l+(L-x)**2)))
               for w,l in [(0.1,1),(0.9,10)])

checks=0
def check(cond,desc):
    global checks
    assert cond, desc
    checks+=1

# Three *distinct* sign-changing positive roots of a cubic exhaust its roots.
for a,b in [(1,2),(12,14),(53,55)]:
    check(P(a)*P(b)<0, f'P sign bracket {a,b}')
check(P(0)>0 and P(2)<0 and P(14)>0 and P(55)<0,'P sign regime')

# The cubic H has exactly two positive roots: two sign changes, Descartes upper bound 2.
check(H(0)>0 and H(12)<0 and H(40)<0 and H(41)>0 and H(49)>0,'H sign pattern')
check(q1(F(0))>0 and q2(F(0))>0,'positive products at center')
check(H(F(0))>0,'strict central local minimum of log-cost')
check(F(340,2500)*F(27169,22201)**9 < 1,'exact off-center beats center')

# Algebraic identities from the sum of two squared-distance denominators.
for u in [F(i,4) for i in range(197)]:
    check(q1(u)>0 and q2(u)>0, 'two positive kernel products')
    left=(2*u-96)*q2(u)+9*(2*u+102)*q1(u)
    check(left==2*H(u),'exact stationary polynomial')

# Check local and global geometry independently of algebraic proof.
r1=bisect(H,11,12)
r2=bisect(H,40,41)
a=7-sqrt(r2)
b=7+sqrt(r2)
check(0<a<1<b<14,'two strict asymmetric interior optima')
check(cost(a)<cost(7),'asymmetric global winner')
check(abs(cost(a)-cost(b))<1e-12,'reflection symmetry')
check(cost(7)<cost(7-sqrt(r1)),'center separated by a barrier')
for x in [0.1,0.5,1,1.5,2,3,4.5,5,6,7,9,11,13.9]:
    dh=1e-5
    approx=(cost(x+dh)-cost(x-dh))/(2*dh)
    check(abs(approx-dcost(x))<1e-7,'gradient finite differences')

# Single-species: derivative in u is exactly 2(u+ell**2-h**2)/Q_ell(u).
for ell in [F(1),F(2),F(10)]:
    for h in [F(1,2),F(1),F(2),F(5),F(12)]:
        ustar=max(F(0),h*h-ell*ell)
        def Q(u):return u*u+2*(ell*ell-h*h)*u+(ell*ell+h*h)**2
        for j in range(50):
            u=h*h*F(j,49)
            check(Q(u)>=Q(ustar),'single-scale global minimizer of kernel product')

print('ASSERTIONS_PASSED', checks)
print('H_ROOTS',f'{r1:.12f}',f'{r2:.12f}')
print('OPTIMAL_LOCATIONS',f'{a:.12f}',f'{b:.12f}')
print('LOG_COST_CENTER',f'{cost(7):.12f}','LOG_COST_OFFCENTER',f'{cost(a):.12f}')
print('MIDPOINT_STABILITY_TRANSITIONS_L',*[f'{2*sqrt(bisect(P,*bounds)):.12f}' for bounds in [(1,2),(12,14),(53,55)]])
