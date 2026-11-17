"""Exact, standalone certificate for the induced-forest complex of the Pappus graph.
No external mathematical packages are required for the Morse computation.
"""
from collections import Counter, deque, defaultdict
from functools import lru_cache
import json, math

LCF = (5, 7, -7, 7, -7, -5) * 3
N = len(LCF)
PIVOTS = (17,11,13,7,3,0,9,16,5,12,10,14,8,6,4,2,15,1)


def graph():
    e = set()
    for i,k in enumerate(LCF):
        e.add(tuple(sorted((i, (i+1)%N))))
        e.add(tuple(sorted((i, (i+k)%N))))
    assert len(e) == 27
    adj = [0]*N
    for a,b in e:
        adj[a] |= (1<<b)
        adj[b] |= (1<<a)
    assert all(x.bit_count()==3 for x in adj)
    return tuple(sorted(e)),tuple(adj)


def is_forest(mask, adj):
    parent=list(range(N))
    def rt(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]
            a=parent[a]
        return a
    for u in range(N):
        if not (mask>>u)&1: continue
        neighbors=adj[u]&mask&~((1<<(u+1))-1)
        while neighbors:
            lb=neighbors&-neighbors
            v=lb.bit_length()-1
            neighbors ^= lb
            r,s=rt(u),rt(v)
            if r==s:return False
            parent[r]=s
    return True


def independent_forest_check(mask, edges):
    # Independent component-count test: forest iff edges = vertices - components.
    present=set(i for i in range(N) if mask>>i & 1)
    neighbor={i:set() for i in present}
    edges_here=0
    for a,b in edges:
        if a in present and b in present:
            neighbor[a].add(b)
            neighbor[b].add(a)
            edges_here+=1
    unseen=set(present);components=0
    while unseen:
        components+=1
        start=unseen.pop();stack=[start]
        while stack:
            v=stack.pop()
            for w in neighbor[v]&unseen:
                unseen.remove(w);stack.append(w)
    return edges_here==len(present)-components


def all_faces(adj):
    faces=[];fvector=Counter()
    for s in range(1<<N):
        if is_forest(s,adj):
            faces.append(s)
            fvector[s.bit_count()-1]+=1
    return faces,dict(sorted(fvector.items()))


def vertex_matching(faces):
    # Perform disjoint stage matchings, visiting bits in PIVOTS order.
    # The empty face is included in this *augmented* matching.
    free=set(faces)
    low2up={}
    up2low={}
    for v in PIVOTS:
        b=1<<v
        for f in faces:
            if not f & b and f in free and f|b in free:
                free.remove(f)
                free.remove(f|b)
                low2up[f]=f|b
                up2low[f|b]=f
    assert len(free)+2*len(low2up)==len(faces)
    assert 0 not in free and 0 in low2up
    return sorted(free),low2up,up2low


def directed_hasse_acyclic(faces, low2up, up2low):
    faceset=set(faces)
    indeg={s:0 for s in faces}
    arrows=0
    for upper in faces:
        t=upper
        while t:
            bit=t&-t; t-=bit
            lower=upper^bit
            if low2up.get(lower)==upper:
                indeg[upper]+=1
            else:
                indeg[lower]+=1
            arrows+=1
    todo=deque(x for x in faces if indeg[x]==0)
    processed=0
    while todo:
        face=todo.popleft(); processed+=1
        if face in low2up:
            high=low2up[face]
            indeg[high]-=1
            if indeg[high]==0:todo.append(high)
        bits=face
        while bits:
            b=bits&-bits;bits-=b
            lower=face^b
            if low2up.get(lower)!=face:
                indeg[lower]-=1
                if indeg[lower]==0:todo.append(lower)
    assert processed==len(faces), (processed,len(faces))
    return arrows,processed


def boundary(high):
    t=high;idx=0
    while t:
        bit=t&-t;t-=bit
        yield (high^bit), (-1 if idx&1 else 1)
        idx+=1


def morse_critical_boundary(critical,low2up,up2low):
    critset=set(critical)
    @lru_cache(None)
    def reduce_lower(low):
        if low in critset:return ((low,1),)
        if low in up2low:return ()
        upper=low2up.get(low)
        if upper is None: raise AssertionError(('unmatched noncritical',low))
        pivot_sign=next(sign for f,sign in boundary(upper) if f==low)
        out=defaultdict(int)
        for f,s in boundary(upper):
            if f==low:continue
            for target,coeff in reduce_lower(f):
                out[target] -= pivot_sign*s*coeff
        return tuple(sorted((x,v) for x,v in out.items() if v))
    crit_dim=Counter(x.bit_count()-1 for x in critical)
    source=[x for x in critical if x.bit_count()==12]
    target=[x for x in critical if x.bit_count()==11]
    assert crit_dim=={10:43,11:3},crit_dim
    values=[]
    for h in source:
        acc=defaultdict(int)
        for f,sgn in boundary(h):
            for x,c in reduce_lower(f):
                acc[x]+=sgn*c
        assert all(x in target for x in acc)
        values.append([acc[x] for x in target])
    return source,target,values,reduce_lower.cache_info()


def graph_automorphisms(edges):
    # Derive all permutations by backtracking adjacency, without networkx.
    edge_set=set(edges)
    adj=[set() for _ in range(N)]
    for x,y in edges:adj[x].add(y);adj[y].add(x)
    # Need better efficient choice: graph is cubic, branch on mapped-neighbor constraint.
    mappings=[]
    def dfs(partial,used):
        if len(partial)==N:
            mappings.append(tuple(partial[i] for i in range(N)));return
        unassigned=[i for i in range(N) if i not in partial]
        v=max(unassigned,key=lambda i:(len(adj[i]&partial.keys()),-i))
        hits={partial[w] for w in adj[v] if w in partial}
        misses={partial[w] for w in partial if w not in adj[v] and w!=v}
        for x in range(N):
            if x in used or not hits<=adj[x] or adj[x]&misses:continue
            partial[v]=x
            dfs(partial,used|{x})
            del partial[v]
    dfs({},set())
    assert len(mappings)==216,len(mappings)
    return sorted(mappings)


def inverse(g):
    v=[0]*len(g)
    for i,x in enumerate(g):v[x]=i
    return tuple(v)

def compose(g,h):return tuple(g[h[i]] for i in range(len(g)))

def cycle_lengths(g):
    seen=set(); lengths=[]
    for i in range(N):
        if i in seen:continue
        j=i;cycle=[]
        while j not in seen:
            seen.add(j);cycle.append(j);j=g[j]
        lengths.append(len(cycle))
    return tuple(sorted(lengths))

def cycles(g):
    seen=set(); items=[]
    for i in range(N):
        if i in seen:continue
        j=i;cyc=[]
        while j not in seen:
            seen.add(j);cyc.append(j);j=g[j]
        items.append(sum(1<<k for k in cyc))
    return items

def trace_character(g,adj):
    # Every g-invariant vertex subset is a union of permutation cycles.
    # sign(g|S)*(-1)^{|S|-1}=(-1)^{number of included cycles-1}.
    orbit=cycles(g);tot=0
    for a in range(1<<len(orbit)):
        s=0
        for k,cyc in enumerate(orbit):
            if a>>k&1:s|=cyc
        if is_forest(s,adj):
            tot += (-1 if a.bit_count()%2==0 else 1)
    return tot


def direct_signed_trace(g, adj):
    # A separate implementation of the signed simplicial Lefschetz sum.
    tot=0
    orbit=cycles(g)
    for j in range(1<<len(orbit)):
        mask=0
        for k, o in enumerate(orbit):
            if j>>k&1:mask|=o
        if not is_forest(mask,adj):continue
        vertices=[v for v in range(N) if mask>>v&1]
        target=[g[v] for v in vertices]
        inversions=sum(target[i]>target[k] for i in range(len(target)) for k in range(i+1,len(target)))
        sign=(-1 if (inversions+len(vertices)-1)%2 else 1)
        tot+=sign
    return tot


def conjugacy_classes(group):
    gset=set(group);identity=tuple(range(N))
    assert len(group)==len(gset) and identity in gset
    classes=[]
    remaining=set(group)
    while remaining:
        g=min(remaining)
        conj={compose(compose(h,g),inverse(h)) for h in group}
        assert conj<=remaining
        remaining-=conj
        classes.append(sorted(conj))
    return sorted(classes,key=lambda c:(-len(c),c[0]))


def main():
    edges,adj=graph()
    faces, fvector=all_faces(adj)
    for s in range(1<<N):
        assert is_forest(s,adj)==independent_forest_check(s,edges),s
    assert len(faces)==204492
    assert sum(((-1)**d)*c for d,c in fvector.items())==40
    crit,low2up,up2low=vertex_matching(faces)
    assert Counter(s.bit_count()-1 for s in crit)=={10:43,11:3}
    arrows,processed=directed_hasse_acyclic(faces,low2up,up2low)
    source,target,M,cacheinfo=morse_critical_boundary(crit,low2up,up2low)
    # rank three with determinant ±1 from explicit 3x3 minor
    # M is 3x43; choose any 3 columns with unit determinant.
    import itertools
    pivot=None
    for ijk in itertools.combinations(range(len(target)),3):
        v=[[M[i][j] for j in ijk] for i in range(3)]
        det=(v[0][0]*(v[1][1]*v[2][2]-v[1][2]*v[2][1])
            -v[0][1]*(v[1][0]*v[2][2]-v[1][2]*v[2][0])
            +v[0][2]*(v[1][0]*v[2][1]-v[1][1]*v[2][0]))
        if abs(det)==1:pivot=(ijk,v,det);break
    print('PAPPUS_FOREST_FVECTOR',json.dumps(fvector,sort_keys=True))
    print('MATCHED_PAIRS',len(low2up),'CRITICAL_DIMS',dict(sorted(Counter(s.bit_count()-1 for s in crit).items())))
    print('DIRECTED_HASSE',arrows,'TOPOLOGICAL_SORT_VISITED',processed)
    print('MORSE_BOUNDARY_11_TO_10',json.dumps(M))
    print('UNIMODULAR_MINOR',json.dumps(pivot))
    assert pivot is not None
    group=graph_automorphisms(edges)
    classes=conjugacy_classes(group)
    assert len(classes)==13,len(classes)
    ctable=[]
    for c in classes:
        representative=c[0];ch=trace_character(representative,adj)
        assert all(trace_character(g,adj)==ch for g in c)
        ctable.append(dict(size=len(c),order=math.lcm(*cycle_lengths(representative)),cycles=cycle_lengths(representative),trace=ch,representative=representative))
    numerator_inv=sum(c['size']*c['trace'] for c in ctable)
    numerator_norm=sum(c['size']*c['trace']**2 for c in ctable)
    assert numerator_inv%216==0 and numerator_norm%216==0
    invs=numerator_inv//216
    norm=numerator_norm//216
    assert sum(c['size'] for c in ctable)==216
    idtrace=trace_character(tuple(range(N)),adj)
    assert idtrace==40
    special=[z for z in ctable if z['order']==3 and z['cycles']==(3,3,3,3,3,3)]
    assert len(special)==2 and {z['trace'] for z in special}=={1,4}
    for z in ctable:
        assert direct_signed_trace(z['representative'],adj)==z['trace']
    print('GROUP_ORDER',len(group),'CLASSES',len(classes),'CHARACTER',json.dumps(ctable,separators=(',',':')))
    print('CHARACTER_IDENTITY',idtrace,'INVARIANT_DIMENSION',invs,'CHARACTER_INNER_PRODUCT',norm)
    print('PAPPUS_FOREST_CERTIFICATE_PASS')

if __name__=='__main__':main()
