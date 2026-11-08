"""Exact finite checks of weighted Euclidean widths of coordinate-scaled order polytopes.

Run with Python 3. No external packages. These experiments are not an infinite proof.
"""
from itertools import combinations, product


def all_poset_closures(n):
    pairs = list(combinations(range(n), 2))
    seen = set()
    for bits in range(1 << len(pairs)):
        relation = {(i, j) for t, (i, j) in enumerate(pairs) if bits >> t & 1}
        changed = True
        while changed:
            new = relation | {(i, k) for i, j in relation for h, k in relation if j == h}
            changed = new != relation
            relation = new
        key = tuple(sorted(relation))
        if key not in seen:
            seen.add(key)
            yield relation


def check(n, relation, weights):
    subsets = range(1 << n)
    filters = [mask for mask in subsets
               if all(not(mask >> i & 1) or (mask >> j & 1) for i, j in relation)]
    chains = [mask for mask in subsets if mask and all(
        (i, j) in relation for i, j in combinations([i for i in range(n) if mask >> i & 1], 2))]
    H = max(sum(weights[i] for i in range(n) if mask >> i & 1) for mask in chains)
    heaviest = [mask for mask in chains if sum(weights[i] for i in range(n) if mask >> i & 1) == H]
    directions = set()
    for mask in heaviest:
        indices = [i for i in range(n) if mask >> i & 1]
        for sign in (-1, 1):
            u = tuple(sign * ((-1) ** j) if i in indices and (j := indices.index(i)) >= 0 else 0
                      for i in range(n))
            directions.add(u)
            values = [sum(u[i] for i in range(n) if F >> i & 1) for F in filters]
            assert max(values) - min(values) == 1, (n, relation, weights, u)
            assert sum(u[i] * u[i] * weights[i] for i in range(n)) == H
    for u in product((-1, 0, 1), repeat=n):
        if not any(u):
            continue
        values = [sum(u[i] for i in range(n) if F >> i & 1) for F in filters]
        width = max(values) - min(values)
        dual_squared = sum(u[i] * u[i] * weights[i] for i in range(n))
        assert H * width * width >= dual_squared, (n, relation, weights, u)
        if H * width * width == dual_squared:
            assert u in directions, (n, relation, weights, u, directions)
    return len(heaviest), len(filters)


def main():
    count, examples, contacts = 0, 0, 0
    for n in range(1, 6):
        for relation in all_poset_closures(n):
            for weights in [tuple([1] * n), tuple(range(1, n + 1)),
                            tuple(1 + (3 * i + 2) % 5 for i in range(n))]:
                num, F = check(n, relation, weights)
                count += 1
                examples += F
                contacts += num
    print('POSET_WEIGHTED_WIDTH_CHECKS_PASSED poset_weight_profiles=', count,
          'filter_sets=', examples, 'heaviest_chains=', contacts)


if __name__ == '__main__':
    main()
