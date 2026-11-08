"""Exact checks for crown-cycle factorization in ordinary two-particle K_{p,q} configurations."""
from itertools import permutations
from collections import deque


def crown(p):
    edges=[(i,k) for i in range(p) for k in range(p) if i!=k]
    adj=[[] for _ in range(2*p)]
    tree=[]; parent=list(range(2*p))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    for j,(i,k) in enumerate(edges):
        a,b=find(i),find(p+k)
        if a!=b:
            parent[a]=b;tree.append(j)
            adj[i].append((p+k,j,1));adj[p+k].append((i,j,-1))
    assert len(tree)==2*p-1
    vectors=[]
    for j,(i,k) in enumerate(edges):
        if j in tree:continue
        start,end=p+k,i
        queue=deque([start]);prev={start:None}
        while queue and end not in prev:
            node=queue.popleft()
            for nxt,idx,sign in adj[node]:
                if nxt not in prev:
                    prev[nxt]=(node,idx,sign);queue.append(nxt)
        assert end in prev
        vec=[0]*len(edges);vec[j]=1
        cur=end
        while cur!=start:
            old,idx,sign=prev[cur];vec[idx]+=sign;cur=old
        assert all(sum(vec[k] for k,(i,j) in enumerate(edges) if i==s)==0 for s in range(p))
        assert all(sum(vec[k] for k,(i,j) in enumerate(edges) if j==s)==0 for s in range(p))
        vectors.append(vec)
    assert len(vectors)==p*p-3*p+1
    return edges,vectors


def graph(p,q):
    V=tuple(range(p+q));E=tuple((i,p+j) for i in range(p) for j in range(q))
    C0=tuple((v,w) for v in V for w in V if v!=w)
    C1=tuple((0,e,v) for e in E for v in V if v not in e)+tuple((1,v,e) for v in V for e in E if v not in e)
    C2=tuple((e,d) for e in E for d in E if set(e).isdisjoint(d))
    return V,E,C0,C1,C2


def group_action(p,q,a,b,side=False):
    if not side:
        return tuple(a[i] for i in range(p))+tuple(p+b[j] for j in range(q)),1
    assert p==q
    return tuple(p+b[i] for i in range(p))+tuple(a[j] for j in range(q)),-1


def chain_trace(p,q,a,b,side=False,particle_swap=False):
    V,E,C0,C1,C2=graph(p,q)
    g,edge_sign=group_action(p,q,a,b,side)
    def edge(e):
        x,y=g[e[0]],g[e[1]]
        return (min(x,y),max(x,y))
    def cell0(z):
        v,w=z
        return (g[w],g[v]) if particle_swap else (g[v],g[w])
    def cell1(z):
        if z[0]==0: # edge,vertex
            e,v=z[1:]
            return (1,g[v],edge(e)) if particle_swap else (0,edge(e),g[v])
        v,e=z[1:]
        return (0,edge(e),g[v]) if particle_swap else (1,g[v],edge(e))
    def cell2(z):
        e,d=z
        return (edge(d),edge(e)) if particle_swap else (edge(e),edge(d))
    tr0=sum(cell0(x)==x for x in C0)
    tr1=edge_sign*sum(cell1(x)==x for x in C1)
    tr2=(-1 if particle_swap else 1)*sum(cell2(x)==x for x in C2)
    fverts=sum(g[x]==x for x in V)
    fedges=sum(edge(e)==e for e in E)
    h1g=edge_sign*fedges-fverts+1
    trh1=0 if particle_swap else 2*h1g
    return tr0-tr1+tr2-1+trh1


def calc(p,q):
    P,B=crown(p),crown(q)
    ep, vp=P;eq,vq=B
    V,E,C0,C1,C2=graph(p,q)
    assert len(C2)==len(ep)*len(eq)
    index={x:i for i,x in enumerate(C2)}
    c1ind={x:i for i,x in enumerate(C1)}
    boundary=[{} for _ in C2]
    for i,(e,d) in enumerate(C2):
        x,y=e;u,v=d
        terms=[((1,y,d),1),((1,x,d),-1),((0,e,v),-1),((0,e,u),1)]
        for term,z in terms:boundary[i][c1ind[term]]=z
    # Exact column checks of top-cycle generators.
    for a in vp:
        for b in vq:
            out={}
            for i,(x,y) in enumerate(ep):
                if not a[i]:continue
                for j,(s,t) in enumerate(eq):
                    if not b[j]:continue
                    n=index[((x,p+s),(y,p+t))]
                    for k,z in boundary[n].items():out[k]=out.get(k,0)+a[i]*b[j]*z
            assert all(v==0 for v in out.values())
    # All distinct fundamental-cycle tensor generators are independent since
    # each has a unique pair of non-tree chord positions.
    assert len(vp)*len(vq)==(p*p-3*p+1)*(q*q-3*q+1)
    # Need numerical rank of full boundary to ensure no extra top cycles.
    # Deterministic GF(101) elimination of sparse rows
    pivots={}
    for col in boundary:
        vec=dict(col)
        while vec:
            lead=min(vec)
            factor=vec[lead]%101
            if not factor: del vec[lead];continue
            if lead not in pivots:
                inverse=pow(factor,-1,101)
                pivots[lead]={j:(v*inverse)%101 for j,v in vec.items() if v%101}
                break
            base=pivots[lead]
            for j,v in base.items():
                vec[j]=(vec.get(j,0)-factor*v)%101
                if vec[j]==0:del vec[j]
    rank=len(pivots)
    assert len(C2)-rank==len(vp)*len(vq),(p,q,len(C2),rank,len(vp)*len(vq))
    # Since basis cycles have independent chord coordinates and span dimension,
    # over Z the kernel is their primitive tensor lattice (proved separately).
    permsp=list(permutations(range(p)))
    permsq=list(permutations(range(q)))
    checks=0
    for a in permsp:
        for b in permsq:
            for swap in (False,True):
                for side in ((False,True) if p==q else (False,)):
                    actual=chain_trace(p,q,a,b,side,swap)
                    ta=sum(a[i]==i for i in range(p));tb=sum(b[j]==j for j in range(q))
                    aa=sum(a[a[i]]==i and a[i]!=i for i in range(p))//2
                    bb=sum(b[b[j]]==j and b[j]!=j for j in range(q))//2
                    if not side:
                        expected=-(2*aa-1)*(2*bb-1) if swap else (ta*ta-3*ta+1)*(tb*tb-3*tb+1)
                    else:
                        ab=tuple(a[b[i]] for i in range(p))
                        f=sum(ab[i]==i for i in range(p))
                        expected=(-1 if swap else 1)*(f*f-3*f+1)
                    assert actual==expected,(p,q,a,b,side,swap,actual,expected)
                    checks+=1
    return (p,q,len(C0),len(C1),len(C2),len(C2)-rank,checks)

if __name__=='__main__':
    total=0
    for pair in ((3,3),(3,4),(4,4),(3,5)):
        ans=calc(*pair);total+=ans[-1]
        print('K_{%d,%d}: cells %d,%d,%d, beta2=%d, exact symmetric actions=%d'%ans)
    print('CROWN_TENSOR_INTEGRAL_TOP_HOMOLOGY_PASS actions='+str(total))
