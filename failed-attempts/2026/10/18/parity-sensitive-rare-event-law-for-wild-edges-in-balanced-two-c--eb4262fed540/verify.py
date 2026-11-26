"""Independent exact checks for balanced two-colour complete-graph wild numbers.
No external data dependencies. Run with Python 3.10+.
"""
from itertools import combinations
from math import comb, exp


def components(n, edges):
    parent = list(range(n))
    def root(a):
        while a != parent[a]:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    for a, b in edges:
        a, b = root(a), root(b)
        if a != b:
            parent[a] = b
    return len({root(x) for x in range(n)})


def exact(n):
    all_edges = list(combinations(range(n), 2))
    N = len(all_edges)
    m = N // 2
    total = comb(N, m)
    counts = {}
    score = 0
    for inds in combinations(range(N), m):
        chosen = set(inds)
        E1 = [all_edges[j] for j in inds]
        E2 = [all_edges[j] for j in range(N) if j not in chosen]
        W = components(n, E1) + components(n, E2) - 2
        counts[W] = counts.get(W, 0) + 1
        score += W
    isolated = n * (comb(N-(n-1),m) + comb(N-(n-1),N-m)) / total
    observed = score / total
    return counts, total, observed, isolated


if __name__ == '__main__':
    print('Exhaustive balanced two-colour graphs:')
    for n in range(4, 8):
        counts,total,observed,isolated = exact(n)
        assert sum(counts.values()) == total
        assert observed >= isolated - 1e-12
        print(f'n={n} total={total} distribution={sorted(counts.items())} E(W)={observed:.12g} E(isolates)={isolated:.12g}')
    print('Second-order finite-population expansion:')
    for n in (24, 40, 81, 100, 102, 200, 202, 300):
        N = n*(n-1)//2
        m = N//2
        p = lambda mm: comb(N-(n-1),mm)/comb(N,mm)
        isol = n*(p(m)+p(N-m))
        lead = (4/exp(1))*n*2.0**(-n)
        eps = N % 2
        estimate = lead*(1+(1+6*eps)/(3*n*n))
        normalized = (isol/lead-1)*n*n
        assert abs(isol/estimate-1) < 1.0/n**3 * 100
        print(f'n={n} parity={eps} scaled_coefficient={normalized:.10f} predicted={(1+6*eps)/3:.10f} rel_error={isol/estimate-1:+.3e}')
    print('All exact enumeration and expansion checks passed.')
