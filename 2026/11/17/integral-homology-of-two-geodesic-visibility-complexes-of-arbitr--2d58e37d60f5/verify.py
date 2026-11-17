#!/usr/bin/env python3
"""Direct dual-enumeration and mod-two rank checks for multipartite visibility complexes.
No external dependencies; the integral and homotopy assertions require the written proof.
"""
from itertools import combinations
from math import comb


def dual_faces(sizes):
    n=sum(sizes); parts=[]; off=0
    for k in sizes:
        parts.append(tuple(range(off,off+k))); off+=k
    faces={()}
    for i, pi in enumerate(parts):
        external=tuple(v for j,pj in enumerate(parts) if j!=i for v in pj)
        for k in range(1,len(pi)-1):
            for a in combinations(pi,k):
                faces.add(tuple(a))
                for b in external: faces.add(tuple(sorted(a+(b,))))
        for b in external: faces.add((b,))
    bydim={}
    for f in faces: bydim.setdefault(len(f)-1,[]).append(f)
    return {d:sorted(f) for d,f in bydim.items()}


def gf2_rank(cols):
    basis={}
    for x in cols:
        while x:
            pivot=x.bit_length()-1
            if pivot in basis: x^=basis[pivot]
            else: basis[pivot]=x;break
    return len(basis)


def reduced_betti(faces):
    ranks={}
    for d in sorted(faces):
        if d<1:continue
        idx={f:i for i,f in enumerate(faces[d-1])}
        cols=[]
        for f in faces[d]:
            vec=0
            for i in range(len(f)):
                vec ^= (1<<idx[f[:i]+f[i+1:]])
            cols.append(vec)
        ranks[d]=gf2_rank(cols)
    return {d:len(fs)-ranks.get(d,0)-ranks.get(d+1,0)
            for d,fs in faces.items() if d>=0 and len(fs)-ranks.get(d,0)-ranks.get(d+1,0)>0}


def predicted_betti(sizes):
    t=len(sizes); n=sum(sizes)
    b={1:comb(t-1,2),2:sum((sizes[i]-1)*(sizes[j]-1)
      for i in range(t) for j in range(i+1,t))}
    for q in sizes: b[q-2]=b.get(q-2,0)+(q-1)*(n-q-1)
    return {k:v for k,v in b.items() if v}


def exhaustive_visibility_equivalence(sizes):
    # Independently build the complete multipartite graph as adjacency bitmasks.
    t=len(sizes);masks=[];off=0
    for q in sizes:
        masks.append(((1<<q)-1)<<off);off+=q
    adjacency=[]
    for u in range(off):
        adj=0
        for v in range(off):
            if u!=v and not any((m & (1<<u)) and (m & (1<<v)) for m in masks):
                adj |= 1<<v
        adjacency.append(adj)
    # Same-part nonedges have identical sets of intermediate vertices, calculated
    # here from the independently generated actual adjacency relation.
    intermediates=[]
    for mask in masks:
        vs=[u for u in range(off) if mask & (1<<u)]
        intermediates.append(adjacency[vs[0]] & adjacency[vs[1]])
    count=0;bad=0
    for subset in range(1<<off):
        selected=[(subset&mask).bit_count() for mask in masks]
        # Direct graph test using explicit common-neighbor sets, without the dual
        # face condition in the branch that computes 'actual'.
        actual=all(selected[i]<2 or (intermediates[i]&~subset).bit_count()>=2
                   for i in range(t))
        complement=[sizes[i]-selected[i] for i in range(t)]
        dual_member=any(complement[i]<=sizes[i]-2 and
                        sum(complement[j] for j in range(t) if j!=i)<=1
                        for i in range(t))
        if actual==dual_member:bad+=1
        count+=1
    assert not bad,(sizes,bad)
    return count


def run():
    cases=[(3,(5,5,5)),(4,(4,4,4,4)),(4,(5,5,5,5)),
           (4,(5,6,5,5)),(5,(5,5,5,5,5))]
    for _,sizes in cases:
        faces=dual_faces(sizes)
        observed=reduced_betti(faces)
        # d=0 includes one connected component; remove the unreduced contribution.
        observed[0]=observed.get(0,0)-1
        observed={d:v for d,v in observed.items() if v}
        expected=predicted_betti(sizes)
        assert observed==expected,(sizes,observed,expected)
        print('PARTS',sizes,'FACES',sum(len(v) for k,v in faces.items() if k>=0),
              'DUAL_REDUCED_BETTI',observed,flush=True)
    print('DIRECT_VISIBILITY_SUBSETS',exhaustive_visibility_equivalence((5,5,5,5)),flush=True)
    print('MULTIPARTITE_FTMV_DUAL_CHECK_PASS',flush=True)

if __name__=='__main__':run()
