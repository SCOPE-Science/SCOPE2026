"""Exact boundary-state transfer and independent small-instance checks.

Run: python3 verify.py
For independent full 16-vertex enumeration: c++ -O3 -std=c++17 exhaustive.cpp -o exhaustive && ./exhaustive
"""
from itertools import product
from math import exp, log

COLORS = (0, 1, 2)
TRIPLES = list(product(COLORS, repeat=3))


def boundary_transfer(old):
    out = {}
    for a, b, c in TRIPLES:
        terms = []
        for d in COLORS:
            a0, a1 = old[a, b, d]
            b0, b1 = old[b, c, d]
            c0, c1 = old[c, a, d]
            energy = int(d == a) + int(d == b) + int(d == c) + a0 + b0 + c0
            terms.append((energy, a1 * b1 * c1))
        best = min(e for e, _ in terms)
        out[a, b, c] = (best, sum(cnt for e, cnt in terms if e == best))
    return out


def graph(depth):
    adj = [set() for _ in range(3)]
    faces = [(0, 1, 2)]
    def link(a, b):
        adj[a].add(b)
        adj[b].add(a)
    link(0, 1); link(1, 2); link(2, 0)
    for _ in range(depth):
        future = []
        for a, b, c in faces:
            d = len(adj)
            adj.append(set())
            link(a, d); link(b, d); link(c, d)
            future.extend([(a, b, d), (b, c, d), (c, a, d)])
        faces = future
    return [(i, j) for i in range(len(adj)) for j in adj[i] if i < j], len(adj)


def small_brute(depth):
    edges, n = graph(depth)
    count, best = 0, len(edges) + 1
    for spins in product(COLORS, repeat=n):
        energy = sum(spins[u] == spins[v] for u, v in edges)
        if energy < best:
            best, count = energy, 1
        elif energy == best:
            count += 1
    return best, count


def main():
    old = {t: (0, 1) for t in TRIPLES}
    alpha, beta, gamma = 2, 1, 9
    for depth in range(0, 10):
        energy_by_state = {
            (a, b, c): (int(a == b) + int(b == c) + int(c == a) + e, cnt)
            for (a, b, c), (e, cnt) in old.items()
        }
        ground = min(v[0] for v in energy_by_state.values())
        deg = sum(v[1] for v in energy_by_state.values() if v[0] == ground)
        if depth <= 2:
            assert (ground, deg) == small_brute(depth)
        if depth >= 2:
            assert ground == (3 ** (depth-1) + 1) // 2
            assert deg == 18 * beta + 6 * gamma
            assert [old[t][0] for t in ((0,0,0), (0,0,1), (0,1,2))] == [ground-2, ground-1, ground]
            assert [old[t][1] for t in ((0,0,0), (0,0,1), (0,1,2))] == [alpha, beta, gamma]
            a2 = alpha ** 3 + 2 * beta ** 3
            b2 = beta ** 2 * (alpha + beta)
            c2 = 3 * beta ** 2 * gamma
            alpha, beta, gamma = a2, b2, c2
        old = boundary_transfer(old)
        print(f"generation={depth} ground_energy={ground} ground_count_digits={len(str(deg))}")
    # Stable calculation of the two positive entropy coefficients.
    s = log(2.0)
    entropy_c = log(2.0) / 9.0
    correction_k = s / 4.0
    for depth in range(2, 13):
        d = log(1 + 2 * exp(-3*s))
        eps = d - log(1 + exp(-s))
        entropy_c += d / 3 ** (depth+1)
        correction_k += eps / 2 ** (depth+1)
        s = 2*s + eps
    assert 0.17188293688 < 2*entropy_c < 0.17188293690
    assert 0.13396840665 < correction_k < 0.13396840667
    print('entropy_per_site=', 2*entropy_c)
    print('stretched_correction_k=', correction_k)
    print('ALL_TRANSFER_CHECKS_PASS')

if __name__ == '__main__':
    main()
