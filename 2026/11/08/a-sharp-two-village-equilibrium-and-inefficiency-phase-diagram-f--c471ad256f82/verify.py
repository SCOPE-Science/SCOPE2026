#!/usr/bin/env python3
"""Exact independent enumeration for two-site equal-cost facility choice."""
from fractions import Fraction as Q
from itertools import product


def equilibrium(profile,m,C,d):
    n=2*m
    loads=[profile.count(0),profile.count(1)]
    for i,s in enumerate(profile):
        x=0 if i<m else 1
        own=(d if x!=s else Q(0))+C/loads[s]
        target=1-s
        other=(d if x!=target else Q(0))+C/(loads[target]+1)
        if own>other:
            return False
    return True


def social(profile,m,C,d):
    loads=[profile.count(0),profile.count(1)]
    opening=C*sum(k>0 for k in loads)
    distance=d*sum((0 if i<m else 1)!=profile[i] for i in range(2*m))
    return opening+distance


def predicted(profile,m,C,d):
    L=C/Q(m*(m+1)); U=C*(1-Q(1,2*m))
    return (profile==(0,)*(2*m) and d<=U) or (profile==(1,)*(2*m) and d<=U) or (profile==(0,)*m+(1,)*m and d>=L)


def verify():
    cnt=0
    for m in range(1,6):
        for C in (Q(1),Q(7,5)):
            L=C/(m*(m+1)); U=C*(1-Q(1,2*m))
            ds=sorted({Q(1,100), L/2,L, (L+U)/2, U, U+Q(1,100), C/m, C/m+Q(1,100), Q(2)*C})
            for d in ds:
                outcomes=[p for p in product((0,1), repeat=2*m) if equilibrium(p,m,C,d)]
                expected=[p for p in product((0,1), repeat=2*m) if predicted(p,m,C,d)]
                assert outcomes==expected,(m,C,d,outcomes,expected)
                best=min(social(p,m,C,d) for p in product((0,1), repeat=2*m))
                assert best==min(C+m*d,2*C),(m,C,d,best)
                poa=max(social(p,m,C,d) for p in outcomes)/best
                # evaluate the worst candidate across all equal-mass profiles
                target=max((C+m*d if d<=U else Q(0)), (2*C if d>=L else Q(0)))/best
                assert poa==target
                cnt+=2**(2*m)
    print('PASSED all candidate PNE and optimality checks across',cnt,'labeled allocations')
    for m in range(1,8):
        C=Q(1);L=C/(m*(m+1));U=C*(1-Q(1,2*m))
        zL=(2*C)/(C+m*L)
        zU=(C+m*U)/min(C+m*U,2*C)
        sharp=max(zL,zU)
        expected=Q(4,3) if m==1 else Q(3,2) if m==2 else Q(2*m+1,4)
        assert sharp==expected,(m,sharp,expected)
        print('m=',m,'thresholds=',L,U,'sharpPoA=',sharp)

if __name__=='__main__':verify()
