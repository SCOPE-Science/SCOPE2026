"""Exact finite-state proof certificate and independent arithmetic tests.

Only the standard library is needed. The finite-state identities certify an
infinite-length recurrence; direct finite samples are additional diagnostics.
"""
from collections import deque

START = ('N', 2)

def transition(state, digit):
    """Process next Zeckendorf position, starting with position 2."""
    if state[0] == 'N':
        phase = state[1]
        if digit == 0:
            return ('N', (phase + 1) % 4)
        return ('S', (phase + 1) % 4,
                int(phase in (2, 3)), 1, 1, True)
    _, phase, a, b, gap_mod4, adjacent = state
    if digit == 0:
        return ('S', (phase + 1) % 4, a, b,
                (gap_mod4 + 1) % 4, False)
    if adjacent:
        return None
    odd_t = int(gap_mod4 in (0, 1))
    epsilon = int(gap_mod4 in (0, 2))
    return ('S', (phase + 1) % 4,
            (odd_t * a + epsilon * b) % 2, a, 1, True)


def build_automaton():
    states = [START]
    seen = {START}
    queue = deque(states)
    while queue:
        state = queue.popleft()
        for digit in (0, 1):
            target = transition(state, digit)
            if target is not None and target not in seen:
                seen.add(target)
                states.append(target)
                queue.append(target)
    index = {s: i for i, s in enumerate(states)}
    edges = [tuple(index[v] for digit in (0, 1)
                   if (v := transition(s, digit)) is not None)
             for s in states]
    return states, edges


def Tv(edges, vector):
    return [sum(vector[j] for j in edge) for edge in edges]


def certificate():
    states, edges = build_automaton()
    assert len(states) == 84
    out = [int(s[0] == 'N' or s[2] == 1) for s in states]
    orbit = [out]
    for _ in range(5):
        orbit.append(Tv(edges, orbit[-1]))
    # Q(T) = T^5-2T^4+T^3-2T+2I.
    w = [v5 - 2*v4 + v3 - 2*v1 + 2*v0
         for v0, v1, v3, v4, v5
         in zip(orbit[0], orbit[1], orbit[3], orbit[4], orbit[5])]
    assert w[0] == 0
    Tw = Tv(edges, w)
    assert Tw[0] == 0
    assert Tv(edges, Tw) == w
    # These three identities imply e_start^T T^j Q(T)out=0 for all j>=0.
    B = [orbit[k][0] for k in range(6)]
    v = orbit[-1]
    for k in range(6, 36):
        v = Tv(edges, v)
        B.append(v[0])
    assert B[:12] == [1,2,3,4,5,8,13,20,29,44,69,108]
    assert all(B[k] == 2*B[k-1] - B[k-2] +
               2*B[k-4] - 2*B[k-5] for k in range(5, len(B)))
    return B


def fibonacci_values(limit):
    values = [1, 2]
    while values[-1] <= limit:
        values.append(values[-1] + values[-2])
    return values


def word_parity(n, values):
    word = [0] * len(values)
    for j in range(len(values)-1, -1, -1):
        if values[j] <= n:
            word[j] = 1
            n -= values[j]
    assert n == 0
    state = START
    for digit in word:
        state = transition(state, digit)
        assert state is not None
    return 1 if state[0] == 'N' else state[2]


def arithmetic_checks(B):
    limit = 17711
    values = fibonacci_values(limit)
    counts = [0] * limit
    counts[0] = 1
    for f in values:
        if f >= limit:
            break
        for n in range(limit-1, f-1, -1):
            counts[n] += counts[n-f]
    assert all(counts[n] % 2 == word_parity(n, values)
               for n in range(limit))
    fib = [1, 2]
    while fib[-1] < limit:
        fib.append(fib[-1] + fib[-2])
    assert all(sum(counts[n] % 2 for n in range(f)) == B[k]
               for k, f in enumerate(fib) if f <= limit)
    # A second independent computation uses bitset XOR over F_2.
    bits = 1
    for f in values:
        if f >= limit:
            break
        bits ^= bits << f
        bits &= (1 << limit)-1
    assert all(((bits >> n) & 1) == (counts[n] % 2)
               for n in range(limit))
    return limit

if __name__ == '__main__':
    seq = certificate()
    n = arithmetic_checks(seq)
    print('PASS: 84 reachable states, exact polynomial vector recurrence certificate')
    print('PASS: two boundary dot products and period-two residual vector')
    print(f'PASS: {n} direct Fibonacci partition parities plus bitset confirmation')
    print('PASS: Fibonacci-prefix parity counts through index', n)
    print('B_0,...,B_15 =', seq[:16])
