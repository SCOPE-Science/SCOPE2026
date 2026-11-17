"""Reproduce the finite checks for the two-petal avalanche homology law.

Only standard Python. Vertices: hub=0, auxiliary petal vertex=1,
long-cycle vertices=2,...,m. Edges are 0->1->0 and
0->2->3->...->m->0.
"""
from itertools import combinations


def dynamics(m):
    n=m+1
    out=[[] for _ in range(n)]
    out[0]=[1,2]
    out[1]=[0]
    for j in range(2,m):out[j]=[j+1]
    out[m]=[0]
    deg=list(map(len,out))
    c=[0]+[1]*m
    seen={};fire=[];states=[]
    while tuple(c) not in seen:
        seen[tuple(c)]=len(fire)
        states.append(tuple(c))
        f=frozenset(v for v in range(n) if c[v]>=deg[v])
        assert f
        fire.append(f)
        nxt=c[:]
        for v in f:
            nxt[v]-=deg[v]
            for w in out[v]:nxt[w]+=1
        assert min(nxt)>=0
        c=nxt
        assert len(fire)<=m+3
    return fire,seen[tuple(c)],states


def expected_facets(m):
    V=set(range(m+1))
    return {frozenset(V-{0}),frozenset(V-{1,2})} | {
        frozenset(V-{t,t+2}) for t in range(3,m-1)
    }


def maximal(s):
    return {x for x in s if not any(x<y for y in s)}


def gf2_reduced_betti(facets):
    ss={frozenset()}
    for f in facets:
        vals=sorted(f)
        for k in range(1,len(vals)+1):
            ss.update(map(frozenset,combinations(vals,k)))
    dims={d:sorted((tuple(sorted(f)) for f in ss if len(f)==d+1)) for d in range(-1,max(len(x) for x in ss))}
    rank={};
    for d in range(0,max(dims)+1):
        low={x:i for i,x in enumerate(dims[d-1])}
        pivots={}
        for f in dims[d]:
            v=0
            for i in range(len(f)):
                v^=1<<low[f[:i]+f[i+1:]]
            while v:
                j=v.bit_length()-1
                if j in pivots:v^=pivots[j]
                else:pivots[j]=v;break
        rank[d]=len(pivots)
    b={d:len(dims[d])-rank.get(d,0)-rank.get(d+1,0) for d in dims if d>=0}
    return {d:k for d,k in b.items() if k}


def predicted(m):
    q,r=divmod(m,6)
    return {4*q+r-2:1} if q>=1 and r<=2 else {}


def main():
    total=0
    for m in range(5,49):
        s,rep,states=dynamics(m)
        assert rep==2 and len(s)==m+2,(m,rep,len(s))
        facets=maximal(set(s))
        exp=expected_facets(m)
        assert facets==exp,(m,facets^exp)
        assert len(facets)==m-2
        total+=len(s)
        # At small dimensions, independently enumerate ALL faces and mod-two ranks.
        if m<=13:
            betti=gf2_reduced_betti(facets)
            assert betti==predicted(m),(m,betti,predicted(m))
            print('m',m,'faces checked','betti',betti,'facets',len(facets))
    print('all m=5..48 firing transitions and facets checked; rounds',total)
    print('AVALANCHE_TWO_PETAL_MOD_SIX_HOMOLOGY_PASS')

if __name__=='__main__':main()
