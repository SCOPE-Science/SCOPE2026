#!/usr/bin/env python3
"""Independent finite metric-diagram enumeration for even-diameter equilateral-base pair counts."""
from itertools import product


def tri(a,b,c):
    return abs(a-b) <= c <= a+b


def exact_count(h, n, s):
    # Independent brute-force enumeration of two distance vectors.
    diameter=2*h
    good=[]
    for v in product(range(1,diameter+1), repeat=n):
        if all(tri(v[i],v[j],diameter) for i in range(n) for j in range(i+1,n)):
            good.append(v)
    return sum(all(tri(x[i],y[i],s) for i in range(n)) for x in good for y in good)


def decomposition(h,n,s):
    # Separate zero, one and two exceptional coordinates without enumerating vectors.
    safe=range(h,2*h+1)
    low=range(1,h)
    k=lambda a,b:int(tri(a,b,s))
    z=sum(k(a,b) for a in safe for b in safe)
    one=0; same=0; distinct=0
    for t in low:
        a=sum(k(t,b) for b in safe)
        b=sum(k(x,y) for x in range(2*h-t,2*h+1) for y in safe)
        one += 2*n*a*b**(n-1)
        for u in low:
            c=sum(k(x,y) for x in range(2*h-t,2*h+1)
                                for y in range(2*h-u,2*h+1))
            same += n*k(t,u)*c**(n-1)
            if n>=2:
                e=sum(k(t,y) for y in range(2*h-u,2*h+1))
                f=sum(k(x,u) for x in range(2*h-t,2*h+1))
                distinct += n*(n-1)*e*f*c**(n-2)
    return z**n+one+same+distinct


def upper_closed(h,n,s):
    assert h<=s<=2*h
    low=range(1,h)
    c=lambda t:sum(tri(t,b,s) for b in range(h,2*h+1))
    e=lambda t,u:sum(tri(t,b,s) for b in range(2*h-u,2*h+1))
    base=(h+1)**(2*n)
    one=2*n*sum(c(t)*((t+1)*(h+1))**(n-1) for t in low)
    same=n*sum((t+u>=s)*((t+1)*(u+1))**(n-1) for t in low for u in low)
    distinct=(n*(n-1)*sum(e(t,u)*e(u,t)*((t+1)*(u+1))**(n-2) for t in low for u in low) if n>=2 else 0)
    return base+one+same+distinct


def endpoint_difference(h,n):
    result=0
    for t in range(1,h):
        for u in range(1,h):
            p=(t+1)*(u+1)
            q=max(0,t+u-h+1)
            d=(min(t,u)+1)**2-q*q
            if t+u>=h:
                result+=n*p**(n-1)
            if n>=2:
                result-=n*(n-1)*d*p**(n-2)
    return result

if __name__=='__main__':
    checks=0
    for h,nmax in [(2,4),(3,3),(4,3),(5,2)]:
        for n in range(1,nmax+1):
            for s in range(1,2*h+1):
                got=exact_count(h,n,s)
                assert got==decomposition(h,n,s),(h,n,s,got,decomposition(h,n,s))
                if s>=h:
                    assert got==upper_closed(h,n,s),(h,n,s,'closed')
                checks+=1
    print('DIRECT_METRIC_DIAGRAM_CHECKS',checks)
    for h in range(2,13):
        for n in range(1,7):
            assert upper_closed(h,n,h)-upper_closed(h,n,2*h)==endpoint_difference(h,n)
            if n==1: assert endpoint_difference(h,n)==h*(h-1)//2
            if n>=h+1:assert endpoint_difference(h,n)<0
    print('FINITE_ENDPOINT_IDENTITY_CHECKS',sum(6 for h in range(2,13)))
    for n in range(1,10):
        t1=7**n+2*n*5**(n-1)+n*4**(n-1)
        t2=9**n+4*n*6**(n-1)+n*4**(n-1)+(n*(n-1)*4**(n-2) if n>1 else 0)
        t3=9**n+6*n*6**(n-1)+n*(n-1)*4**(n-1)
        t4=9**n+4*n*6**(n-1)+n*(n-1)*4**(n-1)
        assert [t1,t2,t3,t4]==[decomposition(2,n,s) for s in range(1,5)]
        if n>=2: assert t4-t2==n*(3*n-7)*4**(n-2)
    print('DIAMETER_FOUR_CLOSED_FORMS_OK')
    print('ALL_METRIC_TYPE_CHECKS_PASS')
