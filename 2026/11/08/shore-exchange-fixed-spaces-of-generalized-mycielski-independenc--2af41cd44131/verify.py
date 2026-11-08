"""Independent finite checks of balanced-bipartite Mycielskian involution fixed spaces.
Python 3 standard library, no external data required.
"""
from itertools import combinations
from collections import defaultdict

def graph(a,ell):
    verts=[('w',-1,0)] + [(s,i,t) for t in range(1,ell+2) for s in ('A','B') for i in range(a)]
    E=set()
    def edge(u,v): E.add(frozenset((u,v)))
    for s in ('A','B'):
        for i in range(a): edge(('w',-1,0),(s,i,1))
    for t in range(1,ell+1):
        for i in range(a):
            for j in range(a):
                edge(('A',i,t),('B',j,t+1))
                edge(('B',i,t),('A',j,t+1))
    for i in range(a):
        for j in range(a): edge(('A',i,ell+1),('B',j,ell+1))
    return verts,E

def involute(v):
    if v[0]=='w':return v
    return ('B' if v[0]=='A' else 'A',v[1],v[2])

def fixed_graph(a,ell):
    V,E=graph(a,ell)
    assert {frozenset((involute(u),involute(v))) for u,v in (tuple(x) for x in E)}==E
    orbits=[];seen=set()
    for v in V:
        if v not in seen:
            o=frozenset((v,involute(v)));seen.update(o)
            if not (len(o)==2 and o in E):orbits.append(o)
    expected={frozenset((('w',-1,0),))}
    expected|={frozenset((('A',i,t),('B',i,t))) for t in range(1,ell+1) for i in range(a)}
    assert set(orbits)==expected,(a,ell,'orbit set')
    orbit_edges={frozenset((i,j)) for i in range(len(orbits)) for j in range(i+1,len(orbits))
                 if any(frozenset((u,v)) in E for u in orbits[i] for v in orbits[j])}
    def level(o): return next(iter(o))[2]
    # apex is level zero. The orbit graph must be complete between consecutive
    # levels and edgeless among vertices of any single level.
    for i,j in combinations(range(len(orbits)),2):
        assert (frozenset((i,j)) in orbit_edges)==(abs(level(orbits[i])-level(orbits[j]))==1),(a,ell,i,j)
    # Every layer consists of false twins, enabling elementary collapse.
    for t in range(1,ell+1):
        layer=[i for i,o in enumerate(orbits) if level(o)==t]
        for x,y in combinations(layer,2):
            Nx={j for j in range(len(orbits)) if frozenset((x,j)) in orbit_edges}
            Ny={j for j in range(len(orbits)) if frozenset((y,j)) in orbit_edges}
            assert Nx==Ny and y not in Nx
    return V,E,orbits,orbit_edges

def ind_faces(n,E):
    adj=[0]*n
    for e in E:
        x,y=tuple(e)
        adj[x]|=1<<y;adj[y]|=1<<x
    faces=[0]
    # construct from independent subsets in reverse order
    for v in range(n):
        bit=1<<v
        faces.extend(f|bit for f in list(faces) if not (f&adj[v]))
    return faces

def betti_mod2(faces):
    by_dim=defaultdict(list)
    for f in faces:
        if f:by_dim[f.bit_count()-1].append(f)
    maxdim=max(by_dim,default=-1)
    ranks={}
    for d in range(1,maxdim+1):
        rows={f:i for i,f in enumerate(by_dim[d-1])}
        piv={};rank=0
        for f in by_dim[d]:
            # d-th boundary, sign irrelevant over F_2
            a=f; c=0
            while a:
                bit=a&-a;a-=bit;c^=1<<rows[f^bit]
            while c:
                p=c.bit_length()-1
                if p not in piv:piv[p]=c;rank+=1;break
                c^=piv[p]
        ranks[d]=rank
    out={}
    for d in range(maxdim+1):
        z=len(by_dim[d])-ranks.get(d,0)
        b=z-ranks.get(d+1,0)
        if d==0:b-=1
        if b:out[d]=b
    return out

def formula(ell):
    k=ell//3
    if ell%3==0: return {},(2*k,2,0) # Betti of ambient, trace
    dim_=2*k+1
    return ({k:1},(dim_,1,(-1)**(k+1)))

checks=0; face_checks=0; betti_checks=0; trace_checks=0
for a in (1,2,3):
    for ell in range(0,7):
        V,E,O,EO=fixed_graph(a,ell)
        checks+=1
        expect,amb=formula(ell)
        faces=ind_faces(len(O),EO)
        # independent orbit sets are in bijection with invariant independent faces
        for f in faces:
            support=set().union(*(O[i] for i in range(len(O)) if f>>i&1))
            assert all(not e<=support for e in E)
            assert all(involute(v) in support for v in support)
        face_checks+=len(faces)
        # Reduced Lefschetz: empty face contributes -1 to unreduced alternating sum
        reduced=sum((-1)**(f.bit_count()-1) for f in faces)
        assert reduced == ((-1)**amb[0])*amb[2],(a,ell,reduced,amb)
        trace_checks+=1
        if a<=2 and ell<=5:
            b=betti_mod2(faces)
            assert b==expect,(a,ell,b,expect)
            betti_checks+=1
        if a==2:print('a=2 ell=',ell,'orbit_vertices=',len(O),'fixed_faces=',len(faces),'reduced_homology=',expect,'ambient_trace=',amb[2])
# Independent signed-simplex trace check without orbit-graph enumerator
for a in (1,2):
    for ell in range(0,4):
        V,E=graph(a,ell); n=len(V)
        index={v:i for i,v in enumerate(V)}
        move=[index[involute(v)] for v in V]
        # use brute-force invariant subsets of full graph, with independent test
        trace=-1 # empty simplex in reduced Lefschetz convention
        for mask in range(1,1<<n):
            if any((mask>>i)&1 != (mask>>move[i])&1 for i in range(n)):continue
            support={v for i,v in enumerate(V) if mask>>i&1}
            if any(e<=support for e in E):continue
            pairs=sum(1 for i in range(n) if mask>>i&1 and move[i]>i)
            trace+=(-1)**(mask.bit_count()-1+pairs)
        amb=formula(ell)[1]
        assert trace == ((-1)**amb[0])*amb[2],(a,ell,trace,amb)
        trace_checks+=1
print('ALL_VERIFY_OK', 'graph_orbit_cases=',checks,'invariant_faces=',face_checks,'GF2_cases=',betti_checks,'signed_Lefschetz_cases=',trace_checks)
