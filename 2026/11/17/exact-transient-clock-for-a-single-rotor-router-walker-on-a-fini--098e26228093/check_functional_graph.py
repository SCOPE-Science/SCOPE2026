"""Independent functional-graph enumeration for one-chip rotor walks on rings.

Run: python3 check_functional_graph.py
No external Python dependencies.
"""
from collections import deque
from fractions import Fraction


def predicted(n, rotors, chip):
    k = rotors.bit_count()
    c = (chip - k) % n
    b = [(rotors >> ((c + j) % n)) & 1 for j in range(n)]
    s = sum(j * b[j] for j in range(n))
    if b[0] == 0:
        r = max((j for j in range(1, n) if b[j]), default=0)
        return 2*s - k*k - r
    ell = min((j for j in range(1, n) if not b[j]), default=n)
    return 2*s - k*k + ell


def run(n):
    states = n * (1 << n)
    nxt = [0] * states
    incoming = [0] * states
    for rotor in range(1 << n):
        for chip in range(n):
            rotor_after = rotor ^ (1 << chip)
            chip_after = (chip + (1 if (rotor_after >> chip) & 1 else -1)) % n
            src, dst = rotor*n + chip, rotor_after*n + chip_after
            nxt[src] = dst
            incoming[dst] += 1
    pending = deque(i for i, d in enumerate(incoming) if d == 0)
    transient = []
    while pending:
        s = pending.popleft()
        transient.append(s)
        t = nxt[s]
        incoming[t] -= 1
        if incoming[t] == 0:
            pending.append(t)
    depth = [0] * states
    for state in reversed(transient):
        depth[state] = depth[nxt[state]] + 1
    total = 0
    longest = 0
    maximizers = 0
    for state, actual in enumerate(depth):
        rotor, chip = divmod(state, n)
        expected = predicted(n, rotor, chip)
        assert actual == expected, (n, rotor, chip, actual, expected)
        total += actual
        if actual > longest:
            longest = actual
            maximizers = 1
        elif actual == longest:
            maximizers += 1
    assert longest == (n-1)*(n-2)//2
    assert maximizers == 2*n
    assert states - len(transient) == 2*n*n
    mean = Fraction(total, states)
    formula_mean = Fraction(n*n-5*n+8, 4) - Fraction(1, 2**(n-1))
    assert mean == formula_mean, (n, mean, formula_mean)
    print(f'n={n:2d} states={states:7d} max={longest:3d} maximizers={maximizers:3d} recurrent={states-len(transient):4d} mean={mean}')


if __name__ == '__main__':
    for n in range(3, 15):
        run(n)
    print('PASS functional graph, n=3..14')
