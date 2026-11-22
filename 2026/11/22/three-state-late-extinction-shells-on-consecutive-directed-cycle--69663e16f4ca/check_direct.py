"""Exhaustive labelled-state verification of the late extinction shell theorem.
Run: python check_direct.py
"""
from collections import Counter


def graph(a):
    assert a >= 2
    n = 2*a
    arcs = [(i, i+1) for i in range(a-1)] + [(a-1, 0), (0, a)]
    arcs += [(i, i+1) for i in range(a, 2*a-1)] + [(2*a-1, 0)]
    pred = [0]*n
    for u, v in arcs:
        pred[v] |= 1 << u
    return pred


def step(state, preds):
    nxt = 0
    for vertex, mask in enumerate(preds):
        if (state & mask) == mask:
            nxt |= 1 << vertex
    return nxt


def verify(a):
    preds = graph(a)
    n, E = 2*a, a*(a+1)
    maximum = (1 << n)-1
    counts = Counter()
    by_zero_weight = {}
    for initial in range(1 << n):
        if initial == maximum:
            assert step(initial, preds) == initial
            continue
        state = initial
        for t in range(E+1):
            if state == 0:
                counts[t] += 1
                if t >= E-a+1:
                    by_zero_weight[t, n-initial.bit_count()] = by_zero_weight.get((t, n-initial.bit_count()), 0)+1
                break
            state = step(state, preds)
        else:
            raise AssertionError(('not extinct at E', a, initial))
    assert sum(counts.values()) == (1 << n)-1
    for t in range(E-a+1, E):
        assert counts[t] == 3, (a,t,counts[t])
        assert by_zero_weight.get((t,1)) == 2
        assert by_zero_weight.get((t,2)) == 1
    assert counts[E] == 1 and by_zero_weight.get((E,1)) == 1
    return (a, 1 << n, E)

if __name__ == '__main__':
    for a in range(2, 8):
        print('PASS',verify(a))
