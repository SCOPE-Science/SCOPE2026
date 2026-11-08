#!/usr/bin/env python3
"""Exact finite verifier for the ordinary four-cut complex of KG(5,2).

Python standard library only. Run in a directory with morse_pairs.json.
The reported topology follows from Forman's acyclic-matching theorem.
"""
import collections
import itertools
import json
import pathlib

VERTICES = tuple(itertools.combinations(range(5), 2))
N = len(VERTICES)
FULL = (1 << N) - 1
EDGES = frozenset((i, j) for i in range(N) for j in range(i)
                  if set(VERTICES[i]).isdisjoint(VERTICES[j]))
ADJ = tuple(sum(1 << (j if i == k else i) for i, j in EDGES
                for k in (i, j) if k == v) for v in range(N))


def subsets(size):
    for positions in itertools.combinations(range(N), size):
        yield sum(1 << j for j in positions)


def connected(mask):
    # Independent breadth-first search on induced graph.
    reached = mask & -mask
    queue = [reached.bit_length() - 1]
    while queue:
        v = queue.pop()
        nbrs = ADJ[v] & mask & ~reached
        while nbrs:
            bit = nbrs & -nbrs
            nbrs -= bit
            reached |= bit
            queue.append(bit.bit_length() - 1)
    return reached == mask


def construct():
    disconnected = {s for s in subsets(4) if not connected(s)}
    connected4 = set(subsets(4)) - disconnected
    facets = {FULL ^ s for s in disconnected}
    faces = {0}
    for f in facets:
        t = f
        while t:
            faces.add(t)
            t = (t - 1) & f
    # A genuinely different face membership test: one disconnected 4-set
    # must lie in the complement of the face.
    alternative = {s for s in range(1 << N)
                   if (s.bit_count() <= 6 and any((d & s) == 0 for d in disconnected))}
    assert faces == alternative
    assert len(EDGES) == 15
    assert len(disconnected) == 140 and len(connected4) == 70
    assert len(facets) == 140 and len(faces) == 766
    fvec = tuple(sum(t.bit_count() == d+1 for t in faces) for d in range(6))
    assert fvec == (10, 45, 120, 210, 240, 140)
    # The twelve absent four-dimensional simplices are complements of
    # the twelve induced 5-cycles, the sharp girth-five obstruction.
    absent = set(subsets(5)) - faces
    pentagons = {t for t in subsets(5)
                 if connected(t) and all((ADJ[v] & t).bit_count() == 2
                                         for v in range(N) if (t >> v) & 1)}
    assert len(absent) == len(pentagons) == 12
    assert absent == {FULL ^ t for t in pentagons}
    assert all(t in faces for t in subsets(4))
    return faces, facets, disconnected, connected4


def morsify(faces, order):
    unmatched = set(faces - {0})
    pairs = []
    for v in order:
        bit = 1 << v
        for lower in sorted(tuple(unmatched), key=lambda s:(s.bit_count(), s)):
            upper = lower | bit
            if not(lower & bit) and lower in unmatched and upper in unmatched:
                unmatched.remove(lower)
                unmatched.remove(upper)
                pairs.append((lower, upper))
    return unmatched, pairs


def verify_morse(faces, critical, pairs):
    all_faces = faces - {0}
    pair_to_lower = {}
    matched = set()
    for lower, upper in pairs:
        assert lower in all_faces and upper in all_faces
        assert lower.bit_count() + 1 == upper.bit_count()
        assert lower & upper == lower
        assert lower not in matched and upper not in matched
        matched.add(lower); matched.add(upper)
        pair_to_lower[upper] = lower
    assert all_faces == matched | critical and not(matched & critical)
    outgoing = {m:[] for m in all_faces}
    indegree = dict.fromkeys(all_faces, 0)
    incidences = 0
    for upper in all_faces:
        s = upper
        while s:
            bit = s & -s
            s -= bit
            lower = upper ^ bit
            if not lower:
                continue
            incidences += 1
            if pair_to_lower.get(upper) == lower:
                a,b = lower,upper
            else:
                a,b = upper,lower
            outgoing[a].append(b)
            indegree[b] += 1
    # A directed cycle is absent iff every node is removed by topological sort.
    q = collections.deque(m for m,d in indegree.items() if d==0)
    visited = 0
    while q:
        m=q.popleft();visited+=1
        for x in outgoing[m]:
            indegree[x]-=1
            if indegree[x]==0:q.append(x)
    assert visited == len(all_faces), ('directed cycle',visited)
    return incidences


def gf2_rank(columns):
    pivots = {}
    for col in columns:
        while col:
            k=col.bit_length()-1
            if k not in pivots:
                pivots[k]=col
                break
            col ^= pivots[k]
    return len(pivots)


def mod2_homology(faces):
    bydim = {d:sorted(f for f in faces if f.bit_count()==d+1) for d in range(6)}
    ranks={}
    for dim in range(1,6):
        index={face:i for i,face in enumerate(bydim[dim-1])}
        columns=[]
        for f in bydim[dim]:
            boundary=0
            for i in range(N):
                if f>>i & 1:
                    boundary ^= (1 << index[f ^ (1<<i)])
            columns.append(boundary)
        ranks[dim]=gf2_rank(columns)
    # augmented C0 -> F2 has rank 1
    reduced={d:len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0)
             for d in range(6)}
    reduced[0]-=1
    assert tuple(reduced[d] for d in range(6)) == (0,0,0,0,0,26),reduced
    return ranks,reduced


def parity(seq):
    inv=sum(x>y for i,x in enumerate(seq) for y in seq[i+1:])
    return -1 if inv & 1 else 1


def cycle_type(p):
    seen=set();result=[]
    for v in range(5):
        if v in seen:continue
        w=v;k=0
        while w not in seen:
            seen.add(w);w=p[w];k+=1
        result.append(k)
    return tuple(sorted(result,reverse=True))


def move_vertex(p):
    assert len(p)==5
    return tuple(VERTICES.index(tuple(sorted((p[a],p[b])))) for a,b in VERTICES)


def move_face(s,p):
    return sum(1<<p[i] for i in range(N) if s>>i&1)


def oriented_sign(s,p):
    mapped=[p[i] for i in range(N) if s>>i&1]
    sorted_positions=tuple(mapped.index(x) for x in sorted(mapped))
    return parity(sorted_positions)


def irreducible_character(lam,mu):
    # Frobenius/Vandermonde coefficient formula for the S5 character.
    from itertools import product
    L=len(lam)
    target=[lam[i]+L-i-1 for i in range(L)]
    ans=0
    for sigma in itertools.permutations(range(L)):
        required=tuple(target[i]-(L-1-sigma[i]) for i in range(L))
        if min(required)<0:continue
        ways=0
        for allocation in product(range(L),repeat=len(mu)):
            partial=[0]*L
            for j,i in enumerate(allocation):partial[i]+=mu[j]
            if tuple(partial)==required:ways+=1
        ans += parity(sigma)*ways
    return ans


def character_and_decomposition(faces):
    classes = collections.Counter()
    characters={}
    for p in itertools.permutations(range(5)):
        induced=move_vertex(p)
        assert {move_face(f,induced) for f in faces} == faces
        tr=0
        for face in faces - {0}:
            if move_face(face,induced)==face:
                tr += ((-1)**(face.bit_count()-1))*oriented_sign(face,induced)
        reduced_lefschetz=tr-1
        homology_trace=-reduced_lefschetz  # H5 only
        mu=cycle_type(p)
        classes[mu]+=1
        if mu in characters:assert characters[mu]==homology_trace
        characters[mu]=homology_trace
    expected={
        (1,1,1,1,1):26,(2,1,1,1):6,(2,2,1):-2,
        (3,1,1):2,(3,2):0,(4,1):0,(5,):1
    }
    assert characters==expected
    assert sum(classes.values())==120
    partitions=[(5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1)]
    multiplicities={}
    for lam in partitions:
        numerator=sum(classes[mu]*characters[mu]*irreducible_character(lam,mu)
                      for mu in classes)
        assert numerator%120==0
        multiplicities[lam]=numerator//120
    expected_mult={(5,):1,(4,1):2,(3,2):1,(3,1,1):2,
                   (2,2,1):0,(2,1,1,1):0,(1,1,1,1,1):0}
    assert multiplicities==expected_mult
    return classes,characters,multiplicities


def main():
    faces,facets,disconnected,connected4=construct()
    expected=json.loads((pathlib.Path(__file__).parent/'morse_pairs.json').read_text())
    crit,pairs=morsify(faces,tuple(range(N)))
    assert pairs == [tuple(x) for x in expected['pairs']]
    assert sorted(crit) == expected['critical_faces']
    assert len(pairs)==369 and len(crit)==27
    assert sum(c.bit_count()==1 for c in crit)==1
    assert sum(c.bit_count()==6 for c in crit)==26
    assert all(c.bit_count() in (1,6) for c in crit)
    incidences=verify_morse(faces,crit,pairs)
    assert incidences==expected['hasse_incidences']
    revcrit,revpairs=morsify(faces,tuple(reversed(range(N))))
    assert len(revpairs)==369 and sum(x.bit_count()==6 for x in revcrit)==26
    assert verify_morse(faces,revcrit,revpairs)==incidences
    ranks,mod2=mod2_homology(faces)
    classes,characters,multiplicities=character_and_decomposition(faces)
    print('graph: vertices=10 edges=15; connected four-sets=70; disconnected=140')
    print('face vector: 10 45 120 210 240 140; including empty: 766')
    print('all 210 four-vertex faces present; 12 missing five-vertex faces are precisely pentagon complements')
    print('Morse pairs=369; critical: one vertex and 26 dimension-five faces')
    print(f'complete Hasse incidences checked: {incidences}; two acyclic matchings')
    print('mod-2 boundary ranks:', ' '.join(f'{d}:{ranks[d]}' for d in range(1,6)))
    print('group |S5|=120; character by descending partition:')
    for mu in sorted(characters,reverse=True):
        print(f'  {mu}: class_size={classes[mu]}, trace={characters[mu]}')
    print('irreducible multiplicities:', multiplicities)
    print('PETERSEN_FOUR_CUT_WEDGE26_AND_S5_CHARACTER_VERIFIED')

if __name__=='__main__':
    main()
