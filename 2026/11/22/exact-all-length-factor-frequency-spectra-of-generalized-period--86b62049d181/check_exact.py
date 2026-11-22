"""Exact phase-mass enumeration for generalized period-doubling factor frequencies.
Run: python3 check_exact.py
"""
from collections import Counter, defaultdict
from math import ceil, log2

def direct_spectrum(q, n):
    L = 1 << (n-1).bit_length()
    D = (1 << q) - 1
    weights = defaultdict(int)
    for r in range(L):
        hole = (-r-1) % L
        block = []
        for i in range(n):
            if i == hole:
                block.append(-1)
            else:
                x = r+i+1
                block.append(((x & -x).bit_length()-1) % q)
        if hole >= n:
            weights[tuple(block)] += D
        else:
            for j in range(q):
                b = list(block)
                b[hole] = ((L.bit_length()-1) + j) % q
                weights[tuple(b)] += 1 << (q-j-1)
    assert sum(weights.values()) == L*D
    return Counter(weights.values())

def claimed_spectrum(q, n):
    if n == 1:
        return Counter({1<<j:1 for j in range(q)})
    if n == 2:
        c = Counter({2:3})
        for j in range(2,q): c[1<<j] = 2
        return c
    L = 1 << (n-1).bit_length()
    M = L//4
    a = max(0, 3*M-n)
    c = max(0, n-3*M)
    b = M-a-c
    out = Counter()
    if 4*b+6*c: out[2]=4*b+6*c
    if q==2:
        if 3*a+b: out[4]=3*a+b
    else:
        if 3*a+3*b+4*c: out[4]=3*a+3*b+4*c
        for j in range(3,q):
            if 2*a+3*b+4*c: out[1<<j]=2*a+3*b+4*c
        if 2*a+b: out[1<<q]=2*a+b
    return out

checked=0
for q in range(2,11):
    for n in range(1,130):
        a=direct_spectrum(q,n)
        b=claimed_spectrum(q,n)
        assert a==b, (q,n,a,b)
        checked+=1
print(f'PASS: exact phase enumeration matches the quartet frequency table for {checked} pairs, q=2..10 and n=1..129.')
print('Example q=3, n=13:', sorted(direct_spectrum(3,13).items()))
print('Example q=2, n=16:', sorted(direct_spectrum(2,16).items()))
