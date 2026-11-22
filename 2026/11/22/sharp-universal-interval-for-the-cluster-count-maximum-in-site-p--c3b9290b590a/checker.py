"""Finite, exact checks for cactus site-percolation cluster-count formulas.
Standard-library only. These checks support but do not replace the proof.
"""
from itertools import combinations
from math import comb
from fractions import Fraction


def edges_of(n):
    return list(combinations(range(n),2))


def component_count(n, edges, mask):
    parent=list(range(n))
    def root(v):
        while parent[v]!=v:
            v=parent[v]
        return v
    for u,v in edges:
        if mask>>u&1 and mask>>v&1:
            ru,rv=root(u),root(v)
            parent[ru]=rv
    return len({root(v) for v in range(n) if mask>>v&1})


def connected(n, edges):
    if not n: return True
    return component_count(n,edges,(1<<n)-1)==1


def cycles(n, edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v);adj[v].append(u)
    out=set()
    for start in range(n):
        def dfs(path,vis):
            u=path[-1]
            for v in adj[u]:
                if v==start and len(path)>=3:
                    a=tuple(path)
                    b=(start,)+tuple(reversed(path[1:]))
                    out.add(min(a,b))
                elif v>start and v not in vis:
                    dfs(path+[v],vis|{v})
        dfs([start],{start})
    return sorted(out)


def cactus(n, edges):
    if not connected(n,edges):return False
    c=cycles(n,edges)
    for u,v in edges:
        if sum(u in cyc and v in cyc and (cyc.index(u)-cyc.index(v))%len(cyc) in (1,len(cyc)-1) for cyc in c)>1:
            return False
    return True


def add_poly(a,b):
    t=[0]*max(len(a),len(b))
    for i,v in enumerate(a):t[i]+=v
    for i,v in enumerate(b):t[i]+=v
    return t


def mul_poly(a,b):
    r=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):r[i+j]+=u*v
    return r


def binomial_weights(n,k):
    ans=[0]*(n+1)
    for j in range(n-k+1):ans[k+j]=(-1)**j*comb(n-k,j)
    return ans


def test_graph(n,edges):
    cc=cycles(n,edges)
    ec=[0]*(n+1);enc=[0]*(n+1)
    for mask in range(1<<n):
        k=mask.bit_count()
        c=component_count(n,edges,mask)
        w=binomial_weights(n,k)
        for j,v in enumerate(w):
            ec[j]+=v*c;enc[j]+=v*k*c
    predicted=[0]*(n+1)
    predicted[1]+=n
    predicted[2]-=len(edges)
    for cy in cc:predicted[len(cy)]+=1
    assert ec==predicted, (n,edges,ec,predicted)
    derivative=[(i+1)*ec[i+1] for i in range(n)]
    lhs=add_poly(enc,[-n*x for x in ([0]+ec)])
    rhs=mul_poly([0,1,-1],derivative)
    assert lhs==rhs+[0]*(len(lhs)-len(rhs)), (n,edges,lhs,rhs)
    return 2


def main():
    tests=0; graphs=0
    for n in range(2,6):
        e=edges_of(n)
        for mask in range(1<<len(e)):
            ed=[pair for i,pair in enumerate(e) if mask>>i&1]
            if cactus(n,ed):
                tests+=test_graph(n,ed);graphs+=1
    # Sweep a deterministic sample of six-vertex graphs.
    n=6;e=edges_of(n)
    for mask in range(0,1<<len(e),17):
        ed=[pair for i,pair in enumerate(e) if mask>>i&1]
        if cactus(n,ed):
            tests+=test_graph(n,ed);graphs+=1
    def f(n,e,l,p):return n-2*e*p+sum(k*p**(k-1) for k in l)
    for t in range(2,60):
        n=3*t+1;e=4*t;ls=[4]*t
        lo,hi=0.0,1.0
        for _ in range(85):
            mid=(lo+hi)/2
            if f(n,e,ls,mid)>0:lo=mid
            else:hi=mid
        root=(lo+hi)/2
        assert .40927 < root <=.75
        tests+=1
    print(f'PASS: {tests} exact identities or numerical sanity checks on {graphs} exhaustively evaluated cactus graphs; finite checks are not proof of the general theorem')

if __name__=='__main__':main()
