"""Finite independent checks of the balance law for cross-partition widths.
Only verifies bounded examples; the general theorem has a separate proof.
"""
from itertools import combinations, product
from math import comb


def C(n, r):
    return comb(n, r) if 0 <= r <= n else 0


def cross_gap(z, selected):
    A = set(selected)
    return max(abs(z[i] - z[j]) for i in A for j in range(len(z)) if j not in A)


def nontrivial_component_size(z, threshold):
    n = len(z)
    parent = list(range(n))
    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i in range(n):
        for j in range(i+1, n):
            if abs(z[i] - z[j]) > threshold:
                parent[root(i)] = root(j)
    sizes = {}
    for i in range(n):
        r = root(i)
        sizes[r] = sizes.get(r, 0) + 1
    large = [s for s in sizes.values() if s >= 2]
    assert len(large) <= 1
    return large[0] if large else 0


def check(z):
    n = len(z)
    for threshold in [0, 1, 2, 4, 6, 10]:
        s = nontrivial_component_size(z, threshold)
        tails = []
        for p in range(1, n // 2 + 1):
            good = sum(cross_gap(z, A) <= threshold for A in combinations(range(n), p))
            total = C(n, p)
            if s:
                num = C(p, s) + C(n-p, s)
                den = C(n, s)
                assert good * den == num * total, (z, threshold, p, good, total, num, den)
            else:
                assert good == total
            tails.append((good, total))
        for (a,b), (c,d) in zip(tails,tails[1:]):
            assert a*d >= c*b


def main():
    profiles = 0
    for n in range(3, 8):
        # Distinct values, intervals of varying sizes; 2-5 random-free profiles per n
        for z in [tuple(range(n)), tuple(i*i for i in range(n)),
                  tuple(i*i+i//2 for i in range(n)), tuple((-1)**i * (i+1) for i in range(n))]:
            check(z)
            profiles += 1
    # Conditional strictness on a positive interval near the full range
    for n in range(4, 15):
        z = tuple(i*i+2*i for i in range(n))
        sortedz = sorted(z)
        lower = max(sortedz[-1]-sortedz[1],sortedz[-2]-sortedz[0])
        upper = sortedz[-1]-sortedz[0]
        assert lower < upper
        t = (lower + upper)/2
        assert nontrivial_component_size(z,t) == 2
        for p in range(1,n//2):
            q=n-p
            f_p = (C(p,2)+C(q,2))/C(n,2)
            f_next=(C(p+1,2)+C(q-1,2))/C(n,2)
            assert f_next < f_p
    print('BALANCED_BIPARTITE_WIDTH_CHECKS_PASSED', 'profiles=', profiles, 'strict_samples=',11)

if __name__ == '__main__': main()
