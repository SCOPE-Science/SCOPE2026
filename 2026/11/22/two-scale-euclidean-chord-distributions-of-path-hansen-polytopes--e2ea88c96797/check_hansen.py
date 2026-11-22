#!/usr/bin/env python3
"""Independent exact distance enumeration for path Hansen polytopes.

No external packages are required. This checker compares unordered distances
against a four-state transfer and a third-order coefficient recurrence.
"""
from collections import Counter
from functools import lru_cache
from math import comb, sqrt

STATES = ((0,0), (1,0), (0,1), (1,1))


def masks(n):
    return [x for x in range(1 << n) if not x & (x << 1)]


def pair_polys(n):
    """Weighted ordered pairs, independently enumerated."""
    a, b = Counter(), Counter()
    for x in masks(n):
        for y in masks(n):
            a[(x ^ y).bit_count()] += 1
            b[(x ^ y).bit_count() + 4 * (x & y).bit_count()] += 1
    return a, b


def distance_poly(n):
    vertices = [(s, x) for s in (-1, 1) for x in masks(n)]
    d = Counter()
    for i, (s,x) in enumerate(vertices):
        for t,y in vertices[i+1:]:
            value = (s-t)**2 + sum((s*((x>>j)&1)-t*((y>>j)&1))**2 for j in range(n))
            d[value] += 1
    return d


def from_transfer(n, plus):
    # The pair state at each site is (x_i,y_i); no consecutive ones in either.
    v = [1,1,1,1]
    if n == 0:
        return Counter({0:1})
    layers = [Counter({(x^y) + (4*(x&y) if plus else 0):1}) for x,y in STATES]
    for _ in range(1, n):
        next_layers = [Counter() for _ in STATES]
        for i,(a,b) in enumerate(STATES):
            for j,(c,d) in enumerate(STATES):
                if a*c or b*d: continue
                w = (c^d) + (4*(c&d) if plus else 0)
                for k,count in layers[i].items():
                    next_layers[j][k+w] += count
        layers = next_layers
    result = Counter()
    for layer in layers:
        result.update(layer)
    return result


def from_cubic(n, plus):
    # Coefficients [q^0,...] represented with Counter.
    @lru_cache(None)
    def rec(i):
        if i < 0: return Counter()
        if i == 0: return Counter({0:1})
        # N(q,t)=(1 + (q+q^4)t - q^5 t^2) for plus, and
        # (1+(1+q)t -q t^2) for minus.
        # D(q,t)=(1-(1+q)t -(q+q^4)t^2+q^5 t^3) for plus,
        # (1-(1+q)t -(1+q)t^2+q t^3) for minus.
        if plus:
            nco = {1:Counter({1:1,4:1}),2:Counter({5:-1})}
            dco = {1:Counter({0:1,1:1}),2:Counter({1:1,4:1}),3:Counter({5:-1})}
        else:
            nco = {1:Counter({0:1,1:1}),2:Counter({1:-1})}
            dco = {1:Counter({0:1,1:1}),2:Counter({0:1,1:1}),3:Counter({1:-1})}
        out = Counter(nco.get(i,{}))
        for j,pol in dco.items():
            if i-j>=0:
                for k,c in rec(i-j).items():
                    for shift,d in pol.items(): out[k+shift]+=c*d
        return Counter({k:c for k,c in out.items() if c})
    return rec(n)


def main():
    for n in range(0, 13):
        a,b = pair_polys(n)
        assert a == from_transfer(n,False) == from_cubic(n,False), (n,'A')
        assert b == from_transfer(n,True) == from_cubic(n,True), (n,'B')
        f = len(masks(n))
        d = a.copy()
        d[0] -= f
        d += Counter({k+4:v for k,v in b.items()})
        assert d == distance_poly(n), (n,'D',d,distance_poly(n))
        assert sum(d.values()) == comb(2*f,2)
    for n in (50,100,200):
        for plus,mu,var in ((False, 2/5,14/(25*sqrt(5))),
                            (True,(8-2*sqrt(5))/5,(54-8*sqrt(5))/(25*sqrt(5)))):
            # Moment transfer avoids polynomial expansion.
            # Transfer first and second raw moments with exact integer arithmetic.
            z = [(1,(a^b)+4*(a&b) if plus else a^b, ((a^b)+4*(a&b) if plus else a^b)**2) for a,b in STATES]
            for _ in range(n-1):
                nz = [(0,0,0) for _ in STATES]
                for i,(a,b) in enumerate(STATES):
                    mass,m1,m2 = z[i]
                    for j,(c,d) in enumerate(STATES):
                        if a*c or b*d: continue
                        w=(c^d) + (4*(c&d) if plus else 0)
                        x,y,v = nz[j]
                        nz[j] = (x+mass, y+m1+w*mass, v+m2+2*w*m1+w*w*mass)
                z = nz
            T=sum(x for x,_,_ in z)
            ave=sum(x for _,x,_ in z)/T
            vv=sum(x for _,_,x in z)/T-ave*ave
            assert abs(ave/n-mu)<0.02 and abs(vv/n-var)<0.03,(n,plus,ave/n,vv/n,mu,var)
            if n==200: print(('plus' if plus else 'minus'), 'n=200 mean/n', round(ave/n,8), 'var/n',round(vv/n,8))
    print('HANSEN_PATH_CHORD_PASS: enumerated n=0..12; independent transfers, cubic recurrences, and asymptotic moments checked')


if __name__=='__main__':
    main()
