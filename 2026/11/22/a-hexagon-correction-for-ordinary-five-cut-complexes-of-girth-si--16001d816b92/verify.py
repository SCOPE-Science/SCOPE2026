"""Self-contained finite checks for the six-cycle correction to five-cut complexes.

Python 3 standard library only. The infinite assertion is proved separately.
"""
from itertools import combinations
from collections import defaultdict, deque
from math import comb


def graph(n, edges):
    a = [0] * n
    for x, y in edges:
        assert 0 <= x < n and 0 <= y < n and x != y
        a[x] |= 1 << y
        a[y] |= 1 << x
    return a


def connected(a, vs):
    if not vs:
        return False
    allowed = sum(1 << x for x in vs)
    seen = 1 << vs[0]
    while True:
        grown = seen
        for x in vs:
            if seen & (1 << x):
                grown |= a[x]
        grown &= allowed
        if grown == seen:
            return seen == allowed
        seen = grown


def is_hexagon(a, s):
    return all((a[x] & sum(1 << y for y in s)).bit_count() == 2 for x in s) and connected(a, s)


def examples():
    yield 'cycle_10', graph(10, [(i, (i+1) % 10) for i in range(10)]), 0, None
    yield 'cycle_11', graph(11, [(i, (i+1) % 11) for i in range(11)]), 0, None
    yield 'hexagon_plus_isolates', graph(10, [(i, (i+1) % 6) for i in range(6)]), 1, None
    yield 'two_hexagons', graph(12, [(i, i+1) for i in range(0,5)] + [(5,0)] + [(i,i+1) for i in range(6,11)] + [(11,6)]), 2, None
    # Three length-three branches with common endpoints: three overlapping hexagons.
    arms = [(0, 2, 3, 1), (0, 4, 5, 1), (0, 6, 7, 1)]
    yield 'overlapping_hexagons', graph(10, [(p[i],p[i+1]) for p in arms for i in range(3)]), 3, None
    # Incidence of the seven Fano lines (the difference set {0,1,3}).
    lines = [{j % 7,(j+1)%7,(j+3)%7} for j in range(7)]
    yield 'heawood', graph(14, [(p,7+i) for i, line in enumerate(lines) for p in line]), 28, 491
    yield 'mobius_kantor', graph(16, [(i,(i+1)%8) for i in range(8)]+[(i,8+i) for i in range(8)]+[(8+i,8+((i+3)%8)) for i in range(8)]), 24, 1101
    offsets = [5,7,-7,7,-7,-5]*3
    yield 'pappus', graph(18, [(i,(i+1)%18) for i in range(18)] + [(i,(i+offsets[i])%18) for i in range(18)]), 18, 2074


def verify_case(name,a,want_c6,want_b):
    n = len(a)
    # For each graph edge, an alternative path of length at most four
    # would yield a forbidden cycle of length three, four, or five.
    for x in range(n):
        for y in range(x+1,n):
            if not (a[x] & (1<<y)):
                continue
            frontier={x}; seen={x}
            for distance in range(1,5):
                reach=set()
                for v in frontier:
                    for w in range(n):
                        if (a[v] & (1<<w)) and {v,w}!={x,y} and w not in seen:
                            reach.add(w)
                if y in reach:
                    assert distance >= 5, (name, 'short cycle',x,y,distance+1)
                seen.update(reach); frontier=reach

    five = [frozenset(S) for S in combinations(range(n),5) if connected(a,S)]
    six = [frozenset(S) for S in combinations(range(n),6) if is_hexagon(a,S)]
    assert len(six) == want_c6, (name,len(six),want_c6)
    # These checks characterize all 6- and 7-faces of the Alexander dual.
    for S in combinations(range(n),6):
        all_connected = all(connected(a,T) for T in combinations(S,5))
        assert all_connected == is_hexagon(a,S), (name,'6-face',S)
    for S in combinations(range(n),7):
        assert not all(connected(a,T) for T in combinations(S,5)), (name,'7-face',S)
    extensions = defaultdict(set)
    for T in five:
        for v in T:
            F=frozenset(T-{v})
            if not connected(a,tuple(F)):
                extensions[F].add(T)
    # Stronger connector lemma, on all disconnected 4-subsets.
    for S in combinations(range(n),4):
        F=frozenset(S)
        if connected(a,S):
            continue
        ext=extensions.get(F,set())
        assert len(ext) <= 2, (name,'too many connectors',S,ext)
        if len(ext) == 2:
            U=frozenset.union(*ext)
            assert len(U) == 6 and U in six, (name,'no hexagon',S,ext)

    assigned = set()
    pair_three_faces = set()
    all_cycle_fives = set()
    for C in six:
        cycle_fives = {v:frozenset(C-{v}) for v in C}
        assert all(T in five for T in cycle_fives.values())
        assert all_cycle_fives.isdisjoint(cycle_fives.values()), (name,'two cycles share a path')
        all_cycle_fives.update(cycle_fives.values())
        # Root C6 at the first removed vertex. Edges between nonadjacent vertices
        # index precisely the disconnected four-sets shared by two cycle paths.
        root=min(C); gone={root}; pending=deque([root]); order=[]
        while pending:
            old=pending.popleft()
            for new in sorted(C-gone):
                F=frozenset(C-{old,new})
                if connected(a,tuple(F)):
                    continue
                assert extensions[F] == {cycle_fives[old],cycle_fives[new]}, (name,'incomplete cycle block',C,F)
                gone.add(new); pending.append(new)
                order.append((F,cycle_fives[new]))
        assert len(gone)==6 and len(order)==5
        assigned.update(cycle_fives.values())
        for F,T in order:
            assert F not in pair_three_faces
            pair_three_faces.add(F)
    # Each non-cycle connected tree has a cut vertex with a globally private face.
    for T in five:
        if T in all_cycle_fives:
            continue
        private=[frozenset(T-{v}) for v in T if not connected(a,tuple(T-{v})) and extensions[frozenset(T-{v})] == {T}]
        assert private, (name,'no private tree face',T)
        F=private[0]
        assert F not in pair_three_faces
        pair_three_faces.add(F)
    assert len(pair_three_faces) == len(five)-len(six)
    rank=comb(n-1,4)-len(five)+len(six)
    assert rank >= 0 and (want_b is None or rank==want_b), (name,rank,want_b)
    print(f'{name}: n={n}, connected5={len(five)}, hexagons={len(six)}, free3faces={len(pair_three_faces)}, beta={rank}')


def main():
    count=0
    for name,adj,c6,beta in examples():
        verify_case(name,adj,c6,beta)
        count+=1
    print('HEXAGON_FIVE_CUT_CHECKS_PASS',count)

if __name__=='__main__':
    main()
