"""Integer-only verification for endpoint-started rotor walks on paths."""
from collections import Counter


def update(state, n):
    p, bits = state
    if p == 0:
        return (1, bits)
    if p == n - 1:
        return (n - 2, bits)
    flag = 1 << (p - 1)
    bits ^= flag  # toggle first
    return (p + 1 if bits & flag else p - 1, bits)


def recurrent_condition(state, n):
    p, bits = state
    for site in range(1, n - 1):
        right = bool(bits & (1 << (site - 1)))
        if site < p and not right:
            return False
        if site > p and right:
            return False
    return True


def predicted(mask, n):
    marked = [site for site in range(1, n - 1)
              if mask & (1 << (site - 1))]
    return 0 if not marked else 2 * sum(marked) - max(marked)


def verify(n):
    m = n - 2
    counts = Counter()
    for bits in range(1 << m):
        state, elapsed = (0, bits), 0
        while not recurrent_condition(state, n):
            state = update(state, n)
            elapsed += 1
            assert elapsed <= m * m
        assert elapsed == predicted(bits, n), (n, bits, elapsed)
        counts[elapsed] += 1
    assert len(counts) and sum(counts.values()) == 1 << m
    assert max(counts) == m*m and counts[m*m] == 1
    return counts


if __name__ == '__main__':
    for n in range(3, 19):
        counts = verify(n)
        print(f'n={n}, total={sum(counts.values())}, max={max(counts)}, maximizers={counts[max(counts)]}')
    print('ALL ENDPOINT CHECKS PASS')
