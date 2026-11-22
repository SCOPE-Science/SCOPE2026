"""Exact integer certificate for cyclic majority-rule singleton-predecessor counts.

Run with Python 3, no third-party dependencies.  Matrices encode the
number of labelled closed walks, saturated at 2.
"""
from collections import deque

PAIR = [(a, b) for a in (0, 1) for b in (0, 1)]

def letter_matrix(symbol):
    out = [0] * 16
    for i, (left, middle) in enumerate(PAIR):
        for j, (next_middle, right) in enumerate(PAIR):
            if middle == next_middle and int(left + middle + right >= 2) == symbol:
                out[4*i+j] = 1
    return tuple(out)

def multiply_cap2(a, b):
    return tuple(min(2, sum(a[4*i+k]*b[4*k+j] for k in range(4)))
                 for i in range(4) for j in range(4))

def construct():
    generators = tuple(letter_matrix(b) for b in (0, 1))
    assert generators[0] != generators[1]
    identity = tuple(int(i == j) for i in range(4) for j in range(4))
    states, indices, edges = [identity], {identity: 0}, []
    queue = deque([0])
    while queue:
        i = queue.popleft()
        successors = []
        for generator in generators:
            product = multiply_cap2(states[i], generator)
            if product not in indices:
                indices[product] = len(states)
                states.append(product)
                queue.append(indices[product])
            successors.append(indices[product])
        edges.append(tuple(successors))
    return states, edges

# D(z) = sum_{i=0}^{18} DENOM[i] z^i
DENOM = (1, 0, -1, 0, -1, -4, -3, 0, 0, -4, -2,
         6, 7, 2, 2, 4, 1, -2, -1)
# P(z) = sum_{i=0}^{20} NUMER[i] z^i
NUMER = (0, 2, 4, -2, 2, 18, 8, -14, -6, 36, 12,
         -78, -76, 0, -10, -52, -4, 44, 16, -6, -2)


def main():
    states, edges = construct()
    assert len(states) == 476, len(states)
    final = [int(sum(s[5*i] for i in range(4)) == 1) for s in states]
    assert sum(final) == 136

    def advance_on_states(v):
        # From any state, the number of accepted suffixes of length k+1.
        return [v[a] + v[b] for (a, b) in edges]

    # All length-21 suffix counts: exact 476-coordinate polynomial identity.
    vs = [final]
    for _ in range(21):
        vs.append(advance_on_states(vs[-1]))
    for state in range(len(states)):
        residue = sum(coefficient * vs[21-i][state]
                      for i, coefficient in enumerate(DENOM))
        assert residue == 0, ('vector recurrence', state, residue)

    u = [v[0] for v in vs]
    assert u[0] == 0
    for n in range(21):
        numerator_coefficient = sum(DENOM[i]*u[n-i]
                                    for i in range(min(n, 18)+1))
        assert numerator_coefficient == NUMER[n], (n, numerator_coefficient)

    # Independent forward DP through 120 lengths.
    counts = [1] + [0]*(len(states)-1)
    generated = []
    for n in range(1, 121):
        nxt = [0]*len(states)
        for s, weight in enumerate(counts):
            if weight:
                for t in edges[s]:
                    nxt[t] += weight
        counts = nxt
        generated.append(sum(counts[s] for s in range(len(states)) if final[s]))
    assert generated[:12] == [2, 4, 0, 6, 20, 26, 28, 38, 108, 182, 242, 330]
    for n in range(21, 121):
        assert sum(DENOM[i]*generated[n-i-1]
                   for i in range(19)) == 0
    print('PASS: 476 saturated matrices, 136 accepting states')
    print('PASS: all 476 coordinates of the degree-21 vector identity')
    print('PASS: exact numerator/denominator and 120 coefficients')
    print('Initial singleton counts U_1..U_12:', generated[:12])

if __name__ == '__main__':
    main()
