"""Reproducible finite checks for fixed point complexes of cyclic prism perfect-matching complexes."""
from itertools import combinations
from collections import defaultdict, deque


def grid_edges(n):
    E=[]
    for i in range(n):
        E.append(((0,i),(1,i))) # rung, index i
    for layer in (0,1):
        for i in range(n):
            a,b=(layer,i),(layer,(i+1)%n)
            E.append(tuple(sorted([a,b])))
    return [tuple(sorted(e)) for e in E]

def perfect_matchings(n):
    E=grid_edges(n)
    adj=defaultdict(list)
    for i,(u,v) in enumerate(E):
        adj[u].append((v,i)); adj[v].append((u,i))
    full=frozenset((l,j) for l in (0,1) for j in range(n))
    def rec(unmatched,chosen):
        if not unmatched:
            yield frozenset(chosen); return
        u=min(unmatched)
        for v,ei in adj[u]:
            if v in unmatched:
                yield from rec(unmatched-{u,v},chosen+(ei,))
    return set(rec(full,()))

def fixed_faces_from_perfect_matchings(n):
    pm=perfect_matchings(n)
    swap=lambda ei:ei if ei<n else (ei+n if ei<2*n else ei-n)
    invariant=set()
    invariant_raw=set()
    for match in pm:
        for k in range(len(match)+1):
            for cs in combinations(match,k):
                S=frozenset(cs)
                if {swap(e) for e in S}==set(S):
                    invariant_raw.add(S)
                    tt=frozenset([('R',e) for e in S if e<n]+[('H',e-n) for e in S if n<=e<2*n])
                    invariant.add(tt)
    direct_trace = -sum((-1)**(len(S)+sum(n<=e<2*n for e in S)) for S in invariant_raw)
    return invariant, len(pm), direct_trace

def tile_complex(n):
    # R_i is a 1-column tile, H_i is a 2-column tile on i, i+1.
    tiles=[('R',i) for i in range(n)]+[('H',i) for i in range(n)]
    occ={t:(1<<t[1]) if t[0]=='R' else (1<<t[1])|(1<<((t[1]+1)%n)) for t in tiles}
    out=set()
    def rec(pos,used,face):
        if pos==len(tiles):
            out.add(frozenset(face)); return
        rec(pos+1,used,face)
        t=tiles[pos]
        if not used&occ[t]: rec(pos+1,used|occ[t],face+[t])
    rec(0,0,[])
    return out

def matching(n,faces):
    # In unaugmented face poset, the singleton R0 is left critical.
    pairs={}; critical=[]
    for F in faces:
        H=frozenset(t[1] for t in F if t[0]=='H')
        free=[i for i in range(n) if i not in H and (i-1)%n not in H]
        if not free:
            critical.append(F); continue
        i=free[0]; rung=('R',i)
        low=F-{rung}
        high=low|{rung}
        if low and low in faces and high in faces:
            pairs[low]=high
        elif not low: critical.append(high)
    # ensure only 0 and top critical, no unmatched faces
    covered=set(pairs)|set(pairs.values())
    c=faces-{frozenset()}-covered
    assert len(pairs)*2+len(c)==len(faces)-1
    assert len(c)==(1+(2 if n%2==0 else 0)),(n,len(c))
    assert len([x for x in c if len(x)==1])==1
    if n%2==0: assert sorted(len(x) for x in c)==[1,n//2,n//2] or n==2
    else: assert all(len(x)==1 for x in c)
    return pairs,c

def hasse_acyclic(faces,pairs):
    # Each unmatched cover from high to low, matched cover from low to high.
    fs=set(faces)-{frozenset()}
    ind={F:0 for F in fs}; out=defaultdict(list); incidences=0
    for hi in fs:
        for x in hi:
            lo=hi-{x}
            if not lo: continue
            assert lo in fs
            incidences+=1
            if pairs.get(lo)==hi: u,v=lo,hi
            else: u,v=hi,lo
            out[u].append(v);ind[v]+=1
    q=deque(u for u in fs if ind[u]==0); seen=0
    while q:
        u=q.popleft();seen+=1
        for v in out[u]:
            ind[v]-=1
            if ind[v]==0:q.append(v)
    assert seen==len(fs),(seen,len(fs))
    return incidences

def reduced_lefschetz(n,faces):
    # layer exchange on each invariant full face acts by one transposition per H_i;
    # reduced Lefschetz is -sum_{invariant F including empty} (-1)^|F| sign.
    val=-sum((-1)**len(F) for F in faces)
    expected=0 if n%2 else -2*((-1)**(n//2))
    assert val==expected,(n,val,expected)
    return val


def run():
    for n in range(3,11):
        F=tile_complex(n)
        actual,np,rawtrace= fixed_faces_from_perfect_matchings(n)
        assert F==actual,(n,len(F),len(actual),len(F^actual))
        p,c=matching(n,F)
        e=hasse_acyclic(F,p)
        lefs=reduced_lefschetz(n,F)
        assert rawtrace==lefs,(n,rawtrace,lefs)
        print(f'n={n} perfect_matchings={np} invariant_faces={len(F)} matched_pairs={len(p)} critical_dimensions={sorted(len(f)-1 for f in c)} Hasse_incidences={e} reduced_Lefschetz={lefs} OK')
    print('ALL_VERIFY_OK')

if __name__=='__main__':run()

# Additional independent finite graph-family checks.  These are deliberately
# constructed from the perfect matchings of each Cartesian prism, not by
# assuming the monomer-dimer face characterization.
def graph_cases():
    return [
        ('K2', 2, [(0,1)]),
        ('P3', 3, [(0,1),(1,2)]),
        ('P4', 4, [(0,1),(1,2),(2,3)]),
        ('K4', 4, [(i,j) for i in range(4) for j in range(i+1,4)]),
        ('2K2', 4, [(0,1),(2,3)]),
        ('C4', 4, [(0,1),(1,2),(2,3),(0,3)]),
        ('empty4', 4, []),
        ('P5', 5, [(i,i+1) for i in range(4)]),
        ('K33', 6, [(i,j) for i in range(3) for j in range(3,6)]),
    ]

def pm_graph(n, edges):
    edges=[tuple(sorted(e)) for e in edges]
    adj=defaultdict(list)
    for i,(u,v) in enumerate(edges):
        adj[u].append((v,i)); adj[v].append((u,i))
    def rec(remaining):
        if not remaining:
            yield frozenset(); return
        u=min(remaining)
        for v,ei in adj[u]:
            if v in remaining:
                for S in rec(remaining-{u,v}):yield S|{ei}
    return set(rec(frozenset(range(n))))

def graph_prism_invariant_faces(n, edges):
    E=[tuple(sorted(e)) for e in edges]
    # Order graph prism edges rungs, first-layer edges, second-layer edges.
    prism=[((0,i),(1,i)) for i in range(n)]
    prism += [((0,u),(0,v)) for u,v in E]
    prism += [((1,u),(1,v)) for u,v in E]
    adj=defaultdict(list)
    for idx,(u,v) in enumerate(prism):
        adj[u].append((v,idx));adj[v].append((u,idx))
    def rec(remaining,chosen):
        if not remaining:
            yield frozenset(chosen);return
        u=min(remaining)
        for v,eid in adj[u]:
            if v in remaining:
                yield from rec(remaining-{u,v},chosen+(eid,))
    pm=set(rec(frozenset((side,i) for side in (0,1) for i in range(n)),()))
    inv=set(); tr=0
    for P in pm:
        for k in range(len(P)+1):
            for items in combinations(P,k):
                S=set(items)
                def swap(x):
                    if x<n:return x
                    return x+len(E) if x<n+len(E) else x-len(E)
                if {swap(x) for x in S}!=S:continue
                T=frozenset([('R',x) for x in S if x<n]+[('H',x-n) for x in S if n<=x<n+len(E)])
                inv.add(T)
    return inv,len(pm)

def tile_graph(n,edges):
    E=[tuple(sorted(e)) for e in edges]
    T=[('R',i) for i in range(n)]+[('H',j) for j in range(len(E))]
    occ=[1<<i for i in range(n)]+[(1<<u)|(1<<v) for (u,v) in E]
    faces=set()
    def rec(j,covered,face):
        if j==len(T):
            faces.add(frozenset(face));return
        rec(j+1,covered,face)
        if not (covered&occ[j]):rec(j+1,covered|occ[j],face+[T[j]])
    rec(0,0,[])
    return faces

def graph_matching(n,edges,faces):
    E=[tuple(sorted(e)) for e in edges]
    pairs={}
    for F in faces:
        occupied=set()
        for typ,j in F:
            if typ=='H':occupied.update(E[j])
        free=[i for i in range(n) if i not in occupied]
        if not free:continue
        i=free[0];r=('R',i)
        lo=F-{r};hi=lo|{r}
        if lo and lo in faces and hi in faces:pairs[lo]=hi
    covered=set(pairs)|set(pairs.values())
    crit=set(faces)-{frozenset()}-covered
    expected=pm_graph(n,edges)
    assert len(crit)==1+len(expected)
    assert sorted(len(f)-1 for f in crit)==sorted([0]+[n//2-1]*len(expected))
    return pairs,crit,hasse_acyclic(faces,pairs),len(expected)

def run_other_graphs():
    for name,n,edges in graph_cases():
        actual,number=graph_prism_invariant_faces(n,edges)
        F=tile_graph(n,edges)
        assert F==actual,(name,len(F),len(actual),len(F^actual))
        pairs,crit,inc,p=graph_matching(n,edges,F)
        assert (-sum((-1)**len(f) for f in F)) == (p*(-1)**(n//2-1) if n%2==0 else 0)
        print(f'{name} n={n} prism_PMs={number} base_PMs={p} invariant_faces={len(F)} matched_pairs={len(pairs)} critical_dimensions={sorted(len(f)-1 for f in crit)} Hasse_incidences={inc} OK')
    print('ALL_GRAPH_FAMILY_VERIFY_OK')

if __name__=='__main__':run_other_graphs()
