"""Direct finite verification of strong-odd colorings of crown graphs.

Run: python crown_strong_odd_verify.py
Uses Python standard library only. These computations do not replace the proof.
"""
from collections import Counter
from functools import lru_cache
from itertools import product
from math import comb, factorial


def crown(n):
    return [sum(1 << (n + j) for j in range(n) if j != i)
            for i in range(n)] + [sum(1 << j for j in range(n) if j != i)
                                    for i in range(n)]


def permitted(mask, neighbors):
    if any(mask & neighbors[v] for v in range(len(neighbors)) if mask >> v & 1):
        return False
    return all((mask & adj).bit_count() % 2 == 1 or (mask & adj) == 0
               for adj in neighbors)


def predicted_masks(n):
    result = {1 << j for j in range(2*n)}
    result.update((1 << j) | (1 << (j+n)) for j in range(n))
    if n % 2 == 0:
        result.update(((1 << n)-1, ((1 << n)-1) << n))
    return result


def falling(q, k):
    return factorial(q) // factorial(q-k) if q >= k else 0


def coefficient_count(n, q):
    return (sum(comb(n,s)*falling(q,2*n-s) for s in range(n+1))
            + (2*falling(q,n+1)+falling(q,2) if n % 2 == 0 else 0))


def partition_profile(n, masks):
    full = (1 << (2*n))-1
    classes_by_vertex = [[m for m in masks if m & (1 << j)] for j in range(2*n)]

    @lru_cache(None)
    def f(remaining):
        if remaining == 0:
            return ((0,1),)
        first = (remaining & -remaining).bit_length()-1
        total = Counter()
        for subset in classes_by_vertex[first]:
            if subset & remaining != subset:
                continue
            for k, multiplicity in f(remaining ^ subset):
                total[k+1] += multiplicity
        return tuple(sorted(total.items()))

    return dict(f(full)), f.cache_info()


def brute_colorings(n,q,neighbors):
    count = 0
    for colors in product(range(q), repeat=2*n):
        if any(colors[v] == colors[w] for v in range(2*n)
               for w in range(v+1,2*n) if neighbors[v] >> w & 1):
            continue
        valid = True
        for v in range(2*n):
            counts = [0]*q
            row = neighbors[v]
            while row:
                lowbit = row & -row
                w = lowbit.bit_length()-1
                counts[colors[w]] += 1
                row ^= lowbit
            if any(x > 0 and x%2 == 0 for x in counts):
                valid = False
                break
        count += valid
    return count


def main():
    tested_masks = 0
    for n in range(3,10):
        neighbors = crown(n)
        actual = {m for m in range(1,1 << (2*n)) if permitted(m,neighbors)}
        expected = predicted_masks(n)
        tested_masks += (1 << (2*n)) - 1
        assert actual == expected, (n,sorted(actual^expected))
        profile, cache = partition_profile(n,actual)
        expected_profile = Counter({2*n-s:comb(n,s) for s in range(n+1)})
        if n % 2 == 0:
            expected_profile[n+1] += 2
            expected_profile[2] += 1
        assert profile == dict(expected_profile), (n,profile,expected_profile)
        for q in range(1,2*n+3):
            assert sum(c*falling(q,k) for k,c in profile.items()) == coefficient_count(n,q)
        print(f'n={n} subsets={(1<<(2*n))-1} valid_classes={len(actual)} '
              f'partitions={sum(profile.values())} '
              f'min_colors={min(profile)} states={cache.currsize} OK')
    direct = 0
    for n, qs in ((3,(1,2,3,4,5)),(4,(1,2,3,4)),(5,(2,3,4))):
        neighbors = crown(n)
        for q in qs:
            actual = brute_colorings(n,q,neighbors)
            predicted = coefficient_count(n,q)
            assert actual == predicted, (n,q,actual,predicted)
            direct += q**(2*n)
            print(f'brute n={n} q={q} assignments={q**(2*n)} valid={actual} OK')
    print(f'ALL_OK graph_subsets={tested_masks} direct_assignments={direct}')

if __name__ == '__main__':
    main()
