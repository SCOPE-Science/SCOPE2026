"""Finite independent checks for cyclic-port truncation Rips theorem.
Run: python3 verify.py .  Requires only Python standard library.
"""
from itertools import combinations
from random import Random


def make_base(n, edges):
    G=[set() for _ in range(n)]
    for a,b in edges:
        assert 0<=a<n and 0<=b<n and a!=b
        G[a].add(b);G[b].add(a)
    return G

def cycle_ports(H):
    """Return port vertices (u,v) and adjacency for the cyclic replacement."""
    ports=[(u,v) for u in range(len(H)) for v in sorted(H[u])]
    ix={p:i for i,p in enumerate(ports)}
    N=[set() for _ in ports]
    for u, neighbors in enumerate(H):
        ds=sorted(neighbors)
        if len(ds)>=2:
            for i in range(len(ds)):
                a=ix[u,ds[i]];b=ix[u,ds[(i+1)%len(ds)]]
                N[a].add(b);N[b].add(a)
    for (u,v),a in ix.items():
        b=ix[v,u];N[a].add(b);N[b].add(a)
    return ports,N

def square_graph(N):
    return [((nb|set.union(*(N[j] for j in nb)) if nb else set())-{i}) for i,nb in enumerate(N)]

def maximal_cliques(N):
    out=[]
    def visit(R,P,X):
        if not P and not X:
            out.append(tuple(sorted(R)));return
        pivot=max(P|X,key=lambda x:len(P&N[x])) if P|X else None
        for v in list(P-(N[pivot] if pivot is not None else set())):
            visit(R|{v},P&N[v],X&N[v]);P.remove(v);X.add(v)
    visit(set(),set(range(len(N))),set())
    return out

def all_faces(facets):
    fs={}
    for facet in facets:
        for k in range(1,len(facet)+1):
            fs.setdefault(k,set()).update(combinations(facet,k))
    return {k:sorted(v) for k,v in fs.items()}

def rank2(cols):
    pivots={}
    for c in cols:
        while c:
            j=c.bit_length()-1
            if j in pivots:c^=pivots[j]
            else:pivots[j]=c;break
    return len(pivots)

def bettis(faces):
    dims=sorted(faces)
    ranks={0:0}
    for k in dims[1:]:
        idx={t:i for i,t in enumerate(faces[k-1])}
        cols=[]
        for f in faces[k]:
            bit=0
            for s in combinations(f,k-1):bit ^= 1<<idx[s]
            cols.append(bit)
        ranks[k]=rank2(cols)
    return [len(faces[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in dims]

def verify(H,label):
    n=len(H); dmax=max(map(len,H)); e=sum(map(len,H))//2
    assert e>0 and all(H)
    for a in range(n):
        assert not any(b in H[c] for b,c in combinations(H[a],2)), 'not triangle-free'
    ports,N=cycle_ports(H);N2=square_graph(N)
    F=all_faces(maximal_cliques(N2)); b=bettis(F)
    F1=all_faces(maximal_cliques(N)); b1=bettis(F1)
    special=sum(len(NH) in (4,5) for NH in H)
    assert b1[0]==1 and b1[1]==(e-n+1)+special and all(z==0 for z in b1[2:]),(label,b1,special)
    assert b[0]==1 and b[1]==e-n+1 and all(z==0 for z in b[2:]),(label,b,e-n+1)
    # The inverse image over a base vertex is a simplex in the scale-two complex.
    for u in range(n):
        p=[i for i,v in enumerate(ports) if v[0]==u]
        assert all(j in N2[i] for i,j in combinations(p,2))
    # Simplicial projection: every 2-Rips face projects into an edge of H.
    for face in F.values():
        for sigma in face:
            us={ports[i][0] for i in sigma}
            assert len(us)<=2,(label,sigma,us)
            if len(us)==2:
                a,c=sorted(us);assert c in H[a]
    # Edge-fiber complete characterization and flag-vertex dominance.
    for a in range(n):
        for c in H[a]:
            if a>c:continue
            port_a=ports.index((a,c));port_c=ports.index((c,a))
            fiber={i for i,(u,v) in enumerate(ports) if u in (a,c)}
            for x in fiber:
                if ports[x][0]==a and x!=port_a:
                    assert ((N2[x]&fiber)|{x}) <= ((N2[port_a]&fiber)|{port_a})
                if ports[x][0]==c and x!=port_c:
                    assert ((N2[x]&fiber)|{x}) <= ((N2[port_c]&fiber)|{port_c})
            for k,Fk in F.items():
                for sigma in Fk:
                    ps={ports[i][0] for i in sigma}
                    if ps=={a,c}:
                        assert port_a in sigma or port_c in sigma
    return len(ports),[len(F[k]) for k in sorted(F)],b,b1

def main():
    examples=[]
    def add(n,edges,label):
        H=make_base(n,edges)
        if min(map(len,H))>=1 and max(map(len,H))<=5: examples.append((label,H))
    add(2,[(0,1)],'edge')
    add(6,[(0,i) for i in range(1,6)],'five-arm star')
    for n in (4,5,6,7,8):add(n,[(i,(i+1)%n) for i in range(n)],f'cycle {n}')
    add(10,[(i,j) for i in range(5) for j in range(5,10)],'K5,5')
    add(8,[(i,j) for i in range(4) for j in range(4,8)],'K4,4')
    add(8,[(i,i^b) for i in range(8) for b in (1,2,4) if i<i^b],'cube')
    for m,n in [(4,4),(4,5)]:
        def k(i,j):return (i%m)*n+(j%n)
        E=set()
        for i in range(m):
            for j in range(n):
                for a,b in ((k(i,j),k(i+1,j)),(k(i,j),k(i,j+1))):E.add(tuple(sorted((a,b))))
        add(m*n,E,f'grid-torus-{m}x{n}')
    rng=Random(10351)
    for t in range(36):
        # A bipartite graph ensures absence of triangles.
        la=rng.randint(2,6);lb=rng.randint(2,6);n=la+lb
        E=[(i,j) for i in range(la) for j in range(la,n) if rng.randrange(3)!=0]
        H=make_base(n,E)
        if max(map(len,H))<=5 and all(H) and sum(map(len,H))>=2*n-2:
            # Require connectivity (all examples tested are connected).
            seen={0};todo=[0]
            while todo:
                q=todo.pop()
                for v in H[q]-seen:seen.add(v);todo.append(v)
            if len(seen)==n:examples.append((f'random-bipartite-{t}',H))
    for label,H in examples:
        v,f,b,b1=verify(H,label)
        print(label,'base',len(H),sum(map(len,H))//2,'ports',v,'f',f,'Betti2',b,'Betti1',b1)
    # Degree-six obstruction, independent graph metric and clique enumeration.
    S=make_base(7,[(0,i) for i in range(1,7)])
    ports,G=cycle_ports(S);K=all_faces(maximal_cliques(square_graph(G)))
    b=bettis(K)
    assert b[:3] == [1,0,1] and all(v==0 for v in b[3:]),b
    assert sum((-1)**(i-1)*len(K[i]) for i in K)==2
    print('degree-six obstruction: 6-star Rips Betti',b,'faces',[len(K[i]) for i in sorted(K)])
    print('CYCLIC_TRUNCATION_RIPS2_CHECKS_OK',len(examples),'examples')
if __name__=='__main__':main()
