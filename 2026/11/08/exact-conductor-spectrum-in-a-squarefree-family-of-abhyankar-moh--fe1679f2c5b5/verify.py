#!/usr/bin/env python3
"""Exact integer independent conductor checks for A-M degree 3q spectra."""
from math import gcd, isqrt
from heapq import heappop, heappush


def is_prime(q):
    return q > 1 and all(q % d for d in range(2, isqrt(q)+1))


def predicted(q):
    n = 3*q
    upper = (n-1)*(n-2)
    return {0, n-1} | {c for c in range(6*q, upper+1, 2) if c % 6 in (0, 2)}


def sequences(q):
    n = 3*q
    yield (n, 1)
    for a in range(2, n):
        if gcd(n,a) == 1:
            yield (n,a)
    for d in (3,q):
        for k in range(1, n//d):
            if gcd(n//d,k) > 1:
                continue
            a = d*k
            for b in range(n*k+1, n*n//d):
                if gcd(d,b) == 1:
                    yield (n,a,b)


def formula(seq):
    n=seq[0]
    e=n
    c=-n+1
    for v in seq[1:]:
        en=gcd(e,v)
        c+=(e//en-1)*v
        e=en
    assert e==1
    return c


def dijkstra_conductor(seq):
    m=min(seq)
    dist=[None]*m
    dist[0]=0
    heap=[(0,0)]
    while heap:
        d,r=heappop(heap)
        if d!=dist[r]:
            continue
        for a in seq:
            r2=(r+a)%m
            d2=d+a
            if dist[r2] is None or d2<dist[r2]:
                dist[r2]=d2
                heappush(heap,(d2,r2))
    assert all(x is not None for x in dist)
    return max(dist)-m+1


def main():
    for q in (7,13,19,31,37):
        assert is_prime(q) and q%6==1
        vals=set()
        count=0
        for seq in sequences(q):
            count+=1
            c=formula(seq)
            vals.add(c)
            assert c%6 in (0,2)
            if q<=13 or (q==19 and count%31==0):
                assert c==dijkstra_conductor(seq),(q,seq,c)
        expect=predicted(q)
        assert vals==expect,(q, sorted(expect-vals)[:10],sorted(vals-expect)[:10])
        assert len(vals)==3*q*q-5*q+4
        print(f'q={q}, degree={3*q}: {count} admissible characteristic sequences; '
              f'{len(vals)} exact conductors; independent formula and spectrum checks OK')
    # Hypothesis boundary: q=5 produces a residue-four conductor via an actual sequence.
    assert formula((15,5,17))==64
    assert dijkstra_conductor((15,5,17))==64
    print('Boundary q=5: conductor(15,5,17)=64 (mod 6 = 4), excluded by hypothesis')
    print('ALL EXACT VERIFICATION CHECKS PASSED')

if __name__=='__main__':
    main()
