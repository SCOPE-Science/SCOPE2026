#!/usr/bin/env python3
"""Construct exact palindrome witnesses at arbitrarily large integer centers."""
from verify_profiles import val,prediction

def profile(q,c,h):
    cc=str(val(c)%q)
    for t in range(1,h+1):
        a=val(c-t)%q; b=val(c+t)%q
        if a!=b: return None
        cc=str(a)+cc+str(b)
    return cc

if __name__=='__main__':
    checks=0
    for q in range(3,17):
        m=1+(1<<(q+1))
        for k in range(0,11):
            hs={1<<k,(1<<(k+1))-1}
            if k:
                hs|={3*(1<<(k-1))-1,3*(1<<(k-1))}
            for h in sorted(hs):
                produced=set()
                for r in range(k+1,k+q+1):
                    w=profile(q,1<<r,h)
                    assert w is not None
                    produced.add(w)
                w=profile(q,(1<<k)*m,h)
                assert w is not None
                produced.add(w)
                if k>=1 and h<3*(1<<(k-1)):
                    w=profile(q,(1<<(k-1))*m,h)
                    assert w is not None
                    produced.add(w)
                assert len(produced)==prediction(q,2*h+1),(q,k,h,len(produced))
                checks+=1
    print('PASS',checks,'constructive profiles for q=3..16, dyadic lengths and switch boundaries')
