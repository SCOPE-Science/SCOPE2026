#!/usr/bin/env python3
"""Self-contained integer tests of cubic fixed-column dyadic residue frequencies."""
from collections import Counter
from math import comb

def F(n):
    return comb(n, 3) if n >= 3 else 0

def v2(x):
    if x == 0:
        return None
    x = abs(x)
    return (x & -x).bit_length() - 1

def charts(t):
    return [F(4*t)//4, F(4*t+1)//2, F(4*t+2)//4, (F(4*t+3)-1)//2]

def run():
    cases=0
    for t in range(400):
        g=charts(t)
        assert 3*g[0] == t*(2*t-1)*(4*t-1)
        assert 3*g[1] == t*(4*t-1)*(4*t+1)
        assert 3*g[2] == t*(2*t+1)*(4*t+1)
        assert 3*g[3] == 11*t+24*t*t+16*t*t*t
        cases+=4
    for r in range(4):
        for m in range(1,9):
            vals=[charts(t)[r] % (1 << m) for t in range(1 << m)]
            assert len(set(vals)) == (1 << m)
    for k in range(1,14):
        mod=1<<k
        period=2*mod
        counts=Counter(F(n) % mod for n in range(period))
        assert len(counts)==mod
        for b in range(mod):
            expected=(3 if b==0 else 1) if k==1 else (5 if b%4==0 else 1)
            assert counts[b]==expected, (k,b,counts[b],expected)
        for n in range(period):
            assert F(n+period) % mod == F(n) % mod
        shift=mod
        assert F(3+shift)%mod != F(3)%mod if k>=2 else F(1+shift)%mod != F(1)%mod
        if k<=10:
            for d in (1,2):
                vals=Counter(comb(n,d)%mod if n>=d else 0 for n in range(2*mod))
                assert set(vals.values()) == {2} and len(vals)==mod
    print('VERIFY_OK levels=1..13 charts=%d bijective_charts=32 exact_fibers=PASS least_periods=PASS lower_columns=PASS'%cases)

if __name__=='__main__':
    run()
