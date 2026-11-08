"""Finite, independently enumerated checks for neighborhood complexes of clique fibers.
Pure Python 3. This verifies finite cases only; the uniform proof is in RESULT.md.
"""
from collections import defaultdict


def bit_subsets(mask):
    q=mask
    while True:
        yield q
        if q==0:break
        q=(q-1)&mask


def graph(m,n,edges):
    adj=[set() for _ in range(m*n)]
    def connect(a,b):adj[a].add(b);adj[b].add(a)
    for v in range(n):
        for a in range(m):
            for b in range(a+1,m):connect(v*m+a,v*m+b)
    for u,v in edges:
        for a in range(m):connect(u*m+a,v*m+a)
    return adj


def faces_from_adjacency(adj):
    out={0}
    for nbrs in adj:
        fac=sum(1<<k for k in nbrs)
        out.update(bit_subsets(fac))
    return out


def rank2(columns):
    basis={}
    for c in columns:
        while c:
            k=c.bit_length()-1
            if k in basis:c^=basis[k]
            else:basis[k]=c;break
    return len(basis)


def reduced_betti2(faces):
    fs=defaultdict(list)
    for f in faces:
        if f:fs[f.bit_count()-1].append(f)
    ranks={}
    for d in sorted(fs):
        if not d:continue
        low_index={f:i for i,f in enumerate(fs[d-1])}
        cols=[]
        for f in fs[d]:
            c=0;x=f
            while x:
                b=x&-x;x-=b
                c^=1<<low_index[f^b]
            cols.append(c)
        ranks[d]=rank2(cols)
    return {d:len(fs[d])-ranks.get(d,0)-ranks.get(d+1,0)-(d==0) for d in fs}


def check(m,n,edges):
    H=[set() for _ in range(n)]
    for u,v in edges:H[u].add(v);H[v].add(u)
    # The combinatorial hypotheses, checked independently for every finite example.
    assert all(u!=v for u,v in edges)
    assert len(set(tuple(sorted(x)) for x in edges))==len(edges)
    d=[[0 if u==v else 10000 for v in range(n)] for u in range(n)]
    for u,v in edges:d[u][v]=d[v][u]=1
    for k in range(n):
        for i in range(n):
            for j in range(n):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    assert all(d[0][v]<10000 for v in range(n))
    assert all(not (v in H[u] and w in H[u] and w in H[v]) for u in range(n) for v in H[u] for w in H[u] if w!=v)
    for u in range(n):
        for w in range(u+1,n):
            assert d[u][w]!=2 or len(H[u]&H[w])==1

    N=m*n
    adj=graph(m,n,edges)
    faces=faces_from_adjacency(adj)
    before=len(faces)
    pairs1=[]; pairs2=[]
    for v in range(n):
        for a in range(m):
            pivot=next(b for b in range(m) if b!=a)
            h=1<<(m*v+pivot)
            others=sum(1<<(m*v+b) for b in range(m) if b!=a and b!=pivot)
            off=sum(1<<(m*u+a) for u in H[v])
            for T in bit_subsets(off):
                if T.bit_count()<2:continue
                for A in bit_subsets(others):pairs1.append((T|A,(T|A)|h))
            for u in H[v]:
                T=1<<(m*u+a)
                for A in bit_subsets(others):
                    if A.bit_count()>=2:pairs2.append((T|A,(T|A)|h))

    def collapse(pairs):
        for lo,hi in sorted(pairs,key=lambda p:p[0].bit_count(),reverse=True):
            assert lo in faces and hi in faces,(m,n,'missing pair',lo,hi)
            # Unique remaining codimension-one coface implies this is a genuine free face.
            remaining=[lo|(1<<j) for j in range(N) if not(lo>>j)&1 and (lo|(1<<j)) in faces]
            assert remaining==[hi],(m,n,'not free',lo,hi,len(remaining))
            faces.remove(lo);faces.remove(hi)
    collapse(pairs1)
    collapse(pairs2)
    core={0}
    for v in range(n):
        row=sum(1<<(m*v+a) for a in range(m))
        for f in bit_subsets(row):
            if f!=row:core.add(f)
    for v in range(n):
        for u in H[v]:
            for a in range(m):
                h=next(b for b in range(m) if b!=a)
                for b in range(m):
                    if a!=b:core.add((1<<(m*u+a))|(1<<(m*v+b)))
                for w in range(m):
                    if w not in (a,h):
                        core.add((1<<(m*u+a))|(1<<(m*v+h))|(1<<(m*v+w)))
    assert faces==core,(m,n,'core mismatch',len(faces),len(core))
    # Each base-edge interface has a connected graph of triangle relations on
    # the m(m-1) cross-edge generators; its integer incidence matrix is
    # consequently unimodular after restricting to a spanning tree.
    for u,v in edges:
        cross={(a,b) for a in range(m) for b in range(m) if a!=b}
        relations=[]
        for a in range(m):
            h=next(k for k in range(m) if k!=a)
            for w in range(m):
                if w not in (a,h):relations.append(((a,h),(a,w)))
            for w in range(m):
                if w not in (a,h):relations.append(((h,a),(w,a)))
        assert len(relations)==2*m*(m-2)
        seen={next(iter(cross))}
        while True:
            further={y for x,y in relations if x in seen}|{x for x,y in relations if y in seen}
            if further<=seen:break
            seen|=further
        assert seen==cross,(m,n,'relation connectivity')
        assert len(relations)-len(cross)+1==m*m-3*m+1
    predicted_pairs=(m*(1<<(m-2))*sum((1<<len(H[v]))-len(H[v])-1 for v in range(n))
                      +2*m*len(edges)*((1<<(m-2))-m+1))
    assert len(pairs1)+len(pairs2)==predicted_pairs,(m,n,'collapse total')
    cycle_rank=len(edges)-n+1
    lam=m*m-3*m+1
    expected=defaultdict(int)
    expected[1]+=cycle_rank
    expected[2]+=len(edges)*lam
    expected[m-2]+=n
    actual={d:k for d,k in reduced_betti2(faces_from_adjacency(adj)).items() if k}
    expect={d:k for d,k in expected.items() if k}
    assert actual==expect,(m,n,'betti',actual,expect)
    print('PASS',m,n,len(edges),'faces',before-1,'collapse_pairs',len(pairs1)+len(pairs2),'betti',actual)
    return len(pairs1)+len(pairs2)


if __name__=='__main__':
    family={
      'singleton':(1,[]),
      'edge':(2,[(0,1)]),
      'path4':(4,[(0,1),(1,2),(2,3)]),
      'star5':(5,[(0,1),(0,2),(0,3),(0,4)]),
      'C5':(5,[(i,(i+1)%5) for i in range(5)]),
      'C6':(6,[(i,(i+1)%6) for i in range(6)]),
      'two_C5':(9,[(0,1),(1,2),(2,3),(3,4),(4,0),(0,5),(5,6),(6,7),(7,8),(8,0)]),
      'Petersen':(10,[(i,(i+1)%5) for i in range(5)]+[(5+i,5+(i+2)%5) for i in range(5)]+[(i,5+i) for i in range(5)]),
    }
    count=0;total=0
    for m in (4,5,6):
        for name,(n,edges) in family.items():
            if m>4 and n>6:continue
            if m==6 and n==6:continue
            total+=check(m,n,edges);count+=1
    print('ALL_CHECKS_PASS',count,'total_verified_elementary_collapses',total)
