#!/usr/bin/env python3
"""Stand-alone face and homology checks for directed cyclic path bouquets.
All graph and simplicial objects constructed from their definitions.
No external libraries needed.
"""
from itertools import combinations
from collections import defaultdict

def construction(ell,n):
    assert ell>=3 and n>=1
    k=ell-2
    s,t=0,1
    branches=list(range(2,n+2))
    common=[t]+list(range(n+2,n+2+k-1))+[s]
    arcs=[(s,b) for b in branches]+[(b,t) for b in branches]+list(zip(common[:-1],common[1:]))
    assert len(arcs)==2*n+k
    return arcs

def multipath(arcs, mask):
    out={};inc={}
    for i,(a,b) in enumerate(arcs):
        if not (mask>>i)&1:continue
        if a in out or b in inc:return False
        out[a]=b;inc[b]=a
    # degree at most one: any cycle is detected by repeatedly following out.
    for v in out:
        seen=set()
        cur=v
        while cur in out:
            if cur in seen:return False
            seen.add(cur);cur=out[cur]
    return True

def expected(ell,n,mask):
    k=ell-2
    P=[i for i in range(n) if mask>>i&1]
    Q=[i for i in range(n) if mask>>(n+i)&1]
    if len(P)>1 or len(Q)>1:return False
    if len(P)==1 and P==Q and all(mask>>(2*n+j)&1 for j in range(k)):return False
    return True

def rank_f2(cols):
    piv={}
    for x in cols:
        while x:
            k=x.bit_length()-1
            if k in piv:x^=piv[k]
            else:piv[k]=x;break
    return len(piv)

def reduced_betti(faces):
    bydim=defaultdict(list)
    for mask in faces:
        if mask:bydim[mask.bit_count()-1].append(mask)
    mx=max(bydim)
    rank={}
    for d in range(1,mx+1):
        index={m:i for i,m in enumerate(bydim[d-1])}
        cols=[]
        for face in bydim[d]:
            z=0
            for i in range(face.bit_length()):
                if face>>i&1:z^=1<<index[face^(1<<i)]
            cols.append(z)
        rank[d]=rank_f2(cols)
    betti={d:len(bydim[d])-rank.get(d,0)-rank.get(d+1,0)-(1 if d==0 else 0)
           for d in bydim}
    return {d:b for d,b in betti.items() if b}

def permutation_closure(n, generators):
    identity=tuple(range(n))
    group={identity}; queue=[identity]
    for p in queue:
        for g in generators:
            nxt=tuple(p[g[i]] for i in range(n))
            if nxt not in group:group.add(nxt);queue.append(nxt)
    return sorted(group)

def quotient_betti(ell,n,generators):
    group=permutation_closure(n,generators)
    k=ell-2
    faces=[m for m in range(1<<(2*n+k)) if expected(ell,n,m)]
    def permute(m,p):
        v=m & (((1<<k)-1)<<(2*n))
        for i in range(n):
            if m>>i&1:v|=1<<p[i]
            if m>>(n+i)&1:v|=1<<(n+p[i])
        return v
    orbit_rep={m:min(permute(m,p) for p in group) for m in faces}
    bydim=defaultdict(set)
    for m in faces:
        if m:bydim[m.bit_count()-1].add(orbit_rep[m])
    bydim={d:sorted(v) for d,v in bydim.items()}
    ranks={}
    for d in range(1,max(bydim)+1):
        index={m:i for i,m in enumerate(bydim[d-1])}
        cols=[]
        for simplex in bydim[d]:
            z=0
            for i in range(simplex.bit_length()):
                if simplex>>i&1:
                    z^=1<<index[orbit_rep[simplex^(1<<i)]]
            cols.append(z)
        ranks[d]=rank_f2(cols)
    return {d:b for d in bydim if (b:=len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0))},group

def run():
    count=0
    for ell in range(3,9):
        for n in range(1,7):
            arcs=construction(ell,n)
            N=len(arcs)
            # Check the *actual graph* against the proposed face rule for every arc subset.
            for mask in range(1<<N):
                assert multipath(arcs,mask)==expected(ell,n,mask),(ell,n,mask)
            count+=1
    print('Exact face-rule exhaustivity: PASS (36 cases; ell=3..8, n=1..6)')
    cases=0
    for ell in range(3,8):
        for n in range(1,6):
            if 2*n+ell-2>14:continue
            arcs=construction(ell,n)
            faces=[m for m in range(1<<len(arcs)) if multipath(arcs,m)]
            betti=reduced_betti(faces)
            assert betti=={ell-2:n},(ell,n,betti)
            assert len(faces)==(n+1)**2*2**(ell-2)-n,(ell,n,len(faces))
            cases+=1
    print(f'Independent mod-two homology and face count: PASS ({cases} cases)')
    tests=0
    for ell in [4,5,6]:
        n=4
        identity=tuple(range(n))
        transposition=(1,0,2,3)
        cycle=(1,2,3,0)
        doubtrans=(1,0,3,2)
        for gens in [[],[transposition],[cycle],[doubtrans],[transposition,cycle]]:
            betti,group=quotient_betti(ell,n,gens)
            orbits={min(p[i] for p in group) for i in range(n)}
            assert betti=={ell-2:len(orbits)},(ell,gens,betti,len(orbits))
            fixed={i for i in range(n) if all(p[i]==i for p in group)}
            if fixed:
                fixed_betti=reduced_betti([m for m in range(1<<(2*len(fixed)+ell-2)) if expected(ell,len(fixed),m)])
                assert fixed_betti=={ell-2:len(fixed)}
            tests+=1
    print(f'Subgroup quotient and fixed-support checks: PASS ({tests} cases)')
    print('Sample dimensions, face counts, top mod-two ranks:')
    for ell,n in [(3,3),(4,4),(5,4),(6,4),(7,4)]:
        faces=[m for m in range(1<<len(construction(ell,n))) if expected(ell,n,m)]
        print(f'  ell={ell}, n={n}: dim={ell-1}, faces={len(faces)}, beta_{ell-2}={n}')
if __name__=='__main__':run()
