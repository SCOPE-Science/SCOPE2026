#!/usr/bin/env python3
"""Exact uniform-modulus certificate for reversal factors of a->aa(a+1).
All cycles of the integer difference systems are checked, not sampled moduli.
"""
from collections import Counter
from math import gcd

BASE = (0, 0, 1, 0, 0, 1, 1, 1, 2)
TEMPLATE = tuple((i // 9, BASE[i % 9]) for i in range(18))
EXPECTED = {
    3: {(0,0,0),(0,0,1),(0,1,0),(0,-1,-1)},
    4: {(0,0,1,0),(0,1,0,0),(0,-1,-1,0)},
    5: {(0,0,1,0,0),(0,1,0,0,1),(0,-1,-1,0,-1)},
    6: {(0,0,1,0,0,1),(0,1,0,0,1,0),(0,-1,-1,0,-1,-1)},
    7: {(0,0,1,0,0,1,0),(0,1,0,0,1,0,0),(0,-1,-1,0,-1,-1,0)},
    8: {(0,0,1,0,0,1,0,0)},
    9: set(),
}

def solve_system(left, right_reversed):
    """Xi+offset = Xj+offset modulo q. Return integral component
    offsets, components, gcd of all cycle inconsistencies.
    A system is solvable modulo q exactly when q divides the gcd,
    with gcd=0 interpreted as solvable for all q.
    """
    adjacency = [[] for _ in range(4)]
    for (x, ox), (y, oy) in zip(left, right_reversed):
        adjacency[x].append((y, ox-oy))
        adjacency[y].append((x, oy-ox))
    potential, component, cycle_gcd = {}, {}, 0
    for root in range(4):
        if root in potential:
            continue
        potential[root], component[root] = 0, root
        queue = [root]
        for x in queue:
            for y, delta in adjacency[x]:
                if y not in potential:
                    potential[y] = potential[x] + delta
                    component[y] = root
                    queue.append(y)
                else:
                    cycle_gcd = gcd(cycle_gcd, potential[y]-potential[x]-delta)
    return potential, component, abs(cycle_gcd)

def main():
    print('Symbolic integer-cycle certificate for every alphabet q>=3')
    for n in range(3, 10):
        patterns = set()
        gcd_hist = Counter()
        connected_valid = 0
        for i in range(19-n):
            left = TEMPLATE[i:i+n]
            for j in range(19-n):
                right = tuple((x+2, o) for x,o in TEMPLATE[j:j+n])[::-1]
                potentials, components, g = solve_system(left, right)
                gcd_hist[g] += 1
                if g:
                    assert g in (1, 2), ('nonuniform modulus exception', n, i, j, g)
                    continue
                first_component = components[left[0][0]]
                assert all(components[x] == first_component for x, _ in left)
                base = potentials[left[0][0]] + left[0][1]
                patterns.add(tuple(potentials[x]+offset-base for x,offset in left))
                connected_valid += 1
        assert patterns == EXPECTED[n], (n, patterns, EXPECTED[n])
        print(f'n={n}: patterns={sorted(patterns)}; valid-window-pairs={connected_valid}; cycle-gcd-histogram={dict(sorted(gcd_hist.items()))}')
    print('PASS: exact normalized reversible factors for all q>=3, and none at n=9')

if __name__ == '__main__':
    main()
