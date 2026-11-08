"""Exact direct-payoff check of a two-hub social-distance network formation classification.

Run: python verify_biclique_sdncg.py
Only the standard library is required. No finite test proves the infinite-family theorem.
"""
from itertools import product
from fractions import Fraction
from math import comb, factorial


def distances(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    sums = []
    for source in range(n):
        d = [-1] * n
        d[source] = 0
        queue = [source]
        for v in queue:
            for w in adj[v]:
                if d[w] == -1:
                    d[w] = d[v] + 1
                    queue.append(w)
        if len(queue) != n:
            return None
        sums.append(sum(d))
    return tuple(sums)


def edges_of(s):
    result = []
    for i, bits in enumerate(s):
        if bits & 1:
            result.append((0, i + 2))
        if bits & 2:
            result.append((1, i + 2))
    return result


def direct_stability(s, alpha):
    n = len(s) + 2
    present = set(edges_of(s))
    before = distances(n, present)
    if before is None:
        return False
    for u in range(2):
        for leaf in range(2, n):
            e = (u, leaf)
            if e in present:
                after = distances(n, present - {e})
                if after is None:
                    continue
                if any(after[v] - before[v] > alpha for v in e):
                    return False
            else:
                after = distances(n, present | {e})
                if all(before[v] - after[v] < alpha for v in e):
                    return False
    return True


def theorem_stability(s, alpha):
    a = s.count(1)
    b = s.count(2)
    c = s.count(3)
    k = len(s)
    if c == 0 or 0 in s:
        return False
    if c == 1:
        return alpha <= 2 * (min(a, b) + 1)
    if a == b == 0:
        return alpha >= 2
    return a == b and a > 0 and alpha == 2 * (a + 1)


def theorem_count(k, alpha):
    r = max(0, -(-alpha // 2) - 1)  # ceil(alpha/2) - 1, exact for Fraction
    count = k * sum(comb(k - 1, a) for a in range(r, k - r))
    if alpha >= 2:
        count += 1
    for t in range(1, (k - 2) // 2 + 1):
        if alpha == 2 * (t + 1):
            count += factorial(k) // (factorial(t)**2 * factorial(k - 2*t))
    return count


def potential(s, alpha):
    a = s.count(1)
    b = s.count(2)
    c = s.count(3)
    return alpha * c + 2 * (a + 1) * (b + 1)


def potential_checks(k, alpha):
    checks = 0
    for s in product(range(1, 4), repeat=k):
        if 3 not in s:
            continue
        old = distances(k + 2, edges_of(s))
        old_phi = potential(s, alpha)
        for i in range(k):
            for bit in (1, 2):
                ns = list(s)
                if s[i] & bit:
                    ns[i] ^= bit
                    after = distances(k + 2, edges_of(ns))
                    if after is None:
                        continue
                    improves = any(after[v] - old[v] > alpha for v in ((0 if bit == 1 else 1), i+2))
                else:
                    ns[i] |= bit
                    after = distances(k + 2, edges_of(ns))
                    improves = all(old[v] - after[v] < alpha for v in ((0 if bit == 1 else 1), i+2))
                assert improves == (potential(ns, alpha) > old_phi), (k, alpha, s, ns, improves)
                checks += 1
    return checks


def main():
    states_examined = 0
    alpha_profiles = 0
    stable_states_checked = 0
    for k in range(3, 8):
        all_states = list(product(range(4), repeat=k))
        for twice_alpha in range(1, 2*k + 9):
            alpha = Fraction(twice_alpha, 2)
            direct = 0
            claimed = 0
            for s in all_states:
                d = direct_stability(s, alpha)
                t = theorem_stability(s, alpha)
                assert d == t, (k, alpha, s, d, t)
                direct += d
                claimed += t
                states_examined += 1
            assert direct == claimed == theorem_count(k, alpha), (k, alpha, direct, claimed)
            alpha_profiles += 1
            stable_states_checked += direct
        print(f'k={k}: {len(all_states)} states, {2*k+8} parameter probes, all checks passed')
    pc = 0
    for k in range(3, 7):
        for twice_alpha in range(1, 2*k+7):
            pc += potential_checks(k, Fraction(twice_alpha, 2))
    print(f'PASS: {states_examined} direct payoff/profile tests, {alpha_profiles} exact count comparisons, {stable_states_checked} confirmed equilibrium instances, {pc} improving-move/potential comparisons')

if __name__ == '__main__':
    main()
