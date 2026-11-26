#!/usr/bin/env python3
"""Exact rational-transfer certificate for limited domination on Möbius ladders.
Only Python's standard library is needed. No third-party paper or network access.
"""
from collections import defaultdict
from itertools import combinations

def add(a, b):
    c = dict(a)
    for i, v in b.items():
        c[i] = c.get(i, 0) + v
        if c[i] == 0:
            del c[i]
    return c

def neg(a):
    return {i: -v for i, v in a.items()}

def mul(a, b):
    c = defaultdict(int)
    for i, v in a.items():
        for j, w in b.items():
            c[i + j] += v * w
    return {i: v for i, v in c.items() if v}

def pmul(a, b):
    return mul(a, b)

def scale(a, n):
    return {i: n * v for i, v in a.items() if n * v}

def P(*coeff):
    return {i: v for i, v in enumerate(coeff) if v}

states = [(a, b) for a in range(4) for b in range(4)]
state_no = {v: i for i, v in enumerate(states)}
def swap(x):
    return ((x & 1) << 1) | ((x & 2) >> 1)
def allowed(a, b, c):
    for r in (0, 1):
        bit = (b >> r) & 1
        n = ((a >> r) & 1) + ((c >> r) & 1) + ((b >> (1-r)) & 1)
        if n < (2 if bit else 1):
            return False
    return True

edges = [[] for _ in states]
for i, (a, b) in enumerate(states):
    for c in range(4):
        if allowed(a, b, c):
            edges[i].append((state_no[(b, c)], b.bit_count()))
assert sum(map(len, edges)) == 26

def trace_sequence(L):
    normal, twisted = [P() for _ in range(L+1)], [P() for _ in range(L+1)]
    for i, (a, b) in enumerate(states):
        t = state_no[(swap(a), swap(b))]
        cur = {(i, 0): 1}
        for k in range(L+1):
            for (j, exponent), count in cur.items():
                if j == i:
                    normal[k] = add(normal[k], {exponent: count})
                if j == t:
                    twisted[k] = add(twisted[k], {exponent: count})
            if k != L:
                nxt = defaultdict(int)
                for (j, exponent), count in cur.items():
                    for v, w in edges[j]:
                        nxt[(v, exponent+w)] += count
                cur = nxt
    return normal, twisted

normal, twisted = trace_sequence(16)
assert normal[0] == {0:16} and twisted[0] == {0:4}

# Finite exact characteristic-polynomial certificate using Newton identities.
d = [{0:1}]
for k in range(1,17):
    x = {}
    for j in range(1,k+1):
        x = add(x, mul(d[k-j], normal[j]))
    assert all(v % k == 0 for v in x.values())
    d.append({e: -(v//k) for e,v in x.items() if v})

expected_D = [
 P(1), P(0,-2,-1), P(0,0,1,2), P(0,0,0,0,-2,-2),
 P(0,0,0,0,-1,2,1), P(0,0,0,0,0,2,-1,0,-1),
 P(0,0,0,0,0,0,-1), P(0,0,0,0,0,0,0,0,0,0,1),
 P(0,0,0,0,0,0,0,0,0,0,1)
]
assert d == expected_D + [{} for _ in range(8)], (d, expected_D)

# By adjugate formula the numerator degree is <= 15; certify its coefficients.
num = []
for k in range(16):
    x = {}
    for j in range(k+1):
        x = add(x, mul(d[j], twisted[k-j]))
    num.append(x)
expected_N = [
 P(4), P(0,-8,-3), P(0,0,4,10), P(0,0,0,0,-6,-6),
 P(0,0,0,0,0,2,2), P(0,0,0,0,0,0,-1,-4,-3),
 P(0,0,0,0,0,0,0,-4,2), P(0,0,0,0,0,0,0,0,2,0,1)
]
assert num == expected_N + [{} for _ in range(8)], (num, expected_N)
print('CHARACTERISTIC_AND_TWISTED_TRACE_CERTIFICATE_OK', len(states), sum(map(len,edges)))

# t-coefficients of constant and linear terms after substituting t -> t/z.
def at_exp(seq, extra):
    return {i: poly.get(i+extra,0) for i,poly in enumerate(seq) if poly.get(i+extra,0)}
N0,N1=at_exp(expected_N,0),at_exp(expected_N,1)
D0,D1=at_exp(expected_D,0),at_exp(expected_D,1)
assert N0==P(4,-8,4)
assert D0==P(1,-2,1,0,-1,2,-1)
assert N1==P(0,-3,10,-6,2,-1,-4,2)
assert D1==P(0,-1,2,-2,2,-1)
H0top=P(4);H0bot=P(1,0,0,0,-1)
H1top=P(0,1,4,7,0,-2);H1bot=P(1,0,-2,0,1)
assert mul(D0,H0top)==mul(N0,H0bot)
assert mul(add(mul(N1,D0),neg(mul(N0,D1))),H1bot)==mul(mul(D0,D0),H1top)
print('LOW_COEFFICIENT_GENERATING_FUNCTIONS_OK')

# Comparison with a separate direct implementation on the 2n-cycle plus antipodes.
def direct(n):
    v = 2*n
    neighbors = [(1<<((i-1)%v))|(1<<((i+1)%v))|(1<<((i+n)%v)) for i in range(v)]
    histogram = defaultdict(int)
    for mask in range(1<<v):
        good=True
        for i in range(v):
            d=(neighbors[i]&mask).bit_count()
            if ((mask>>i)&1 and d<2) or (not ((mask>>i)&1) and d==0):
                good=False;break
        if good:histogram[mask.bit_count()]+=1
    return dict(histogram)
for n in range(2,10):
    brute=direct(n)
    assert twisted[n]==brute, (n,twisted[n],brute)
    m=min(brute)
    predicted=n if n%4==0 else n+1
    minimum_count=4 if n%4==0 else (3*n if n%2 else 2*n)
    assert (m,brute[m])==(predicted,minimum_count)
    print('DIRECT_ENUMERATION_OK',n,predicted,minimum_count)
for n in range(10,17):
    m=min(twisted[n])
    pred=n if n%4==0 else n+1
    cnt=4 if n%4==0 else (3*n if n%2 else 2*n)
    assert (m,twisted[n][m])==(pred,cnt)
print('TRANSFER_EXTENDED_CHECK_OK 10..16')
print('VERIFY_OK')
