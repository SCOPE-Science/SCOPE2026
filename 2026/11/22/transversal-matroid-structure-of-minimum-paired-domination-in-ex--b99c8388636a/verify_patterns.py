#!/usr/bin/env python3
"""Independent finite tests for an all-order paired-domination matroid theorem."""
from itertools import combinations, permutations
from math import comb

SLOTS = (1, 6, 9, 10, 12)  # 4-bit role masks for x0,x1,x2,A,B.


def class_neighbours(i, j):
    return i == j or ((i - j) % 5 in (1, 4))


def graph_test(classes, chosen):
    selected = set(chosen)
    if any(not any(class_neighbours(classes[v], classes[u]) for u in selected)
           for v in range(len(classes))):
        return False
    s = tuple(chosen)
    return any(class_neighbours(classes[s[i]], classes[s[j]]) and
               class_neighbours(classes[s[k]], classes[s[l]])
               for i, j, k, l in ((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)))


def transversal_test(classes, chosen):
    return any(all(SLOTS[classes[v]] & (1 << slot)
                   for v, slot in zip(chosen, p))
               for p in permutations(range(4)))


def all_occupancy_patterns():
    out = {}
    for core in range(8):
        bits = [(core >> i) & 1 for i in range(3)]
        for na in range(5):
            nb = 4 - sum(bits) - na
            if not 0 <= nb <= 4:
                continue
            t = tuple(bits + [na, nb])
            representatives = tuple(i for i, c in enumerate(t) for _ in range(c))
            assert len(representatives) == 4
            # For a 4-selection, domination of every fibre is equivalent
            # to dominating one representative of each of the five fibres.
            dominant = all(t[i] or t[(i - 1) % 5] or t[(i + 1) % 5]
                           for i in range(5))
            matching = any(class_neighbours(representatives[i], representatives[j])
                           and class_neighbours(representatives[k], representatives[l])
                           for i, j, k, l in ((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)))
            tv = transversal_test(representatives, range(4))
            assert tv == bool(dominant and matching), (t, tv, matching, dominant)
            out[t] = tv
    assert len(out) == 28
    assert sum(out.values()) == 13
    return out


def check_graphs():
    total = 0
    for a in range(1, 9):
        for b in range(1, 9):
            classes = [0, 1, 2] + [3] * a + [4] * b
            count = 0
            for chosen in combinations(range(len(classes)), 4):
                g = graph_test(classes, chosen)
                t = transversal_test(classes, chosen)
                assert g == t, (a, b, chosen)
                count += g
                total += 1
            assert count == a*a*b + a*b*b + a*a + a*b + b*b, (a, b, count)
    return total


def witness_nonmatroid_cycle():
    n = 7
    def cycle_pd(S):
        if any(not any(((u-v)%n in (1,n-1)) or u == v for u in S)
               for v in range(n)):
            return False
        return any(((i-j)%n in (1,n-1)) and ((k-l)%n in (1,n-1))
                   for i,j,k,l in ((S[0],S[1],S[2],S[3]),
                                     (S[0],S[2],S[1],S[3]),
                                     (S[0],S[3],S[1],S[2])))
    left = (0,1,3,4); right = (0,2,3,6)
    assert cycle_pd(left) and cycle_pd(right)
    assert not cycle_pd((0,1,2,3))
    assert not cycle_pd((0,1,3,6))


if __name__ == '__main__':
    patterns = all_occupancy_patterns()
    trials = check_graphs()
    witness_nonmatroid_cycle()
    print('PASS: 28 structural occupancy patterns; 13 admissible patterns')
    print(f'PASS: {trials} graph-versus-transversal subset comparisons, 64 parameter pairs')
    print('PASS: exact all-parameter counting formula on tested range')
    print('PASS: paired-domination basis-exchange counterexample on C7')
