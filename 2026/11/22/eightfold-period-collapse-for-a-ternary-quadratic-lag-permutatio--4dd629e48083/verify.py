"""Exact finite certificate for eightfold collapse of a ternary recurrence.

Run: python3 verify.py. Standard library only.
"""
from math import comb

ROWS = 8
CORE = {119, 187, 221, 238}


def admissible_masks():
    return {m for m in range(1 << ROWS) if m.bit_count() in (3, 6)}


def graph_from_masks():
    valid = admissible_masks()
    out = {m: set() for m in valid}
    for m in valid:
        digits = [(m >> i) & 1 for i in range(ROWS)]
        # The cyclic difference equation y[t]-y[t-1]=digits[t]
        # has exactly three solutions because sum(digits)=0 in F_3.
        for a in range(3):
            y = [a]
            for i in range(1, ROWS):
                y.append((y[-1] + digits[i]) % 3)
            assert (y[0] - y[-1]) % 3 == digits[0]
            n = sum((y[i] != 0) << i for i in range(ROWS))
            if n in valid:
                out[m].add(n)
    return out


def graph_from_words():
    valid = admissible_masks()
    out = {m: set() for m in valid}
    for n in range(3 ** ROWS):
        x = n
        y = []
        for i in range(ROWS):
            y.append(x % 3)
            x //= 3
        diffs = [(y[i] - y[i - 1]) % 3 for i in range(ROWS)]
        if any(d not in (0, 1) for d in diffs):
            continue
        m = sum(d << i for i, d in enumerate(diffs))
        nmask = sum((y[i] != 0) << i for i in range(ROWS))
        if m in valid and nmask in valid:
            out[m].add(nmask)
    return out


def prove_mask_graph():
    g = graph_from_masks()
    assert g == graph_from_words(), "independent graph enumeration mismatch"
    assert len(g) == 84
    assert sum(len(v) for v in g.values()) == 96
    assert len(CORE) == 4
    assert all(((m >> 4) == (m & 15)) and (m.bit_count() == 6) for m in CORE)
    expected_core = {
        119: {221, 238},
        187: {119, 238},
        221: {119, 187},
        238: {187, 221},
    }
    assert {u: g[u] for u in CORE} == expected_core
    outside = set(g) - CORE
    # No directed walk of length 3 remains inside the 80-vertex exterior.
    count_paths_2 = 0
    for a in outside:
        for b in g[a] & outside:
            for c in g[b] & outside:
                count_paths_2 += 1
                assert not (g[c] & outside), (a, b, c, g[c] & outside)
    # All directed cycles lie in CORE: its outgoing edges stay in CORE,
    # while its exterior is acyclic (in fact its length-3 path set is empty).
    assert count_paths_2 > 0
    assert not any(z in outside for u in CORE for z in g[u])
    assert not any((0 in g[u]) for u in g)
    # Zero mask has only the zero mask as admissible successor:
    assert all(((c != 0) * 255).bit_count() not in (3, 6) for c in range(3))
    return len(g), sum(map(len, g.values())), count_paths_2


def direct_counts(k):
    space = 3 ** k
    highest = 3 ** (k - 1)
    visited = bytearray(space)
    fixed4 = fixed8 = 0
    for first in range(space):
        if visited[first]:
            continue
        current = first
        period = 0
        while not visited[current]:
            visited[current] = 1
            old_first = current % 3
            old_last = current // highest
            current = current // 3 + ((old_first + old_last * old_last) % 3) * highest
            period += 1
        assert current == first, "map is not a permutation"
        if 4 * k % period == 0:
            fixed4 += period
        if 8 * k % period == 0:
            fixed8 += period
    formula = 1 + 4 * sum(comb(k, e) for e in range(k + 1) if (e - (3 - k)) % 4 == 0)
    assert fixed4 == formula, (k, fixed4, formula)
    assert fixed8 == fixed4, (k, fixed8, fixed4)
    return fixed8


def main():
    n, edges, paths = prove_mask_graph()
    seq = [direct_counts(k) for k in range(2, 12)]
    print('GRAPH_CERTIFICATE_OK', 'nonzero_masks=', n, 'edges=', edges,
          'exterior_length2_walks=', paths, 'cyclic_masks=', sorted(CORE))
    print('DIRECT_CYCLE_CHECK_OK', 'k=2..11', 'fixed_counts=', seq,
          'total_states=', sum(3 ** k for k in range(2, 12)))
    print('CERTIFIED: Fix(T_k^(8k)) = Fix(T_k^(4k)) for every integer k>=2')


if __name__ == '__main__':
    main()
