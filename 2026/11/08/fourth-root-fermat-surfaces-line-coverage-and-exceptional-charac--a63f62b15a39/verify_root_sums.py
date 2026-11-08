#!/usr/bin/env python3
"""An independent exhaustive audit of short fourth-root sums.

Enumerates every word of length up to four in {0, +/-1, +/-i}
over F_p or F_{p^2}. Checks the support counts used to compute
points on the Fermat surface of degree (q-1)/4. Standard library only.
"""
from itertools import product
from collections import Counter


def short_sums(p):
    # Gaussian-integer arithmetic, reduced modulo p. This works for
    # both split and nonsplit fourth roots, except that when p=1 mod4
    # an extra evaluation i -> a in Fp is necessary.
    def add(a,b): return ((a[0]+b[0])%p,(a[1]+b[1])%p)
    roots=[(0,0),(1,0),((-1)%p,0),(0,1),(0,(-1)%p)]
    if p%4==1:
        i=next(t for t in range(p) if (t*t+1)%p==0)
        eq=lambda a:(a[0]+i*a[1])%p==0
    else: eq=lambda a:a==(0,0)
    counts=Counter()
    for y in product(roots,repeat=4):
        z=(0,0)
        for a in y:z=add(z,a)
        if eq(z) and y != ((0,0),)*4:counts[sum(a!=(0,0) for a in y)]+=1
    expected={3:Counter({2:24,3:16,4:36}),
              5:Counter({2:24,3:48,4:52})}.get(p,Counter({2:24,4:36}))
    assert counts==expected,(p,counts,expected)
    return dict(sorted(counts.items()))


def norm_control():
    norms={a*a+b*b for a in range(-4,5) for b in range(-4,5)
           if 0<abs(a)+abs(b)<=4}
    assert norms=={1,2,4,5,8,9,10,16},norms
    return norms


def closed_form(p,d):
    c=short_sums(p)
    N=sum(c[t]*d**t for t in c)//(4*d)
    U=9*d**3+6*d
    assert sum(c[t]*d**t for t in c)%(4*d)==0
    off={3:4*d*d,5:4*d**3+12*d*d}.get(p,0)
    assert N-U==off
    return N,U,off

if __name__=='__main__':
    print('Possible nonzero short Gaussian norms:', sorted(norm_control()))
    for p in (3,5,7,11,13,17,19,29,37,41,43,53,61,73):
        print('characteristic',p,'root-quadruple-support',short_sums(p))
    for p,d in [(3,2),(3,20),(5,6),(5,156),(7,12),(13,3),(17,4),(29,7),(37,9)]:
        print('p,d',p,d,'surface,union,off',closed_form(p,d))
    print('VERIFY_ROOT_SUMS_OK')
