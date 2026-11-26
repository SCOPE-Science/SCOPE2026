"""Exhaustive binary order-five de Bruijn palindromic-length certificate.

Run: python3 verify.py
All 2048 rotation classes and 65536 rooted words are examined.
Uses only the Python standard library.
"""

from collections import Counter

ORDER = 5
EDGE_COUNT = 1 << ORDER
VERTICES = 1 << (ORDER - 1)


def euler_cycles():
    """Generate all Euler circuits, fixing the unique 00000 edge first."""
    ans = set()
    path = [0]

    def dfs(vertex, used):
        if len(path) == EDGE_COUNT:
            if vertex == 0:
                ans.add(''.join(str(e >> 4) for e in path))
            return
        for edge in (2 * vertex, 2 * vertex + 1):
            if (used >> edge) & 1 == 0:
                path.append(edge)
                dfs(edge & 15, used | (1 << edge))
                path.pop()

    dfs(0, 1)
    return ans


def switch_cycles():
    """Enumerate all 2^16 local bijections (incoming to outgoing)."""
    cycles = set()
    accepted_masks = 0
    for mask in range(1 << VERTICES):
        edge = 0
        visited = 0
        order = []
        while not (visited >> edge) & 1:
            visited |= 1 << edge
            order.append(edge)
            v = edge & 15
            incoming_index = edge >> 4
            edge = 2 * v + (incoming_index ^ ((mask >> v) & 1))
        if edge == 0 and len(order) == EDGE_COUNT:
            accepted_masks += 1
            cycles.add(''.join(str(e >> 4) for e in order))
    assert accepted_masks == len(cycles)
    return cycles


def pal_length_slices(w):
    """Shortest-palindromic-suffix recurrence, testing literal substrings."""
    dp = [0] + [len(w) + 1] * len(w)
    for end in range(1, len(w) + 1):
        for start in range(end):
            part = w[start:end]
            if part == part[::-1]:
                dp[end] = min(dp[end], dp[start] + 1)
    return dp[-1]


def pal_length_centers(w):
    """Independent center expansion with forward dynamic programming."""
    size = len(w)
    costs = [0] + [size + 1] * size
    for center in range(size):
        for parity in (0, 1):
            left, right = center, center + parity
            while left >= 0 and right < size and w[left] == w[right]:
                costs[right + 1] = min(costs[right + 1], 1 + costs[left])
                left -= 1
                right += 1
    return costs[-1]


EXPECTED_ROOTS = {4: 384, 5: 3554, 6: 18266,
                  7: 29118, 8: 12138, 9: 2030, 10: 46}
EXPECTED_MINMAX = {(4, 7): 48, (5, 7): 120, (5, 8): 350,
                   (5, 9): 64, (6, 7): 118, (6, 8): 742,
                   (6, 9): 74, (6, 10): 8, (7, 8): 254,
                   (7, 9): 154, (7, 10): 8, (8, 9): 92,
                   (8, 10): 14, (9, 10): 2}
EXCEPTIONAL = {
    '00000110100111110110001010111001',
    '00000100111010100011011111001011',
}


def run():
    from_euler = euler_cycles()
    from_switch = switch_cycles()
    assert from_euler == from_switch and len(from_euler) == 2048
    root_hist = Counter()
    cycle_hist = Counter()
    hard = set()
    for base in sorted(from_euler):
        assert len(base) == 32 and base[:5] == '00000'
        assert len({(base + base)[i:i + 5] for i in range(32)}) == 32
        values = []
        for start in range(32):
            word = base[start:] + base[:start]
            via_suffix = pal_length_slices(word)
            via_centers = pal_length_centers(word)
            assert via_suffix == via_centers, (base, start)
            values.append(via_suffix)
            root_hist[via_suffix] += 1
        pair = (min(values), max(values))
        cycle_hist[pair] += 1
        if pair[0] == 9:
            assert values.count(9) == 29 and values.count(10) == 3
            hard.add(base)
    assert dict(root_hist) == EXPECTED_ROOTS
    assert dict(cycle_hist) == EXPECTED_MINMAX
    assert hard == EXCEPTIONAL
    assert sum(root_hist.values()) == 65536
    assert sum(cycle_hist.values()) == 2048
    print('VERIFY_OK binary_debruijn_order5_cycles=2048 rooted_words=65536 '
          'independent_cycle_generators=2 independent_palindrome_parsers=2 '
          'root_spectrum=' + ','.join(f'{k}:{root_hist[k]}' for k in sorted(root_hist)) +
          ' exceptional_min9_cycles=2 minmax_cells=14')


if __name__ == '__main__':
    run()
