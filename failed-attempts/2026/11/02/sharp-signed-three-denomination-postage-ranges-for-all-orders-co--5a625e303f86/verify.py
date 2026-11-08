#!/usr/bin/env python3
"""Independent finite arithmetic checks for a sharp signed additive basis."""
from math import gcd

def check(b):
    assert b >= 2 and b % 2 == 0
    h = 6*b - 3
    x, y = 2*b, 3*b+1
    T = 9*b*b-3
    assert gcd(x,y)==1
    # Direct two-dimensional enumeration of the multiplicities in an h-fold sum.
    represented=set()
    for s in range(h+1):
        for t in range(h-s+1):
            represented.add(-h*b+s*x+t*y)
    assert all(n in represented for n in range(T+1)), b
    assert T+1 not in represented, b
    # Independent endpoint/residue-class certificate for the proposed closed form.
    rows={}
    for s in range(y):
        k=3*b-s
        S=-h*b+s*x
        E=S+(h-s)*y
        assert S==3*b-2*b*k
        assert E==T-3*b+(b+1)*k
        residue=S%y
        assert residue not in rows
        rows[residue]=(S,E)
    assert len(rows)==y
    for r,(S,E) in rows.items():
        first=r
        last=T-(T-r)%y
        assert S<=first and last<=E, (b,r,S,E,first,last)
    return h,T

if __name__=='__main__':
    for b in range(2,101,2):
        h,T=check(b)
        if b<=8:
            print(f"h={h}: exact construction reaches {T}")
    print("VERIFY_OK: 50 even parameters, direct and residue certificate checks")
