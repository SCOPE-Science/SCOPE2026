"""Exact checks for isolated-site-indicator tomography on finite graphs.

Requires Python 3 standard library only. Run: python verify.py
"""
from fractions import Fraction
from itertools import combinations

CHECKS = 0

def check(cond, label):
    global CHECKS
    if not cond:
        raise AssertionError(label)
    CHECKS += 1

def graph_edges(n, bits):
    pairs = list(combinations(range(n), 2))
    return [p for i, p in enumerate(pairs) if (bits >> i) & 1]

def find_component_cliques(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    seen = set()
    components = []
    for i in range(n):
        if i in seen:
            continue
        stack, part = [i], set()
        while stack:
            v = stack.pop()
            if v in part:
                continue
            part.add(v)
            stack.extend(adj[v] - part)
        seen |= part
        components.append(part)
    return all(all((u == v) or v in adj[u] for u in C for v in C) for C in components), [len(C) for C in components]

def verify(n, bits, a, b):
    es = graph_edges(n, bits)
    edge_set = set(es)
    nbr = [set() for _ in range(n)]
    for u, v in es:
        nbr[u].add(v)
        nbr[v].add(u)
    total = b ** n
    means = [0] * n
    joint = [[0] * n for _ in range(n)]
    for mask in range(1 << n):
        retained = set(j for j in range(n) if mask & (1 << j))
        isolated = [v for v in retained if not (nbr[v] & retained)]
        weight = a ** len(retained) * (b - a) ** (n - len(retained))
        for i in isolated:
            means[i] += weight
            for j in isolated:
                joint[i][j] += weight
    check(sum(a ** k * (b - a) ** (n - k) for k in range(n + 1)) > 0, 'weight sanity')
    for i in range(n):
        d = len(nbr[i])
        check(means[i] == a * (b-a) ** d * b ** (n-d-1), ('mean', n,bits,i,a,b))
    for i,j in combinations(range(n),2):
        adjacent = (i,j) in edge_set
        c = len(nbr[i] & nbr[j])
        if adjacent:
            check(joint[i][j] == 0, ('edge joint',n,bits,i,j))
        else:
            pow_q = len(nbr[i]) + len(nbr[j]) - c
            expected = a*a*(b-a)**pow_q*b**(n-2-pow_q)
            check(joint[i][j] == expected, ('nonedge joint',n,bits,i,j))
        covnumerator = joint[i][j]*total - means[i]*means[j]
        check((covnumerator < 0) == adjacent, ('negative iff adjacent',n,bits,i,j))
        check((covnumerator > 0) == (not adjacent and c>0), ('positive iff dist2',n,bits,i,j))
        check((covnumerator == 0) == (not adjacent and c==0), ('zero iff dist>2',n,bits,i,j))
    is_cliques, sizes = find_component_cliques(n,es)
    has_dist2 = any(i!=j and j not in nbr[i] and (nbr[i]&nbr[j]) for i in range(n) for j in range(n))
    check(is_cliques == (not has_dist2), ('clique vs distance2',n,bits))
    if is_cliques and len(set(sizes)) == 1 and sizes[0]>=2:
        d=sizes[0]-1
        check(all(len(nb)==d for nb in nbr), 'same cliques degree')
    else:
        check(has_dist2 or len({len(nb) for nb in nbr})>1 or (not es), 'parameter identifiable reason')

for n in range(1,6):
    for bits in range(1 << (n*(n-1)//2)):
        for a,b in [(2,5),(3,7)]:
            verify(n,bits,a,b)

# Exact non-identifiability for any disjoint union of edges: p and 1-p.
for blocks in range(1,6):
    p1, p2 = Fraction(1,4), Fraction(3,4)
    mu1 = p1*(1-p1)
    mu2 = p2*(1-p2)
    check(mu1==mu2,('K2 ambiguity',blocks))
    check((1-2*mu1)**blocks == (1-2*mu2)**blocks,'same all-zero probability')

# K3 has a second p-value, algebraically: p=1/4, p'=(7-sqrt(13))/8.
# The polynomial f(x)=x(1-x)^2-f(1/4) factors as
# (x-1/4)*(x*x-7*x/4+9/16), with the nontrivial root in (1/3,1).
from math import sqrt
pprime = (7-sqrt(13))/8
check(1/3<pprime<1, 'second K3 parameter interval')
check(abs(pprime*(1-pprime)**2-Fraction(9,64))<1e-15, 'second K3 parameter equality')

print('VERIFY_OK', CHECKS, 'assertions (including two numeric root checks)')
