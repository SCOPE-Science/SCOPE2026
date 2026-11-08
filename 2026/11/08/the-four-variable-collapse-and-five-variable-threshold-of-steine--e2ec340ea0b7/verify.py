"""Independent finite incidence and pebble one-step profile checks for Steiner quadruple systems.

All outputs are computed from explicit blocks; no external packages.
"""
from itertools import combinations, product
from collections import defaultdict


def binary_sqs(m):
    n = 2 ** m
    blocks = {frozenset(t) for t in combinations(range(n), 4) if t[0] ^ t[1] ^ t[2] ^ t[3] == 0}
    return n, blocks


def mobius_sqs10():
    xy = list(product(range(3), repeat=2))
    indexed = {x: i for i, x in enumerate(xy)}
    blocks = set()
    # Each affine line, with infinity as the 4th point.
    for a, b, c in product(range(3), repeat=3):
        if a == b == 0:
            continue
        line = frozenset(indexed[x] for x in xy if (a*x[0]+b*x[1]) % 3 == c)
        assert len(line) == 3
        blocks.add(line | {9})
    # Each anisotropic quadratic circle has 4 points.
    for cx, cy, radius in product(range(3), range(3), (1, 2)):
        circle = frozenset(indexed[x] for x in xy if ((x[0]-cx)**2+(x[1]-cy)**2) % 3 == radius)
        assert len(circle) == 4
        blocks.add(circle)
    return 10, blocks


def verify_design(n, blocks):
    assert all(len(b) == 4 for b in blocks)
    assert len(blocks) == n*(n-1)*(n-2)//24
    counts = defaultdict(int)
    for block in blocks:
        for t in combinations(sorted(block), 3):
            counts[t] += 1
    assert len(counts) == n*(n-1)*(n-2)//6
    assert set(counts.values()) == {1}


def profile(t, blockset):
    # Equality and all arity-four positive relation positions, including repetitions.
    equality = tuple(t[i] == t[j] for i in range(len(t)) for j in range(i+1, len(t)))
    if len(t) < 4:
        return equality, ()
    positives = tuple(ids for ids in combinations(range(len(t)),4)
                      if frozenset(t[i] for i in ids) in blockset
                      and len({t[i] for i in ids}) == 4)
    return equality, positives


def catalog(n, blocks, width):
    # Profile of a tuple of currently placed pebbles must determine the
    # complete set of observable one-point extensions. Check this exhaustively.
    summaries = {}
    occurrences = defaultdict(int)
    total = 0
    for m in range(width):
        for t in product(range(n), repeat=m):
            p = profile(t, blocks)
            extensions = frozenset(profile(t + (x,), blocks) for x in range(n))
            key = m, p
            if key in summaries:
                assert summaries[key] == extensions, f'non-uniform extension: n={n}, width={width}, stationary={t}'
            else:
                summaries[key] = extensions
            occurrences[key] += 1
            total += 1
    return summaries, total


def main():
    designs = {'SQS8': binary_sqs(3), 'SQS10': mobius_sqs10(), 'SQS16': binary_sqs(4)}
    for name,(n,blocks) in designs.items():
        verify_design(n, blocks)
        print(f'{name}: order={n}, blocks={len(blocks)}, all {n*(n-1)*(n-2)//6} triples completed uniquely')
    for width in (4,5):
        cats = {}
        for name,(n,blocks) in designs.items():
            cats[name], count = catalog(n,blocks,width)
            print(f'{name}, width={width}: {count} stationary tuples, {len(cats[name])} profile types')
        for left,right in combinations(designs, 2):
            print(f'width={width}, {left} vs {right}: equal extension catalogues={cats[left] == cats[right]}')
        if width==4:
            assert cats['SQS8']==cats['SQS10']==cats['SQS16']
        else:
            assert cats['SQS8']!=cats['SQS10']==cats['SQS16']
            distinct_nonblock= lambda p: p[0] == (False,)*6 and not p[1]
            miss = [(key,ext) for key,ext in cats['SQS10'].items() if key[0]==4 and distinct_nonblock(key[1])]
            assert len(miss)==1
            key, ext = miss[0]
            assert len(ext)==9, f'expected 4 equalities + 4 completions + generic, got {len(ext)}'
            assert len(cats['SQS8'][key]) == 8
            print('width=5: nonblock stationary distinct four: SQS8 8 extension profiles; SQS10/16 9')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
