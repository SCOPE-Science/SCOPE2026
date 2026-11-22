"""Exact exhaustive certificate for Frobenius on genus-four 2-isogeny kernels.

Run: python3 verify_kernel_spectra.py
Reads kernel_spectra.csv from the same directory. Standard library only.
"""
from collections import Counter
from functools import reduce
from itertools import combinations, product
from pathlib import Path
import csv
import math

N = 10
DIM = 8
FULL = (1 << N) - 1


def pair(a, b):
    """Weil pairing of even subsets modulo complements in binary coordinates."""
    return ((a & b).bit_count() + ((a.bit_count() & 1) * (b.bit_count() & 1))) % 2


def extend_subspaces():
    spaces = {(0,)}
    counts = []
    for level in range(1, 5):
        output = set()
        for space in spaces:
            members = set(space)
            for v in range(1, 1 << DIM):
                if v in members or any(pair(v, u) for u in space):
                    continue
                output.add(tuple(sorted(members | {u ^ v for u in space})))
        spaces = output
        counts.append(len(spaces))
        assert all(len(space) == 2 ** level for space in spaces)
    assert counts == [255, 5355, 11475, 2295]
    return spaces


def rref_subspaces():
    isotropic = set()
    all_four_planes = 0
    for pivots in combinations(range(DIM), 4):
        choice_lists = []
        for p in pivots:
            free = [j for j in range(p + 1, DIM) if j not in pivots]
            choice_lists.append([
                (1 << p) | sum((1 << j) for j, b in zip(free, bits) if b)
                for bits in product((0, 1), repeat=len(free))
            ])
        for basis in product(*choice_lists):
            all_four_planes += 1
            if any(pair(basis[i], basis[j]) for i in range(4) for j in range(i + 1, 4)):
                continue
            elems = tuple(sorted(reduce(int.__xor__,
                (basis[i] for i in range(4) if (m >> i) & 1), 0)
                for m in range(16)))
            isotropic.add(elems)
    assert all_four_planes == 200787
    assert len(isotropic) == 2295
    return isotropic


def even_subset(binary):
    return binary | ((binary.bit_count() % 2) << 8)


def act_vector(vector, permutation):
    subset = even_subset(vector)
    out = 0
    for i in range(N):
        if (subset >> i) & 1:
            out ^= 1 << permutation[i]
    if (out >> 9) & 1:
        out ^= FULL
    result = out & 255
    assert even_subset(result) == out
    return result


def perm_from_partition(parts):
    arr = list(range(N))
    index = 0
    for length in parts:
        for j in range(length):
            arr[index + j] = index + ((j + 1) % length)
        index += length
    assert index == N
    return arr


def integer_partitions(n, max_value=10):
    if n == 0:
        yield ()
    else:
        for m in range(min(n, max_value), 0, -1):
            for suffix in integer_partitions(n - m, m):
                yield (m,) + suffix


def permute_subspaces(permutation, spaces, index):
    action = [act_vector(v, permutation) for v in range(256)]
    assert len(set(action)) == 256
    # Check group action preserves both vector addition and the Weil pairing.
    assert all(action[v ^ w] == (action[v] ^ action[w])
               for v in range(256) for w in range(256))
    assert all(pair(action[v], action[w]) == pair(v, w)
               for v in range(256) for w in range(256))
    return [index[tuple(sorted(action[v] for v in space))] for space in spaces], action


def component_partition(spaces, index):
    generators = []
    for i in range(9):
        swap = list(range(N))
        swap[i], swap[i + 1] = swap[i + 1], swap[i]
        induced, _ = permute_subspaces(swap, spaces, index)
        generators.append(induced)
    label = [-1] * len(spaces)
    result = []
    for start in range(len(spaces)):
        if label[start] >= 0:
            continue
        component_id = len(result)
        queue = [start]
        label[start] = component_id
        for node in queue:
            for action in generators:
                next_node = action[node]
                if label[next_node] < 0:
                    label[next_node] = component_id
                    queue.append(next_node)
        result.append(set(queue))
    assert sorted(map(len, result)) == [945, 1350]
    return sorted(result, key=len)


def cycles(permutation, allowed):
    allowed = set(allowed)
    seen = set()
    result = Counter()
    for i in sorted(allowed):
        if i in seen:
            continue
        node = i
        length = 0
        while node not in seen:
            assert node in allowed
            seen.add(node)
            length += 1
            node = permutation[node]
        assert node == i
        result[length] += 1
    assert sum(k * v for k, v in result.items()) == len(allowed)
    return result


def encode_cycles(counter):
    return ' '.join(str(length) + ':' + str(count) for length, count in sorted(counter.items()))


def main():
    by_extension = extend_subspaces()
    by_rref = rref_subspaces()
    assert by_extension == by_rref
    spaces = sorted(by_rref)
    index = {space: i for i, space in enumerate(spaces)}
    first, second = component_partition(spaces, index)
    assert len(first) + len(second) == len(spaces) == math.prod([3, 5, 9, 17])

    results = []
    for partition in integer_partitions(N):
        action, vector_action = permute_subspaces(perm_from_partition(partition), spaces, index)
        a, b = cycles(action, first), cycles(action, second)
        total = a + b
        assert total == cycles(action, range(2295))
        results.append({
            'branch_partition': ' '.join(map(str, partition)),
            'rational_J2_points': str(sum(v == vector_action[v] for v in range(256))),
            'rational_kernels': str(total[1]),
            'all_kernels': encode_cycles(total),
            'orbit_945': encode_cycles(a),
            'orbit_1350': encode_cycles(b)
        })
    table_path = Path(__file__).with_name('kernel_spectra.csv')
    with table_path.open('r', encoding='utf-8', newline='') as f:
        expected = list(csv.DictReader(f))
    assert results == expected, 'A table entry differs from the exhaustive recomputation'
    assert len(results) == 42
    assert len({row['all_kernels'] for row in results}) == 29
    assert sorted({int(row['rational_kernels']) for row in results}) == [
        0, 1, 2, 3, 5, 6, 7, 9, 11, 15, 39, 45, 135, 151, 2295]
    pair_5 = next(r for r in results if r['branch_partition'] == '2 2 2 2 2')
    pair_4 = next(r for r in results if r['branch_partition'] == '2 2 2 2 1 1')
    assert (pair_5['rational_J2_points'], pair_5['rational_kernels']) == ('16', '151')
    assert (pair_4['rational_J2_points'], pair_4['rational_kernels']) == ('16', '39')
    # Five different irreducible monic quadratics over F_5.
    quadratics = [(0, 2), (0, 3), (1, 1), (1, 2), (2, 3)]
    assert len(set(quadratics)) == 5
    assert all((a*a - 4*b) % 5 in (2, 3) for a, b in quadratics)
    print('GENUS_FOUR_2295_LAGRANGIANS_42_TYPES_29_SPECTRA_VERIFIED')


if __name__ == '__main__':
    main()
