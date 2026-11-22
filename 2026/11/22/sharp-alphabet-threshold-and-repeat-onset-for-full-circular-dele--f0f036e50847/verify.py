"""Reproduce exact circular-deletion mask injectivity tests.

Only the mathematical deletion channel and finite checks are implemented.
Run with Python 3 standard library: python verify.py
"""
from itertools import combinations, product
from math import comb


def canonical_necklace(seq):
    """Lexicographically least cyclic rotation; reversal is never identified."""
    seq = tuple(seq)
    if not seq:
        return ()
    return min(seq[k:] + seq[:k] for k in range(len(seq)))


def descendants_with_multiplicity(source, deletions):
    """Map each deletion mask to its oriented output necklace."""
    n = len(source)
    outputs = {}
    for mask in combinations(range(n), deletions):
        erased = set(mask)
        survivor = tuple(source[i] for i in range(n) if i not in erased)
        outputs[mask] = canonical_necklace(survivor)
    return outputs


def marker_construction(t, n):
    assert 1 <= t < n
    # t unique marker labels, and t+1 distinct data labels in cyclic order
    return tuple(range(t)) + tuple(t + (j % (t+1)) for j in range(n-t))


def check_constructions():
    cases, masks = 0, 0
    for t in range(1, 6):
        for n in range(t+1, t+13):
            s = marker_construction(t, n)
            outputs = descendants_with_multiplicity(s, t)
            expected = comb(n, t)
            assert len(outputs) == expected
            assert len(set(outputs.values())) == expected, (t, n, s)
            cases += 1
            masks += expected
    return cases, masks


def check_critical_length():
    cases, masks = 0, 0
    # Complete, finite check of the necessity at the critical odd length.
    for t, q_values in [(1, range(1,4)), (2, range(1,6))]:
        n = 2*t+1
        for q in q_values:
            for source in product(range(q), repeat=n):
                outputs = descendants_with_multiplicity(source, t)
                full = len(set(outputs.values())) == comb(n, t)
                assert full == (len(set(source)) == n), (t, q, source)
                cases += 1
                masks += comb(n, t)
    return cases, masks


def check_nonmonotone_sample():
    # Independent finite diagnostic, NOT part of the universal theorem.
    results = {}
    for n, q in [(5, 4), (6, 4), (7, 4)]:
        expected = comb(n, 2)
        maximum = 0
        for source in product(range(q), repeat=n):
            count = len(set(descendants_with_multiplicity(source, 2).values()))
            maximum = max(maximum, count)
        results[n] = (maximum, expected)
    assert results == {5:(9,10), 6:(15,15), 7:(20,21)}
    return results


def main():
    c, m = check_constructions()
    print(f'CONSTRUCTION_PASS parameter_pairs={c} deletion_masks={m} t=1..5 n=t+1..t+12')
    c2, m2 = check_critical_length()
    print(f'CRITICAL_PASS complete_words={c2} deletion_masks={m2} t=1,2 q<=2t+1')
    out=check_nonmonotone_sample()
    print(f'FINITE_DIAGNOSTIC_PASS q=4 two-deletion necklace maxima={out}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
