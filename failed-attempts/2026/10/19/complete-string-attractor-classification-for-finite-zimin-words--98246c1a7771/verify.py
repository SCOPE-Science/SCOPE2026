"""Finite independent checks for the complete string-attractor law of Zimin words."""
from itertools import product
from math import comb
from random import Random


def zimin_recursive(n):
    w = (1,)
    for j in range(2, n + 1):
        w = w + (j,) + w
    return w


def zimin_valuation(n):
    return tuple(1 + (i & -i).bit_length() - 1 for i in range(1, (1 << n)))


def coverage_masks(word):
    n = len(word)
    masks = {}
    for a in range(n):
        for b in range(a + 1, n + 1):
            key = word[a:b]
            masks[key] = masks.get(key, 0) | (((1 << (b-a)) - 1) << a)
    return list(masks.values())


def position_classes(word):
    return [[i for i, c in enumerate(word) if c == a] for a in range(1, max(word) + 1)]


def check_set(mask, coverage):
    return all(bool(mask & fm) for fm in coverage)


def letter_cover(mask, classes):
    return all(any(mask & (1 << i) for i in cls) for cls in classes)


def main():
    checks = 0
    exhaustive_sets = 0
    min_candidates = 0
    large_samples = 0
    rng = Random(104729)
    for n in range(1, 9):
        w = zimin_recursive(n)
        assert w == zimin_valuation(n)
        classes = position_classes(w)
        assert [len(c) for c in classes] == [1 << (n-j) for j in range(1,n+1)]
        assert len(w) == (1 << n)-1
        for j,cls in enumerate(classes, 1):
            r = (1 << (j-1))-1
            standard = w[cls[0]-r:cls[0]+r+1]
            assert len(standard) == (1 << j)-1
            for idx in cls:
                assert w[idx-r:idx+r+1] == standard
                checks += 1
        if n <= 6:
            cover = coverage_masks(w)
            min_expected = 1 << (n*(n-1)//2)
            counted = 0
            if n <= 4:
                for m in range(1 << len(w)):
                    assert check_set(m, cover) == letter_cover(m, classes)
                    exhaustive_sets += 1
            for selection in product(*classes):
                mask = sum(1 << p for p in selection)
                assert check_set(mask, cover)
                counted += 1
            assert counted == min_expected
            min_candidates += counted
            # Removing any of the represented symbols defeats its singleton factor.
            for sel in [tuple(c[0] for c in classes),tuple(c[-1] for c in classes)]:
                mask = sum(1 << p for p in sel)
                for p in sel:
                    assert not check_set(mask & ~(1 << p), cover)
        elif n <= 7:
            cover = coverage_masks(w)
            for _ in range(80):
                selected = tuple(rng.choice(c) for c in classes)
                mask = sum(1 << p for p in selected)
                assert check_set(mask, cover)
                large_samples += 1
    print('VERIFY_OK',f'exhaustive_subsets_n1_to4={exhaustive_sets}',
          f'optimal_candidates_n1_to6={min_candidates}',
          f'large_random_sets={large_samples}',
          f'center_neighborhood_checks={checks}',
          'whole_attractor_polynomial_derived_from_symbol_classes')


if __name__ == '__main__':
    main()
