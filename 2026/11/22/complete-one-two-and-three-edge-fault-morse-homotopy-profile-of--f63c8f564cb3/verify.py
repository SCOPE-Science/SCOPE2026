#!/usr/bin/env python3
"""Exact finite certificates for ordinary Morse complexes of small edge faults in K(3,3).

Only the Python standard library is needed. Nonempty faces are encoded as bitmasks
of incidences (v,e). The matching is a matching of the *face poset*, not the
graph's incidence poset. Every accepted assertion is checked directly.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations, product

V = tuple(range(6))
BASE = tuple((a, b) for a in range(3) for b in range(3, 6))
# For each fault type: representative deleted edges, a fixed pivot order, counts
# of critical simplices by dimension, and number of nonempty simplices.
CASES = {
 "intact": ((), (11,9,0,16,2,15,10,3,5,17,14,6,7,8,4,1,13,12), {0:1,4:80},1791),
 "one": (((0,3),), (12,11,7,13,6,0,8,3,9,4,10,2,5,14,15,1), {0:1,3:1,4:17},1023),
 "two_incident": (((0,3),(0,4)), (1,10,9,5,11,2,3,7,8,4,0,12,6,13), {0:1,3:4},527),
 "two_disjoint": (((0,3),(1,4)), (1,10,9,5,11,2,3,7,8,4,0,12,6,13), {0:1,3:2,4:2},575),
 "three_star": (((0,3),(0,4),(0,5)), (1,9,8,5,10,2,3,7,4,0,11,6), {0:1,3:8},215),
 "three_path": (((0,3),(0,4),(1,3)), (7,11,0,8,5,6,3,10,4,1,9,2), {0:1},271),
 "three_pair_and_edge": (((0,3),(0,4),(1,5)), (7,11,0,8,5,6,3,10,4,1,9,2), {0:1,3:4},287),
 "three_matching": (((0,3),(1,4),(2,5)), (1,9,8,5,10,2,3,7,4,0,11,6), {0:1,3:2,4:2},319),
}


def face_set(deleted):
    edges = tuple(e for e in BASE if e not in deleted)
    incidence = tuple((v,i,w) for i,(a,b) in enumerate(edges)
                      for v,w in ((a,b),(b,a)))
    n = len(incidence)
    faces = set()
    for mask in range(1,1<<n):
        if mask.bit_count()>5:  # no gradient on a connected graph can use all 6 vertices
            continue
        used_v=used_e=0
        next_vertex=[-1]*6
        valid=True
        for i,(v,e,w) in enumerate(incidence):
            if (mask>>i)&1:
                if (used_v>>v)&1 or (used_e>>e)&1:
                    valid=False;break
                used_v |= 1<<v
                used_e |= 1<<e
                next_vertex[v]=w
        if not valid:continue
        for v in V:
            seen=set()
            x=v
            while x!=-1:
                if x in seen:
                    valid=False;break
                seen.add(x)
                x=next_vertex[x]
            if not valid:break
        if valid:faces.add(mask)
    return faces,n


def matching(faces,n,order):
    assert sorted(order)==list(range(n))
    left=set(faces)
    pairs=[]
    for p in order:
        bit=1<<p
        for a in sorted(left,key=lambda x:(x.bit_count(),x)):
            if a not in left or a&bit:continue
            b=a|bit
            if b in left:
                left.remove(a);left.remove(b);pairs.append((a,b))
    assert 2*len(pairs)+len(left)==len(faces)
    return pairs,left


def acyclic_hasse(faces,n,pairs):
    # Unmatched cover arrows point downward; matched arrows point upward.
    matched_upper={u:l for l,u in pairs}
    indeg={f:0 for f in faces}
    arrows=defaultdict(list)
    for upper in faces:
        for i in range(n):
            if not (upper>>i)&1:continue
            lower=upper^(1<<i)
            if lower==0:continue
            assert lower in faces
            if matched_upper.get(upper)==lower:
                source,target=lower,upper
            else:
                source,target=upper,lower
            arrows[source].append(target);indeg[target]+=1
    queue=deque(f for f in faces if indeg[f]==0)
    visited=0
    while queue:
        f=queue.popleft();visited+=1
        for t in arrows[f]:
            indeg[t]-=1
            if indeg[t]==0:queue.append(t)
    assert visited==len(faces), 'gradient cycle detected'


def reduced_differential(faces,n,pairs,critical):
    # With no critical 1- or 2-cells, all possibly nonzero differentials
    # in the Morse chain complex are from degree 4 to degree 3.
    c3=sorted(f for f in critical if f.bit_count()==4)
    c4=sorted(f for f in critical if f.bit_count()==5)
    low_to_high={l:u for l,u in pairs}
    high_to_low={u:l for l,u in pairs}
    def boundary(upper):
        return tuple((upper^(1<<v),(-1)**pos)
                 for pos,v in enumerate(i for i in range(n) if (upper>>i)&1))
    @lru_cache(None)
    def reduce_three(face):
        if face in critical:
            assert face in c3
            return {c3.index(face):1}
        if face in high_to_low:
            return {}
        assert face in low_to_high
        upper=low_to_high[face]
        lead=dict(boundary(upper))[face]
        output=Counter()
        for another,coefficient in boundary(upper):
            if another==face:continue
            for idx,val in reduce_three(another).items():
                output[idx]-=lead*coefficient*val
        return {i:v for i,v in output.items() if v}
    for top in c4:
        result=Counter()
        for face,coefficient in boundary(top):
            for i,v in reduce_three(face).items():
                result[i]+=coefficient*v
        assert all(result[i]==0 for i in range(len(c3))), (top,dict(result))
    return len(c3),len(c4)


def gf2_homology(faces,n):
    layers=[[f for f in faces if f.bit_count()==d+1] for d in range(5)]
    layers=[sorted(layer) for layer in layers]
    rank=[0]*5
    for d in range(1,5):
        index={f:i for i,f in enumerate(layers[d-1])}
        basis={}
        for top in layers[d]:
            col=0
            for i in range(n):
                if (top>>i)&1:col ^= 1<<index[top^(1<<i)]
            while col:
                pivot=col.bit_length()-1
                if pivot in basis:col^=basis[pivot]
                else:basis[pivot]=col;break
        rank[d]=len(basis)
    beta=[len(layers[d])-rank[d]-(rank[d+1] if d<4 else 0)
          for d in range(5)]
    beta[0]-=1
    return beta


def prove_orbits():
    # Natural bipartition permutations, and optional shore swap.
    actions=[]
    for p,q,swap in product(permutations(range(3)),permutations(range(3)),(False,True)):
        mapping={}
        for a,b in BASE:
            u=p[a] if not swap else 3+q[a]
            v=3+q[b-3] if not swap else p[b-3]
            mapping[(a,b)]=tuple(sorted((u,v)))
        actions.append(mapping)
    grouped={k:set() for k in range(4)}
    for deleted,_,_,_ in CASES.values():
        k=len(deleted)
        grouped[k].update(frozenset(mapping[e] for e in deleted)
                          for mapping in actions)
    for k in range(4):
        universe={frozenset(S) for S in combinations(BASE,k)}
        assert grouped[k]==universe, (k,len(grouped[k]),len(universe))
    return sum(len(grouped[k]) for k in grouped)


def main():
    assert prove_orbits()==130
    for name,(deleted,order,wanted,face_count) in CASES.items():
        faces,n=face_set(frozenset(deleted))
        assert len(faces)==face_count
        pairs,critical=matching(faces,n,order)
        acyclic_hasse(faces,n,pairs)
        actual=dict(Counter(f.bit_count()-1 for f in critical))
        assert actual==wanted,(name,actual,wanted)
        b3,b4=reduced_differential(faces,n,pairs,critical)
        assert b3==wanted.get(3,0) and b4==wanted.get(4,0)
        gf2=gf2_homology(faces,n)
        assert gf2==[0,0,0,b3,b4],(name,gf2)
        print(name, 'faces',len(faces),'matched_pairs',len(pairs),
              'critical',sorted(actual.items()),'signed_d4_zero',True,
              'mod2_betti',gf2)
    print('PASS: all 130 fault sets covered by eight orbits; exact integral Morse certificates verified')

if __name__=='__main__':
    main()
