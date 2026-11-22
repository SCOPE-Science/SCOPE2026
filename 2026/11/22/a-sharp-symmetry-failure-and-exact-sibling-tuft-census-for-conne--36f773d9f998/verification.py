"""Finite independent checks of a threshold-graph sibling/tuft enumerator.

Uses Python's standard library. Run: python verification.py
The general theorem relies on the written proof, not these finite checks.
"""
from itertools import product
from collections import Counter

MAX_N = 12

def stats_from_graph(word):
    n = len(word)
    neigh = [set() for _ in range(n)]
    for j in range(1, n):
        if word[j] == '1':
            for i in range(j):
                neigh[i].add(j)
                neigh[j].add(i)
    classes = Counter(frozenset(neigh[v] | {v}) for v in range(n))
    siblings = max(classes.values()) - 1
    tufts = max(sum(len(neigh[v]) == 1 for v in neigh[u]) for u in range(n))
    degrees = tuple(sorted(len(a) for a in neigh))
    return siblings, tufts, degrees

def stats_from_runs(word):
    a, b, i = [], [], 0
    while i < len(word):
        j = i
        while j < len(word) and word[j] == '0':
            j += 1
        a.append(j-i)
        i = j
        while j < len(word) and word[j] == '1':
            j += 1
        b.append(j-i)
        i = j
    assert all(x > 0 for x in a+b)
    siblings = max([b[0]-1+int(a[0] == 1)] + [v-1 for v in b[1:]])
    tufts = a[-1] if b[-1] == 1 else 0
    return siblings, tufts

def plus(*args):
    out = [0] * (MAX_N + 1)
    for arr in args:
        for i, v in enumerate(arr):
            out[i] += v
    return out

def times(a, b):
    out = [0] * (MAX_N + 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b[:MAX_N + 1-i]):
                out[i+j] += x*y
    return out

def Zpow(t):
    out = [0] * (MAX_N + 1)
    if t <= MAX_N:
        out[t] = 1
    return out

def B(m, low=1):
    return plus(*(Zpow(i) for i in range(low, min(m, MAX_N)+1)))

def div_by_one_minus_v(num, v):
    assert v[0] == 0
    out = [0] * (MAX_N + 1)
    for n in range(MAX_N+1):
        out[n] = num[n] + sum(v[j]*out[n-j] for j in range(1,n+1))
    return out

GEOM = [1]*(MAX_N+1)
Z = Zpow(1)
ZZ = Zpow(2)

def cumulative_series(p, q):
    # U = z B_p + (z^2/(1-z)) B_(p+1)
    U = plus(times(Z, B(p)), times(times(ZZ, GEOM), B(p+1)))
    # V = (z/(1-z)) B_(p+1)
    V = times(times(Z, GEOM), B(p+1))
    # W = z B_q + (z/(1-z)) D_(p+1)
    W = plus(times(Z, B(q)), times(times(Z, GEOM), B(p+1, 2)))
    # R = [p,q>=1] z^2 + z D_p + z D_q + z^2/(1-z) D_(p+1)
    R = plus(ZZ if min(p,q)>=1 else Zpow(MAX_N+1),
             times(Z, B(p,2)), times(Z, B(q,2)),
             times(times(ZZ,GEOM), B(p+1,2)))
    return plus(R, div_by_one_minus_v(times(U,W),V))

def fibonacci(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a

checked = 0
for n in range(2,MAX_N+1):
    dist = Counter()
    degree_sequences = set()
    for mids in product('01',repeat=n-2):
        w='0'+''.join(mids)+'1'
        s,t,d = stats_from_graph(w)
        assert (s,t)==stats_from_runs(w), (w,(s,t),stats_from_runs(w))
        assert d not in degree_sequences, (n,w,d)
        degree_sequences.add(d)
        dist[s,t] += 1
    assert sum(dist.values()) == 2**(n-2)
    assert sum(v for (s,t),v in dist.items() if s==0)==fibonacci(n-2)
    if n >= 3:
        assert sum(v for (s,t),v in dist.items() if t==0)==2**(n-3)
    for p in range(0,7):
        for q in range(0,7):
            actual=sum(v for (s,t),v in dist.items() if s<=p and t<=q)
            predicted=cumulative_series(p,q)[n]
            assert actual == predicted, (n,p,q,actual,predicted)
            checked += 1
    print('n=%d types=%d sibling_zero=%d tuft_zero=%d PASS' % (
       n,len(degree_sequences),
       sum(v for (s,t),v in dist.items() if s==0),
       sum(v for (s,t),v in dist.items() if t==0)))
print('CUMULATIVE_COMPARISONS',checked)
print('VERIFY_OK')
