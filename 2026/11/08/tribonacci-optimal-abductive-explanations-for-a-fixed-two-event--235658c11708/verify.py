"""Reproduce exact AXp/CXp counts for bounded finite-trace response.
Uses only Python's standard library; full semantic checks are independent of the
combinatorial transversal construction on small traces.
"""
from itertools import product
from collections import Counter


def value(mask, n):
    # Request variables occupy bits 0..n-1; deliveries n..2n-1.
    return all(not ((mask >> i) & 1) or ((mask >> (n+i)) & 1)
               or ((mask >> (n+i+1)) & 1) for i in range(n-1))


def clauses(mask, n):
    edges = []
    for i in range(n-1):
        edge = set()
        if not (mask >> i) & 1:
            edge.add(i)
        if (mask >> (n+i)) & 1:
            edge.add(n+i)
        if (mask >> (n+i+1)) & 1:
            edge.add(n+i+1)
        assert edge  # Only compliant traces are considered.
        edges.append(frozenset(edge))
    return edges


def minimize(sets):
    return {s for s in sets if not any(t < s for t in sets)}


def transversals(edges):
    family = {frozenset()}
    for edge in edges:
        next_family = set()
        for s in family:
            if s & edge:
                next_family.add(s)
            else:
                for x in edge:
                    next_family.add(s | {x})
        family = minimize(next_family)
    return family


def minimal_clause_sets(edges):
    return minimize(set(edges))


def direct_semantic_explanations(mask, n, all_masks):
    false_traces = [other for other in all_masks if not value(other, n)]
    total = (1 << (2*n)) - 1
    axp_weak = set()
    cxp_weak = set()
    for submask in range(total+1):
        possible_failure_with_locked = any(((other ^ mask) & submask) == 0
                                           for other in false_traces)
        if not possible_failure_with_locked:
            axp_weak.add(submask)
        possible_failure_with_unlocked = any(((other ^ mask) & (~submask & total)) == 0
                                             for other in false_traces)
        if possible_failure_with_unlocked:
            cxp_weak.add(submask)
    def minsets(weak):
        return {m for m in weak if not any((s != m) and (s & m) == s for s in weak)}
    return minsets(axp_weak), minsets(cxp_weak)


def encode(family):
    return {sum(1 << i for i in s) for s in family}


def maximizing_mask(n, last_request=0):
    return sum(1 << (n+i) for i in range(n)) | (last_request << (n-1))


def spectrum(n):
    result = Counter()
    for bits in product([0,1], repeat=n):
        if bits[0] and bits[1] or bits[-2] and bits[-1]:
            continue
        if any(bits[j] and bits[j+1] and bits[j+2] for j in range(n-2)):
            continue
        size = sum(bits) + sum(not (bits[j] or bits[j+1]) for j in range(n-1))
        result[size] += 1
    return result


def run():
    direct_checks = 0
    for n in range(2,5):
        all_masks = range(1 << (2*n))
        for mask in all_masks:
            if not value(mask, n):
                continue
            edges = clauses(mask, n)
            predicted_axps = encode(transversals(edges))
            predicted_cxps = encode(minimal_clause_sets(edges))
            actual_axps, actual_cxps = direct_semantic_explanations(mask, n, all_masks)
            assert actual_axps == predicted_axps, ('AXp', n, mask)
            assert actual_cxps == predicted_cxps, ('CXp', n, mask)
            direct_checks += 1
    print('Independent semantic AXp/CXp checks:', direct_checks)
    expected = [3,5,9,17,31,57,105]
    model_checks = 0
    for n, expected_count in zip(range(2,9), expected):
        maximum = 0
        maximizing = []
        for mask in range(1 << (2*n)):
            if not value(mask, n):
                continue
            model_checks += 1
            k = len(transversals(clauses(mask, n)))
            if k > maximum:
                maximum = k
                maximizing = [mask]
            elif k == maximum:
                maximizing.append(mask)
        assert maximum == expected_count, (n,maximum)
        assert set(maximizing) == {maximizing_mask(n), maximizing_mask(n,1)}
        assert len(minimal_clause_sets(clauses(maximizing_mask(n),n))) == n-1
        assert sum(spectrum(n).values()) == maximum
        print('length', n, 'maximum AXps', maximum, 'maximizers', len(maximizing),
              'sizes', dict(sorted(spectrum(n).items())))
    print('Satisfying traces tested against sharp maximum:', model_checks)
    tribonacci = [0,0,3,5,9]
    for n in range(5,20):
        tribonacci.append(sum(tribonacci[-3:]))
    for n in range(2,20):
        assert sum(spectrum(n).values()) == tribonacci[n]
        if n >= 3:
            assert spectrum(n)[n-1] == 4
        assert min(spectrum(n)) == n//2
        assert max(spectrum(n)) == n-1
    print('All recurrence, size-spectrum, and top-coefficient checks passed: n=2..19')


if __name__ == '__main__':
    run()
