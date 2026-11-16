#!/usr/bin/env python3
"""Reproduce 2-adic Walsh valuations for Hamiltonian-cycle incidence orbits.

Exhaustive Walsh transform for 3 <= n <= 8 and independent signed
Hamiltonian dynamic programming for selected larger graphs.
Python 3 standard library only.
"""
from collections import Counter
from itertools import permutations
from math import factorial
import random


def v2(x):
    assert x != 0
    return (abs(x) & -abs(x)).bit_length()-1


def s2(x):
    return x.bit_count()


def orbit(n):
    edges = [(i, j) for i in range(1, n) for j in range(i + 1, n)]
    index = {edge: t for t, edge in enumerate(edges)}
    output = []
    for p in permutations(range(1, n)):
        if p[0] > p[-1]:
            continue
        cycle = (0,) + p + (0,)
        mask = 0
        for u, v in zip(cycle, cycle[1:]):
            if u and v:
                mask |= 1 << index[min(u, v), max(u, v)]
        output.append(mask)
    assert len(output) == factorial(n-1)//2
    assert len(set(output)) == len(output)
    return output, len(edges)


def fwht_in_place(a):
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(h):
                x, y = a[i+j], a[i+h+j]
                a[i+j], a[i+h+j] = x+y, x-y
        h *= 2


def signed_cycles_dp(n, negative_edges):
    # independent Held-Karp sum of oriented cycles, divided by two
    negative_edges = set(tuple(sorted(e)) for e in negative_edges)
    wt = [[-1 if tuple(sorted((i,j))) in negative_edges else 1
           for j in range(n)] for i in range(n)]
    size = 1 << (n-1)
    rows = [[0]*(n-1) for _ in range(size)]
    for j in range(n-1):
        rows[1 << j][j] = wt[0][j+1]
    for mask in range(1, size):
        if mask.bit_count() == 1:
            continue
        subset = mask
        while subset:
            bit = subset & -subset
            j = bit.bit_length()-1
            prev = mask ^ bit
            s = 0
            while prev:
                b = prev & -prev
                i = b.bit_length()-1
                s += rows[mask ^ bit][i]*wt[i+1][j+1]
                prev ^= b
            rows[mask][j] = s
            subset ^= bit
    total = sum(rows[-1][j]*wt[j+1][0] for j in range(n-1))
    assert total % 2 == 0
    return total//2


def main():
    from array import array
    for n in range(3,9):
        vectors, d = orbit(n)
        a = array("q", [0])* (1 << d)
        for mask in vectors: a[mask] = 1
        h=1
        while h < len(a):
            for start in range(0, len(a),2*h):
                for i in range(start,start+h):
                    x,y=a[i],a[i+h]
                    a[i],a[i+h]=x+y,x-y
            h*=2
        m=factorial(n-1)//2
        if n in (3,4,6,7,8):
            modulus=2**(v2(m)+1)
            assert all((int(w)-m)%modulus==0 for w in a), (n, modulus)
            assert all(w!=0 for w in a)
            assert all((abs(w)&-abs(w))==2**v2(m) for w in a)
        if n==5:
            assert sum(w==0 for w in a)==32
            # exactly one negative edge (not incident with the gauge vertex)
            assert a[1]==0
        assert int(sum(int(w)*int(w) for w in a))==len(a)*m
        print(f'n={n} |H|={m} quotient={len(a)} zeros={sum(w==0 for w in a)} '
              f'minabs={min(abs(w) for w in a)} v2(|H|)={v2(m)}')
        if n<=7:
            rng=random.Random(8927+n)
            edge_set=[(i,j) for i in range(1,n) for j in range(i+1,n)]
            for _ in range(12):
                mask=rng.randrange(1<<len(edge_set))
                A=[e for i,e in enumerate(edge_set) if mask>>i&1]
                assert signed_cycles_dp(n,A)==int(a[mask])
    # Below are independent recurrence calculations, not evidence for all n.
    for n in (12,14,15,16):
        m=factorial(n-1)//2
        mod=1<<(v2(m)+1)
        rng=random.Random(819+n)
        for trial in range(3 if n<16 else 1):
            A=[(i,j) for i in range(n) for j in range(i+1,n)
               if rng.randrange(2)]
            w=signed_cycles_dp(n,A)
            assert w!=0 and (w-m)%mod==0 and v2(w)==v2(m)
        print(f'n={n} modulus={mod} tested DP signings={3 if n<16 else 1}: PASS')
    # Two distinct exact checks for the boundary counterexample at nine vertices.
    negative={(i,j) for i in range(1,5) for j in range(i+1,5)}
    from collections import Counter
    distribution=Counter()
    for p in permutations(range(1,9)):
        if p[0]>p[-1]: continue
        cyc=(0,)+p+(0,)
        k=sum(tuple(sorted((u,v))) in negative for u,v in zip(cyc,cyc[1:]))
        distribution[k]+=1
    assert sorted(distribution.items())==[(0,1440),(1,8640),(2,8640),(3,1440)]
    assert sum((-1)**k*count for k,count in distribution.items())==0
    assert signed_cycles_dp(9,negative)==0
    print('n=9 K4-negative edges: distribution 1440,8640,8640,1440; Walsh value 0: PASS')
    # Verify digit-sum criterion and enumeration of theorem parameters.
    for n in range(3,161):
        family=any(n==((1<<r)-(1<<j)) for r in range(2,10) for j in range(r))
        criterion=all(s2(k)<=s2(n-1) for k in range(n))
        assert family==criterion,(n, family, criterion)
    print('BINARY_HAMILTONIAN_2ADIC_CHECKS_PASS')

if __name__ == '__main__':
    main()
