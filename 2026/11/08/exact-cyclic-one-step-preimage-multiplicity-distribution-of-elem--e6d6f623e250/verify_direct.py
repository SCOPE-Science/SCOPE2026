#!/usr/bin/env python3
"""Independent direct indexed-ring image enumeration; not an infinite proof."""
from collections import Counter

def image(x,n):
    y=0
    for i in range(n):
        a=(x>>((i-1)%n))&1
        b=(x>>i)&1
        c=(x>>((i+1)%n))&1
        y|=(a^(b|c))<<i
    return y

def run():
    s=[3,1,1]
    for n in range(3,17): s.append(s[-1]+2*s[-3])
    for n in range(1,17):
        hist=Counter(image(x,n) for x in range(1<<n))
        sizes=Counter(hist.values())
        sizes[0]=(1<<n)-len(hist)
        d=int(n%3==0)
        target={0:(1+s[n]-2*d)//2,1:2**n-1-s[n]+3*d,2:(1+s[n]-6*d)//2,3:d}
        assert all(sizes.get(k,0)==v for k,v in target.items())
        assert all(k<=3 for k in sizes)
        if d: assert [y for y,v in hist.items() if v==3]==[(1<<n)-1]
    print('DIRECT_VERIFY_OK n=1..16')
if __name__=='__main__':run()
