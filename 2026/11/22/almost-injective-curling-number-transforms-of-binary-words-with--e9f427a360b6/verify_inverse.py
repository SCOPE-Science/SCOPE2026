"""Independent exhaustive inverse-image grouping from the proved three-gap formula.
Run with Python 3, no third-party dependencies.
"""
from collections import defaultdict
from math import comb


def encode(a, b, c):
    result = []
    for i in range(a):
        result.append(i + 1)
    result.append(1)
    for j in range(b):
        result.append(j + 1)
    result.append(1 + int(a >= b))
    for k in range(c):
        if k == 0 and b > 0 and a + 1 >= b:
            result.append(2)
        else:
            result.append(k + 1)
    return bytes(result) if max(result) <= 255 else tuple(result)


def inverse_classes(n):
    groups = defaultdict(list)
    for a in range(n - 1):
        for b in range(n - a - 1):
            c = n - 2 - a - b
            groups[encode(a, b, c)].append((a, b, c))
    return groups


def run():
    examples = {}
    for n in range(2, 101):
        groups = inverse_classes(n)
        doubles = sorted(sorted(v) for v in groups.values() if len(v) > 1)
        expected = {2: 0, 3: 0, 4: 3, 5: 1, 6: 1}.get(n, 2)
        assert len(doubles) == expected, (n, doubles)
        assert all(len(v) < 3 for v in groups.values())
        assert len(groups) == comb(n, 2) - expected
        if n >= 7:
            assert doubles == sorted([
                sorted([(n - 4, 1, 1), (n - 4, 2, 0)]),
                sorted([(n - 5, 1, 2), (n - 5, 2, 1)]),
            ]), (n, doubles)
        if n in (4, 5, 6, 7):
            examples[n] = doubles
    print('PASS independent inverse grouping; n=2..100')
    print(f'image_counts_n4_n5_n6_n7={[len(inverse_classes(n)) for n in [4,5,6,7]]}')
    print(f'doubleton_fibers_n4_n5_n6_n7={examples}')
    print('all_nontrivial_fibers_have_size_two=True')


if __name__ == '__main__':
    run()
