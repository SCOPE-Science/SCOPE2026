#!/usr/bin/env python3
"""Standalone checks for bounded-length partition transfer clique complexes."""
from itertools import combinations

def partitions_bounded(n, k):
    def go(rem, maximum, slots, prefix):
        if not rem:
            yield prefix
        elif slots:
            for x in range(min(maximum, rem), 0, -1):
                yield from go(rem-x, x, slots-1, prefix+(x,))
    return list(go(n,n,k,()))

def transfer_neighbors(p):
    out=set()
    for i,part in enumerate(p):
        if part == 0: continue
        for j in range(len(p)+1):
            if j==i: continue
            x=list(p); x[i]-=1
            if j==len(p): x.append(1)
            else: x[j]+=1
            q=tuple(sorted((t for t in x if t), reverse=True))
            if q!=p:out.add(q)
    return out

def conjugate(p):
    return tuple(sum(x>=j for x in p) for j in range(1,p[0]+1))

def conjugate_edge(p,q):
    a=conjugate(p);b=conjugate(q)
    m=max(len(a),len(b)); d=[(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(m)]
    return sorted(t for t in d if t)==[-1,1]

def graph(n,k):
    verts=partitions_bounded(n,k)
    ids={p:i for i,p in enumerate(verts)}
    N=[{i} for i in range(len(verts))]
    for i,p in enumerate(verts):
        for q in transfer_neighbors(p):
            if q in ids:N[i].add(ids[q])
    return verts,N

def check_lex(n):
    vs=sorted((p+(0,)*(3-len(p)) for p in partitions_bounded(n,3)))
    vs.sort(key=lambda p:(p[0],p[1]))
    ids={p:i for i,p in enumerate(vs)}
    N=[{i} for i in range(len(vs))]
    for i,p in enumerate(vs):
        for q in transfer_neighbors(p):
            q=q+(0,)*(3-len(q))
            if q in ids:N[i].add(ids[q])
    assert vs[-1]==(n,0,0)
    for i,(a,b,c) in enumerate(vs[:-1]):
        dest=(a+1,b,c-1) if c else (a+1,b-1,0)
        dest=tuple(sorted(dest,reverse=True))
        j=ids[dest]
        assert j>i, (n,vs[i],dest)
        current={t for t in N[i] if t>=i}
        assert current <= N[j], (n,vs[i],dest,current)
    return len(vs)-1

CERTIFICATE=[
 ((2,2,2,2),(3,2,2,1)),
 ((4,4),(5,3)),
 ((5,1,1,1),(5,2,1)),
 ((5,3),(5,2,1)),
 ((6,1,1),(6,2)),
 ((8,),(7,1)),
 ((7,1),(6,2)),
 ((6,2),(5,2,1)),
 ((5,2,1),(4,3,1)),
]

def check_eight():
    vs,N=graph(8,4);ids={p:i for i,p in enumerate(vs)}
    assert len(vs)==15
    for i,p in enumerate(vs):
        for j,q in enumerate(vs):
            if i!=j: assert (j in N[i]) == conjugate_edge(p,q), (p,q)
    alive=set(range(len(vs)))
    for p,q in CERTIFICATE:
        i,j=ids[p],ids[q]
        assert i in alive and j in alive
        assert N[i]&alive <= N[j]&alive, (p,q)
        alive.remove(i)
    remain=[vs[i] for i in sorted(alive)]
    assert len(remain)==6
    nons=set()
    for i,j in combinations(alive,2):
        if j not in N[i]:nons.add(frozenset((vs[i],vs[j])))
    expected={frozenset(p) for p in [
     ((4,3,1),(3,2,2,1)),
     ((4,2,2),(3,3,1,1)),
     ((4,2,1,1),(3,3,2)),
    ]}
    assert nons==expected
    # The six-vertex residual graph is the complete graph minus a perfect matching;
    # its flag complex is the join of three two-point spaces (octahedral 2-sphere).
    # Count all cliques in original and residual graphs, independently.
    def counts(indices):
        out=[]
        for r in range(1,len(indices)+1):
            v=sum(all(j in N[i] for i,j in combinations(c,2)) for c in combinations(indices,r))
            if v:out.append(v)
        return out
    assert counts(list(range(len(vs))))==[15,30,18,1]
    assert counts(sorted(alive))==[6,12,8]
    return len(CERTIFICATE),remem(remain)

def remem(remain):return ';'.join(str(x) for x in remain)

if __name__=='__main__':
    for n in range(1,31):
        vs,N=graph(n,3)
        for i,p in enumerate(vs):
            for j,q in enumerate(vs):
                if i!=j:assert (j in N[i])==conjugate_edge(p,q),(n,p,q)
    foldcount=sum(check_lex(n) for n in range(1,151))
    f,remain=check_eight()
    print('PARTITION_TRANSFER_BOUNDARY_PASS')
    print('Independent conjugate-vs-transfer graph agreement: n=1..30, length <=3 and n=8, length <=4')
    print('Explicit lexicographic domination sweep: n=1..150; verified vertex folds:',foldcount)
    print('At n=8, length <=4: 15 vertices, 30 edges, 18 triangles, 1 tetrahedron')
    print('At n=8: 9 valid strong folds; remaining flag complex has f-vector (6,12,8)')
    print('Remaining graph is the octahedral graph, with opposite nonedges forming a perfect matching')
    print('Remaining vertex set:',remain)
