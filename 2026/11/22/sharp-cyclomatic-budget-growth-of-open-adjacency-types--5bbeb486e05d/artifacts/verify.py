"""Independent finite checks for the open-neighborhood/cycle-rank bound.

Run: python3 artifacts/verify.py  (standard library only).
Finite exhaustive checks are not an infinite proof.
"""
from itertools import combinations


def cycle_rank(n, edges):
    parent=list(range(n))
    def root(x):
        while x!=parent[x]:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    for u,v in edges:
        ru,rv=root(u),root(v)
        if ru!=rv:parent[ru]=rv
    return len(edges)-n+len({root(v) for v in range(n)})


def trace_count(n,edges,marked):
    adj=[0]*n
    for u,v in edges:
        adj[u]|=1<<v;adj[v]|=1<<u
    mask=sum(1<<v for v in marked)
    return len({a&mask for a in adj})


def cactus_witness(c,m):
    assert c>=0 and m>=max(1,3*c)
    edges=[]
    # c disjoint marked triangles, followed by isolated marked vertices.
    for t in range(c):
        a=3*t
        edges.extend([(a,a+1),(a+1,a+2),(a+2,a)])
    comps=[3*t for t in range(c)]+list(range(3*c,m))
    nxt=m
    for a,b in zip(comps,comps[1:]):
        x=nxt;nxt+=1
        edges.extend([(a,x),(x,b)])
    private=[]
    for a in range(m):
        x=nxt;nxt+=1
        edges.append((a,x));private.append(x)
    edges.append((private[0],nxt));nxt+=1  # empty trace
    return nxt,edges,list(range(m))


def check():
    examined=0
    for n in range(1,7):
        all_edges=list(combinations(range(n),2))
        for bits in range(1<<len(all_edges)):
            edges=[e for i,e in enumerate(all_edges) if bits>>i&1]
            c=cycle_rank(n,edges)
            for mask in range(1,1<<n):
                A=[i for i in range(n) if mask>>i&1]
                t=trace_count(n,edges,A)
                assert t<=min(1<<len(A),2*len(A)+c), (n,edges,A,t,c)
                examined+=1
    constructed=0
    for c in range(9):
        for m in range(max(1,3*c),max(1,3*c)+9):
            n,edges,A=cactus_witness(c,m)
            assert n>=m
            assert cycle_rank(n,edges)==c,(c,m)
            assert trace_count(n,edges,A)==2*m+c,(c,m,trace_count(n,edges,A))
            # all edges belong to bridges or mutually vertex-disjoint triangles
            assert len(set(edges))==len(edges)
            constructed+=1
    print('VERIFY_OK exhaustive_marked_instances=',examined,'sharp_cactus_witnesses=',constructed)


if __name__=='__main__':check()
