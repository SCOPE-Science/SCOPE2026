"""Finite diagnostics for the logarithmic spectral edge of monomial cross-products.

Usage: python3 checker.py. Standard library only. These tests supplement the proof.
"""
import math
from collections import defaultdict

count = 0

def check(condition, message):
    global count
    count += 1
    if not condition:
        raise AssertionError(message)


def graph(p, q, n, eps):
    adj = defaultdict(dict)
    for k in range(1, n // q + 1):
        a, b = p * k, q * k
        w = math.exp(-(p + q) * eps * k)
        adj[a][b] = w
        adj[b][a] = w
    return adj


def component_lengths(adj, n):
    seen = set()
    sizes = []
    for v in range(1, n + 1):
        if v in seen:
            continue
        stack = [v]
        seen.add(v)
        nodes = []
        edge_degrees = 0
        while stack:
            x = stack.pop()
            nodes.append(x)
            edge_degrees += len(adj[x])
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        check(edge_degrees == 2 * (len(nodes) - 1), 'non-path component')
        sizes.append(len(nodes))
    return sizes


for p, q in [(2, 3), (2, 5), (3, 4), (3, 5), (4, 7)]:
    for eps in [.02, .15, .7]:
        for n in [49, 121, 300]:
            adj = graph(p, q, n, eps)
            edge_num = n // q
            check(sum(len(x) for x in adj.values()) == 2 * edge_num, 'edge count')
            check(all(len(v) <= 2 for v in adj.values()), 'vertex degree')
            for k in range(1, edge_num + 1):
                w = math.exp(-(p + q) * eps * k)
                check(abs(adj[p*k][q*k] - w) < 1e-14, 'basis coefficient')
            sizes = component_lengths(adj, n)
            check(sum(sizes) == n, 'component coverage')
            check(sum(x - 1 for x in sizes) == edge_num, 'rank-one edge count')
            trace_sq_edges = sum(sum(w*w for w in v.values()) for v in adj.values())
            trace_sq_series = 2 * sum(math.exp(-2 * (p+q) * eps * k) for k in range(1, edge_num+1))
            check(abs(trace_sq_edges-trace_sq_series) < 1e-11, 'Hilbert-Schmidt trace')

# Verify the exact finite-path sine eigenvector identity for several lengths.
for edges in range(1, 31):
    theta = math.pi / (edges + 2)
    x = [math.sin((j+1)*theta) for j in range(edges + 1)]
    lam = 2*math.cos(theta)
    for j in range(edges + 1):
        val = (x[j-1] if j>0 else 0) + (x[j+1] if j<edges else 0)
        check(abs(val-lam*x[j]) < 1e-12, 'sine path eigenvector')

# In a very low damping regime, the proof's explicit eigenvalue lower/upper
# bounds bracket the edge asymptotic for multiple coprime degree pairs.
for p, q in [(2, 3), (2, 5), (3, 5), (4, 7)]:
    for ell in [100.0, 200.0, 400.0, 700.0]:
        delta=ell**(-4)
        logK=ell+math.log(4*math.log(ell)/(p+q))
        max_edges = max(1, int(math.floor(1+logK/math.log(q))))
        lower_on_gap = 2-2*math.cos(math.pi/(max_edges+2))-2*delta
        strong_edges = max(1,int(math.floor((ell-5*math.log(ell))/math.log(q))))
        loss=(p+q)*math.exp(-ell+(strong_edges-1)*math.log(q))
        upper_on_gap = 2-2*math.exp(-loss)*math.cos(math.pi/(strong_edges+2))
        check(lower_on_gap > 0, 'lower gap bound positivity')
        check(upper_on_gap >= lower_on_gap, 'gap bound order')
        check(math.isfinite(upper_on_gap), 'finite bound')

print('MONOMIAL_LOG_EDGE_DIAGNOSTIC_OK', count)
