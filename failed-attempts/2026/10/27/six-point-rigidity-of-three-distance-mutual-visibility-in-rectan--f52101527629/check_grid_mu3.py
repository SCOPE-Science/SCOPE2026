#!/usr/bin/env python3
"""Exact, dependency-free enumeration of 3-distance mutual-visibility sets in Cartesian grids.

For each grid the search recursively enumerates ALL cliques in the graph joining
vertices at Manhattan distance at most 3.  Every 3-distance mutual-visibility
set is one of these cliques.  Geodesic feasibility is checked separately using
explicit monotone shortest paths (no use of the proposed theorem).
"""
from itertools import combinations, permutations


def internally_clear(u, v, occupied):
    """Check the original definition using every shortest coordinate-step order."""
    a, b = u
    c, d = v
    dx, dy = c-a, d-b
    dist = abs(dx)+abs(dy)
    if dist > 3:
        return False
    steps = ([('r', 1 if dx > 0 else -1)] * abs(dx)
             + [('c', 1 if dy > 0 else -1)] * abs(dy))
    for order in set(permutations(steps)):
        row, col = a, b
        clear = True
        for axis, sg in order[:-1]:
            if axis == 'r':
                row += sg
            else:
                col += sg
            if (row, col) in occupied:
                clear = False
                break
        if clear:
            return True
    return False


def is_visible_set(S):
    occupied = set(S)
    return all(internally_clear(a,b,occupied) for a,b in combinations(S,2))


def predicted_value(m,n):
    a,b=sorted((m,n))
    if a==1:
        return 1 if b==1 else 2
    if a==2:
        return 3 if b==2 else 4
    if a==3 and b==3:
        return 5
    return 6


def predicted_max_sets(m,n):
    """Only the nondegenerate m,n>=3, max>=4 claimed tile classification."""
    result=set()
    if m>=3 and n>=4:
        base={(0,1),(0,2),(1,0),(1,3),(2,1),(2,2)}
        for i in range(m-2):
            for j in range(n-3):
                result.add(frozenset((i+a,j+b) for a,b in base))
    if m>=4 and n>=3:
        base={(b,a) for a,b in {(0,1),(0,2),(1,0),(1,3),(2,1),(2,2)}}
        for i in range(m-3):
            for j in range(n-2):
                result.add(frozenset((i+a,j+b) for a,b in base))
    return result


def brute_grid(m,n):
    vertices=[(i,j) for i in range(m) for j in range(n)]
    size=len(vertices)
    dclose={v:{w for w in vertices if v!=w and abs(v[0]-w[0])+abs(v[1]-w[1])<=3}
            for v in vertices}
    # Enumerates each nonempty bounded-diameter subset EXACTLY ONCE by its
    # strictly increasing vertex indices. Does not skip any set of size <= optimum.
    best=0
    maxima=set()
    tested_cliques=0
    def dfs(chosen, candidates):
        nonlocal best,maxima,tested_cliques
        if chosen:
            tested_cliques += 1
            if len(chosen)>=best and is_visible_set(chosen):
                if len(chosen)>best:
                    best=len(chosen)
                    maxima=set()
                maxima.add(frozenset(chosen))
        for t,v in enumerate(candidates):
            new=[w for w in candidates[t+1:] if w in dclose[v]]
            dfs(chosen+[v],new)
    dfs([],vertices)
    return best,maxima,tested_cliques


def main():
    cases=[(1,4),(1,6),(2,3),(2,4),(2,7),(3,3),(3,4),(3,5),(4,4),(4,5),(5,5),(6,6),(6,8)]
    total_cliques=0
    for m,n in cases:
        value, maxima, count=brute_grid(m,n)
        total_cliques+=count
        assert value==predicted_value(m,n), (m,n,value)
        if min(m,n)>=3 and max(m,n)>=4:
            expected=predicted_max_sets(m,n)
            assert maxima==expected, (m,n,len(maxima),len(expected),maxima^expected)
            assert len(maxima)==(m-2)*max(n-3,0)+max(m-3,0)*(n-2)
        if (m,n)==(3,3):
            assert len(maxima)==4
        print(f'GRID {m}x{n}: optimum={value} maximum_sets={len(maxima)} diameter3_cliques_checked={count}')
    print(f'VERIFICATION_OK cases={len(cases)} total_bounded_diameter_subsets={total_cliques}')

if __name__=='__main__':
    main()
