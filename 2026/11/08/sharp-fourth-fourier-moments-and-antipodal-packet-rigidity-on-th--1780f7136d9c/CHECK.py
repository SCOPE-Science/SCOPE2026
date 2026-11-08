#!/usr/bin/env python3
"""Exact coefficient-convolution checks for prime-square modular hyperbola extension."""
from collections import defaultdict
from itertools import product
import math
import cmath


def check_prime(p):
    n = p*p
    units = [x for x in range(n) if x % p]
    inv = {x: pow(x, -1, n) for x in units}

    def fourth(a):
        conv = defaultdict(complex)
        for x in units:
            for y in units:
                conv[((x+y)%n,(inv[x]+inv[y])%n)] += a[x]*a[y]
        return sum(abs(z)**2 for z in conv.values())

    def structural(a):
        blocks = {r:[a[(r+p*k)%n] for k in range(p)] for r in range(1,p)}
        t = {r:sum(abs(v)**2 for v in blocks[r]) for r in blocks}
        def cyclic(u,v):
            return [sum(u[k]*v[(s-k)%p] for k in range(p)) for s in range(p)]
        sam = sum(sum(abs(v)**2 for v in cyclic(blocks[r],blocks[r])) for r in blocks)
        antip = [cyclic(blocks[r], blocks[p-r]) for r in range(1,(p+1)//2)]
        opp = 4 * (sum(sum(abs(v)**2 for v in c[:-1]) for c in antip) + abs(sum(c[-1] for c in antip))**2)
        cross = 4*sum(t[r]*t[s] for r in range(1,p) for s in range(r+1,p) if r+s != p)
        return sam+opp+cross

    patterns = []
    patterns.append({x:1 for x in units})
    patterns.append({x:complex((x*13 + x*x*3 + p) % 7-3,(x*x+2*x) % 5-2) for x in units})
    patterns.append({x:complex((x*5+1)%3-1,(x*x+2)%3-1) for x in units})
    for r in range(1,(p+1)//2):
        pattern = {x:0 for x in units}
        for k in range(p):
            pattern[r+p*k] = 1
            pattern[(-r+p*k)%n] = 1
        patterns.append(pattern)
    for ix, pat in enumerate(patterns):
        m=fourth(pat)
        st=structural(pat)
        assert abs(m-st)<1.e-7,(p,m,st)
        s=sum(abs(z)**2 for z in pat.values())
        assert m <= (3*p/2)*s*s+1.e-6,(p,m,s)
        if p in (3,5) and ix==1:
            avg = sum(abs(sum(pat[x]*cmath.exp(2j*math.pi*(u*x+v*inv[x])/n)
                              for x in units))**4
                      for u in range(n) for v in range(n))/n**2
            assert abs(avg-m)<1.e-6,(p,avg,m)
    for r in range(1,(p+1)//2):
        a={x:0 for x in units}
        for k in range(p):
            a[r+p*k]=1
            a[(-r+p*k)%n]=1
        m=fourth(a)
        assert m==6*p**3,(p,m)
        ell=1
        a={x:0 for x in units}
        for k in range(p):
            a[r+p*k]=cmath.exp(2j*math.pi*ell*k/p)
            a[(-r+p*k)%n]=1j*cmath.exp(2j*math.pi*ell*k/p)
        m=fourth(a)
        assert abs(m-6*p**3)<1e-7,(p,m)
    return len(patterns)+2*(p-1)//2

if __name__=='__main__':
    tot = sum(check_prime(p) for p in (3,5,7))
    print('PRIME_SQUARE_HYPERBOLA_PASS primes=3,5,7 patterns='+str(tot)+' sharp_ratio=3p/2')
