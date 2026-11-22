"""Exact finite certificate for the binary-partition residue-fiber theorem.

Requires Python 3 standard library only. Arithmetic in the finite automaton is
modulo 128; population identities are integer identities.
"""
from collections import deque
from math import comb

MOD = 128
ROOT = 'root'


def transform(state, bit):
    """Section of g(x)/(1-x)^2, in the integer-valued binomial basis."""
    if state == ROOT:
        return (1, 2) if bit == 0 else (2, 2)
    degree = len(state) - 1
    values = []
    for n in range(degree + 3):
        q = 2 * n + bit
        values.append(sum(a * comb(q + 2, j + 2)
                          for j, a in enumerate(state) if j <= q) % MOD)
    differences = [sum((-1) ** (j - i) * comb(j, i) * values[i]
                       for i in range(j + 1)) % MOD
                   for j in range(degree + 3)]
    while differences and differences[-1] == 0:
        differences.pop()
    return tuple(differences)


def construct():
    states = [ROOT]
    lookup = {ROOT: 0}
    transitions = []
    queue = deque([ROOT])
    while queue:
        state = queue.popleft()
        outs = []
        for bit in (0, 1):
            target = transform(state, bit)
            if target not in lookup:
                lookup[target] = len(states)
                states.append(target)
                queue.append(target)
            outs.append(lookup[target])
        transitions.append(tuple(outs))
        assert len(states) <= 100, 'Unexpected automaton enlargement'
    assert len(states) == len(transitions) == 100
    assert max(len(s) for s in states if isinstance(s, tuple)) == 5
    return states, transitions


def output(state):
    if state == ROOT:
        return 1
    return state[0] if state else 0


def forward(row, transitions):
    next_row = [0] * len(row)
    for i, weight in enumerate(row):
        if weight:
            a, b = transitions[i]
            next_row[a] += weight
            next_row[b] += weight
    return next_row


def backward(column, transitions):
    return [column[a] + column[b] for a, b in transitions]


def direct_counts(limit):
    # An independent coefficient construction from the finite Euler product.
    coeff = [0] * limit
    coeff[0] = 1
    power = 1
    while power < limit:
        for _ in range(2):
            for n in range(power, limit):
                coeff[n] = (coeff[n] + coeff[n - power]) % MOD
        power *= 2
    return coeff


def main():
    states, transitions = construct()
    assert all(transform(s, b) == states[transitions[i][b]]
               for i, s in enumerate(states) for b in (0, 1))
    # After a leading zero, the constant coefficient is unchanged;
    # binary representations of arbitrary length are therefore valid.
    assert all(output(states[transitions[i][0]]) == output(states[i])
               for i in range(len(states)))
    coeff = direct_counts(1 << 14)
    # Read the binary digits least significant first; leading zeroes allowed.
    for n, expected in enumerate(coeff):
        state = 0
        for bitpos in range(14):
            state = transitions[state][(n >> bitpos) & 1]
        assert output(states[state]) == expected, (n, expected)
    # For each target residue divisible by 16, certify the order-two
    # recurrence at every level >= 11, by Cayley-Hamilton in dimension 100.
    row_11 = [1] + [0] * (len(states) - 1)
    for _ in range(11):
        row_11 = forward(row_11, transitions)
    row_12 = forward(row_11, transitions)
    offsets = [2, -2, 1, 3, -1, 0, -2, -2]
    for j, offset in enumerate(offsets):
        target = 16 * j
        u = [int(output(s) == target) for s in states]
        count_11 = sum(a * b for a, b in zip(row_11, u))
        count_12 = sum(a * b for a, b in zip(row_12, u))
        assert count_11 == 2 ** 6 + offset
        assert count_12 == 2 ** 7 + offset
        tu = backward(u, transitions)
        ttu = backward(tu, transitions)
        z = [a - 3 * b + 2 * c for a, b, c in zip(ttu, tu, u)]
        probe = row_11[:]
        for k in range(len(states)):
            assert sum(a * b for a, b in zip(probe, z)) == 0, (target, k)
            probe = forward(probe, transitions)
    # Additional independent aggregate sanity checks at two larger depths.
    population = [1] + [0] * (len(states) - 1)
    for L in range(18):
        if L in (14, 17):
            hist = {r: sum(c for i, c in enumerate(population)
                           if output(states[i]) == r)
                    for r in range(0, 128, 16)}
            assert all(hist[r] == (2 ** (L - 5) + offsets[r // 16])
                       for r in hist)
        population = forward(population, transitions)
    # A state is stable for the target 112 if every binary continuation
    # gives the same indicator value. This proves a uniform error bound
    # for arbitrary aligned dyadic blocks, not only blocks from zero.
    flags = [int(output(s) == 112) for s in states]
    possible = [{flag} for flag in flags]
    for iteration in range(len(states) + 1):
        updated = [possible[i] | possible[a] | possible[b]
                   for i, (a, b) in enumerate(transitions)]
        if updated == possible:
            break
        possible = updated
    else:
        raise AssertionError('Reachability closure did not converge')
    unstable = [int(len(possible[i]) == 2) for i in range(len(states))]
    assert sum(unstable) == 37
    row_7 = [1] + [0] * (len(states) - 1)
    for _ in range(7):
        row_7 = forward(row_7, transitions)
    assert sum(a * b for a, b in zip(row_7, unstable)) == 10
    # If a 100-dimensional integer row sequence has 100 successive zero
    # terms after an annihilating polynomial, Cayley-Hamilton makes all
    # later terms zero. Here the difference of successive masses is zero.
    z = [a - b for a, b in zip(backward(unstable, transitions),
                                unstable)]
    probe = row_7[:]
    for k in range(len(states)):
        assert sum(a * b for a, b in zip(probe, z)) == 0, k
        probe = forward(probe, transitions)
    print('VERIFY_OK', 'states=100', 'independent_coefficients=16384',
          'Cayley_Hamilton_probes=900', 'residue_classes=8',
          'unstable_suffixes=10_from_depth=7', 'from_depth=11')


if __name__ == '__main__':
    main()
