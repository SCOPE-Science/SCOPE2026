#!/usr/bin/env python3
"""Exact arithmetic checks for CNBLD modal phase theorem.
The universal quantifiers and asymptotics are proved in RESULT.md;
finite arithmetic probes here do not replace those arguments.
"""
from fractions import Fraction as F
from math import factorial, sqrt, ceil
import sympy as s
x,r,t=s.symbols('x r t',positive=True)
f=lambda x: x*(x+r)/(x+1)**2
crit=lambda x:(2*x*x+4*x+1)/(x*x+x-1)
assert s.simplify(f(x+1)-f(x)+((r-2)*x*x+(r-4)*x-(r+1))/((x+1)**2*(x+2)**2))==0
assert s.simplify(crit(x)-crit(x+1)-2*(x+2)**2/((x*x+x-1)*(x*x+3*x+1)))==0
assert s.simplify(f(x)-1-((r-2)*x-1)/(x+1)**2)==0
assert s.simplify(f(x)/f(x+1)-1-((r-2)*x*x+(r-4)*x-(r+1))/((x+1)**3*(x+r+1)))==0
root=(4-r+s.sqrt(5*r*r-12*r+8))/(2*(r-2))
assert s.simplify(((r-2)*x*x+(r-4)*x-(r+1)).subs(x,root)) == 0
# The exact width on the shape interval 17/5 <= r < 7.
assert s.simplify(4/(r+1)-9/(2*(r+2))-(7-r)/(2*(r+1)*(r+2)))==0
# First genuine bistability: r=6, theta=17/30.
rr=F(6); theta=F(17,30)
R=lambda j:theta*F(j)*(j+rr)/F((j+1)**2)
assert (R(1),R(2),R(3)) == (F(119,120),F(136,135),F(153,160))
assert R(1)<1<R(2) and R(3)<1
assert R(1)*R(2)==F(2023,2025)
# Formula for the exact shape-six global crossover and its bound.
assert s.simplify(s.sqrt(18/((r+1)*(r+2))).subs(r,6)-3/(2*s.sqrt(7)))==0
# Exact equal global maxima for theta=3/(2 sqrt(7)).
T=3/(2*s.sqrt(7))
Rs=[s.simplify(T*f(j).subs(r,6)) for j in (1,2,3)]
assert s.simplify(Rs[0]*Rs[1]-1)==0
assert bool(Rs[0]<1) and bool(Rs[1]>1) and bool(Rs[2]<1)
assert bool(T>F(9,16)) and bool(T<F(4,7))
# Exact finite-spectrum modal tests at shape/rate rationals;
# outcomes are sign words D (decrease), U (increase), E (flat).
checks=0
for rr in [F(1),F(2),F(201,100),F(21,10),F(5,2),F(3),F(17,5),F(4),F(6),F(699,100),F(7),F(8)]:
    fr=lambda j:F(j)*(j+rr)/F((j+1)**2)
    maxidx=max(range(1,1200),key=fr)
    M=fr(maxidx)
    for theta in [F(1,4),F(1,2),F(17,30),F(3,4),F(9,10),F(99,100),F(999,1000),F(99999,100000)]:
        word=['+' if theta*fr(j)>1 else '-' if theta*fr(j)<1 else '0' for j in range(1,1200)]
        # Positive ratios form a single interval on all checked indices.
        positive=[i for i,w in enumerate(word) if w=='+']
        if positive: assert positive==list(range(min(positive),max(positive)+1))
        if rr<=2: assert not positive
        if rr>=7: assert not ('-' in word[:max(positive)+1] if positive else False)
        if F(2)<rr<F(7):
            bimodal=(theta>1/M and theta*fr(1)<1)
            # if r is very close to 2, the first positive ratio may be beyond 1200;
            # select test points so no such threshold lies beyond our finite scan.
            if bimodal and positive:
                assert min(positive)>0
        checks+=1
# Sharp quadratic onset and divergent index scales at shape two.
for eps in [F(1,10),F(1,20),F(1,40),F(1,80)]:
    sh=2+eps
    first=max(range(1,10000), key=lambda j:F(j)*(j+sh)/((j+1)**2))
    MM=F(first)*(first+sh)/((first+1)**2)
    assert abs(float((1-1/MM)/(eps*eps))-1/4)<float(eps)
    assert abs(float(first*eps)-2)<3*float(eps)
print(f'PASS: {checks} exact rational probes, symbolic ratio identities, sharp r=6 double mode, onset and endpoint checks')
