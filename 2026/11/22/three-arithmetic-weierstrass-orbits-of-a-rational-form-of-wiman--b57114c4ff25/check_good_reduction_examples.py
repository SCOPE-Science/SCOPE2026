#!/usr/bin/env python3
"""Finite-field sanity checks of the forty distinguished branch points.

These are finite reduction examples, NOT a proof of the characteristic-zero
Galois classification or of canonical Weierstrass behavior in finite fields.
"""

def root_n(p,n):
    for x in range(2,p):
        if pow(x,n,p)==1 and all(pow(x,d,p)!=1 for d in range(1,n) if n%d==0):
            return x
    raise AssertionError

def sqroot(p,n):
    return next((x for x in range(p) if (x*x-n)%p==0),None)

def quadrics(x,p):
    a,b,c,d,e=x
    return ((a*a+2*b*e+2*c*d)%p,
            (c*c+2*a*e+2*b*d)%p,
            (e*e+2*a*d+2*b*c)%p)

for p in (11,31,41,61,101,181):
    z=root_n(p,5)
    ph=(1+z+pow(z,4,p))%p
    i=sqroot(p,-1)
    s=sqroot(p,ph)
    pts=set()
    if i is not None and s is not None:
        r2=i*pow(z,2,p)*s%p
        r3=pow(z,4,p)*s%p
        r4=i*z%p
        for a in range(5):
            for e2 in (1,-1):
                for e3 in (1,-1):
                    for e4 in (1,-1):
                        v=[0]*5
                        for d,r in ((1,1),(2,e2*r2),(3,e3*r3),(4,e4*r4)):
                            v[(a+d)%5]=r%p
                        x=[sum(pow(z,(-j*k)%5,p)*v[j] for j in range(5))*pow(5,-1,p)%p for k in range(5)]
                        assert quadrics(x,p)==(0,0,0)
                        assert any(x)
                        pts.add(tuple(x))
    assert len(pts) in (0,40)
    print('p=',p,'split_support=',len(pts))
assert len(pts) == 40 # final test prime 181, splits completely
print('GOOD_REDUCTION_EXAMPLES_OK')
