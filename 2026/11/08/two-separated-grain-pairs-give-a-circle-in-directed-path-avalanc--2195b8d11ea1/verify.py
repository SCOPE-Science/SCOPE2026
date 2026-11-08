#!/usr/bin/env python3
"""Independent finite checks for two-block directed-path avalanche complexes."""
from itertools import combinations
from collections import Counter


def fire_sets(n, L):
    # Simulate the actual parallel sandpile, including the absorbing sink.
    c = [0] * n
    for i in (0, 1, L, L+1):
        assert i < n
        c[i] = 1
    sets = []
    for _ in range(n+3):
        firing = tuple(i for i, x in enumerate(c) if x >= 1)
        if not firing:
            break
        sets.append(firing)
        new = list(c)
        for i in firing:
            new[i] -= 1
            if i+1<n:
                new[i+1] += 1
        c = new
    else:
        raise AssertionError('did not stabilize')
    assert not any(c)
    return sets


def faces_of(firing):
    faces = set()
    for s in firing:
        for k in range(1, len(s)+1):
            faces.update(combinations(s,k))
    return faces


def complex_for(n,L):
    sim = fire_sets(n,L)
    expected = [tuple(t+i for i in (0,1,L,L+1) if t+i<n)
                for t in range(n)]
    assert sim == expected, (n,L,sim,expected)
    return faces_of(sim)


def elementary(F, lower, upper):
    lower=tuple(sorted(lower));upper=tuple(sorted(upper))
    assert lower in F and upper in F, (lower,upper)
    assert len(upper)==len(lower)+1, (lower,upper)
    upper_set=set(upper)
    all_cofaces=[z for z in F if set(lower).issubset(z)]
    assert set(all_cofaces)=={lower,upper},(lower,upper,all_cofaces)
    F.remove(lower);F.remove(upper)


def dominated(F, v, u):
    # Complete strong collapse, in descending-dimensional elementary pairs.
    assert v!=u
    incident=[f for f in F if v in f and u not in f]
    for low in sorted(incident, key=lambda f:(-len(f),f)):
        high=tuple(sorted((*low,u)))
        elementary(F,low,high)
    assert all(v not in f for f in F)
    return len(incident)


def proof_collapse(n,L):
    F=complex_for(n,L)
    count=0
    for m in range(n,L+2,-1):
        # Verify the link facets of the last vertex and their cone apex.
        v,u=m-1,m-L-1
        link={tuple(x for x in f if x!=v) for f in F if v in f}
        link.discard(())
        maximal=[f for f in link if not any(set(f)<set(g) for g in link)]
        target={tuple(sorted((m-L-2,m-L-1,m-2))),
                tuple(sorted((m-L-1,m-L)))}
        assert set(maximal)==target, (n,L,m,maximal,target)
        assert all(u in f for f in maximal)
        count+=dominated(F,v,u)
        assert F==complex_for(m-1,L)
    # Base simplicial collapse onto a polygon.
    count+=dominated(F,0,1)
    elementary(F,(1,L),(1,L,L+1));count+=1
    elementary(F,(1,2),(1,2,L+1));count+=1
    elementary(F,(1,),(1,L+1));count+=1
    cycle_edges={tuple(sorted((i,i+1))) for i in range(2,L+1)}
    cycle_edges.add((2,L+1))
    goal=cycle_edges | {(i,) for i in range(2,L+2)}
    assert F==goal, (n,L,F^goal)
    assert count==7+5*(n-L-2), (n,L,count)
    return count


def betti_mod2(F):
    dims=Counter(len(f)-1 for f in F)
    ranks={}
    for d in sorted(dims):
        if d==0:
            continue
        low={f:i for i,f in enumerate(sorted(x for x in F if len(x)==d))}
        pivot={}; rank=0
        for face in sorted(x for x in F if len(x)==d+1):
            vec=0
            for sub in combinations(face,d):
                vec ^= 1<<low[sub]
            while vec:
                j=vec.bit_length()
                if j in pivot:
                    vec ^= pivot[j]
                else:
                    pivot[j]=vec;rank+=1;break
        ranks[d]=rank
    return [dims.get(i,0)-ranks.get(i,0)-ranks.get(i+1,0)-(i==0)
            for i in range(max(dims)+1)]


def main():
    cases=0;faces_seen=0;pairs=0
    for L in range(3,15):
        for tail in range(13):
            n=L+2+tail
            F=complex_for(n,L)
            pairs+=proof_collapse(n,L)
            faces_seen+=len(F)
            cases+=1
    homology_cases=0
    for L in range(3,9):
        for tail in range(7):
            n=L+2+tail
            H=betti_mod2(complex_for(n,L))
            assert H[0]==0 and H[1]==1 and all(x==0 for x in H[2:]),(L,tail,H)
            homology_cases+=1
    print(f'ALL_VERIFY_OK cases={cases} n_range=5..28 face_instances={faces_seen} ' 
          f'elementary_pairs={pairs} independent_mod2_cases={homology_cases}')

if __name__=='__main__':
    main()
