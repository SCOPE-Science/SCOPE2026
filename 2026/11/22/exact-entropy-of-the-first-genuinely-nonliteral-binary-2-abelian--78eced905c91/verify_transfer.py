#!/usr/bin/env python3
"""Exact finite-state certificate for one fixed 2-Abelian-square period.
All counts and polynomial identities are evaluated with Python integers.
"""
from collections import Counter, deque
from itertools import product
from math import gcd

P = [1,0,0,-1,-2,-5,-8,-11,-13,-16,-19,-20,-26,-24,-26,-23,-15,-7,6,15,19,19,14,5,0,-6,-8,-4,-3,1,2,1,1]
N = [1,2,4,7,12,19,30,49,65,90,113,140,150,162,166,171,163,151,132,79,33,-47,-108,-155,-162,-130,-72,-12,41,67,56,39,3,-16,-16,-14,-4]

def key(w):
    return w[0], tuple(sum(w[i:i+2] == pair for i in range(3))
                       for pair in product((0, 1), repeat=2))

four = list(product((0, 1), repeat=4))
classes = {}
for w in four:
    classes.setdefault(key(w), []).append(w)
assert sorted(len(t) for t in classes.values()) == [1]*12 + [2]*2
forbidden = {u + v for u in four for v in classes[key(u)]}
assert len(forbidden) == 20
extra = forbidden - {u+u for u in four}
assert {''.join(map(str,w)) for w in extra} == {'00100100', '01000010','10111101','11011011'}

# State s encodes the last seven bits. Each edge appends a bit.
nexts = []
for s in range(128):
    arcs=[]
    for b in (0, 1):
        block=tuple((s >> i) & 1 for i in range(6,-1,-1)) + (b,)
        if block not in forbidden:
            arcs.append(((s << 1 | b) & 127))
    nexts.append(arcs)
assert sum(map(len,nexts))==236

def evolve(v):
    w=[0]*128
    for i, arcs in enumerate(nexts):
        for j in arcs:
            w[j] += v[i]
    return w

# Exactly check a 33-step vector identity, not just a few count values.
v=[1]*128
vectors=[]
for j in range(34):
    vectors.append(v)
    v=evolve(v)
assert all(sum(P[j]*vectors[33-j][i] for j in range(33))==0
           for i in range(128))

# The initial seven-bit count is 128; the first seven have 2^n choices.
counts=[2**n for n in range(7)] + [sum(vectors[j]) for j in range(34)]
for n in range(40):
    conv = sum(P[j]*counts[n-j] for j in range(min(n,32)+1))
    assert conv == (N[n] if n < len(N) else 0), (n,conv)

# Strong connectivity and aperiodicity of the 128-state graph.
def distances(graph):
    dist={0:0};q=deque([0])
    while q:
        u=q.popleft()
        for v in graph[u]:
            if v not in dist:dist[v]=dist[u]+1;q.append(v)
    return dist
reverse=[[] for _ in range(128)]
for u, arcs in enumerate(nexts):
    for v in arcs:reverse[v].append(u)
d=distances(nexts)
assert len(d)==128 and len(distances(reverse))==128
period=0
for u, arcs in enumerate(nexts):
    for v in arcs:period=gcd(period,d[u]+1-d[v])
assert period==1

# Perron bounds by Collatz-Wielandt, using all-positive T^k 1.
v=[1]*128
out=[[u for u, arc in enumerate(nexts) if j in arc] for j in range(128)]
for k in range(500):
    w=[sum(v[j] for j in arcs) for arcs in nexts]
    v=w
w=[sum(v[j] for j in arcs) for arcs in nexts]
assert all(1897140076437*v[i] < 10**12*w[i] < 1897140076440*v[i] for i in range(128))
low=min(w[i]/v[i] for i in range(128))
high=max(w[i]/v[i] for i in range(128))

print('PASS: 20 forbidden blocks, four nonliteral; 128 states, 236 transitions')
print('PASS: exact polynomial vector identity and all-length rational series')
print('PASS: graph strongly connected, period 1')
print('Perron interval:',low,high)
print('first counts:',counts[:17])

# Separate comparison: avoid only literal length-four squares.
literal_nexts=[]
for state in range(128):
    arcs=[]
    for bit in (0,1):
        window=tuple((state >> i)&1 for i in range(6,-1,-1))+(bit,)
        if window[:4] != window[4:]:
            arcs.append(((state << 1)|bit)&127)
    literal_nexts.append(arcs)
assert sum(map(len,literal_nexts)) == 240
assert all(set(a).issubset(set(b)) for a,b in zip(nexts,literal_nexts))
assert len(distances(literal_nexts)) == 128
v=[1]*128
for _ in range(500):
    v=[sum(v[j] for j in arcs) for arcs in literal_nexts]
w=[sum(v[j] for j in arcs) for arcs in literal_nexts]
assert all(1927561975481*v[i] < 10**12*w[i] < 1927561975485*v[i] for i in range(128))
print('PASS: strict comparator Perron enclosure 1.927561975481 to 1.927561975485')
