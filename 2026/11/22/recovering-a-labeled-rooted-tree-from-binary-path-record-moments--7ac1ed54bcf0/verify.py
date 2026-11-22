"""Independent finite exact checks for binary path-record tree reconstruction.

Run: python3 verify.py
No external packages are required.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from collections import defaultdict
import heapq
import math
import random

checks = 0

def check(condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(f"assertion {checks} failed")

def prufer_tree(seq, n):
    degree = [1] * n
    for x in seq: degree[x] += 1
    heap = [i for i in range(n) if degree[i] == 1]
    heapq.heapify(heap)
    adj = [[] for _ in range(n)]
    for x in seq:
        u = heapq.heappop(heap)
        adj[u].append(x); adj[x].append(u)
        degree[u] -= 1; degree[x] -= 1
        if degree[x] == 1: heapq.heappush(heap, x)
    u = heapq.heappop(heap); v = heapq.heappop(heap)
    adj[u].append(v); adj[v].append(u)
    parent = [-2] * n; parent[0] = -1
    order = [0]
    for u in order:
        for v in adj[u]:
            if parent[v] == -2:
                parent[v] = u
                order.append(v)
    check(len(order) == n)
    return parent

def path(parent, v):
    result = []
    while v >= 0:
        result.append(v)
        v = parent[v]
    return tuple(reversed(result))

def kernel(parent):
    n = len(parent)
    paths = [path(parent, v) for v in range(n)]
    depth = [len(p) - 1 for p in paths]
    means = [Q(1, d + 1) for d in depth]
    joint = {}
    covariance = {}
    for u in range(n):
        for v in range(u + 1, n):
            l = 0
            while l < min(len(paths[u]), len(paths[v])) and paths[u][l] == paths[v][l]:
                l += 1
            if l == min(len(paths[u]), len(paths[v])):
                j = means[u] * means[v]
            else:
                a = len(paths[u]) - l
                b = len(paths[v]) - l
                j = (Q(1, l+a) + Q(1, l+b)) / (l+a+b)
            joint[u,v] = j
            covariance[u,v] = j - means[u] * means[v]
            check((covariance[u,v] == 0) == (l == min(len(paths[u]),len(paths[v]))))
    return means, joint, covariance

def reconstruct(means, joint):
    n = len(means)
    depth = [next(d for d in range(n) if means[v] == Q(1,d+1)) for v in range(n)]
    check(depth.count(0) == 1)
    root = depth.index(0)
    recovered = [-2] * n; recovered[root] = -1
    for v in range(n):
        if v == root: continue
        candidates = [u for u in range(n) if depth[u] == depth[v]-1 and 
                      joint[min(u,v),max(u,v)] == means[u]*means[v]]
        check(len(candidates) == 1)
        recovered[v] = candidates[0]
    return recovered

def check_exact(parent):
    n = len(parent)
    means, joint, cov = kernel(parent)
    counts = [0] * n
    pairs = defaultdict(int)
    for permutation in permutations(range(n)):
        active = [all(permutation[v] < permutation[u] for u in path(parent,v) if u != v) for v in range(n)]
        for v in range(n): counts[v] += active[v]
        for u in range(n):
            for v in range(u+1,n): pairs[u,v] += active[u] and active[v]
    fac = math.factorial(n)
    for v in range(n): check(Q(counts[v],fac) == means[v])
    for (u,v), expected in joint.items(): check(Q(pairs[u,v],fac) == expected)
    check(reconstruct(means,joint) == parent)

for n in range(2, 6):
    for seq in product(range(n),repeat=n-2):
        check_exact(prufer_tree(seq,n))

rng = random.Random(763120)
for i in range(24):
    n = 6
    seq = tuple(rng.randrange(n) for _ in range(n-2))
    check_exact(prufer_tree(seq,n))

for n in range(2, 55):
    for rep in range(20):
        seq = tuple(rng.randrange(n) for _ in range(n-2))
        parent = prufer_tree(seq,n)
        means, joint, cov = kernel(parent)
        check(reconstruct(means, joint) == parent)
        for v in range(n):
            for u in range(n):
                if u == v: continue
                if len(path(parent,u)) == len(path(parent,v))-1 and \
                  u not in path(parent,v):
                    c = cov[min(u,v), max(u,v)]
                    check(c > Q(1, 2*n**3))

print(f"PASS: {checks} exact assertions, including every rooted labeled tree with root 0, n<=5; seeded n=6 and larger tests")
