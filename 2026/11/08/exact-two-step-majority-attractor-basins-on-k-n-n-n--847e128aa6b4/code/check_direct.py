#!/usr/bin/env python3
"""Independent vertex-level verification for synchronous majority on K(n,n,n)."""
from itertools import product
from math import comb


def expected(n):
    b = 0
    for a in range(n + 1):
        for c in range(n + 1):
            if min(a, n-a) < c < max(a, n-a):
                b += 3 * comb(n, a) * comb(n, n-a) * comb(n, c)
    fixed_half = comb(n, n//2)**3 if n % 2 == 0 else 0
    return b, fixed_half


def run(n):
    N = 3*n
    mask = (1<<n) - 1
    parts = [mask << (i*n) for i in range(3)]
    neighbors = [parts[(v//n+1)%3] | parts[(v//n+2)%3] for v in range(N)]
    def update(s):
        t = 0
        for v in range(N):
            ones = (s & neighbors[v]).bit_count()
            if ones > n or (ones == n and (s>>v)&1):
                t |= 1 << v
        return t
    consensus = [0,0]
    two = 0
    balanced = 0
    periodic_two = 0
    for s in range(1<<N):
        z=update(s)
        zz=update(z)
        zzz=update(zz)
        zzzz=update(zzz)
        assert zz == zzzz, (n,s,zz,zzzz)
        if zz != zzz:
            two+=1
            if s == zz: periodic_two += 1
        elif zz == 0:
            consensus[0]+=1
        elif zz == (1<<N)-1:
            consensus[1]+=1
        else:
            assert s == zz and all((s&p).bit_count()*2==n for p in parts)
            balanced+=1
        a,b,c = [(s&p).bit_count() for p in parts]
        predicted=any(v+w == n and min(v,w) < k < max(v,w) for (v,w,k) in [(a,b,c),(a,c,b),(b,c,a)])
        assert predicted == (zz != zzz), (n,s,a,b,c)
    B,H=expected(n)
    assert two == B and balanced == H
    assert periodic_two == 6 * (2**n-2)
    assert consensus[0] == consensus[1] == ((1<<N)-B-H)//2
    print(f"n={n}: states={1<<N}, 2cycle_basin={two}, periodic_2cycle_states={periodic_two}, half_fixed={balanced}, consensus_each={consensus[0]}; verified")


if __name__=='__main__':
    for n in range(1,6):run(n)
    print('DIRECT_CHECK_PASS')
