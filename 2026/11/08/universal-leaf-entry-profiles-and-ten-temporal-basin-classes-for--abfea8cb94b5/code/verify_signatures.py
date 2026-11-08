#!/usr/bin/env python3
"""Exact finite-signature and symbolic count verification for 3-state GHM.
No third-party packages required.
"""
from collections import defaultdict
from math import comb

def mask_states(mask):
    return (c for c in (0, 1, 2) if mask & (1 << c))

def advance(c, has_excited_neighbor):
    if c == 0:
        return int(has_excited_neighbor)
    return (c + 1) % 3

def transition(state):
    hub, core_support, leaf_support = state
    core_next = 0
    for c in mask_states(core_support):
        core_next |= 1 << advance(c, hub == 1 or bool(core_support & 2))
    leaf_next = 0
    for c in mask_states(leaf_support):
        leaf_next |= 1 << advance(c, hub == 1)
    hub_next = advance(hub, bool((core_support | leaf_support) & 2))
    return hub_next, core_next, leaf_next

def orbit_data(state):
    visited = {}
    while state not in visited:
        if len(visited) > 20:
            raise AssertionError('Long signature orbit')
        visited[state] = len(visited)
        state = transition(state)
    return visited[state], len(visited) - visited[state]

# Rows correspond to support sizes 1,2,3 of the nonhub clique vertices;
# columns to support sizes 1,2,3 of the leaves.
EXPECTED = {
    (0,1): ((1,0,0),(0,0,0),(0,0,0)),
    (0,3): ((0,0,0),(3,0,0),(3,0,0)),
    (1,1): ((7,4,0),(4,2,0),(0,0,0)),
    (1,3): ((0,0,0),(1,1,0),(1,1,0)),
    (2,1): ((9,9,3),(6,6,2),(0,0,0)),
    (2,3): ((0,0,0),(2,3,1),(2,3,1)),
    (3,1): ((6,7,3),(5,5,2),(0,0,0)),
    (3,3): ((0,0,0),(2,3,1),(2,3,1)),
    (4,1): ((4,7,3),(3,5,2),(0,0,0)),
    (4,3): ((0,0,0),(1,2,1),(1,2,1)),
}

def weight(n, k):
    return sum((-1)**j * comb(k,j)*(k-j)**n for j in range(k+1))

def expected_count(r,s,t,p):
    R,S,P = 2**r, 2**s, 3**s
    Q=3**r-2**(r+1)+1
    if p==3:
        return Q*(3, S-1, P-1, P-1, P-S)[t]
    return (1, 2*R*S-1, (2*R-1)*P,
            (2*R-1)*P-R*S+R-1,
            (2*R-1)*P-R*S-R+1)[t]

def main():
    found=defaultdict(lambda: [[0]*3 for _ in range(3)])
    total=0
    for h in range(3):
        for a in range(1,8):
            for b in range(1,8):
                t,p=orbit_data((h,a,b))
                assert (t,p) in EXPECTED
                assert (p==3) == ((a | (1<<h)) == 7)
                found[t,p][a.bit_count()-1][b.bit_count()-1]+=1
                total+=1
    assert total==147
    for key in EXPECTED:
        assert tuple(map(tuple,found[key])) == EXPECTED[key], (key,found[key])
    assert sum(sum(map(sum,M)) for M in found.values()) ==147
    checks=0
    for r in range(2,13):
        for s in range(1,13):
            out={}
            for (t,p),mat in found.items():
                v=sum(mat[a][b]*weight(r,a+1)*weight(s,b+1)
                      for a in range(3) for b in range(3))
                assert v==expected_count(r,s,t,p),(r,s,t,p,v)
                out[t,p]=v
                checks+=1
            assert sum(out.values())==3**(r+s+1)
            assert sum(out[t,3] for t in range(5))==3**(s+1)*(3**r-2**(r+1)+1)
            assert sum(out[t,1] for t in range(5))==3**(s+1)*(2**(r+1)-1)
    print('PASS: all 147 exact nonempty support signatures')
    print('PASS: full first-entry and primitive-period coefficient table')
    print('PASS: core-rainbow equivalence, fixed/3-cycle only, sharp T<=4')
    print(f'PASS: {checks} weighted coefficient/formula comparisons, r=2..12,s=1..12')
    for k in sorted(EXPECTED):
        print(f'coefficient {k}: {EXPECTED[k]}')

if __name__=='__main__':main()
