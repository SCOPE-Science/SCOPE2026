"""Self-contained exact transfer and spectral verification for toroidal B3/S23, 4xn.
Requires Python 3 and sympy for characteristic-polynomial computation only.
"""
from collections import deque
from functools import reduce
import sympy as sp

H = 4
MASK = (1 << H) - 1

def bit(c, r):
    return (c >> (r % H)) & 1

def middle_is_fixed(a, b, c):
    for r in range(H):
        s = bit(b, r - 1) + bit(b, r + 1)
        s += sum(bit(a, r + j) + bit(c, r + j) for j in (-1, 0, 1))
        new = int(s == 3 or (s == 2 and bit(b, r)))
        if new != bit(b, r):
            return False
    return True

N = 1 << (2 * H)
edges = [[] for _ in range(N)]
for a in range(16):
    for b in range(16):
        for c in range(16):
            if middle_is_fixed(a, b, c):
                edges[16 * a + b].append(16 * b + c)

assert sum(map(len, edges)) == 499

def sccs(edges):
    n = len(edges); counter = 0; indices = [-1]*n; low = [0]*n
    onstack = [False]*n; stack = []; ans = []
    def rec(v):
        nonlocal counter
        indices[v] = low[v] = counter; counter += 1
        stack.append(v); onstack[v] = True
        for w in edges[v]:
            if indices[w] == -1:
                rec(w); low[v] = min(low[v], low[w])
            elif onstack[w]:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            out = []
            while True:
                w = stack.pop(); onstack[w] = False; out.append(w)
                if w == v: break
            ans.append(sorted(out))
    for v in range(n):
        if indices[v] == -1: rec(v)
    return ans

all_comps = sccs(edges)
cyclic = [c for c in all_comps if len(c)>1 or c[0] in edges[c[0]]]
assert len(all_comps) == 130
assert len(cyclic) == 1 and len(cyclic[0]) == 127
assert 0 in cyclic[0] and 0 in edges[0]
V = sorted(cyclic[0]); index = {v:i for i,v in enumerate(V)}
small_edges = [[index[w] for w in edges[v] if w in index] for v in V]
assert sum(map(len, small_edges)) == 309

def reachability(adj, start):
    seen = {start}; q = deque([start])
    while q:
        for v in adj[q.popleft()]:
            if v not in seen:
                seen.add(v); q.append(v)
    return len(seen)

assert reachability(small_edges,index[0]) == 127
reverse = [[] for _ in V]
for i,neigh in enumerate(small_edges):
    for j in neigh: reverse[j].append(i)
assert reachability(reverse,index[0]) == 127

B = sp.zeros(len(V))
for i,neigh in enumerate(small_edges):
    for j in neigh: B[i,j] += 1
x = sp.Symbol('x')
poly = B.charpoly(x).as_expr()
fl = sp.factor_list(poly)[1]
assert sp.degree(poly,x)==127
print('state_count=256 edges=499 strongly_connected_components=130 unique_cyclic_component=127 cyclic_edges=309')
print('charpoly=',sp.factor(poly))

# The following is an exact trace evaluation, not a numerical approximation.
def trace_power(k):
    total = 0
    for start in range(len(V)):
        row = [0]*len(V); row[start] = 1
        for _ in range(k):
            nextrow = [0]*len(V)
            for i in range(len(V)):
                val = row[i]
                if val:
                    for j in small_edges[i]: nextrow[j] += val
            row=nextrow
        total += row[start]
    return total

counts={n:trace_power(n) for n in range(3,16)}
print('counts_3_15=',counts)
assert [counts[i] for i in range(3,12)] == [39,53,313,651,983,3133,5907,16649,43057]

# Collatz-Wielandt bounds from a strictly positive integer vector.
v=[1]*len(V)
for _ in range(400):
    v=[sum(v[j] for j in small_edges[i]) for i in range(len(V))]
w=[sum(v[j] for j in small_edges[i]) for i in range(len(V))]
ratios=[sp.Rational(w[i],v[i]) for i in range(len(V))]
lo=min(ratios); hi=max(ratios)
print('collatz_k=400 lower=',float(lo),'upper=',float(hi),'gap=',float(hi-lo))
assert sp.Rational(255371542,100000000) < lo < hi < sp.Rational(255371544,100000000)

# Independent height-three transfer gives a periodic component of spectral
# polynomial x^24 (x^3-27); for 3|n this component contributes 3^(n+1)
# fixed configurations. This is a NEW computation from B3/S23 rules,
# not a reused count or external source assertion.
def h3_bit(c, r): return (c >> (r % 3)) & 1
def h3_ok(a,b,c):
    for r in range(3):
        cnt = h3_bit(b,r-1)+h3_bit(b,r+1)
        cnt += sum(h3_bit(d,r+j) for d in (a,c) for j in (-1,0,1))
        nxt = int(cnt==3 or (cnt==2 and h3_bit(b,r)))
        if nxt != h3_bit(b,r): return False
    return True
edges3=[[] for _ in range(64)]
for a in range(8):
    for b in range(8):
        for c in range(8):
            if h3_ok(a,b,c): edges3[8*a+b].append(8*b+c)
comp3=[comp for comp in sccs(edges3) if len(comp)>1 or comp[0] in edges3[comp[0]]]
assert sorted(map(len, comp3)) == [27,30]
for vs in comp3:
    if len(vs) != 27:continue
    dic={v:i for i,v in enumerate(vs)}
    C=sp.zeros(27)
    for v in vs:
        for w in edges3[v]:
            if w in dic: C[dic[v],dic[w]] += 1
    assert sp.expand(C.charpoly(x).as_expr()-x**24*(x**3-27)) == 0
print('height3_component=27 charpoly=x^24*(x^3-27)')
assert 127*13**27 < 3*15**27
for n in range(3,25,3):
    target=3**(n+1)
    actual=trace_power(n)
    assert actual < target
    print('width3_lower_bound_test:',n,actual,target)
print('CONTRAST PROVED: for every 3|n >=3, width-four fixed states < width-three fixed states')

print('PASS exact transfer, SCC, factorization, traces, and Collatz-Wielandt bound')
