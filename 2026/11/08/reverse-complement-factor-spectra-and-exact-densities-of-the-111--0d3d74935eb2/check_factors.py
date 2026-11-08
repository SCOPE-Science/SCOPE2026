#!/usr/bin/env python3
"""Exact finite-state certificate for reverse-complement factors of two pattern-parity words.

Runs using only Python's standard library. Every finite state is reachable by
an integer's binary expansion, and every starting position is represented.
"""
from collections import defaultdict, deque
from fractions import Fraction

EXPECTED = {
    3: {
        'A': {1: '7/48', 2: '3/128', 3: '1/128', 4: '1/128', 5: '1/128'},
        'B': {2: '5/384', 3: '5/384', 4: '1/256', 5: '1/256',
              6: '1/256', 7: '1/256'},
        'max_state': (0, 1, 2), 'max_residue': 8,
    },
    4: {
        'A': {1: '5/64', 2: '7/512', 3: '3/512', 4: '3/512',
              5: '1/512', 6: '1/512', 7: '1/512', 8: '1/512', 9: '1/512'},
        'B': {2: '3/512', 3: '3/512', **{j: '1/1024' for j in range(4, 16)}},
        'max_state': (0, 1, 6), 'max_residue': 16,
    },
}


def bit_pattern_parity(n, d):
    mask = (1 << d) - 1
    parity = 0
    while n:
        parity ^= int((n & mask) == mask)
        n >>= 1
    return parity


def get_states(d):
    q = 1 << (d - 1)
    def step(s, digit):
        a, b, residue = s
        marked = int(residue == q - 1)
        if digit == 0:
            return (a, a ^ marked, (2 * residue) % q)
        return (a ^ marked, b, (2 * residue + 1) % q)
    initial = (0, 0, 0)
    states = [initial]
    seen = {initial}
    for s in states:
        for digit in (0, 1):
            t = step(s, digit)
            if t not in seen:
                seen.add(t)
                states.append(t)
    # Reverse graph connectivity proves irreducibility.
    predecessors = defaultdict(list)
    for s in states:
        for digit in (0, 1):
            predecessors[step(s, digit)].append(s)
    reached = {initial}
    queue = deque([initial])
    while queue:
        for t in predecessors[queue.popleft()]:
            if t not in reached:
                reached.add(t)
                queue.append(t)
    assert len(reached) == len(states)
    assert step(initial, 0) == initial  # Period one, hence aperiodic.
    return sorted(states), step


def solve(A, b):
    """Rational Gauss-Jordan elimination, with independently checked solution."""
    n = len(b)
    original_A = [row[:] for row in A]
    original_b = b[:]
    table = [list(A[i]) + [b[i]] for i in range(n)]
    for k in range(n):
        pivot = next(j for j in range(k, n) if table[j][k] != 0)
        table[k], table[pivot] = table[pivot], table[k]
        scale = table[k][k]
        table[k] = [z / scale for z in table[k]]
        for j in range(n):
            if j != k:
                scale = table[j][k]
                if scale:
                    table[j] = [x - scale * y for x, y in zip(table[j], table[k])]
    x = [table[j][-1] for j in range(n)]
    assert all(sum(original_A[i][j] * x[j] for j in range(n)) == original_b[i] for i in range(n))
    return x


def state_weights(states, step):
    count = len(states)
    index = {s: j for j, s in enumerate(states)}
    matrix = [[Fraction(0) for _ in range(count)] for _ in range(count)]
    for s in states:
        for digit in (0, 1):
            matrix[index[s]][index[step(s, digit)]] += Fraction(1, 2)
    eq = [[matrix[j][i] - int(i == j) for j in range(count)] for i in range(count)]
    eq[-1] = [Fraction(1) for _ in range(count)]
    rhs = [Fraction(0) for _ in range(count)]
    rhs[-1] = Fraction(1)
    w = solve(eq, rhs)
    assert all(z > 0 for z in w)
    assert sum(w) == 1
    assert all(sum(w[i] * matrix[i][j] for i in range(count)) == w[j] for j in range(count))
    return {s: w[i] for i, s in enumerate(states)}


def block_bit(d, k, s, offset):
    """Value at 2**k*t+offset, based on (f(t), f(t+1), t mod 2**(d-1))."""
    block = 1 << k
    q = 1 << (d - 1)
    a, b, residue = s
    if offset >= block:
        offset -= block
        a = b
        residue = (residue + 1) % q
    crossing = 0
    for suffix_length in range(1, d):
        prefix_length = d - suffix_length
        if (residue % (1 << suffix_length) == (1 << suffix_length) - 1
                and offset >> (k - prefix_length) == (1 << prefix_length) - 1):
            crossing ^= 1
    return a ^ bit_pattern_parity(offset, d) ^ crossing


def complement(word):
    return ''.join('1' if c == '0' else '0' for c in word)


def verify(d):
    states, step = get_states(d)
    weights = state_weights(states, step)
    q = 1 << (d - 1)
    k = d + 1
    block = 1 << k
    reference = EXPECTED[d]
    assert len(states) == {3: 14, 4: 24}[d]
    # A separate direct-generation check of the block identity and state map.
    for t in range(512):
        actual = (bit_pattern_parity(t, d), bit_pattern_parity(t + 1, d), t % q)
        assert actual in weights
        assert step(actual, 0) == (bit_pattern_parity(2 * t, d),
                                    bit_pattern_parity(2 * t + 1, d), (2 * t) % q)
        assert step(actual, 1) == (bit_pattern_parity(2 * t + 1, d),
                                    bit_pattern_parity(2 * t + 2, d), (2 * t + 1) % q)
        for offset in range(2 * block):
            assert block_bit(d, k, actual, offset) == bit_pattern_parity(block * t + offset, d)
    enumerated_cases = 0
    all_types = set()
    for m in range(1, block // 2 + 1):
        n = 2 * m
        found = defaultdict(Fraction)
        occurrence_pairs = defaultdict(set)
        for s in states:
            for r in range(block):
                word = ''.join(str(block_bit(d, k, s, offset)) for offset in range(r, r + n))
                enumerated_cases += 1
                if all(word[j] != word[n - j - 1] for j in range(m)):
                    found[word] += weights[s] / block
                    occurrence_pairs[word].add((s, r))
        A = '0' * m + '1' * m
        B = '0' * (m - 1) + '10' + '1' * (m - 1)
        expected = {}
        for family, word in [('A', A), ('B', B)]:
            if m not in reference[family]:
                continue
            expected[word] = Fraction(reference[family][m])
            expected[complement(word)] = Fraction(reference[family][m])
        assert dict(found) == expected, (d, m, found, expected)
        all_types.update(found)
        if m == (1 << d) - 1:
            target = B
            assert occurrence_pairs[target] == {(reference['max_state'], reference['max_residue'])}
            other = tuple(1 - b if j < 2 else b for j, b in enumerate(reference['max_state']))
            assert occurrence_pairs[complement(target)] == {(other, reference['max_residue'])}
    assert len(all_types) == {3: 22, 4: 46}[d], (d, len(all_types))
    print(f'base_pattern={d} states={len(states)} finite_states_x_residues_x_lengths={enumerated_cases}'
          f' distinct_reverse_complement_factors={len(all_types)} max_length={(1 << (d + 1)) - 2}'
          f' terminal_density={Fraction(reference["B"][(1 << d)-1])}')


if __name__ == '__main__':
    verify(3)
    verify(4)
    print('VERIFY_OK')
