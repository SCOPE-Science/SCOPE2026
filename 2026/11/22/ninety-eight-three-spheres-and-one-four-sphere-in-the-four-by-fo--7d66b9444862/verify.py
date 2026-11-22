#!/usr/bin/env python3
"""Exact simplicial and integral Morse certificate for four-by-four rook GP complex.

No third-party Python dependencies. Builds faces from pairwise Hamming geodesics,
constructs lexicographic acyclic face-poset matching, verifies its directed
Hasse graph, and calculates the remaining integral Morse boundary by unit
elimination in integer simplicial chains.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

M = N = 4
SIZE = M*N

def metric_faces():
    def dist(a,b):
        return (a % M != b % M) + (a // M != b // M)
    bad = []
    for a,b,c in combinations(range(SIZE),3):
        if dist(a,b)+dist(b,c)==dist(a,c) or dist(a,c)+dist(c,b)==dist(a,b) or dist(b,a)+dist(a,c)==dist(b,c):
            bad.append((1<<a)|(1<<b)|(1<<c))
    faces = {m for m in range(1,1<<SIZE) if not any(m&t==t for t in bad)}
    return faces,len(bad)

def facet_faces():
    # Independent, purely combinatorial: every column supports zero or one
    # selected vertex, unless all selected edges make a star forest in K4,4.
    all_faces = set()
    for mask in range(1,1<<SIZE):
        edges=[(i%M,i//M) for i in range(SIZE) if mask&(1<<i)]
        # A selected edge-set is a star forest iff every component has diameter 2.
        adj={('r',r):set() for r in range(M)}
        adj.update({('c',c):set() for c in range(N)})
        for r,c in edges:
            adj[('r',r)].add(('c',c));adj[('c',c)].add(('r',r))
        seen=set();valid=True
        for u in adj:
            if u in seen or not adj[u]:continue
            todo=[u];vertices=set()
            while todo:
                x=todo.pop()
                if x in vertices:continue
                vertices.add(x);todo.extend(adj[x]-vertices)
            seen|=vertices
            degrees=[len(adj[v]) for v in vertices]
            if max(degrees)<len(vertices)-1:
                valid=False;break
        if valid: all_faces.add(mask)
    return all_faces

def matching(faces):
    remaining=set(faces)
    matches={}
    for i in range(SIZE):
        for a in sorted(remaining):
            b=a|(1<<i)
            if a&(1<<i) or b not in remaining:continue
            remaining.remove(a);remaining.remove(b)
            matches[a]=b
    return matches,remaining

def boundary(face):
    verts=[i for i in range(SIZE) if face&(1<<i)]
    return {face^(1<<vertex):(-1)**pos for pos,vertex in enumerate(verts)}

def acyclicity(faces,matches):
    indeg={f:0 for f in faces}
    edges=[]
    for b in faces:
        for a in boundary(b):
            if not a: continue
            if matches.get(a)==b: x,y=a,b
            else: x,y=b,a
            indeg[y]+=1
            edges.append((x,y))
    adj=defaultdict(list)
    for x,y in edges: adj[x].append(y)
    queue=deque(x for x in faces if not indeg[x]);visited=0
    while queue:
        x=queue.popleft();visited+=1
        for y in adj[x]:
            indeg[y]-=1
            if indeg[y]==0: queue.append(y)
    assert visited==len(faces),f'cyclic matching {visited} / {len(faces)}'
    return len(edges)

def integer_morse_differential(critical,match):
    bydim=defaultdict(list)
    for c in critical: bydim[c.bit_count()-1].append(c)
    assert len(bydim[4])==1
    coefficients=defaultdict(int)
    for x,v in boundary(bydim[4][0]).items(): coefficients[x]+=v
    critical_three=set(bydim[3]);
    inverse={a:b for a,b in match.items() if a.bit_count()==4}
    nsteps=0
    while True:
        eligible=next((a for a,v in coefficients.items() if v and a in inverse),None)
        if eligible is None:break
        b=inverse[eligible]; db=boundary(b)
        div=db[eligible]
        assert abs(div)==1
        factor=coefficients[eligible]//div
        for x,v in db.items():coefficients[x]-=factor*v
        nsteps+=1
        assert nsteps<=20000
    leftovers={x:v for x,v in coefficients.items() if v}
    # Remaining noncritical 3-faces are the *upper* cells of 2--3
    # cancellation pairs. Their coordinates vanish under that cancellation.
    assert all(x in critical_three or x in match.values() for x in leftovers)
    assert not leftovers, leftovers
    critical_coefficients={x:v for x,v in leftovers.items() if x in critical_three}
    import math
    divisor=math.gcd(*(abs(x) for x in critical_coefficients.values()))
    assert divisor == 0 and not critical_coefficients,(divisor,critical_coefficients)
    return nsteps,divisor,len(critical_coefficients)

def mod2_boundary_ranks(faces):
    bydim=defaultdict(list)
    for f in faces: bydim[f.bit_count()-1].append(f)
    ranks={}
    for d in range(1,max(bydim)+1):
        ids={f:i for i,f in enumerate(bydim[d-1])}
        pivots={}
        for f in bydim[d]:
            z=0
            for face in boundary(f):z^=1<<ids[face]
            while z:
                p=z.bit_length()
                if p not in pivots: pivots[p]=z;break
                z^=pivots[p]
        ranks[d]=len(pivots)
    return {d:len(v)-ranks.get(d,0)-ranks.get(d+1,0) for d,v in bydim.items()}

def main():
    faces,bad=metric_faces()
    assert faces==facet_faces()
    pairs,critical=matching(faces)
    assert len(faces)==1440 and len(pairs)==670
    counts=dict(sorted(Counter(f.bit_count()-1 for f in critical).items()))
    assert counts=={0:1,3:98,4:1},counts
    relations=acyclicity(faces,pairs)
    steps,smith_factor,support=integer_morse_differential(critical,pairs)
    betti=mod2_boundary_ranks(faces)
    assert betti=={0:1,1:0,2:0,3:98,4:1,5:0}
    print(f'forbidden_geodesic_triples={bad}')
    print(f'nonempty_faces={len(faces)} hasse_cover_relations={relations}')
    print(f'paired_faces={2*len(pairs)} pairs={len(pairs)}')
    print(f'critical_cells={counts} graph_acyclic=True')
    print(f'integral_critical_four_to_three_boundary_gcd={smith_factor} nonzero_entries={support} gradient_reductions={steps}')
    print(f'independent_mod2_betti={dict(sorted(betti.items()))}')
    print('VERIFY_OK: homotopy = wedge of 98 copies S^3 and one S^4')

if __name__=='__main__':main()
