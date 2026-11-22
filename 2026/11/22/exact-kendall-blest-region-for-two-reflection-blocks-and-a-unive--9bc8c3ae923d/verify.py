#!/usr/bin/env python3
"""Exact rational checks for the two-reflection-block Kendall--Blest theorem.

The proof for arbitrary real parameters is in RESULT.md. The finite tests here
are diagnostics; polynomial identities are checked coefficient by coefficient.
"""
from fractions import Fraction as Q
from math import isclose

checks = 0

def eq(x, y):
    global checks
    checks += 1
    assert x == y, (x, y)

def poly_add(a,b):
    n=max(len(a),len(b))
    return [ (a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]

def poly_mul(a,b):
    o=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):o[i+j]+=x*y
    return o

def poly_sub(a,b):return poly_add(a,[-x for x in b])
def poly_der(a):return [(i+1)*a[i+1] for i in range(len(a)-1)]
def poly_pow(a,n):
    v=[1]
    for _ in range(n):v=poly_mul(v,a)
    return v

def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

# f=(r^4+2r^3+1)/(1+r^2)^2,
# f'= -2r(r^3-2r^2-3r+2)/(1+r^2)^3.
N=[1,0,0,2,1]
D=poly_pow([1,0,1],2)
P=[2,-3,-2,1]
left=poly_sub(poly_mul(poly_der(N),D),poly_mul(N,poly_der(D)))
right=poly_mul([-0,-4,6,4,-2],[1,0,1]) # -2r P(r)*(1+r^2)
# Direct numerator is N'D - ND'; equals -2rP(r)*(1+r^2).
eq(trim(left),trim(right))
# 1-f = 2r^2(1-r)/(1+r^2)^2.
eq(trim(poly_sub(D,N)),[0,0,2,-2])
# The cubic has unique (0,1) root: strictly negative derivative there;
# bracket it by exact rational evaluations.
def p(r):return r**3-2*r**2-3*r+2
lo=Q(5293,10000);hi=Q(5294,10000)
assert p(lo)>0 and p(hi)<0
checks+=2
for j in range(1001):
    r=Q(j,1000)
    eq(3*r*r-4*r-3<0,True)
    if 0<r<1:
        eq((1+r*r)**2-(r**4+2*r**3+1),2*r*r*(1-r))

# Identity behind the two-block loss and the first-branch formula.
def block_penalty(h,l):
    # integral of (2x-l)^2 is (4/3-2+1)*l^3 = l^3/3.
    integral=Q(4,3)*l**3-2*l**3+l**3
    eq(integral,l**3/3)
    return 6*(2-2*h-l)*integral

def block_eta(blocks):return 1-sum((block_penalty(h,l) for h,l in blocks),Q(0))
def tau(blocks):return 1-2*sum((l*l for h,l in blocks),Q(0))
def F(a,b):return a**4+2*a**3*b+b**4
for den in range(4,36):
    for i in range(1,den//2+1):
        for j in range(i,den-i+1):
            a=Q(i,den);b=Q(j,den)
            if a+b>1:continue
            # Two blocks packed at upper end.
            top=[(1-a-b,a),(1-b,b)]
            eq(block_eta(top),1-2*F(a,b))
            eq(tau(top),1-2*(a*a+b*b))
            # Swap the two lengths, still right-packed.
            swap=[(1-a-b,b),(1-a,a)]
            eq((1-block_eta(top))-(1-block_eta(swap)),4*a*b*(a*a-b*b))
            # Moving both blocks strictly left cannot improve eta.
            if a+b<1:
                shift=Q(1,100)*(1-a-b)
                shifted=[(1-a-b-shift,a),(1-b-shift,b)]
                assert block_eta(shifted)<block_eta(top)
                checks+=1
            # For a+b=1, first branch in t matches the polynomial in z=b-a.
            if a+b==1:
                z=b-a
                eq(1-2*F(a,b),(1+z-3*z*z-z**3)/2)
                eq(tau(top),-z*z)
            # For one block length a, upper placement is optimal.
            eq(block_eta([(1-a,a)]),1-2*a**4)

# The transition parameters and the optimizer lengths obey
# a+b=1 exactly when s=s_star; no floating-point reliance.
for den in range(2,100):
    r=Q(1,den)
    z=(1-r)/(1+r)
    s2=(1+r*r)/(1+r)**2
    eq(s2,(1+z*z)/2)
    a=r/(1+r);b=1/(1+r)
    eq(a+b,Q(1));eq(a*a+b*b,s2)
    eq(1-2*F(a,b),(1+z-3*z*z-z**3)/2)

# Strict refinement of any finite packed increasing block family with spare length.
def packed_cost(lengths):
    return sum((a**4+2*a**3*sum(lengths[i+1:])
                for i,a in enumerate(lengths)),Q(0))
for k in range(1,8):
    for scale in range(k+1,k+17):
        v=[Q(i,scale*k*(k+1)) for i in range(1,k+1)]
        slack=1-sum(v)
        assert slack>0
        a=v[0]
        # Rational parametrization of a circle: c^2+d^2=a^2.
        tt=Q(1,100) * slack/(a+slack)
        c=a*2*tt/(1+tt*tt)
        d=a*(1-tt*tt)/(1+tt*tt)
        eq(c*c+d*d,a*a)
        assert c<d and c+d-a<slack
        checks+=1
        expanded=[c,d]+v[1:]
        old=packed_cost(v);new=packed_cost(expanded)
        eq(old-new, 2*c*c*d*(d-c)+2*sum(v[1:])*(a**3-c**3-d**3))
        assert old>new
        checks+=1

# All-block universal lower envelope for rational Pythagorean lengths.
# This is diagnostic; the all-count theorem follows from monotonic g(x)=2sqrt(x)-x.
for vec,denom in [([3,4],5), ([1,2,2],3), ([3,4,12],13)]:
    for scale in range(2,37):
        # Choose rational s small enough that the block lengths fit.
        ss=Q(denom,scale*sum(vec))
        blocks=[]
        for i,v in enumerate(vec):
            ell=ss*Q(v,denom)
            left=Q(0) if i==0 else sum((w for h,w in blocks),Q(0))
            blocks.append((left,ell))
        tt=tau(blocks)
        eq((1-tt)/2,ss*ss)
        lower=1-2*ss**3*(2-ss)
        assert block_eta(blocks)>lower
        checks+=1
        # Single block at the origin attains the exact lower bound.
        eq(block_eta([(Q(0),ss)]),lower)
        # Translation from origin to the right endpoint fills the one-block range.
        eq(block_eta([(1-ss,ss)]),1-2*ss**4)

print('PASS',checks,'exact rational and polynomial assertions')
