#!/usr/bin/env python3
"""Reproducibility checks for an independent equal-pulse founding model.

This program tests examples and identities; the accompanying proof establishes
universal claims. Requires only Python's standard library.
"""
import math
from decimal import Decimal, getcontext


def p_two(x):
    return -math.expm1(-x) - x * math.exp(-x)


def q(x, s):
    return 1 - s * p_two(x)


def ell(x, s):
    return -math.log1p(-s * p_two(x))


def d_ell(x, s):
    return s * x * math.exp(-x) / q(x, s)


def d2_ell(x, s):
    ex = math.exp(-x)
    return s * ex * ((1-s)*(1-x)+s*ex) / q(x, s)**2


def N(x, s):
    return x*d_ell(x, s)-ell(x, s)


def bisect(g, lo, hi, steps=100):
    vlo = g(lo)
    vhi = g(hi)
    assert vlo*vhi < 0, (lo, hi, vlo, vhi)
    for _ in range(steps):
        mid=(lo+hi)/2
        vm=g(mid)
        if vm == 0:
            return mid
        if vlo*vm>0:
            lo, vlo=mid,vm
        else:
            hi,vhi=mid,vm
    return (lo+hi)/2


def xi(s):
    assert 0<s<1
    lo=1.0
    hi=4.0
    while N(hi,s)>=0:
        hi*=2
        assert hi<1e8
    return bisect(lambda x:N(x,s), lo, hi)


def rate(m, B, s):
    return m*ell(B/m,s)


def threshold(m,s):
    x=xi(s)
    return bisect(lambda B: rate(m+1,B,s)-rate(m,B,s),m*x,(m+1)*x)


def compare_precision():
    getcontext().prec=58
    D=Decimal
    e=D(1).exp()
    for s in (D('0.1'),D('0.5'),D('0.9')):
        for x in (D('0.25'),D('1'),D('3'),D('7')):
            Q=D(1)-s+s*(D(1)+x)*(-x).exp()
            v=float(-Q.ln())
            assert abs(ell(float(x),float(s))-v)<4e-15


def main():
    tests=0
    compare_precision();tests+=12
    ss=(0.01,0.1,0.5,0.75,0.9,0.99)
    for s in ss:
        x=xi(s)
        assert 1<x and abs(N(x,s))<1e-11
        tests+=2
        for a in (0.08,0.2,0.5,0.99):
            assert N(a*x,s)>0
            tests+=1
        for a in (1.01,1.5,2,4):
            assert N(a*x,s)<0
            tests+=1
        for t in (0.1,0.5,1,2,4,8,12):
            h=1e-3
            numerical=(ell(t+h,s)-2*ell(t,s)+ell(t-h,s))/(h*h)
            assert abs(numerical-d2_ell(t,s))<1e-6, (s,t,numerical,d2_ell(t,s))
            tests+=1
        prev=0
        for m in range(1,26):
            th=threshold(m,s)
            assert m*x<th<(m+1)*x
            assert th>prev
            assert abs(rate(m,th,s)-rate(m+1,th,s))<1e-10
            prev=th;tests+=3
            for B in (th-0.0001,th+0.0001):
                signs=rate(m+1,B,s)-rate(m,B,s)
                assert (signs<0 if B<th else signs>0), (m,s,B,signs)
                tests+=1
        for B in (0.1,0.9,2,4,8,15,30,60,100):
            mid=B/x
            cands={max(1,math.floor(mid)),max(1,math.ceil(mid))}
            selected=max(cands,key=lambda m:rate(m,B,s))
            brute=max(range(1,max(150,round(2*mid)+10)),key=lambda m:rate(m,B,s))
            assert selected==brute, (s,B,selected,brute)
            tests+=1
        for t in (0.1,0.5,1,1.5,2,3,8):
            B=2*t
            D=(1-q(t,s)**2)-(1-q(2*t,s))
            closed=s*math.exp(-2*t)*((1-s)*(math.exp(t)-1-t)**2-t*t)
            assert abs(D-closed)<1e-12
            tests+=1
    s=0.5
    assert abs(xi(s)-2.2424270968135293)<1e-11
    assert abs(threshold(1,s)-3.1262514854817884)<1e-11
    assert abs(threshold(2,s)-5.4654815936445234)<1e-11
    tests+=3
    print('PASS',tests,'numerical identities, signs, adjacencies, thresholds and brute-force comparisons')
    print('s=0.5 xi=',format(xi(.5),'.14f'),'B1=',format(threshold(1,.5),'.14f'),'B2=',format(threshold(2,.5),'.14f'))

if __name__=='__main__':
    main()
