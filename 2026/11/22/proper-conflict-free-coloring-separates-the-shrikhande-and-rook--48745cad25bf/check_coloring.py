#!/usr/bin/env python3
"""Reproduce the two explicit proper open-neighborhood conflict-free certificates.

No third-party packages needed. Run: python3 check_coloring.py
"""
from collections import Counter

COLORS = {
    'Shrikhande': [
        [0, 4, 0, 2],
        [1, 3, 2, 4],
        [2, 0, 1, 0],
        [3, 1, 3, 4],
    ],
    'Rook': [
        [0, 1, 2, 4],
        [1, 4, 3, 2],
        [2, 3, 0, 5],
        [5, 0, 1, 3],
    ],
}

STEP = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
V = [(i,j) for i in range(4) for j in range(4)]

def adjacent(g, a, b):
    if a == b:
        return False
    (i,j),(p,q) = a,b
    if g == 'Shrikhande':
        return ((p-i)%4,(q-j)%4) in STEP
    if g == 'Rook':
        return i == p or j == q
    raise ValueError(g)

def certificate(g, labels):
    col = {v: labels[v[0]][v[1]] for v in V}
    all_col = set(col.values())
    assert len(all_col) == (5 if g == 'Shrikhande' else 6)
    for v in V:
        neighbors = [w for w in V if adjacent(g,v,w)]
        assert len(neighbors) == 6
        assert all(col[v] != col[w] for w in neighbors), (g,v,'not proper')
        counts = Counter(col[w] for w in neighbors)
        assert 1 in counts.values(), (g,v,'missing singleton')
    for u in V:
        for v in V:
            if u == v:
                continue
            common = sum(adjacent(g,u,w) and adjacent(g,v,w) for w in V)
            assert common == 2, (g,u,v,'not srg(16,6,2,2)')
    local = [w for w in V if adjacent(g,(0,0),w)]
    comps=[]
    unseen=set(local)
    while unseen:
        seed=unseen.pop(); component={seed}; frontier=[seed]
        while frontier:
            w=frontier.pop()
            for x in list(unseen):
                if adjacent(g,w,x):
                    unseen.remove(x); component.add(x); frontier.append(x)
        comps.append(len(component))
    assert sorted(comps) == ([6] if g == 'Shrikhande' else [3,3])
    print(f'{g}: 16 vertices, degree 6, all nonzero common-neighbor counts 2, '
          f'{len(all_col)}-color proper conflict-free witness verified')


def difference_set_check():
    for d in V:
        ways = sum(((a-b)%4,(c-e)%4) == d
                   for (a,c) in STEP for (b,e) in STEP)
        assert ways == (6 if d == (0,0) else 2), (d,ways)
    print('Shrikhande: all 15 nonzero differences occur exactly twice in STEP-STEP')

if __name__ == '__main__':
    difference_set_check()
    for g,lab in COLORS.items():
        certificate(g,lab)
    print('PASS')
