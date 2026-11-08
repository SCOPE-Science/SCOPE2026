#!/usr/bin/env python3
"""Exact dynamic-programming certificate for cyclic binary reversal covers."""
from collections import defaultdict

EXPECTED = {1:(2,1), 2:(4,1), 3:(8,2), 4:(14,8), 5:(26,128)}

def reverse_bits(x, n):
    y = 0
    for _ in range(n):
        y = 2*y+(x&1)
        x >>= 1
    return y

def counts_through(n, cap):
    representatives = sorted({min(i, reverse_bits(i,n)) for i in range(1<<n)})
    index = {x:i for i,x in enumerate(representatives)}
    label = [index[min(i,reverse_bits(i,n))] for i in range(1<<n)]
    full_mask = (1<<len(representatives))-1
    small_mask = (1<<(n-1))-1
    dp = {(1<<label[0],0):1}
    out = {}
    for L in range(n,cap+1):
        total = 0
        for (seen,last),ways in dp.items():
            z = seen; state = last
            for _ in range(n-1):
                edge = state<<1
                z |= 1<<label[edge]
                state = edge&small_mask
            if z == full_mask: total += ways
        out[L] = total
        nxt = defaultdict(int)
        for (seen,last),ways in dp.items():
            for bit in (0,1):
                edge = (last<<1)|bit
                nxt[(seen | (1<<label[edge]),edge&small_mask)] += ways
        dp = nxt
    return len(representatives),out

def main():
    for n,(opt,number) in EXPECTED.items():
        classes,counts = counts_through(n,opt)
        assert classes == (2**n+2**((n+1)//2))//2
        assert all(counts[L]==0 for L in range(classes,opt))
        assert counts[opt]==number
        print(f'order={n} classes={classes} min_length={opt} rooted_optima={number}')
    print('DP_VERIFY_OK')

if __name__ == '__main__': main()
