"""Independent finite checks for folded-cube neighborhood intersection and module formulas."""
from itertools import combinations
from math import comb


def canonical(x,n):
    return min(x,x^((1<<n)-1))

def graph(n):
    vertices=list(range(1<<(n-1)))
    neighbor={u:set(canonical(u^(1<<k),n) for k in range(n)) for u in vertices}
    return vertices,neighbor

def validate(n):
    vertices,N=graph(n)
    Q={canonical((1<<i)^(1<<j),n) for i in range(n) for j in range(i+1,n)}
    assert len(Q)==comb(n,2)
    for u,v in combinations(vertices,2):
        t=canonical(u^v,n)
        assert len(N[u]&N[v])==(2 if t in Q else 0)
    for t in vertices[1:]:
        pair_count=sum(canonical(u^t,n) in N[w] for w in vertices for u in N[w])
        assert pair_count==(2*len(vertices) if t in Q else 0)
        # An invariant nonempty face cannot include two translation orbits.
        for w in vertices:
            orbits=sum(canonical(u^t,n) in N[w] for u in N[w])//2
            assert orbits==(1 if t in Q else 0)
    H={}
    for j in range(0,n,2):
        m=(n-1)*(n-2)//2 if j==0 else (((n-2*j)**2 + n*n-6*n+8)//4)
        H[j]=m
    beta=2**(n-3)*(n*n-5*n+8)-1
    assert sum(comb(n,j)*m for j,m in H.items())==beta
    print('n',n,'vertices',len(vertices),'weight-two classes',len(Q),'dimensions',H,'betti2',beta)

if __name__=='__main__':
    for k in [3,5,7]:validate(k)
