#!/usr/bin/env python3
"""Exact rational verification of cubic Legendre BV projection's global sharp gain.
Uses only the Python standard library; floating-point values are never used for the proof.
"""
from fractions import Fraction as F
from math import isqrt
from functools import reduce

# Polynomials stored in increasing order, exact rational coefficients.
def add(p,q):
    return [ (p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0)
             for i in range(max(len(p),len(q))) ]
def neg(p): return [-x for x in p]
def sub(p,q): return add(p,neg(q))
def mul(p,q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q): out[i+j]+=x*y
    return out
def powpoly(p,n):
    out=[F(1)]
    for _ in range(n): out=mul(out,p)
    return out

def bernstein_coeffs_at_1_16(p):
    # p(u)=sum a_k u^k; p(t/16)=sum b_i Binom(7,i)t^i(1-t)^(7-i)
    from math import comb
    n=len(p)-1
    return [sum(p[k]*F(1,16)**k*F(comb(i,k),comb(n,k)) for k in range(i+1))
            for i in range(n+1)]


def exact_legendre_kernel_identity():
    # Each list is the standard Legendre polynomial in ascending monomial order.
    P=[[F(1)],[F(0),F(1)],[F(-1,2),F(0),F(3,2)],
       [F(0),F(-3,2),F(0),F(5,2)],
       [F(3,8),F(0),F(-30,8),F(0),F(35,8)]]
    lhs={}
    for k in range(1,4):
        factor=sub(P[k-1],P[k+1])
        deriv=[i*P[k][i] for i in range(1,len(P[k]))]
        for i,a in enumerate(factor):
            for j,b in enumerate(deriv):
                lhs[i,j]=lhs.get((i,j),F(0))+a*b/2
    rhs={}
    pref=[F(15,32),F(0),F(-15,32)]
    terms=[(0,[F(3),F(0),F(-7)]),(1,[F(0),F(8)]),
           (2,[F(-7),F(0),F(35)])]
    for j,p in terms:
        product=mul(pref,p)
        for i,a in enumerate(product):
            rhs[i,j]=rhs.get((i,j),F(0))+a
    assert {k:v for k,v in lhs.items() if v}=={k:v for k,v in rhs.items() if v}
    print('LEGENDRE_STEP_KERNEL_POLYNOMIAL_IDENTITY_PASS')

def small_parameter_certificate():
    u=[F(0),F(1)]; one=[F(1)]
    A=sub(mul([F(35)],u),[F(7)])
    d=add(sub(mul([F(245)],powpoly(u,2)),mul([F(138)],u)),[F(21)])
    v=sub(mul([F(6)],u),mul([F(7)],powpoly(u,2)))
    # B= A^4 [108/7+v^2+(12/7)v*sqrt(21)]-4(1-u)^2*d^3.
    # Since v>=0 on [0,1/16] and sqrt(21)>4, B>=P below.
    P=sub(mul(powpoly(A,4),add(add([F(108,7)],powpoly(v,2)),mul([F(48,7)],v))),
          mul([F(4)],mul(powpoly(sub(one,u),2),powpoly(d,3))))
    assert P[0]==0 and len(P)==9
    b=bernstein_coeffs_at_1_16(P[1:])
    expected=[F(162288),F(504825,4),F(43471129,448),F(2112076241,28672),
              F(31610427257,573440),F(446693101541,11010048),
              F(61396126549,2097152),F(5533791782221,268435456)]
    assert b==expected and all(v>0 for v in b)
    print('SMALL_JUMP_PARAMETER_BERNSTEIN_CERTIFICATE_PASS',len(b))

def q_coeff(s):
    c=F(15,32)*(1-s*s)
    return (c*(35*s*s-7),c*(8*s),c*(3-7*s*s))

def square_root_bounds(d):
    assert d>=0
    scale=10**9
    k=isqrt((d.numerator*scale*scale)//d.denominator)
    lo,hi=F(k,scale),F(k+1,scale)
    assert lo*lo<=d<=hi*hi
    return lo,hi

def exact_abs_quadratic_upper(a,b,c):
    # Intervals guaranteed to contain every real zero in [-1,1].
    roots=[]
    if a:
        disc=b*b-4*a*c
        if disc>=0:
            sl,su=square_root_bounds(disc)
            for sign in [-1,1]:
                lo=min((-b+sign*sl)/(2*a),(-b+sign*su)/(2*a))
                hi=max((-b+sign*sl)/(2*a),(-b+sign*su)/(2*a))
                if lo<=1 and hi>=-1:
                    roots.append((max(F(-1),lo),min(F(1),hi)))
    elif b:
        r=-c/b
        if -1<=r<=1: roots.append((r,r))
    roots.sort()
    merged=[]
    for l,r in roots:
        if merged and l<=merged[-1][1]:merged[-1]=(merged[-1][0],max(merged[-1][1],r))
        else:merged.append((l,r))
    def Q(x):return a*x*x+b*x+c
    def primitive(x):return a*x**3/3+b*x*x/2+c*x
    total=F(0);left=F(-1)
    M=abs(a)+abs(b)+abs(c) # |Q(x)|<=M for |x|<=1.
    for l,r in merged+[(F(1),F(1))]:
        if left<l:
            m=(left+l)/2
            sign=1 if Q(m)>=0 else -1
            total+=sign*(primitive(l)-primitive(left))
        if l<r:total+=(r-l)*M
        left=r
    assert total>=0
    return total

def large_parameter_certificate():
    # 300 intervals of radius 1/800 cover [1/4,1].
    # |partial_s Q_s(x)| <= (15/32)*(56+16+8)=75/2,
    # so integral changes by at most 75/800=3/32 in each interval.
    maxU=F(0); arg=F(0)
    for j in range(300):
        s=F(1,4)+F(2*j+1,800)
        a,b,c=q_coeff(s)
        upper=exact_abs_quadratic_upper(a,b,c)
        if upper>maxU:maxU,arg=upper,s
        assert upper<F(17,10),('threshold failed',j,s,upper)
    assert F(17,10)+F(3,32)<F(9,5)
    print('LARGE_JUMP_PARAMETER_300_EXACT_RATIONAL_INTERVALS_PASS')
    print('MAX_RATIONAL_UPPER', maxU, 'AT',arg,'APPROX',float(maxU))
    print('GLOBAL_BOUND_STRICTLY_BELOW_CENTER_VALUE_PASS',F(17,10)+F(3,32))

if __name__=='__main__':
    exact_legendre_kernel_identity()
    small_parameter_certificate()
    large_parameter_certificate()
    print('CUBIC_LEGENDRE_VARIATION_PROJECTION_ALL_CHECKS_PASS')
