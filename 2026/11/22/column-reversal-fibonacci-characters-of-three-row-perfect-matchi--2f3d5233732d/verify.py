"""Exact integer verifier for a column-mirror character of grid tiling complexes.

Run with: python3 verify.py. No external packages required.
"""
from functools import lru_cache
from collections import defaultdict

VERTICAL = ((0, 0), (1, 3), (2, 6))  # tile selection bit, row-coverage mask
SYMBOLS = tuple((v, h) for v in range(4) for h in range(8))

@lru_cache(None)
def advance(state, forced_vertical, forced_horizontal):
    """Determinized tiling-state transition; state is a bitset of 3-bit carries."""
    output = 0
    for incoming in range(8):
        if not (state >> incoming) & 1:
            continue
        for tile_bit, covered in VERTICAL:
            if (tile_bit & forced_vertical) != forced_vertical or (covered & incoming):
                continue
            outgoing = 7 ^ (incoming | covered)
            if forced_horizontal & ~outgoing:
                continue
            output |= 1 << outgoing
    return output

@lru_cache(None)
def finish(state):
    """Alternating sum of forced vertical/axis-loop selections in last column."""
    total = 0
    for forced_vertical in range(4):
        for forced_loops in range(8):
            possible = False
            for incoming in range(8):
                if not ((state >> incoming) & 1):
                    continue
                for tile_bit, covered in VERTICAL:
                    if (tile_bit & forced_vertical) != forced_vertical or covered & incoming:
                        continue
                    actual_loops = 7 ^ (incoming | covered)
                    if not (forced_loops & ~actual_loops):
                        possible = True
                        break
                if possible:
                    break
            if possible:
                total += (-1) ** (forced_vertical.bit_count() + forced_loops.bit_count())
    return total

def make_matrix():
    states = [1]  # singleton incoming row-mask 0
    index = {1: 0}
    k = 0
    while k < len(states):
        state = states[k]
        for v, h in SYMBOLS:
            next_state = advance(state, v, h)
            if next_state and next_state not in index:
                index[next_state] = len(states)
                states.append(next_state)
        k += 1
    matrix = [[0] * len(states) for _ in states]
    for i, state in enumerate(states):
        for v, h in SYMBOLS:
            nxt = advance(state, v, h)
            if nxt:
                matrix[i][index[nxt]] += (-1) ** (v.bit_count() + h.bit_count())
    return states, matrix, [finish(state) for state in states]

def mat_vec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]

def row_mat(row, matrix):
    return [sum(row[i] * matrix[i][j] for i in range(len(row)))
            for j in range(len(row))]

def fibonacci(n):
    if n == -1:
        return 1
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def closed_trace(n):
    if n % 2 == 0:
        k = n // 2
        return (-1) ** (k - 1) * fibonacci(k - 2)
    k = (n - 1) // 2
    return (-1) ** k * fibonacci(k)

def direct_fixed_faces(n):
    """Independent original-grid domino enumeration for small cases."""
    width = 2 * n
    size = 3 * width
    edges = sorted(
        [tuple(sorted((r * width + c, (r + 1) * width + c)))
         for r in range(2) for c in range(width)]
        + [tuple(sorted((r * width + c, r * width + c + 1)))
           for r in range(3) for c in range(width - 1)]
    )
    edge_number = {e: i for i, e in enumerate(edges)}
    def mirror_vertex(v):
        return (v // width) * width + (width - 1 - v % width)
    mirror_edges = [edge_number[tuple(sorted((mirror_vertex(a), mirror_vertex(b))))]
                    for a, b in edges]
    orbits = []
    seen = set()
    for i in range(len(edges)):
        if i not in seen:
            orbit = frozenset((i, mirror_edges[i]))
            orbits.append(orbit)
            seen.update(orbit)
    incident = [[] for _ in range(size)]
    for i, (a, b) in enumerate(edges):
        incident[a].append(i)
        incident[b].append(i)
    tilings = []
    full = (1 << size) - 1
    def recurse(covered, tiles):
        if covered == full:
            tilings.append(frozenset(tiles))
            return
        unmatched = full ^ covered
        v = (unmatched & -unmatched).bit_length() - 1
        for i in incident[v]:
            a, b = edges[i]
            vertices = (1 << a) | (1 << b)
            if covered & vertices == 0:
                recurse(covered | vertices, tiles + (i,))
    recurse(0, ())
    orbit_masks = set()
    symmetric_masks = set()
    for tiling in tilings:
        mask = sum(1 << j for j, orbit in enumerate(orbits) if orbit <= tiling)
        orbit_masks.add(mask)
        if all(mirror_edges[i] in tiling for i in tiling):
            symmetric_masks.add(mask)
    # Check the finite shadow of the TU symmetric extension lemma.
    assert all(any((a & b) == a for b in symmetric_masks) for a in orbit_masks)
    fixed_faces = {0}
    for mask in orbit_masks:
        subset = mask
        while subset:
            fixed_faces.add(subset)
            subset = (subset - 1) & mask
    signed = sum((-1) ** face.bit_count() for face in fixed_faces)
    return len(tilings), len(fixed_faces), signed

def main():
    states, matrix, end_vector = make_matrix()
    assert len(states) == 14
    assert states == [1, 146, 130, 128, 144, 16, 2, 73, 8, 72, 64, 65, 9, 18]
    assert sum(v != 0 for row in matrix for v in row) == 38
    squared = mat_vec(matrix, mat_vec(matrix, end_vector))
    fourth = mat_vec(matrix, mat_vec(matrix, squared))
    residual = [a + b - c for a, b, c in zip(fourth, squared, end_vector)]
    row = [1] + [0] * (len(states) - 1)
    # The first 14 scalar moments vanish, so all vanish by Cayley-Hamilton.
    for _ in range(14):
        assert sum(row[i] * residual[i] for i in range(len(states))) == 0
        row = row_mat(row, matrix)
    row = [1] + [0] * (len(states) - 1)
    observed = []
    for n in range(1, 31):
        z = sum(row[i] * end_vector[i] for i in range(len(states)))
        trace = ((-1) ** n) * z
        assert trace == closed_trace(n), (n, trace, closed_trace(n))
        observed.append(trace)
        row = row_mat(row, matrix)
    print('determinized states: 14; nonzero weighted transitions: 38')
    print('exact 14-moment recurrence certificate: PASS')
    print('traces n=1..15:', observed[:15])
    for n in range(1, 7):
        tilings, faces, z = direct_fixed_faces(n)
        assert (-1) ** n * z == observed[n - 1]
        print(f'original-grid exhaustive n={n}: tilings={tilings}, fixed_faces={faces}, alternating_sum={z}: PASS')
    print('all checks passed')

if __name__ == '__main__':
    main()
