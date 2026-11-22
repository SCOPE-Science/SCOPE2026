"""Exact full-state bfloat16 logistic graphs, with no nonstandard dependencies.

Run: python3 verify_bfloat.py
"""
from bisect import bisect_left
from collections import Counter
from hashlib import sha256
import struct

SCALE = 1 << 133
LAST_INPUT = 0x3f80
LAST_INTERMEDIATE = 0x4080
VALUES = []
for j in range(LAST_INTERMEDIATE + 1):
    exponent, fraction = divmod(j, 128)
    VALUES.append(fraction if exponent == 0 else (128 + fraction) << (exponent - 1))
assert len(VALUES) == 16513
assert VALUES[0] == 0 and VALUES[LAST_INPUT] == SCALE and VALUES[LAST_INTERMEDIATE] == 4*SCALE
assert all(VALUES[j] < VALUES[j+1] for j in range(len(VALUES)-1))


def rounded_code(numerator, denominator=1):
    """Return code minimizing exact rational distance, midpoint even code."""
    assert 0 <= numerator <= denominator*VALUES[-1]
    high = bisect_left(VALUES, (numerator + denominator - 1)//denominator)
    if high == 0:
        return 0
    lower_gap = numerator - denominator*VALUES[high-1]
    higher_gap = denominator*VALUES[high] - numerator
    assert min(lower_gap, higher_gap) >= 0
    if lower_gap < higher_gap or (lower_gap == higher_gap and (high - 1) % 2 == 0):
        return high - 1
    return high


def rounded_code_independent(numerator, denominator=1):
    """Linear local neighbor test using Fraction for an independent rounder."""
    from fractions import Fraction
    exact = Fraction(numerator, denominator)
    low, high = 0, len(VALUES)
    while low < high:
        mid = (low+high)//2
        if VALUES[mid] < exact:
            low = mid + 1
        else:
            high = mid
    if low == 0:
        return 0
    candidates = (low-1, low)
    return min(candidates, key=lambda j: (abs(Fraction(VALUES[j])-exact), j & 1))


def bfloat_from_double(z):
    """Independent approximate check via float32 then explicit bfloat16 RNE."""
    raw32 = struct.unpack('>I', struct.pack('>f', float(z)))[0]
    upper, low = raw32 >> 16, raw32 & 0xffff
    return upper + int(low > 0x8000 or (low == 0x8000 and (upper & 1)))


def census(next_codes):
    n = len(next_codes)
    assert all(0 <= j < n for j in next_codes)
    label, depth = [-1]*n, [-1]*n
    cycles = []
    for start in range(n):
        if label[start] != -1:
            continue
        chain = []
        position = {}
        node = start
        while label[node] == -1 and node not in position:
            position[node] = len(chain)
            chain.append(node)
            node = next_codes[node]
        if node in position:
            core = chain[position[node]:]
            cycle_id = len(cycles)
            cycles.append(core)
            for j in core:
                label[j] = cycle_id
                depth[j] = 0
            chain = chain[:position[node]]
        for j in reversed(chain):
            successor = next_codes[j]
            label[j] = label[successor]
            depth[j] = depth[successor] + 1
    assert all(x >= 0 for x in label+depth)
    for a, b in enumerate(next_codes):
        assert label[a] == label[b]
        assert depth[a] == (0 if depth[a] == 0 else depth[b] + 1)
    for cycle in cycles:
        assert len(set(cycle)) == len(cycle)
        for t, j in enumerate(cycle):
            assert next_codes[j] == cycle[(t+1)%len(cycle)]
    basins = Counter(label)
    return sorted([(len(c), min(c), basins[i]) for i,c in enumerate(cycles)]), max(depth), sum(depth)


def peel_census(successor):
    """Independent Kahn leaf deletion and reverse-tail propagation."""
    from collections import deque
    n = len(successor)
    predecessors = [[] for _ in range(n)]
    indegree = [0]*n
    for u, v in enumerate(successor):
        predecessors[v].append(u)
        indegree[v] += 1
    remaining = [True]*n
    queue = deque(i for i, d in enumerate(indegree) if d == 0)
    while queue:
        u = queue.popleft()
        remaining[u] = False
        v = successor[u]
        indegree[v] -= 1
        if indegree[v] == 0:
            queue.append(v)
    tags = [-1]*n
    for u in range(n):
        if not remaining[u] or tags[u] != -1:
            continue
        cyc = []
        v = u
        while tags[v] == -1:
            tags[v] = -2
            cyc.append(v)
            v = successor[v]
        least = min(cyc)
        for v in cyc:
            tags[v] = least
    queue = deque(i for i in range(n) if remaining[i])
    while queue:
        v = queue.popleft()
        for u in predecessors[v]:
            if tags[u] == -1:
                tags[u] = tags[v]
                queue.append(u)
    assert -1 not in tags
    return tags


def outgoing():
    once = []
    staged = []
    for index in range(LAST_INPUT+1):
        v = VALUES[index]
        once.append(rounded_code(4*v*(SCALE-v), SCALE))
        k = rounded_code(SCALE-v)
        staged.append(rounded_code(4*v*VALUES[k], SCALE))
    return once, staged


def digest(codes):
    return sha256(b''.join(j.to_bytes(2, 'little') for j in codes)).hexdigest()


def verify():
    once, staged = outgoing()
    assert len(once) == len(staged) == 16257
    assert max(once) <= LAST_INPUT and max(staged) <= LAST_INPUT
    expected = [
        ([(1, 0, 4374), (1, 16192, 65), (11, 15804, 11818)], 81, 623656,
         '6efc7e1f5494acc14c02fdcdcfcf81312842f5c55761c31ff024202ef8e2964e'),
        ([(1, 0, 14797), (1, 16192, 65), (4, 16013, 1395)], 99, 773744,
         'e310df8a10ff661ac6d08e6dca42337365c254b48be4dd074f99f2a731ed7870'),
    ]
    for codes, target in zip((once, staged), expected):
        observed_census, longest, sum_depth = census(codes)
        assert (observed_census, longest, sum_depth, digest(codes)) == target, (
            observed_census, longest, sum_depth, digest(codes))
    labels_once = peel_census(once)
    labels_staged = peel_census(staged)
    cross = Counter(zip(labels_once, labels_staged))
    assert cross == Counter({
        (0,0): 4374,
        (15804,0): 10423,
        (15804,16013):1395,
        (16192,16192):65,
    }), cross
    difference = [i for i in range(len(once)) if once[i] != staged[i]]
    assert len(difference) == 275
    assert sum(s != t for s,t in zip(once,staged)) == 275
    # Independent exact Fraction implementation, all changing edges and a
    # all other encoded initial states as well.
    probes = set(difference) | {0, 1, 127, 128, 129, 16192, LAST_INPUT}
    probes.update(range(0, LAST_INPUT+1))
    for index in sorted(probes):
        v = VALUES[index]
        ref_once = rounded_code_independent(4*v*(SCALE-v), SCALE)
        k = rounded_code_independent(SCALE-v)
        ref_staged = rounded_code_independent(4*v*VALUES[k], SCALE)
        assert once[index] == ref_once and staged[index] == ref_staged
    # Independent float conversion sanity check for normal representative inputs.
    for index in range(0x3e00, LAST_INPUT+1, 13):
        val = struct.unpack('>f', struct.pack('>I', index << 16))[0]
        if bfloat_from_double(4*val*(1-val)) != once[index]:
            raise AssertionError(('independent float check mismatch', index))
    # Explicitly check midpoint ties on adjacent codes throughout the domain.
    for i in range(0, LAST_INPUT, 127):
        midpoint = VALUES[i]+VALUES[i+1]
        assert rounded_code(midpoint, 2) == (i if i%2==0 else i+1)
    print('BFLOAT16_EXACT_LOGISTIC_GRAPHS_OK')
    print('states=16257 edges_changed=275')
    print('once:', census(once), digest(once))
    print('staged:', census(staged), digest(staged))
    print('independent_fraction_probes=', len(probes))
    print('basin_cross_tab=', sorted(cross.items()))

if __name__ == '__main__':
    verify()
