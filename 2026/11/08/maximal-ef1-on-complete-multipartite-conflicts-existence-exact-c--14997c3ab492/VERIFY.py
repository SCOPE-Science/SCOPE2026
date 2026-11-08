"""Exact checks for maximal EF1 allocations on multipartite conflict graphs.

Python 3.10+; no third-party dependencies. Tests are finite checks of the
closed formulas and constructive algorithm, not substitutes for the proofs.
"""
from itertools import product
from math import comb, factorial


def bipartite_fair_count(a, b, n):
    assert a >= 1 and b >= 1 and n >= 1
    m = a + b
    if m < n:
        full = factorial(n) // factorial(n - m)
    else:
        h, r = divmod(m, n)
        multiplier = factorial(a) * factorial(b)
        denominator = factorial(h) ** (n - r) * factorial(h + 1) ** r
        choices = 0
        for t in range(n + 1):
            u = a - t * h
            if 0 <= u <= t and 0 <= r - u <= n - t:
                choices += comb(n, t) * comb(t, u) * comb(n - t, r - u)
        full = multiplier * choices // denominator

    def discard_other_part(size):
        if size < n:
            return 0
        d, e = divmod(size, n)
        return (comb(n, e) * factorial(size)
                // (factorial(d) ** (n - e) * factorial(d + 1) ** e))

    return full, discard_other_part(a), discard_other_part(b)


def brute_bipartite(a, b, n, require_ef1):
    good = 0
    for labels in product(range(-1, n), repeat=a + b):
        counts = [0] * n
        feasible = True
        for j in range(n):
            if j in labels[:a] and j in labels[a:]:
                feasible = False
                break
            counts[j] = labels.count(j)
        if not feasible:
            continue
        if require_ef1 and max(counts) - min(counts) > 1:
            continue
        for i, v in enumerate(labels):
            if v != -1:
                continue
            opposing = labels[a:] if i < a else labels[:a]
            if any(j not in opposing for j in range(n)):
                feasible = False
                break
        if feasible:
            good += 1
    return good


def sterling_table(n):
    S = [[0] * (n + 1) for _ in range(n + 1)]
    S[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            S[i][j] = S[i - 1][j - 1] + j * S[i - 1][j]
    return S


def odd_bipartite_all_maximal(t):
    S = sterling_table(t)
    full = 0
    for i in range(1, t + 1):
        for j in range(1, t + 1 - i):
            full += (factorial(t) // factorial(t - i - j)) * S[t][i] * S[t][j]
    return full + 2 * factorial(t)


def multipartite_construct(parts, n):
    assert n >= 1 and parts and min(parts) >= 1
    M = sum(parts)
    if M <= n:
        labels = []
        next_agent = 0
        for size in parts:
            labels.append(list(range(next_agent, next_agent + size)))
            next_agent += size
        return labels

    order = sorted(range(len(parts)), key=lambda i: (-parts[i], i))
    largest = parts[order[0]]
    labels = [[-1] * size for size in parts]
    if largest >= n:
        d, e = divmod(largest, n)
        labels[order[0]] = [j for j in range(n) for _ in range(d + (j < e))]
        return labels

    chosen = []
    total = 0
    for i in order:
        chosen.append(i)
        total += parts[i]
        if total >= n:
            break
    pairs_needed = total - n
    chunks = []
    for i in chosen:
        remaining = list(range(parts[i]))
        while pairs_needed and len(remaining) >= 2:
            chunks.append((i, remaining[:2]))
            remaining = remaining[2:]
            pairs_needed -= 1
        chunks.extend((i, [v]) for v in remaining)
    assert pairs_needed == 0 and len(chunks) == n
    for j, (i, vertices) in enumerate(chunks):
        for v in vertices:
            labels[i][v] = j
    return labels


def check_multipartite(parts, n, labels):
    assert [len(L) for L in labels] == list(parts)
    sizes = [sum(label == j for L in labels for label in L) for j in range(n)]
    assert max(sizes) - min(sizes) <= 1
    for j in range(n):
        assert sum(j in L for L in labels) <= 1
    for i, L in enumerate(labels):
        if -1 not in L:
            continue
        for j in range(n):
            assert any(j in other for k, other in enumerate(labels) if k != i)


def run():
    tested_counts = 0
    for n in range(1, 6):
        for a in range(1, 6):
            for b in range(1, 6):
                if (n + 1) ** (a + b) > 3_000_000:
                    continue
                full, discard_a, discard_b = bipartite_fair_count(a, b, n)
                assert full + discard_a + discard_b == brute_bipartite(a, b, n, True)
                tested_counts += 1

    tested_constructions = 0
    for r in range(1, 6):
        for sizes in product(range(1, 8), repeat=r):
            if sum(sizes) > 20:
                continue
            for n in range(1, 11):
                labels = multipartite_construct(sizes, n)
                check_multipartite(sizes, n, labels)
                tested_constructions += 1

    assert odd_bipartite_all_maximal(3) == brute_bipartite(3, 3, 3, False)
    for t in (3, 5, 7, 9):
        full, keep_a, keep_b = bipartite_fair_count(t, t, t)
        assert full == 0 and keep_a + keep_b == 2 * factorial(t)
        print(f'K_{{{t},{t}}}, {t} agents: fair={keep_a + keep_b}, '
              f'all_maximal={odd_bipartite_all_maximal(t)}')
    print(f'PASS: {tested_counts} exact count comparisons; '
          f'{tested_constructions} constructive checks; '
          'one independent maximal-outcome count')


if __name__ == '__main__':
    run()
