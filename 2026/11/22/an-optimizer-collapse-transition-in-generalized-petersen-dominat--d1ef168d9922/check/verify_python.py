"""Complete finite certificate for [1,2]-domination trace complexity on P(8,2), P(9,2).
No package-specific dependencies. Python >= 3.9.
"""
from itertools import combinations
from functools import lru_cache
from collections import Counter


def family(n):
    adj = []
    for x in range(2 * n):
        if x < n:
            y = (x - 1) % n, (x + 1) % n, n + x
        else:
            i = x - n
            y = i, n + (i - 2) % n, n + (i + 2) % n
        adj.append(sum(1 << t for t in y))
    all_min = []
    for size in range(2 * n + 1):
        candidates = []
        for tup in combinations(range(2 * n), size):
            s = sum(1 << v for v in tup)
            if all((s >> x & 1) or 1 <= (s & adj[x]).bit_count() <= 2
                   for x in range(2 * n)):
                candidates.append(s)
        if candidates:
            return size, candidates
    raise AssertionError('No valid set')


def shattering(n, H):
    supports = set()
    coefficients = []
    for k in range(2 * n + 1):
        count = 0
        for q in combinations(range(2 * n), k):
            traces = {sum(((h >> v) & 1) << i for i, v in enumerate(q)) for h in H}
            if len(traces) == 1 << k:
                supports.add(sum(1 << v for v in q))
                count += 1
        coefficients.append(count)
        if count == 0:
            break
    facets = Counter()
    for s in supports:
        if not any((s | (1 << v)) in supports for v in range(2*n) if not s >> v & 1):
            facets[s.bit_count()] += 1
    return coefficients, facets, supports


def online(n, H):
    num = len(H)
    all_h = (1 << num) - 1
    positive = [sum((1 << i) for i, h in enumerate(H) if h >> v & 1)
                for v in range(2 * n)]
    witness = {}
    @lru_cache(None)
    def rank(pool):
        best = 0
        for v, mask in enumerate(positive):
            on = pool & mask
            off = pool & (all_h ^ mask)
            if on and off:
                d = 1 + min(rank(on), rank(off))
                if d > best:
                    best = d
                    witness[pool] = v
        return best
    depth = rank(all_h)
    def tree(pool, level):
        if not level:
            return None
        for v, mask in enumerate(positive):
            on = pool & mask
            off = pool & (all_h ^ mask)
            if on and off and rank(on) >= level - 1 and rank(off) >= level - 1:
                return (v, tree(off, level - 1), tree(on, level - 1))
        raise AssertionError('No full mistake tree')
    t = tree(all_h, depth)
    def check(t, pool):
        if t is None:
            assert pool
            return 1
        v, low, high = t
        off, on = pool & (all_h ^ positive[v]), pool & positive[v]
        assert off and on
        return check(low, off) + check(high, on)
    leaves = check(t, all_h)
    return depth, rank.cache_info().currsize, t, leaves


def orbit(n, s):
    images = set()
    for r in range(n):
        for flip in (0, 1):
            t = 0
            for x in range(2*n):
                if s >> x & 1:
                    side, i = divmod(x, n)
                    j = (r-i if flip else r+i) % n
                    t |= 1 << (side * n + j)
            images.add(t)
    return images


def main():
    outcomes = {}
    for n, expected_size, expected_num, expected_poly, expected_dim in [
        (8, 6, 248, [1, 16, 116, 464, 812, 32, 0], 6),
        (9, 6, 9, [1, 18, 81, 0], 2),
    ]:
        size, H = family(n)
        poly, facets, supports = shattering(n, H)
        dim, states, tree, leaves = online(n, H)
        assert (size, len(H), poly, dim) == (expected_size, expected_num, expected_poly, expected_dim)
        assert leaves == 1 << dim
        if n == 8:
            assert facets == Counter({4: 660, 5: 32})
            maximal = {s for s in supports if s.bit_count() == 5}
            a = sum(1 << v for v in [2, 4, 7, 8, 9])
            b = sum(1 << v for v in [3, 7, 8, 9, 11])
            assert len(orbit(n, a)) == len(orbit(n, b)) == 16
            assert maximal == orbit(n, a) | orbit(n, b)
        else:
            assert facets == Counter({2:81})
            periodic = set()
            for a in range(3):
                for b in range(3):
                    periodic.add(sum(1 << i for i in range(n) if i % 3 == a) +
                                 sum(1 << (n+i) for i in range(n) if i % 3 == b))
            assert set(H) == periodic
        outcomes[n] = (size, len(H), poly, dim, facets, states, leaves)
        print(f'n={n}; min_size={size}; optima={len(H)}; shattering={poly}; '
              f'VC={len(poly)-2}; Littlestone={dim}; facets={dict(facets)}; '
              f'online_states={states}; tree_leaves={leaves}')
    print('ALL EXACT CHECKS PASSED')

if __name__ == '__main__':
    main()
