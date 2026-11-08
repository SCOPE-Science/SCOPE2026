#!/usr/bin/env python3
"""Exhaustive finite verification for bounded independence and total three-cut complexes of cubic cycle powers.

No external packages. Face and Hasse enumeration is exhaustive for n = 13, 14, 15.
"""
from collections import Counter, deque
from itertools import combinations

CASES = {
    13: {"nonempty": 2756, "forbidden": 13, "morse": {0: 1, 5: 1}, "edges": 13663,
         "critical": [(0,), (4,5,7,8,10,11)], "betti": {5: 1}},
    14: {"nonempty": 3276, "forbidden": 28, "morse": {0: 1, 5: 1}, "edges": 16100,
         "critical": [(0,), (5,7,8,10,11,13)], "betti": {5: 1}},
    15: {"nonempty": 3963, "forbidden": 50, "morse": {0: 1, 4: 2}, "edges": 19500,
         "critical": [(0,), (4,7,10,12,13), (5,8,11,12,14)], "betti": {4: 2}}
}


def independent_triples(n):
    out = []
    for triple in combinations(range(n), 3):
        if all(min((a-b)%n, (b-a)%n)>3 for a,b in combinations(triple, 2)):
            out.append(sum(1<<i for i in triple))
    return out


def faces_bounded(n, forbidden):
    return {s for s in range(1<<n) if not any(s&t==t for t in forbidden)}


def finite_morse_match(faces, n):
    remaining = faces - {0}
    matched = []
    for i in range(n):
        bit = 1<<i
        for lower in sorted(remaining):
            upper = lower | bit
            if lower & bit == 0 and upper in remaining:
                assert lower in remaining and upper.bit_count()==lower.bit_count()+1
                remaining.remove(lower)
                remaining.remove(upper)
                matched.append((lower, upper))
    return matched, remaining


def assert_no_gradient_cycle(faces, n, pairs):
    # Each covering relation upper > lower is directed downward unless matched.
    # Reverse every matching edge. Kahn's topological sort tests acyclicity
    # of the COMPLETE oriented Hasse diagram, not only a sampled subgraph.
    vertices = faces - {0}
    matched = set(pairs)
    assert len(matched)==len(pairs)
    degree = {s:0 for s in vertices}
    successor = {s:[] for s in vertices}
    edges = 0
    for upper in vertices:
        for i in range(n):
            if upper & (1<<i):
                lower = upper ^ (1<<i)
                if lower == 0:
                    continue
                if (lower, upper) in matched:
                    start, end = lower, upper
                else:
                    start, end = upper, lower
                successor[start].append(end)
                degree[end]+=1
                edges+=1
    queue=deque(s for s in vertices if degree[s]==0)
    seen=0
    while queue:
        current=queue.popleft();seen+=1
        for dest in successor[current]:
            degree[dest]-=1
            if degree[dest]==0:
                queue.append(dest)
    assert seen==len(vertices),f'gradient cycle: n={n}, seen={seen}'
    return edges


def betti_mod_two(faces, n):
    # An independent boundary-matrix calculation, not using the Morse pairs.
    levels={j:[s for s in sorted(faces) if s.bit_count()==j] for j in range(n+1)}
    ranks={}
    for j in range(1,n+1):
        index={f:i for i,f in enumerate(levels[j-1])}
        pivots={}
        for s in levels[j]:
            col=0
            for i in range(n):
                if s&(1<<i):
                    col ^= 1<<index[s^(1<<i)]
            while col:
                p=col.bit_length()-1
                if p in pivots:
                    col ^=pivots[p]
                else:
                    pivots[p]=col
                    break
        ranks[j]=len(pivots)
    return {j-1:len(levels[j])-ranks.get(j,0)-ranks.get(j+1,0)
            for j in range(n+1) if len(levels[j])-ranks.get(j,0)-ranks.get(j+1,0)}


def full_two_skeleton_dual(n, triples):
    # A simplex S lies in the total three-cut complex precisely if some
    # independent triple is disjoint from S. Test EVERY S with |S| <=3.
    for j in range(4):
        for subset in combinations(range(n),j):
            mask=sum(1<<i for i in subset)
            if not any(mask & t == 0 for t in triples):
                return False, subset
    return True,None


def main():
    for n,expected in CASES.items():
        forbidden=independent_triples(n)
        faces=faces_bounded(n,forbidden)
        matching,critical=finite_morse_match(faces,n)
        edges=assert_no_gradient_cycle(faces,n,matching)
        actual_crit=sorted(tuple(i for i in range(n) if m&(1<<i)) for m in critical)
        predicted_crit=sorted(expected['critical'])
        counts=dict(Counter(len(s)-1 for s in actual_crit))
        betti=betti_mod_two(faces,n)
        full,missing=full_two_skeleton_dual(n,forbidden)
        assert len(forbidden)==expected['forbidden']
        assert len(faces)-1==expected['nonempty']
        assert len(matching)*2+len(critical)==len(faces)-1
        assert edges==expected['edges']
        assert actual_crit==predicted_crit,(n,actual_crit,predicted_crit)
        assert counts==expected['morse']
        assert betti==expected['betti'],(n,betti)
        assert full,(n,'missing simplex in dual',missing)
        print(f'n={n}: independent_triples={len(forbidden)}, faces={len(faces)}, '
              f'Hasse_edges={edges}, Morse_pairs={len(matching)}, '
              f'critical={counts}, mod2_betti={betti}, '
              'full_dual_2_skeleton=YES, gradient_acyclic=YES')
    print('ALL_BOUNDED_CYCLE_CHECKS_OK')

if __name__=='__main__':
    main()
