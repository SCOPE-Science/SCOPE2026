#!/usr/bin/env python3
"""Standalone finite checks for geometric fixed-point clique-free complexes."""
from itertools import combinations
from collections import defaultdict


def orbits(n, generators):
    unused=set(range(n)); ans=[]
    while unused:
        i=min(unused); todo=[i]; seen={i}
        for v in todo:
            for p in generators:
                w=p[v]
                if w not in seen:
                    seen.add(w);todo.append(w)
        assert all(p[x] in seen for p in generators for x in seen)
        ans.append(tuple(sorted(seen)));unused-=seen
    return ans


def cycles_perm(n, cycles):
    p=list(range(n))
    for cy in cycles:
        for a,b in zip(cy,cy[1:]+cy[:1]):p[a]=b
    assert sorted(p)==list(range(n))
    return tuple(p)


def faces_of_complex(vertex_count, admissible):
    ans={frozenset()}
    for k in range(1,vertex_count+1):
        for c in combinations(range(vertex_count),k):
            if admissible(c):ans.add(frozenset(c))
    for f in ans:
        assert all(frozenset(f-{v}) in ans for v in f)
    return ans


def gf2_rank(rows):
    basis={}
    for x in rows:
        while x:
            h=x.bit_length()-1
            if h not in basis:
                basis[h]=x;break
            x ^= basis[h]
    return len(basis)


def reduced_betti(faces):
    if faces=={frozenset()}:return {}
    dim=max(len(s) for s in faces)-1
    cells={d:sorted([f for f in faces if len(f)==d+1],key=lambda a:tuple(sorted(a))) for d in range(dim+1)}
    ranks={0:1} # augmented boundary C0 -> C(-1) has rank 1 for nonempty complex
    for d in range(1,dim+1):
        lookup={f:i for i,f in enumerate(cells[d-1])}
        rows=[]
        for f in cells[d]:
            b=0
            for v in f:b ^= 1 << lookup[frozenset(f-{v})]
            rows.append(b)
        ranks[d]=gf2_rank(rows)
    ranks[dim+1]=0
    out={}
    for d in range(dim+1):
        b=len(cells[d]) - ranks.get(d,0) - ranks.get(d+1,0)
        if b:out[d]=b
    return out


def predicted(weights, t):
    # Graph has fixed geometric points exactly when an entire vertex orbit is small enough.
    valid=sorted(w for w in weights if w<t)
    if not valid:return None
    w0=valid[0]; other=valid[1:]; out=defaultdict(int)
    for k in range(len(other)+1):
        for sub in combinations(range(len(other)),k):
            weight=sum(other[i] for i in sub)
            if t-w0<=weight<t:
                out[k-1]+=1
    return dict(out)


def check(parts, generators, t):
    n=sum(parts);assert n<=11
    offsets=[]; idx=0
    for z in parts: offsets.append(tuple(range(idx,idx+z)));idx+=z
    pidx={v:i for i,p in enumerate(offsets) for v in p}
    # group action must preserve complete multipartite adjacency, hence maps whole parts to whole parts
    for p in generators:
        assert sorted(p)==list(range(n))
        for a in offsets:
            assert len({pidx[p[v]] for v in a})==1
    v_orbs=orbits(n,generators)
    p_gens=[tuple(pidx[p[a[0]]] for a in offsets) for p in generators]
    p_orbs=orbits(len(parts),p_gens)
    # Every vertex orbit projects surjectively onto exactly one orbit of graph parts.
    support=[frozenset(pidx[v] for v in o) for o in v_orbs]
    part_support={frozenset(o):i for i,o in enumerate(p_orbs)}
    assert all(s in part_support for s in support)
    fiber=[part_support[s] for s in support]
    original=faces_of_complex(len(v_orbs), lambda sub:len(set().union(*(support[j] for j in sub)))<t)
    # Independently build original complex by testing each H-vertex-orbit union against all t-cliques.
    def no_t_clique(sub):
        selected=[v for j in sub for v in v_orbs[j]]
        return not any(len({pidx[v] for v in tup})==t for tup in combinations(selected,t))
    checkfaces=faces_of_complex(len(v_orbs), no_t_clique)
    assert original==checkfaces
    # Delete all but first vertex orbit in each part-orbit fiber; each deletion dominated by representative.
    remaining=set(range(len(v_orbs))); deleted=0
    for q in range(len(p_orbs)):
        reps=[i for i,f in enumerate(fiber) if f==q]
        if not reps:continue
        keeper=reps[0]
        for u in reps[1:]:
            curfaces={f for f in original if f<=remaining}
            maxfaces={f for f in curfaces if not any(f<g for g in curfaces)}
            assert all(keeper in f for f in maxfaces if u in f), (parts,t,keeper,u)
            remaining.remove(u);deleted+=1
    collapse={frozenset(fiber[j] for j in face) for face in original if face<=remaining}
    weights=[len(o) for o in p_orbs]
    weighted=faces_of_complex(len(p_orbs),lambda sub:sum(weights[j] for j in sub)<t)
    assert collapse==weighted
    pred=predicted(weights,t)
    assert (pred is None)==(weighted=={frozenset()})
    if pred is not None:
        observed=reduced_betti(original)
        observed_weighted=reduced_betti(weighted)
        assert observed==observed_weighted==pred,(parts,t,weights,pred,observed,observed_weighted)
    return len(original),len(weighted),deleted, pred


def move_parts(parts, cycles):
    offsets=[];v=0
    for z in parts:offsets.append(list(range(v,v+z)));v+=z
    perm=list(range(v))
    for cy in cycles:
        for a,b in zip(cy,cy[1:]+cy[:1]):
            assert parts[a]==parts[b]
            for va,vb in zip(offsets[a],offsets[b]):perm[va]=vb
    return tuple(perm)


def main():
    cases=[]
    def add(name, parts, generators, ts):
        cases.append((name,parts,generators,ts))
    add('complete-five transposition',[1]*5,[cycles_perm(5,[[0,1]])],[2,3,4,5])
    add('complete-eight two-three cycles',[1]*8,[cycles_perm(8,[[0,1],[2,3,4]])],[2,3,4,5,6])
    add('complete-eight transitive',[1]*8,[cycles_perm(8,[list(range(8))])],[2,3,5])
    add('complete-six identity',[1]*6,[tuple(range(6))],[2,3,4,5,6])
    add('complete-six disjoint-triples',[1]*6,[cycles_perm(6,[[0,1,2],[3,4,5]])],[2,3,4,5])
    add('complete-eight 4+2+1+1',[1]*8,[cycles_perm(8,[[0,1,2,3],[4,5]])],[2,3,4,5,6])
    add('multipartite swapping two equal parts',[2,2,1,1],[move_parts([2,2,1,1],[[0,1]])],[2,3,4,5])
    add('multipartite swapping size-three parts',[3,3,1,1],[move_parts([3,3,1,1],[[0,1]])],[2,3,4,5])
    add('multipartite internal vertex swaps',[2,2,2],[cycles_perm(6,[[0,1],[2,3],[4,5]])],[2,3,4,5])
    add('multipartite both kinds',[2,2,2],[move_parts([2,2,2],[[0,1]]),cycles_perm(6,[[0,1],[2,3],[4,5]])],[2,3,4,5])
    add('multipartite three size-two parts',[2,2,2],[move_parts([2,2,2],[[0,1,2]])],[2,3,4,5])
    add('multipartite varying all parts',[3,2,1,1],[tuple(range(7))],[2,3,4,5])
    total=0;f_orig=0;f_quot=0;dele=0
    for name,parts,gs,ts in cases:
        for t in ts:
            f,q,d,b=check(parts,gs,t)
            total+=1;f_orig+=f;f_quot+=q;dele+=d
            print(name,'t=',t,'fixed_orbit_faces=',f,'quota_faces=',q,'dominated=',d,'betti=',b)
    assert check([1]*8,[cycles_perm(8,[[0,1],[2,3,4]])],5)[3]=={1:2,2:1}
    assert check([1]*5,[cycles_perm(5,[[0,1]])],3)[3]=={0:1,1:1}
    print('ALL_QUOTA_FIXED_CHECKS_OK', 'parameter_cases=',total,'fixed_orbit_faces=',f_orig,'quota_faces=',f_quot,'dominated_deletions=',dele)

if __name__=='__main__':main()
