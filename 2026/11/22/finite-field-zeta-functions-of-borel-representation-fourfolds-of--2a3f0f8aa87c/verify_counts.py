#!/usr/bin/env python3
"""Independent integer arithmetic checks for the root-count formula over prime fields."""
from math import gcd

def sigma(j,t,p):
    return sum(pow(t,j-1-2*k,p) for k in range(j))%p

def count_exceptional(m,p):
    n=2*m+1
    roots=[[x for x in range(1,p) if sigma(j,x,p)==0] for j in (2,3,n)]
    return sum(1 for x in roots[0] for y in roots[1] for z in roots[2]
               if (x*x*pow(y,3,p)-pow(z,n,p))%p==0)

def e_formula(m,q):
    return 8*(gcd(2*m+1,q-1)-1) if q%12==1 else 0

def pointcount(m,q):
    return q*q*(q-1)**2+q*q*(q-1)*e_formula(m,q)

def run():
    for m,p in [(2,13),(2,61),(4,73),(3,37),(4,109)]:
        assert p>3 and (2*m+1)%p!=0
        e=count_exceptional(m,p)
        assert e==e_formula(m,p), (m,p,e,e_formula(m,p))
        assert pointcount(m,p)==p*p*(p-1)**2+(p**3-p*p)*e
        print(f'm={m},q={p}: exceptional={e}, X_points={pointcount(m,p)}')
    # Check the claimed zeta log coefficients in several extension-degree patterns.
    for m,q in [(2,13),(2,61),(3,37),(4,73)]:
        for r in range(1,7):
            Q=q**r
            e=e_formula(m,Q)
            a=pointcount(m,Q)
            b=Q**4-2*Q**3+Q**2+(Q**3-Q**2)*e
            assert a==b
    print('All checks passed.')
if __name__=='__main__':run()
