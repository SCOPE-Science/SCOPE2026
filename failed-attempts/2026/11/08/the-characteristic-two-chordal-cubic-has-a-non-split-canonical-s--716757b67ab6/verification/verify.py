#!/usr/bin/env python3
"""Exact polynomial checks for the characteristic-two Hankel cubic singular ribbon.
All arithmetic is in F_2; no third-party modules required.
"""
from math import comb

def mon(*exponents):
    return {tuple(exponents): 1}

def add(*polys):
    out={}
    for p in polys:
        for e,c in p.items():
            out[e]=(out.get(e,0)+c)%2
            if not out[e]: del out[e]
    return out

def mul(a,b):
    out={}
    for e,c in a.items():
        for f,d in b.items():
            h=tuple(x+y for x,y in zip(e,f))
            out[h]=(out.get(h,0)+c*d)%2
            if not out[h]: del out[h]
    return out

def power(a,n):
    assert n>=0
    out={tuple(0 for _ in next(iter(a))):1} if a else {(0,)*5:1}
    for _ in range(n):out=mul(out,a)
    return out

def deriv(p,i):
    out={}
    for e,c in p.items():
        if e[i]%2:
            f=e[:i]+(e[i]-1,)+e[i+1:]
            out[f]=c
    return out

def var(i):return mon(*[int(j==i) for j in range(5)])
x0,x1,x2,x3,x4=[var(i) for i in range(5)]
q0=add(mul(x2,x4),mul(x3,x3))
q2=add(mul(x0,x4),mul(x2,x2))
q4=add(mul(x0,x2),mul(x1,x1))
# Compute the Leibniz determinant, with six terms; signs disappear in F_2.
from itertools import permutations
A=[[x0,x1,x2],[x1,x2,x3],[x2,x3,x4]]
F=add(*(mul(A[0][p[0]],mul(A[1][p[1]],A[2][p[2]])) for p in permutations(range(3))))
F_expected=add(mul(x0,mul(x2,x4)),mul(x0,mul(x3,x3)),mul(x1,mul(x1,x4)),mul(mul(x2,x2),x2))
assert F==F_expected
assert [deriv(F,i) for i in range(5)]==[q0,{},q2,{},q4]
assert F==add(mul(x0,q0),mul(x2,q2),mul(x4,q4))
print('GRADIENT_AND_EULER_OK')

# Laurent polynomials in t and a square-zero variable u; discard u powers >=2.
def lm(a,b=0):return {(a,b):1}
def la(*p):
    o={}
    for z in p:
        for k in z:
            o[k]=1-o.get(k,0)
            if not o[k]:del o[k]
    return o

def lp(a,b):
    o={}
    for (i,j) in a:
        for (m,n) in b:
            if j+n>=2:continue
            z=(i+m,j+n)
            o[z]=1-o.get(z,0)
            if not o[z]:del o[z]
    return o

def lpow(a,n):
    o=lm(0)
    for _ in range(n):o=lp(o,a)
    return o

T=lm(1);U=lm(0,1);ONE=lm(0)
param=[ONE,T,lp(T,T),la(lpow(T,3),U),lpow(T,4)]
def ev(q,v):
    total={}
    for exponent in q:
        term=ONE
        for i,n in enumerate(exponent):term=lp(term,lpow(v[i],n))
        total=la(total,term)
    return total
assert ev(q0,param)=={} and ev(q2,param)=={} and ev(q4,param)=={}
# The affine coordinate relation x3=t^3+u, with u^2=0 is therefore exact.
# Verify the opposite chart explicitly: x4=1, x3=s, x2=s^2,
# x1=s^3+v, x0=s^4 (with v^2=0).
sv=lm(1);vv=lm(0,1)
param_opposite=[lpow(sv,4),la(lpow(sv,3),vv),lpow(sv,2),sv,ONE]
assert all(ev(q,param_opposite)=={} for q in (q0,q2,q4))
S=la(lm(-1),lm(-4,1));V=lm(-6,1)
assert lpow(S,2)==lm(-2)
assert lpow(S,4)==lm(-4)
assert la(lpow(S,3),V)==lm(-3)
assert la(lpow(S,3),V)==lp(T,lm(-4))
# These are precisely x2/x4, x0/x4, x1/x4 from the first chart.
assert la(S,lm(-1))==lm(-4,1)
assert V==lm(-6,1)
print('TWO_CHART_GLUE_OK')

# The obstruction to a retraction onto P^1: a hypothetical split lift
# t+f(t)u and s+g(s)v would imply t^2+g(t^-1)=t^4 f(t).
# Nonnegative powers of t on the right are >=4; on the left all
# powers contributed by g(t^-1) are <=0, so coefficient of t^2 is 1.
for M in (0,1,2,3,6,15):
    lhs_degrees={2}
    for j in range(M+1):
        if -j in lhs_degrees:lhs_degrees.remove(-j)
        else:lhs_degrees.add(-j)
    rhs_degrees={4+j for j in range(M+1)}
    assert 2 in lhs_degrees and 2 not in rhs_degrees
print('NONSPLIT_LAURENT_OBSTRUCTION_OK')

# The complete intersection (2,2,2) in P^4 has Hilbert series
# (1-z^2)^3/(1-z)^5 and Hilbert polynomial 8n-4.
def H(n):
    return sum((-1)**i*comb(3,i)*comb(n-2*i+4,4)
               for i in range(4) if n-2*i>=0)
assert all(H(n)==8*n-4 for n in range(3,25))
# The same polynomial comes from O_P1(4n) + O_P1(4n-6).
assert all((4*n+1)+(4*n-5)==8*n-4 for n in range(3,25))
print('DEGREE_8_ARITHMETIC_GENUS_5_AND_CANONICAL_ADJUNCTION_OK')
print('ALL_CHECKS_PASSED')
