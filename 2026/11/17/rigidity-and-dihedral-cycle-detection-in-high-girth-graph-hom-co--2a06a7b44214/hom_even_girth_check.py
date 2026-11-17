"""Independent finite checks for even-cycle graph Hom complexes of high-girth graphs.
The vertex adjacency calculation uses only the defining multihomomorphism condition.
"""
from collections import Counter,defaultdict
from itertools import combinations,product

def cycle(n):
    return [set(((i-1)%n,(i+1)%n)) for i in range(n)]

def wedge_cycles(a,b):
    # Identify vertex zero, other vertices disjoint.
    adj=[set() for _ in range(a+b-1)]
    for n,verts in [(a,list(range(a))),(b,[0]+list(range(a,a+b-1)))]:
        for i in range(n):
            u,v=verts[i],verts[(i+1)%n]
            adj[u].add(v);adj[v].add(u)
    return adj

def petersen():
    pairs=list(combinations(range(5),2));n=len(pairs)
    return [{j for j in range(n) if not (set(pairs[i])&set(pairs[j]))} for i in range(n)]

def heawood():
    adj=[set() for _ in range(14)]
    lines=[{j,(j+1)%7,(j+3)%7} for j in range(7)]
    for i in range(7):
        for j,L in enumerate(lines):
            if i in L:adj[i].add(7+j);adj[7+j].add(i)
    return adj

def walks(adj,m):
    out=[]
    def rec(w):
        if len(w)==m:
            if w[0] in adj[w[-1]]:out.append(tuple(w))
            return
        for v in sorted(adj[w[-1]]):rec(w+[v])
    for v in range(len(adj)):rec([v])
    return out

def verify(adj,m,expected_girth_bound=True,check_euler=False):
    n=len(adj); W=walks(adj,m); idx={f:i for i,f in enumerate(W)}
    par=list(range(len(W)))
    def root(x):
        while x!=par[x]:par[x]=par[par[x]];x=par[x]
        return x
    def union(i,j):
        a,b=root(i),root(j)
        if a!=b:par[b]=a
    for i,f in enumerate(W):
        for p in range(m):
            before,after=f[(p-1)%m],f[(p+1)%m]
            for x in adj[before]&adj[after]:
                if x==f[p]:continue
                g=f[:p]+(x,)+f[p+1:]
                assert g in idx
                union(i,idx[g])
    components=defaultdict(list)
    for i,f in enumerate(W):components[root(i)].append(f)
    rigid={f for f in W if all(f[(i-1)%m]!=f[(i+1)%m] for i in range(m))}
    # Any homomorphism without an immediate backtrack is a rigid isolated vertex
    # in graphs with no quadrilaterals; verified by graph 1-skeleton.
    singles={xs[0] for xs in components.values() if len(xs)==1}
    if expected_girth_bound:
        assert all(len(set(f))==m for f in rigid)
        assert rigid==singles
        assert len(rigid)%(2*m)==0
        assert len(components)==(1 if not is_bipartite(adj) else 2)+len(rigid)
        nonsingle=[len(xs) for xs in components.values() if len(xs)>1]
        assert len(nonsingle)==(1 if not is_bipartite(adj) else 2) or (len(W)==len(components))
    result={'vertices':len(W),'components':len(components),'rigid':len(rigid),'m_cycles':len(rigid)//(2*m), 'component_sizes':dict(Counter(len(z) for z in components.values()))}
    if expected_girth_bound:
        # The natural source dihedral group acts on connected components.
        def image(f,rot,refl):
            return tuple(f[(((-i if refl else i)+rot)%m)] for i in range(m))
        labels={f:root(i) for i,f in enumerate(W)}
        nonsingle_labels={r for r,x in components.items() if len(x)>1}
        def source_orbit(f):
            return {image(f,rot,refl) for rot in range(m) for refl in (False,True)}
        for f in rigid:
            orbit=source_orbit(f)
            assert len(orbit)==2*m
            assert orbit<=rigid
        if nonsingle_labels:
            sample=components[next(iter(nonsingle_labels))][0]
            if is_bipartite(adj):
                assert len(nonsingle_labels)==2
                assert labels[image(sample,1,False)]!=labels[sample]
                assert labels[image(sample,0,True)]==labels[sample]
            else:
                assert len(nonsingle_labels)==1
        result['reduced_H0_dihedral_fixed_rank']=len(rigid)//(2*m)
    if check_euler:
        # Every Hom-cell is a product of nonempty simplices. Enumerate all
        # expansions of each vertex map into admissible multihomomorphisms.
        # Each coordinate is represented as a bitmask of admissible target vertices.
        cells=set(); edge={(a,b) for a in range(n) for b in adj[a]}
        for f in W:
            choices=[]
            for p in range(m):
                common=sorted(adj[f[(p-1)%m]]&adj[f[(p+1)%m]])
                choices.append([sum(1<<x for x in subset) for k in range(1,len(common)+1) for subset in combinations(common,k) if f[p] in subset])
            def add(p,z):
                if p==m:
                    if any((a,b) not in edge for a in extract(z[-1]) for b in extract(z[0])):return
                    cells.add(tuple(z));return
                for mask in choices[p]:
                    if p and any((a,b) not in edge for a in extract(z[-1]) for b in extract(mask)):continue
                    add(p+1,z+[mask])
            add(0,[])
        fvec=Counter(sum(q.bit_count()-1 for q in cell) for cell in cells)
        chi=sum((-1)**k*v for k,v in fvec.items())
        b1=sum(map(len,adj))//2-n+1
        theoretical=2-2*b1+len(rigid)
        assert chi==theoretical,(chi,theoretical)
        result['euler']=chi
        result['cell_dims']=dict(sorted(fvec.items()))
    return result

def extract(mask):
    while mask:
        j=mask&-mask
        yield j.bit_length()-1
        mask-=j

def is_bipartite(adj):
    color={}
    for s in range(len(adj)):
        if s in color:continue
        color[s]=0;todo=[s]
        for u in todo:
            for v in adj[u]:
                if v not in color:color[v]=1-color[u];todo.append(v)
                elif color[v]==color[u]:return False
    return True

if __name__=='__main__':
    for name,m,H in [('pentagon',6,cycle(5)),('hexagon',6,cycle(6)),('Petersen',6,petersen()),('Heawood',6,heawood()),('5+6 rose',6,wedge_cycles(5,6)),('heptagon',8,cycle(7)),('octagon',8,cycle(8)),('7+8 rose',8,wedge_cycles(7,8))]:
        out=verify(H,m,True,check_euler=m==6 and len(H)<=14)
        print(name,m,out)
    print('EVEN_CYCLE_HIGH_GIRTH_HOM_PASS')
