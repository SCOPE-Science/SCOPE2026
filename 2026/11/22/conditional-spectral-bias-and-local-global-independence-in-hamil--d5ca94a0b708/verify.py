"""Exact finite checks for conditional threshold-graph statistics.
Requires only Python 3 standard library; run with: python verify.py
"""
from itertools import product
from math import comb

checks = 0

def ballot(t, a):
    # Positive survival, starting at integer height a >= 1.
    low = (t + 1 - a + 1) // 2  # ceil((t+1-a)/2), valid for integers
    return sum(comb(t, j) for j in range(low, low + a) if 0 <= j <= t)


def hamiltonian(edges, n):
    # Independent subset dynamic program for an undirected Hamilton cycle.
    full = (1 << n) - 1
    reachable = {(1, 0)}
    for _ in range(1, n):
        nxt = set()
        for seen, end in reachable:
            for v in range(1, n):
                if not (seen >> v & 1) and (min(v, end), max(v, end)) in edges:
                    nxt.add((seen | (1 << v), v))
        reachable = nxt
    return any(seen == full and (0, end) in edges for seen, end in reachable)


def verify_words(L):
    global checks
    cnt = {}
    surv = 0
    for word in product((0, 1), repeat=L):
        n = L + 1
        edges = {(i, j) for j in range(1, n) for i in range(j) if word[j-1]}
        edge_count = len(edges)
        assert edge_count == sum((j+1)*bit for j, bit in enumerate(word))
        checks += 1
        # Direct graph diagnostics
        degrees = [sum((min(i,j),max(i,j)) in edges for j in range(n) if i != j)
                   for i in range(n)]
        universal = sum(d == n-1 for d in degrees)
        lowdeg = min(degrees)
        trailing = 0
        for bit in reversed(word):
            if bit == 1: trailing += 1
            else: break
        assert universal == (n if trailing == L else trailing)
        assert lowdeg == (n-1 if trailing == L else trailing)
        checks += 2
        s = 0
        area = 0
        positive = True
        for b in reversed(word):
            s += 2*b-1
            area += s
            if s <= 0: positive = False
        # Identity holds for all creation words, not only Hamiltonian ones.
        assert 4*edge_count == L*(L+1) + 2*area
        assert 2*(1+sum(word)) == L+2+s
        checks += 2
        if L <= 8:
            assert hamiltonian(edges, n) == positive
            checks += 1
        if positive:
            surv += 1
            cnt[trailing] = cnt.get(trailing,0)+1
            assert trailing >= 2
            checks += 1
    assert surv == comb(L-1,(L-1)//2)
    checks += 1
    for r in range(2,L):
        assert cnt.get(r,0) == ballot(L-r-1,r-1), (L,r,cnt.get(r,0),ballot(L-r-1,r-1))
        checks += 1
    assert cnt.get(L,0)==1
    checks += 1
    return surv

for L in range(2,13):
    verify_words(L)

# Entirely separate height-state recurrence for sum of positive-walk areas.
counts = {0: (1, 0)}
for L in range(1,80):
    new = {}
    for h, (num, area) in counts.items():
        for h2 in (h+1,h-1):
            if h2 <= 0: continue
            c,a = new.get(h2,(0,0))
            new[h2] = (c+num, a+area+num*h2)
    counts = new
    N = sum(v[0] for v in counts.values())
    T = sum(v[1] for v in counts.values())
    assert N == comb(L-1,(L-1)//2)
    if L%2:
        m = (L-1)//2
        T0 = (3*m+2)*4**m//2
    else:
        m = L//2
        T0 = 3*m*4**(m-1)
    assert T == T0, (L,T,T0)
    checks += 2

# Ballot reflected count checked independently by exhaustive individual steps.
for t in range(0,11):
    for a in range(1,8):
        total = 0
        for steps in product((-1,1),repeat=t):
            h=a
            for e in steps:
                h += e
                if h <= 0: break
            else: total += 1
        assert total == ballot(t,a), (t,a,total,ballot(t,a))
        checks += 1

print(f"PASS: {checks} independent finite assertions, 2..12 creation bits, ")
print("Hamiltonian subset DP through 9 vertices; area recurrence through 79 steps;")
print("ballot reflection through 10 steps and seven starting heights.")
