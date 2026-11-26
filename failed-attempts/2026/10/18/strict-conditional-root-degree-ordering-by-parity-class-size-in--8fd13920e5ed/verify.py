"""Exact small-order checks for the root-parity-size and degree law of Cayley trees.
Run: python3 verify_bipartition_degree.py
Only standard-library Python is required.
"""
from collections import Counter, deque
from fractions import Fraction
from itertools import product
from math import comb, factorial

checks = 0

def prufer_edges(seq, n):
    deg = [1] * n
    for k in seq:
        deg[k] += 1
    edges = []
    for k in seq:
        leaf = next(i for i in range(n) if deg[i] == 1)
        edges.append((leaf, k))
        deg[leaf] -= 1
        deg[k] -= 1
    leaves = [i for i in range(n) if deg[i] == 1]
    edges.append(tuple(leaves))
    return edges

def parity_class_and_degree(edges, n):
    adj = [[] for _ in range(n)]
    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)
    parity = [-1] * n
    parity[0] = 0
    todo = deque([0])
    while todo:
        i = todo.popleft()
        for j in adj[i]:
            if parity[j] == -1:
                parity[j] = 1 - parity[i]
                todo.append(j)
    assert -1 not in parity
    return sum(p == 0 for p in parity), len(adj[0]), parity, adj

for n in range(2, 8):
    ct = Counter()
    for seq in product(range(n), repeat=n-2):
        a, d, _, _ = parity_class_and_degree(prufer_edges(seq, n), n)
        ct[a, d] += 1
    assert sum(ct.values()) == n ** (n-2)
    checks += 1
    for a in range(1, n):
        b = n-a
        class_tree_ct = comb(n-1,a-1)*a**(b-1)*b**(a-1)
        assert sum(ct[a,d] for d in range(1,n)) == class_tree_ct
        checks += 1
        for d in range(1,n):
            expected = (Fraction(class_tree_ct, 1) * Fraction(comb(b-1,d-1) * (a-1)**(b-d), a**(b-1))) if 1<=d<=b else Fraction(0)
            # exponent zero at a=1 allowed (including 0**0=1)
            assert ct[a,d] == expected, (n,a,d,ct[a,d],expected)
            checks += 1
    # Adjacent stochastic order: tails decrease, with some strict inequality.
    for a in range(1,n-1):
        low = sum(ct[a,d] for d in range(1,n))
        high = sum(ct[a+1,d] for d in range(1,n))
        strict = False
        for t in range(2,n):
            lt = Fraction(sum(ct[a,d] for d in range(t,n)), low)
            ht = Fraction(sum(ct[a+1,d] for d in range(t,n)), high)
            assert lt >= ht
            strict |= lt > ht
            checks += 1
        assert strict
    # Mixed identity E[A D] = n-1, E[D] = 2-2/n.
    total = n**(n-2)
    assert Fraction(sum(a*d*k for (a,d),k in ct.items()), total) == n-1
    assert Fraction(sum(d*k for (a,d),k in ct.items()), total) == Fraction(2*n-2,n)
    checks += 2
    print(f'n={n}: {total} Cayley trees; conditional moments and order verified')

# Full class-degree multinomial laws for a fixed bipartition, n<=7.
for n in range(3,8):
    a = max(1,n//2)
    b = n-a
    A = set(range(a))
    B = set(range(a,n))
    observed = Counter()
    for seq in product(range(n), repeat=n-2):
        edges=prufer_edges(seq,n)
        if all((i in A) != (j in A) for i,j in edges):
            d = [0]*n
            for i,j in edges:
                d[i]+=1;d[j]+=1
            observed[tuple(x-1 for x in d)] += 1
    assert sum(observed.values()) == a**(b-1)*b**(a-1)
    checks += 1
    for sequence, count in observed.items():
        ar = sequence[:a]
        br = sequence[a:]
        assert sum(ar) == b-1 and sum(br)==a-1
        expected = Fraction(factorial(b-1)*factorial(a-1),1)
        for e in ar+br: expected /= factorial(e)
        assert count == expected, (n,a,sequence,count,expected)
        checks+=1
print('VERIFIED', checks, 'exact assertions')
