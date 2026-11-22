"""Finite, independent checks for partial-isomorphism extension profiles of partitions.

Run with Python 3.10+; only the standard library is needed.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb, factorial


def partitions(n, minimum=1):
    if n == 0:
        yield ()
        return
    for s in range(minimum, n + 1):
        for suffix in partitions(n - s, s):
            yield (s,) + suffix


def relabel(parts):
    labels = []
    for i, size in enumerate(parts):
        labels.extend([i] * size)
    return labels


def mathematical_formula(parts):
    # Named size multiplicities and the full group order.
    mult = Counter(parts)
    n = sum(parts)
    group_order = 1
    for s, count in mult.items():
        group_order *= factorial(s) ** count * factorial(count)
    if len(mult) == 1:
        return None, 0, group_order
    delta = min(abs(s - t) for s in mult for t in mult if s != t)
    numerator = sum(
        mult[s] * mult[s + delta] * comb(s + delta, delta)
        for s in mult if s + delta in mult
    )
    top_defect, rem = divmod(group_order * numerator, factorial(delta))
    assert rem == 0
    return delta, top_defect, group_order


def enumerate_formulas(parts):
    """Count all and globally extendible induced partial isomorphisms by types."""
    n = sum(parts)
    m = len(parts)
    D = {(): 1}
    # Independent coefficient extraction: each class chooses 0..s members.
    for s in parts:
        nextD = defaultdict(int)
        for alpha, count in D.items():
            nextD[alpha] += count
            for j in range(1, s + 1):
                temp = list(alpha) + [0] * (j - len(alpha))
                temp[j - 1] += 1
                nextD[tuple(temp)] += count * comb(s, j)
        D = dict(nextD)
    all_poly = [0] * (n + 1)
    for alpha, ways in D.items():
        k = sum((j + 1) * a for j, a in enumerate(alpha))
        aut_of_selected_type = 1
        for j, a in enumerate(alpha, 1):
            aut_of_selected_type *= factorial(a) * factorial(j) ** a
        all_poly[k] += ways * ways * aut_of_selected_type

    extend_poly = [1]
    for s, block_count in sorted(Counter(parts).items()):
        factor = [0] * (s * block_count + 1)
        def rec(j, remaining, counts):
            if j == s + 1:
                if remaining:
                    return
                a0 = counts[0]
                val = factorial(block_count) ** 2 // factorial(a0) ** 2
                for l in range(1, s + 1):
                    a = counts[l]
                    val = val * (comb(s, l) ** (2*a)) * (factorial(l) ** a)
                    val //= factorial(a)
                deg = sum(l * counts[l] for l in range(1, s + 1))
                factor[deg] += val
                return
            for a in range(remaining + 1):
                counts.append(a)
                rec(j + 1, remaining - a, counts)
                counts.pop()
        rec(0, block_count, [])
        new = [0] * (len(extend_poly) + len(factor) - 1)
        for i, a in enumerate(extend_poly):
            for j, b in enumerate(factor):
                new[i+j] += a * b
        extend_poly = new
    return all_poly, extend_poly


def enumerate_brute(parts):
    labels = relabel(parts)
    n = len(labels)
    vertices = range(n)
    sizes = dict(Counter(labels))
    # No use of the extension criterion: obtain global automorphisms by enumeration.
    full = [p for p in permutations(vertices) if all(
        (labels[i] == labels[j]) == (labels[p[i]] == labels[p[j]])
        for i in vertices for j in range(i)
    )]
    all_coeff = [0] * (n + 1)
    extend_coeff = [0] * (n + 1)
    for k in range(n + 1):
        global_restrictions = set()
        for domain in combinations(vertices, k):
            for g in full:
                global_restrictions.add((domain, tuple(g[i] for i in domain)))
        extend_coeff[k] = len(global_restrictions)
        for domain in combinations(vertices, k):
            for image in combinations(vertices, k):
                for mapped in permutations(image):
                    if all(
                        (labels[domain[i]] == labels[domain[j]]) ==
                        (labels[mapped[i]] == labels[mapped[j]])
                        for i in range(k) for j in range(i)
                    ):
                        all_coeff[k] += 1
    return all_coeff, extend_coeff, len(full)


def main():
    cases = 0
    for n in range(0, 7):
        for parts in partitions(n):
            ap, rp = enumerate_formulas(parts)
            ab, rb, group_order = enumerate_brute(parts)
            assert (ap, rp) == (ab, rb), (parts, ap, rp, ab, rb)
            delta, defect, group = mathematical_formula(parts) if parts else (None, 0, 1)
            assert group == group_order
            if delta is None:
                assert ap == rp, (parts, ap, rp)
            else:
                assert all(ap[k] == rp[k] for k in range(n - delta + 1, n + 1))
                assert ap[n-delta] - rp[n-delta] == defect
                assert defect > 0
            cases += 1
    print('EXHAUSTIVE_FORMULAS_AND_GLOBAL_RESTRICTIONS_OK', cases)
    # Larger near-total cases: exhaustive map enumeration without group enumeration.
    checked = 0
    for parts in partitions(7):
        delta, defect, group = mathematical_formula(parts)
        if delta is None:
            continue
        n = sum(parts); k = n - delta
        labels = relabel(parts)
        actual = 0
        for domain in combinations(range(n), k):
            for image in combinations(range(n), k):
                for mapped in permutations(image):
                    if not all((labels[domain[i]] == labels[domain[j]]) ==
                               (labels[mapped[i]] == labels[mapped[j]])
                               for i in range(k) for j in range(i)):
                        continue
                    if any(parts[labels[domain[i]]] != parts[labels[mapped[i]]]
                           for i in range(k)):
                        actual += 1
        assert actual == defect, (parts, actual, defect)
        checked += 1
    print('TOP_DEFECTS_SIZE_SEVEN_OK', checked)
    for parts, expected in [((1,2),4), ((1,3),9), ((2,5),400)]:
        delta, defect, _ = mathematical_formula(parts)
        assert defect == expected
    print('ALL_CHECKS_OK')

if __name__ == '__main__':
    main()
