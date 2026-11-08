#!/usr/bin/env python3
"""Exhaustive first-four-round census of unlabeled cographs (no external packages)."""
import itertools
import json
from collections import Counter
from functools import lru_cache

LEAF = ('x',)

@lru_cache(None)
def integer_partitions(n, low=1):
    if n == 0:
        return ((),)
    return tuple((i,) + p for i in range(low, n + 1)
                 for p in integer_partitions(n - i, i))

@lru_cache(None)
def cotrees(n, root):
    """All canonical cotrees on n leaves with given root U/J.

    Internal nodes have >=2 children, adjacent internal labels alternate,
    and the children of each node are a sorted multiset. Thus the
    canonical decomposition theorem gives exactly one per graph class.
    """
    if n == 1:
        return (LEAF,) if root == 'L' else ()
    opposite = 'J' if root == 'U' else 'U'
    result = []
    for parts in integer_partitions(n):
        if len(parts) < 2:
            continue
        multiplicities = Counter(parts)
        options = []
        for size, frequency in sorted(multiplicities.items()):
            pool = (LEAF,) if size == 1 else cotrees(size, opposite)
            options.append(itertools.combinations_with_replacement(pool, frequency))
        for choices in itertools.product(*options):
            children = tuple(sorted(itertools.chain.from_iterable(choices), key=repr))
            result.append((root,) + children)
    # The length equality also checks that no coding collision arises.
    assert len(set(result)) == len(result)
    return tuple(sorted(result, key=repr))

def adjacency(tree):
    if tree == LEAF:
        return (0,)
    label, *children = tree
    child_matrices = [adjacency(c) for c in children]
    n = sum(map(len, child_matrices))
    A = [0] * n
    offset = 0
    for block in child_matrices:
        for row, bits in enumerate(block):
            A[offset + row] |= bits << offset
        offset += len(block)
    if label == 'J':
        offset = 0
        allmask = (1 << n) - 1
        for block in child_matrices:
            blockmask = ((1 << len(block)) - 1) << offset
            for row in range(offset, offset + len(block)):
                A[row] |= allmask ^ blockmask
            offset += len(block)
    assert all(((row >> i) & 1) == 0 for i, row in enumerate(A))
    assert all(((A[i] >> j) & 1) == ((A[j] >> i) & 1)
               for i in range(n) for j in range(n))
    return tuple(A)

def canonical_colors(A):
    """One simultaneous color-signature refinement per strict step."""
    n = len(A)
    colors = (0,) * n
    trace = [1]
    while True:
        old_classes = sorted(set(colors))
        signatures = []
        for i in range(n):
            signature = (colors[i], tuple(sum(1 for j in range(n)
                if colors[j] == c and ((A[i] >> j) & 1)) for c in old_classes))
            signatures.append(signature)
        lookup = {p: index for index, p in enumerate(sorted(set(signatures)))}
        next_colors = tuple(lookup[s] for s in signatures)
        if len(set(next_colors)) == len(old_classes):
            return len(trace) - 1, tuple(trace)
        colors = next_colors
        trace.append(len(set(colors)))

def partition_splitting(A):
    """Independent equitable-partition refinement, directly splitting blocks."""
    n = len(A)
    blocks = [tuple(range(n))]
    steps = 0
    while True:
        old = tuple(blocks)
        new = []
        for B in old:
            buckets = {}
            for v in B:
                signature = tuple(sum((A[v] >> w) & 1 for w in C) for C in old)
                buckets.setdefault(signature, []).append(v)
            new.extend(tuple(group) for _, group in sorted(buckets.items()))
        if len(new) == len(old):
            return steps
        steps += 1
        blocks = new

def complement(tree):
    if tree == LEAF:
        return tree
    return (('J' if tree[0] == 'U' else 'U'),) + tuple(sorted(
        (complement(c) for c in tree[1:]), key=repr))

def has_induced(A, edges):
    for chosen in itertools.combinations(range(len(A)), 4):
        if sum(((A[chosen[i]] >> chosen[j]) & 1)
                for i in range(4) for j in range(i + 1, 4)) != len(edges):
            continue
        for pi in itertools.permutations(range(4)):
            if all(((A[chosen[pi[i]]] >> chosen[pi[j]]) & 1) ==
                   ((i, j) in edges or (j, i) in edges)
                   for i in range(4) for j in range(i + 1, 4)):
                return True
    return False

def code(tree):
    if tree == LEAF:
        return 'x'
    return tree[0] + '(' + ','.join(map(code, tree[1:])) + ')'

def main():
    rows = []
    witnesses = []
    for n in range(1, 12):
        classes = (LEAF,) if n == 1 else cotrees(n, 'U') + cotrees(n, 'J')
        assert len(set(classes)) == len(classes)
        distribution = Counter()
        maximum = -1
        max_codes = []
        for tree in classes:
            A = adjacency(tree)
            steps, trace = canonical_colors(A)
            assert partition_splitting(A) == steps, ('checker disagreement', n, code(tree))
            distribution[steps] += 1
            if steps > maximum:
                maximum = steps
                max_codes = [tree]
            elif steps == maximum:
                max_codes.append(tree)
        rows.append({'order': n, 'graphs': len(classes),
                     'round_distribution': dict(sorted(distribution.items())),
                     'max_strict_rounds': maximum, 'maximizers': len(max_codes)})
        print(n, len(classes), maximum, len(max_codes), dict(sorted(distribution.items())), flush=True)
        if n == 11:
            assert maximum == 4 and len(max_codes) == 2
            assert {w[0] for w in max_codes} == {'U', 'J'}
            u = next(w for w in max_codes if w[0] == 'U')
            j = next(w for w in max_codes if w[0] == 'J')
            assert complement(u) == j
            for w in (u, j):
                A = adjacency(w)
                assert has_induced(A, {(0, 1), (1, 2), (2, 3), (3, 0)})
                steps, trace = canonical_colors(A)
                witnesses.append({'cotree': code(w), 'connected': w[0] == 'J',
                                  'degrees': sorted(int(x.bit_count()) for x in A),
                                  'strict_rounds': steps, 'color_class_trace': trace,
                                  'induced_four_cycle': True})
    assert [r['graphs'] for r in rows] == [1,2,4,10,24,66,180,522,1532,4624,14136]
    assert [r['max_strict_rounds'] for r in rows] == [0,0,1,1,2,2,2,3,3,3,4]
    output = {'maximum_order_checked': 11, 'rows': rows, 'witnesses': witnesses,
              'second_implementation': 'direct block splitting agrees at every graph',
              'total_graphs': sum(r['graphs'] for r in rows)}
    with open('census.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, sort_keys=True, indent=2)
        f.write('\n')
    print('VERIFY_OK', output['total_graphs'])

if __name__ == '__main__':
    main()
