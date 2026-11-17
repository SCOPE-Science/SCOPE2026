#!/usr/bin/env python3
"""Finite numerical corroboration of a bounded-past cubic repeller formula."""
import math

def H(h,x):
    return (1-h)*x+h*x*x*x

def bisect_branch(h,y,which):
    c=math.sqrt((h-1)/(3*h))
    if which==-1: left,right=-1.,-c; increasing=True
    elif which==0: left,right=-c,c; increasing=False
    else: left,right=c,1.; increasing=True
    for _ in range(90):
        mid=(left+right)/2
        if (H(h,mid)<y)==increasing: left=mid
        else: right=mid
    return (left+right)/2

def root(h,eps):
    L=math.log(h)
    def f(s):return -L*s+math.log1p(2*math.exp(-math.log(2)*s))+eps*s
    lo,hi=0.,1.
    for _ in range(100):
        mid=(lo+hi)/2
        if f(mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

def main():
    samples=0
    for h in (64,65,80,128,256,1024,4096):
        a=math.sqrt(1-1/h)
        eps=16/h
        for y in (-1.,-0.75,-0.2,0.,0.4,0.9,1.):
            br=[bisect_branch(h,y,i) for i in (-1,0,1)]
            assert br[0]<br[1]<br[2]
            for i,x in zip((-1,0,1),br):
                assert abs(H(h,x)-y)<2e-10
                assert abs(x)<1.0000001
                if i==0:
                    assert abs(x)<=2/h+1e-10
                    p=1/h
                else:
                    assert abs(abs(x)-a)<=2/h+1e-10
                    p=1/(2*h)
                derivative=abs((1-h)+3*h*x*x)
                assert abs(math.log((1/derivative)/p))<=eps+1e-10
                samples+=1
        lo,mid,hi=root(h,-eps),root(h,0),root(h,eps)
        assert 0<lo<mid<hi<1
        assert hi-mid<0.04
    # Exact critical polynomial identity: 4(h-1)^3-27h=(h-4)(2h+1)^2.
    for h in range(-9,100):
        assert 4*(h-1)**3-27*h==(h-4)*(2*h+1)**2
    for h in (10**4,10**6,10**8,10**10):
        L=math.log(h); A=math.log(3); C=math.log(2)
        third=A/L-2*C*A/(3*L*L)+(C*C*A*(4+A))/(9*L**3)
        assert abs(third-root(h,0))<10/L**4
    print(f"VERIFY_OK branch_residual_and_log_slope={samples} critical_factorizations=109 dimension_root_checks=7 third_term_checks=4")
if __name__=='__main__': main()
