#!/usr/bin/env python3
"""Self-contained exact check for the rule-106 finite-ring inverse-degree law."""
# A pair state is 2*a+b; rule 106 is f(a,b,c)=c XOR (a AND b).
GENERATORS = ((0, 2, 0, 3), (1, 3, 1, 2))
IDENTITY = (0, 1, 2, 3)


def build_monoid():
    states = [IDENTITY]
    known = {IDENTITY: 0}
    edges = []
    for state in states:
        nxt = []
        for g in GENERATORS:
            new = tuple(g[state[i]] for i in range(4))
            j = known.get(new)
            if j is None:
                j = len(states)
                known[new] = j
                states.append(new)
            nxt.append(j)
        edges.append(tuple(nxt))
    return states, edges


def poly_convolution_coefficient(sequence, q, n):
    return sum(q[j] * sequence[n - j] for j in range(len(q)) if 0 <= n - j < len(sequence))


def main():
    states, edges = build_monoid()
    assert len(states) == len(edges) == 41
    assert edges[0][0] != 0 and edges[0][1] != 0
    kinds = [sum(t[i] == i for i in range(4)) for t in states]
    assert sorted(set(kinds)) == [0, 1, 2, 3, 4]
    assert kinds.count(4) == 1 and kinds[0] == 4
    # No positive-length input reaches identity: the generators are singular.
    assert all(0 not in pair for pair in edges)
    # q_A = (1-z^3)(1-z-2z^3).
    q_a = [1, -1, 0, -3, 1, 0, 2]
    p_a = [0, 1, 0, 2, -1, -1, -2]
    q_t = [1, 0, 0, -1]
    p_t = [0, 0, 0, 1]
    # Produces coefficients through 50, 41 states suffice for Cayley-Hamilton.
    distribution = [1] + [0] * (len(states) - 1)
    counts = [[0] * 5 for _ in range(49)]
    counts[0][4] = 1
    for n in range(1, 49):
        nxt = [0] * len(states)
        for i, weight in enumerate(distribution):
            if weight:
                a, b = edges[i]
                nxt[a] += weight
                nxt[b] += weight
        distribution = nxt
        for i, weight in enumerate(distribution):
            counts[n][kinds[i]] += weight
        assert counts[n][4] == 0
        assert sum(counts[n]) == 2**n
        assert sum(k * counts[n][k] for k in range(5)) == 2**n
    a = [c[0] for c in counts]
    t = [c[3] for c in counts]
    for n in range(49):
        expected_a = p_a[n] if n < len(p_a) else 0
        expected_t = p_t[n] if n < len(p_t) else 0
        assert poly_convolution_coefficient(a, q_a, n) == expected_a
        assert poly_convolution_coefficient(t, q_t, n) == expected_t
    # These 41 consecutive zeros, for each numerator, prove all later
    # coefficients vanish: an orbit in a 41-dimensional linear space obeys
    # its matrix's characteristic recurrence by Cayley-Hamilton.
    assert all(poly_convolution_coefficient(a, q_a, n) == 0 for n in range(7, 48))
    assert all(poly_convolution_coefficient(t, q_t, n) == 0 for n in range(4, 45))
    for n in range(1, 49):
        assert t[n] == (int(n % 3 == 0))
        assert counts[n][2] == a[n] - 2*t[n]
        assert counts[n][1] == 2**n - 2*a[n] + t[n]
    # Exactly the all-one word has three predecessors when 3 divides n.
    for n in range(1, 49):
        word = IDENTITY
        for _ in range(n):
            word = tuple(GENERATORS[1][s] for s in word)
        assert sum(word[i] == i for i in range(4)) == 3 * int(n % 3 == 0)
    print('VERIFY_OK: 41 states, full all-length rational fiber spectrum')
    print('n : #0 #1 #2 #3')
    for n in range(1, 13):
        print(n, *counts[n][:4])

if __name__ == '__main__':
    main()
