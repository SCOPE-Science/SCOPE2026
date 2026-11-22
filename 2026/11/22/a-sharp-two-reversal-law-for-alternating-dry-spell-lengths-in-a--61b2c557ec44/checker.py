#!/usr/bin/env python3
"""Reproduce independent numerical diagnostics for a two-stage dry-spell pulse model.

This is a finite numerical diagnostic, not a replacement for the analytic proof.
Uses only the Python standard library and deterministic input grids.
"""
import math

def G1(x):
    return -math.expm1(-x)

def G2(x):
    return -math.expm1(-x) - x * math.exp(-x)

def F(t, a, b, stages=2):
    return math.exp(-b*t) * (G1(a*t) if stages == 1 else G2(a*t))

def gap(m, d, a, b, stages=2):
    return F(m-d, a, b, stages)+F(m+d, a, b, stages)-2*F(m, a, b, stages)

def factored_gap(m,d,a,b,stages=2):
    B=math.cosh(b*d)-1
    C=math.cosh((a+b)*d)-1
    if stages==1:
        H=math.exp(-a*m)*C
    else:
        H=math.exp(-a*m)*((1+a*m)*C-a*d*math.sinh((a+b)*d))
    return 2*math.exp(-b*m)*(B-H)

def bisect(fn, lo, hi, increasing=True, steps=100):
    ylo=fn(lo)
    yhi=fn(hi)
    if increasing:
        assert ylo <= 0 and yhi >= 0, (lo,hi,ylo,yhi)
    else:
        assert ylo >= 0 and yhi <= 0, (lo,hi,ylo,yhi)
    for _ in range(steps):
        mid=(lo+hi)/2
        val=fn(mid)
        if ((val<0)==increasing): lo=mid
        else: hi=mid
    return (lo+hi)/2

def critical_delta(a,b):
    # Ratio F(2d)/F(d) strictly decreases from 4 to 0.
    ratio=lambda d:F(2*d,a,b)/F(d,a,b)
    lo=0.00001/a
    hi=10/a
    assert ratio(lo)>2 and ratio(hi)<2
    return bisect(lambda d:ratio(d)-2,lo,hi,increasing=False)

def test():
    count=0
    for a in [0.3,0.8,1.,2.7,9.0]:
        for b in [0.17,0.6,1.,4.4]:
            dc=critical_delta(a,b);count+=2
            for ratio in [.09,.45,.99,1.01,1.4,2.6]:
                d=dc*ratio
                c=a+b
                B=math.cosh(b*d)-1
                C=math.cosh(c*d)-1
                s=math.sinh(c*d)
                ms=d*s/C
                assert ms>d;count+=1
                H=lambda m: math.exp(-a*m)*((1+a*m)*C-a*d*s)
                assert H(ms)>B;count+=1
                for m in [d, (d+ms)/2, ms, ms+1/c, ms+6/c]:
                    lhs=gap(m,d,a,b)
                    rhs=factored_gap(m,d,a,b)
                    assert abs(lhs-rhs)<1e-10*max(1,abs(lhs),abs(rhs)),(a,b,d,m,lhs,rhs)
                    count+=1
                # H grows strictly before ms and decreases after, independent of parameter ratio.
                assert H((d+ms)/2)<H(ms) and H(ms+1/c)<H(ms);count+=2
                hi=ms+1/c
                while H(hi)>B: hi=ms+2*(hi-ms)
                upper=bisect(lambda m:B-H(m),ms,hi,True)
                assert upper>ms;count+=1
                if d<dc:
                    lower=bisect(lambda m:B-H(m),d,ms,False)
                    assert d<lower<ms<upper;count+=1
                    for m,sgn in [((d+lower)/2,1),((lower+ms)/2,-1),((ms+upper)/2,-1),(upper+1/c,1)]:
                        assert gap(m,d,a,b)*sgn>0,(a,b,d,m)
                        count+=1
                else:
                    assert gap((d+ms)/2,d,a,b)<0 and gap(upper+1/c,d,a,b)>0
                    count+=2
                # For one maturation stage the same comparison always crosses once.
                m1=math.log(C/B)/a
                assert m1>d;count+=1
                assert gap((m1+d)/2,d,a,b,1)<0 and gap(m1+1/c,d,a,b,1)>0
                count+=2
                for m in [d,ms,m1,m1+1/c]:
                    q=gap(m,d,a,b,1)
                    r=factored_gap(m,d,a,b,1)
                    assert abs(q-r)<1e-10*max(1,abs(q),abs(r));count+=1
    d=critical_delta(1.,1.)
    assert abs(d-0.4253049120032362)<1e-12;count+=1
    for m,expect in [(0.25,1),(1.,-1),(3.,1)]:
        assert gap(m,.2,1.,1.)*expect>0;count+=1
    print('PASS: %d deterministic numerical assertions' % count)
    print('a=b=1 critical delta = %.15f' % d)
    for m in [.25,1.,3.]:
        p=F(m,1.,1.)/m
        q=(F(m-.2,1.,1.)+F(m+.2,1.,1.))/(2*m)
        print('m=%g periodic=%.12f alternating=%.12f fractional_difference=%+.9f'% (m,p,q,q/p-1))

if __name__=='__main__': test()
