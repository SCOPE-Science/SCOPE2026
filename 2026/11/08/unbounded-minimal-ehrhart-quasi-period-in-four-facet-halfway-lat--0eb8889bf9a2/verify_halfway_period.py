#!/usr/bin/env python3
"""Independent integer enumeration for rational halfway-lattice parallelograms.
The analytic argument covers every odd q; these finite checks are supplemental.
"""
from fractions import Fraction

def direct_count(q,t):
    # Integer x in [-t/2,t/2], and y bounded by |x+q*y|<=t/2.
    s=0
    for x in range(-t//2-1,t//2+2):
        if 2*abs(x)>t: continue
        for y in range(-(t+2*q)//q-3,(t+2*q)//q+4):
            if 2*abs(x+q*y)<=t:s+=1
    return s

def closed_form(q,t):
    N=t + (1 if t%2==0 else 0)
    a,r=divmod(N,q)
    return (q-r)*a*a+r*(a+1)**2

def constituent(q,residue):
    # P_r(t) = (t+delta)^2/q + r0(q-r0)/q.
    delta=1 if residue%2==0 else 0
    mod=(residue+delta)%q
    return (Fraction(1,q),Fraction(2*delta,q),Fraction(delta*delta+mod*(q-mod),q))

def main():
    cnt=0
    for q in range(3,28,2):
        for t in range(0,94):
            d=direct_count(q,t)
            f=closed_form(q,t)
            assert d==f,(q,t,d,f)
            cnt+=1
        # certificate of minimality: among the 2q constituent polynomials,
        # test that NO proper divisor period is compatible with all coefficients.
        P=[constituent(q,r) for r in range(2*q)]
        for p in range(1,2*q):
            if (2*q)%p == 0:
                assert any(P[r]!=P[(r+p)%(2*q)] for r in range(2*q)),(q,p)
        assert all(P[r]==P[(r+2*q)%(2*q)] for r in range(2*q))
    print(f'PASS: {cnt} exact lattice enumerations, 13 families, proper-period constituent comparisons')
if __name__=='__main__':main()
