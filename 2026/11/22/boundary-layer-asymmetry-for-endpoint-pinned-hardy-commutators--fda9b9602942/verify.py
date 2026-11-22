#!/usr/bin/env python3
"""Rational interval checks for endpoint-pinned Hardy commutator example.
Requires Python 3 standard library only; see RESULT.md for analytic derivation.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from math import log

# Bound log(q), q > 0, by range reduction and positive atanh-series.
def log_bounds(q, terms=48):
    q=F(q)
    assert q>0
    k=0
    r=q
    while r>=2:
        r/=2;k+=1
    while r<1:
        r*=2;k-=1
    def zbound(x):
        z=(x-1)/(x+1)
        assert 0<=z<=F(1,3)
        partial=sum((2*z**(2*j+1)/F(2*j+1)) for j in range(terms))
        rem=2*z**(2*terms+1)/(F(2*terms+1)*(1-z*z))
        return partial,partial+rem
    lo,hi=zbound(r)
    l2,u2=zbound(F(2))
    if k>=0:return lo+k*l2,hi+k*u2
    return lo+k*u2,hi+k*l2

def add_interval(I,J):return I[0]+J[0],I[1]+J[1]
def scale_interval(I,c):return (c*I[0],c*I[1]) if c>=0 else (c*I[1],c*I[0])

def energy(a):
    a=F(a)
    if a==0 or a==F(1,2):
        return add_interval((F(5,12),F(5,12)),scale_interval(log_bounds(2),-F(1,2)))
    # E=5/12-a²+a/2+2a² log a+(-2a²+2a+1/2) log(a+1/2)
    const=F(5,12)-a*a+a/2
    I=(const,const)
    I=add_interval(I,scale_interval(log_bounds(a),2*a*a))
    I=add_interval(I,scale_interval(log_bounds(a+F(1,2)),-2*a*a+2*a+F(1,2)))
    return I

def energy_prime(a):
    a=F(a)
    if a==0 or a==F(1,2):
        return add_interval((F(3,2),F(3,2)),scale_interval(log_bounds(2),-2))
    # E'=7/2-2a+4a log a+(2-4a) log(a+1/2)-1/(a+1/2)
    const=F(7,2)-2*a-1/(a+F(1,2))
    I=(const,const)
    I=add_interval(I,scale_interval(log_bounds(a),4*a))
    I=add_interval(I,scale_interval(log_bounds(a+F(1,2)),2-4*a))
    return I

def pretty(I,digits=18):
    with localcontext() as ctx:
        ctx.prec=50
        return tuple(format(Decimal(v.numerator)/Decimal(v.denominator),f'.{digits}g') for v in I)

if __name__=='__main__':
    baseline=energy(F(0))
    candidate=energy(F(1,64))
    assert candidate[0]>baseline[1]
    print('TENT_EXACT_HS_SQUARE',pretty(baseline))
    print('RATIONAL_SHIFTED_WITNESS_HS_SQUARE',pretty(candidate))
    print('RATIONAL_STRICT_IMPROVEMENT',pretty((candidate[0]-baseline[1], candidate[1]-baseline[0])))
    for a,positive in ((F(0),True),(F(1,100),True),(F(1,64),False),(F(1,2),True)):
        interval=energy_prime(a)
        assert (interval[0]>0) if positive else (interval[1]<0)
        print('DERIVATIVE_SIGN_CERTIFICATE',str(a),'positive' if positive else 'negative',pretty(interval))
    # E'''=-4(4a²+4a-1)/(a(2a+1)³); its unique sign change
    # on (0,1/2) is at (sqrt(2)-1)/2. Therefore E'' increases then
    # decreases, starts at -infinity, ends at 3-4log(2)>0.
    ln2=log_bounds(2)
    assert F(3)-4*ln2[1]>0
    print('UNIQUE_INTERIOR_MAXIMUM_STRUCTURE_PASS')
    # Refined certified bracket for critical point.
    L=F(1,100);R=F(1,64)
    for _ in range(65):
        mid=(L+R)/2
        I=energy_prime(mid)
        if I[0]>0:L=mid
        elif I[1]<0:R=mid
        else:raise AssertionError('log interval too wide')
    print('UNIQUE_MAXIMIZING_SHIFT_BRACKET',pretty((L,R)))
    print('MAXIMUM_HS_SQUARE_BRACKET',pretty((energy(L)[0],energy(R)[1])))
    # Basic numerical quadrature in original kernel, independent from formula.
    def g(x,a):
        if x<a:return -x
        if x<a+.5:return x-2*a
        return 1-x
    import random
    random.seed(18)
    a=F(1,64)
    for a in (F(0),F(1,64),F(1,16)):
        aa=float(a)
        N=1000
        # midpoint quadrature on triangle with t midpoint of x subintervals
        total=0.
        for i in range(N):
            x=(i+.5)/N
            s=0.
            for j in range(i+1):
                t=(j+.5)*x/(i+1)
                s+=(g(x,aa)-g(t,aa))**2
            total+=s/(i+1)/x
        total/=N
        exact=energy(a)
        xx=float((exact[0]+exact[1])/2)
        assert abs(total-xx)<.001, (a,total,xx)
    print('INDEPENDENT_DIRECT_KERNEL_QUADRATURE_PASS')
    print('ALL_ENDPOINT_PINNED_HARDY_CERTIFICATES_PASS')
