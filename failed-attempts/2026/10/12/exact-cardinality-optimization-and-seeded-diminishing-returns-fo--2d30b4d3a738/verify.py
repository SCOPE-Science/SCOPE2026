"""Exact-rational verification of Rao diversity on ultrametric rooted trees.

Only the standard library is used. The theorem is proved separately;
finite tests here independently check the circuit formula and tree knapsack.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import random


def generate_tree(n, seed):
    rng = random.Random(seed)
    # Leaves have unique negative indices; internal nodes have larger indices.
    descendants = {-(i + 1): [i] for i in range(n)}
    heights = {-(i + 1): F(0) for i in range(n)}
    children = {}
    active = list(descendants)
    next_id = 0
    while len(active) > 1:
        a, b = rng.sample(active, 2)
        active.remove(a); active.remove(b)
        h = max(heights[a], heights[b]) + F(rng.randint(1, 7), rng.randint(1, 5))
        u = next_id; next_id += 1
        children[u] = ((a, h-heights[a]), (b, h-heights[b]))
        descendants[u] = descendants[a] + descendants[b]
        heights[u] = h
        active.append(u)
    return active[0], children, descendants, heights


def conductance(root, children, selected):
    @lru_cache(None)
    def c(u):
        if u not in children:
            return None if (-u-1) in selected else F(0)
        ans = F(0)
        for v, length in children[u]:
            z = c(v)
            if z is None:
                ans += 1 / length
            elif z:
                ans += z / (1 + length * z)
        return ans
    return c(root)


def dynamic_program(root, children, heights):
    @lru_cache(None)
    def dp(u):
        if u not in children:
            return {1: F(0)}  # Resistance from the selected leaf to itself.
        (a, la), (b, lb) = children[u]
        xa = {0: None, **dp(a)}
        xb = {0: None, **dp(b)}
        out = {}
        for ka, ra in xa.items():
            for kb, rb in xb.items():
                if not ka + kb:
                    continue
                ca = F(0) if not ka else 1 / (la + ra)
                cb = F(0) if not kb else 1 / (lb + rb)
                res = 1 / (ca + cb)
                k = ka + kb
                if k not in out or res < out[k]:
                    out[k] = res
        return out
    return dp(root)


def inverse_times_ones(A):
    n = len(A)
    augmented = [list(A[i]) + [F(1)] for i in range(n)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if augmented[i][j] != 0)
        augmented[j], augmented[pivot] = augmented[pivot], augmented[j]
        scale = augmented[j][j]
        augmented[j] = [z / scale for z in augmented[j]]
        for i in range(n):
            if i != j:
                k = augmented[i][j]
                if k:
                    augmented[i] = [x - k*y for x, y in zip(augmented[i], augmented[j])]
    return [row[n] for row in augmented]


def direct_max(root, children, descendants, heights, selected):
    H = heights[root]
    common = [[F(0) for _ in selected] for _ in selected]
    selected = sorted(selected)
    # Root-shared time equals sum of lengths whose descendant set contains both leaves.
    for u, cc in children.items():
        for v, ell in cc:
            desc = set(descendants[v])
            for a, i in enumerate(selected):
                for b, j in enumerate(selected):
                    if i in desc and j in desc:
                        common[a][b] += ell
    x = inverse_times_ones(common)
    assert all(v > 0 for v in x)
    r = 1 / sum(x)
    weights = [v * r for v in x]
    Q = sum(weights[a]*weights[b]*2*(H-common[a][b])
            for a in range(len(selected)) for b in range(len(selected)))
    assert Q == 2 * (H-r)
    return r, Q


def run():
    full_checks = dp_checks = marginal_checks = 0
    for n in range(2, 8):
        for seed in range(15):
            root, children, desc, heights = generate_tree(n, seed + 9000*n)
            dp = dynamic_program(root, children, heights)
            H = heights[root]
            by_card = {}
            cvalues = {}
            for k in range(1, n + 1):
                for tup in combinations(range(n), k):
                    selected = frozenset(tup)
                    C = conductance(root, children, selected)
                    assert C > 0
                    R = 1 / C
                    direct_r, direct_q = direct_max(root, children, desc, heights, selected)
                    assert R == direct_r and direct_q == 2*(H-R)
                    cvalues[selected] = C
                    by_card.setdefault(k, []).append(R)
                    full_checks += 1
            for k in range(1, n + 1):
                assert dp[k] == min(by_card[k])
                dp_checks += 1
            for a, Ca in cvalues.items():
                for b, Cb in cvalues.items():
                    if a < b:
                        for x in set(range(n)) - b:
                            Rdiff_A = 1/Ca - 1/cvalues[a | {x}]
                            Rdiff_B = 1/Cb - 1/cvalues[b | {x}]
                            assert Rdiff_A > Rdiff_B > 0, (a,b,x,Rdiff_A,Rdiff_B)
                            marginal_checks += 1
    print(f'VERIFY_OK direct_KKT_vs_conductance={full_checks} knapsack_optima={dp_checks} strict_marginal_triples={marginal_checks}')

if __name__ == '__main__':
    run()
