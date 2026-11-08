#!/usr/bin/env python3
"""Exhaustive configuration-level verification for majority dynamics on triangular books.
Run: python verify_direct.py
"""
from collections import Counter
from math import comb

def update(state, n):
    # Bits 0,1: adjacent hubs. Bits 2,...,n+1: independent common neighbors.
    a = state & 1
    b = (state >> 1) & 1
    bits = (state >> 2) & ((1 << n) - 1)
    s = bits.bit_count()
    def vote(old, ones, deg):
        return int(2 * ones > deg) if 2 * ones != deg else old
    na = vote(a, b+s, n+1)
    nb = vote(b, a+s, n+1)
    if a == b:
        newbits = ((1 << n)-1) if a else 0
    else:
        newbits = bits
    return na | (nb << 1) | (newbits << 2)

def expected(n):
    if n % 2 == 0:
        c = comb(n, n//2)
        return {(1,0):2,(2,0):2+2*c,(1,1):2**n+c+2,
                (2,1):2**n-c-2,(1,2):2**(n+1)-2*c-4}
    c=comb(n,(n-1)//2)
    return {(1,0):2,(2,0):2,(1,1):2**n+2*c+2,
            (2,1):2**n-2*c-2,(1,2):2**(n+1)-4}

checks=0
for n in range(2,15):
    counts=Counter()
    for state in range(1 << (n+2)):
        trajectory = [state]
        index={state:0}
        current=state
        for t in range(1,12):
            current=update(current,n)
            if current in index:
                pre=index[current];period=t-pre
                assert pre <=2 and period in (1,2), (n,state,pre,period)
                counts[(period,pre)]+=1
                break
            index[current]=t
            trajectory.append(current)
        else: raise AssertionError((n,state,'loop not found'))
        checks+=1
    assert dict(counts)=={k:v for k,v in expected(n).items() if v}, (n,counts,expected(n))
    assert sum(counts.values())==1 << (n+2)
    print(f'n={n:2d}: states={1<<(n+2):6d}; '+', '.join(f'{k}={counts[k]}' for k in sorted(counts)))
print(f'PASS: {checks} labelled initial configurations; every entry time and period verified for n=2..14')
