"""Independent shortest-geodesic verification of tree-product total visibility."""
from itertools import combinations
from collections import deque, Counter
from math import comb

def product_graph(t_adj, n):
    # H = K_n square K_2 ; graph = T square H
    tv=len(t_adj); vs=[(t,i,b) for t in range(tv) for i in range(n) for b in range(2)]
    idx={v:j for j,v in enumerate(vs)}; adj=[set() for _ in vs]
    for j,(t,i,b) in enumerate(vs):
        for u in t_adj[t]: adj[j].add(idx[u,i,b])
        for k in range(n):
            if k!=i: adj[j].add(idx[t,k,b])
        adj[j].add(idx[t,i,1-b])
    return vs,[sorted(a) for a in adj]

def full_distance(adj,s):
    d=[-1]*len(adj); d[s]=0; q=deque([s])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if d[v]<0: d[v]=d[u]+1; q.append(v)
    return d

def all_geodesic_boundary_paths(adj,vs,boundary):
    # Geodesic path computation by independent BFS then DAG traversal.
    dmat=[full_distance(adj,s) for s in range(len(vs))]
    B={v:i for i,v in enumerate(boundary)}; tests=[]; maxpaths=0
    for s in range(len(vs)):
        for t in range(s+1,len(vs)):
            D=dmat[s][t]
            if D<=1: continue
            paths=set()
            def rec(v,inside):
                if v==t:
                    paths.add(inside);return
                for w in adj[v]:
                    if dmat[s][w]==dmat[s][v]+1 and dmat[s][w]+dmat[w][t]==D:
                        rec(w,inside | ((1<<B[w]) if w in B and w!=t else 0))
            rec(s,0)
            if 0 in paths: continue
            # prune obsolete geodesics which have a strict superset of internal boundary vertices
            paths={p for p in paths if not any(q!=p and (q&p)==q for q in paths)}
            tests.append(tuple(paths));maxpaths=max(maxpaths,len(paths))
    return tests,maxpaths

def valid(s,tr,boundary):
    bmask=sum(1<<j for j,u in enumerate(boundary) if (s>>u)&1)
    return all(any(bmask&p==0 for p in paths) for paths in tr)

def baseline(S, vs, leaves, n):
    for leaf in leaves:
        chosen={(i,b) for v,(t,i,b) in enumerate(vs) if t==leaf and (S>>v)&1}
        for i in range(n):
            for j in range(n):
                if i!=j and (i,0) in chosen and (j,1) in chosen:return False
    return True

def expected(n,ell):
    a=[0]*(n+1)
    for k in range(n+1): a[k]=2*comb(n,k)
    a[0]-=1;a[2]+=n
    p=[1]
    for _ in range(ell):
        q=[0]*(len(p)+len(a)-1)
        for i,x in enumerate(p):
            for j,y in enumerate(a):q[i+j]+=x*y
        p=q
    return p

def run_case(adj_t,n,limit=None):
    leaves=[i for i,ns in enumerate(adj_t) if len(ns)==1]
    vs,g=product_graph(adj_t,n)
    boundary=[i for i,(t,a,b) in enumerate(vs) if t in leaves]
    tr,maxpaths=all_geodesic_boundary_paths(g,vs,boundary)
    count=Counter();checked=0
    for m in range(1<<len(boundary)):
        s=sum(1<<boundary[j] for j in range(len(boundary)) if (m>>j)&1)
        a=baseline(s,vs,leaves,n)
        b=valid(s,tr,boundary)
        if a!=b:raise AssertionError(('mismatch',adj_t,n,bin(m),a,b))
        if b:count[m.bit_count()]+=1
        checked+=1
    coefficients=expected(n,len(leaves))
    assert [count[k] for k in range(len(coefficients))]==coefficients, (count,coefficients)
    # no middle-layer vertices can appear even in a singleton admissible set
    for u,(t,i,b) in enumerate(vs):
        if t in leaves:continue
        fulls=1<<u
        # test complete graph distance directly by finding geodesic path bypassing u
        for a in range(len(vs)):
            for c in range(a+1,len(vs)):
                if a==u or c==u:continue
                d_all=full_distance(g,a)[c]
                # one removed vertex
                h=[tuple(w for w in ng if w!=u) if j!=u else () for j,ng in enumerate(g)]
                if full_distance(h,a)[c]>d_all or full_distance(h,a)[c]<0:break
            else:continue
            break
        else:raise AssertionError('interior singleton wrongly allowed')
    print('PASS','tree_vertices',len(adj_t),'leaves',len(leaves),'n',n,'boundary_masks',checked,'valid_faces',sum(count.values()),'geodesic_tests',len(tr),'path_variants',maxpaths)
    return checked


def gf2_rank(columns):
    pivots={}
    for x in columns:
        while x:
            k=x.bit_length()-1
            if k not in pivots:
                pivots[k]=x;break
            x^=pivots[k]
    return len(pivots)

def check_mod2_homology(n,ell):
    # Build all local allowed faces independently from forbidden diagonal pairs.
    local=[]
    for mask in range(1<<(2*n)):
        choose={(i,b) for i in range(n) for b in range(2) if (mask>>(2*i+b))&1}
        if all(not ((i,0) in choose and (j,1) in choose) for i in range(n) for j in range(n) if i!=j):
            local.append(mask)
    allfaces=[0]
    for t in range(ell):
        allfaces=[p | (q << (2*n*t)) for p in allfaces for q in local]
    groups={}
    for f in allfaces:groups.setdefault(f.bit_count()-1,[]).append(f)
    maxdim=max(groups)
    ranks={}
    for d in range(1,maxdim+1):
        lows={f:i for i,f in enumerate(groups[d-1])}
        cols=[]
        for f in groups.get(d,[]):
            x=0
            for k in range(2*n*ell):
                if (f>>k)&1:x^=1<<lows[f^(1<<k)]
            cols.append(x)
        ranks[d]=gf2_rank(cols)
    # Add augmented reduced d_0 of rank one, including empty face.
    ranks[0]=1
    betti={d:len(groups.get(d,[]))-ranks.get(d,0)-ranks.get(d+1,0) for d in range(maxdim+1)}
    target={2*ell-1:(n-1)**ell}
    assert {d:r for d,r in betti.items() if r}==target,(n,ell,betti,target)
    print('HOMOLOGY_PASS','n',n,'leaves',ell,'faces',len(allfaces),'top_betti',target)

if __name__=='__main__':
    trees=[[[1],[0,2],[1]],[[1],[0,2],[1,3],[2]],[[1,2,3],[0],[0],[0]],[[1],[0,2,3],[1,4],[1],[2]]]
    c=0
    for ti,n in [(0,2),(0,3),(1,2),(2,2),(3,2)]:c+=run_case(trees[ti],n)
    for n,ell in [(2,2),(3,2),(2,3)]:check_mod2_homology(n,ell)
    print('VERIFY_OK', 'cases=5',f'boundary_masks={c}','all_shortest_paths=PASS','face_polynomials=PASS','forbidden_interior_singletons=PASS','mod2_homology=PASS')
