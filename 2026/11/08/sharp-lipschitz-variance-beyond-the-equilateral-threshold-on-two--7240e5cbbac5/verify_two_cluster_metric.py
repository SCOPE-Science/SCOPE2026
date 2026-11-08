"""Standalone exact-arithmetic checks for two-class metric spread; Python stdlib."""
from fractions import Fraction as F
from itertools import product
from collections import deque


def predicted(a,b,s):
    N=a+b
    best=None
    witnesses=[]
    for x,y in ((a,b),(b,a)):
        for k in range(x+1):
            for h in range(y+1):
                S=s*k+y*(s-1)+(2-s)*h
                Q=s*s*k+(y-h)*(s-1)**2+h
                V=Q/F(N)-S*S/F(N*N)
                if best is None or V>best:
                    best=V; witnesses=[(x,y,k,h)]
                elif V==best:
                    witnesses.append((x,y,k,h))
    return best,witnesses


def prufer_edges(seq,N):
    deg=[1]*N
    for x in seq:deg[x]+=1
    E=[]
    for x in seq:
        y=next(j for j,d in enumerate(deg) if d==1)
        E.append((x,y)); deg[x]-=1; deg[y]-=1
    u,v=[j for j,d in enumerate(deg) if d==1]
    E.append((u,v))
    return E


def brute_extreme(a,b,s):
    N=a+b
    D=[[F(0) if i==j else s if (i<a)==(j<a) else F(1) for j in range(N)] for i in range(N)]
    best=F(-1);potentials=set();nvalid=0
    for seq in product(range(N),repeat=N-2):
        edges=prufer_edges(seq,N)
        nei=[[] for _ in range(N)]
        for k,(u,v) in enumerate(edges):
            nei[u].append((v,k));nei[v].append((u,k))
        for signs in product((-1,1),repeat=N-1):
            f=[None]*N;f[0]=F(0);queue=deque([0])
            while queue:
                u=queue.popleft()
                for v,k in nei[u]:
                    if f[v] is None:
                        x,y=edges[k]; inc=signs[k]*D[x][y]
                        f[v]=f[u]+(inc if u==x else -inc)
                        queue.append(v)
            if any(abs(f[u]-f[v])>D[u][v] for u in range(N) for v in range(u)):
                continue
            nvalid+=1
            M=sum(f)/N
            val=sum((x-M)**2 for x in f)/N
            if val>best:best=val;potentials={tuple(f)}
            elif val==best:potentials.add(tuple(f))
    return best,len(potentials),nvalid


def run():
    cases=[(a,b,F(p,q)) for a,b in [(2,2),(2,3),(3,2),(2,4),(4,2),(3,3)] for p,q in [(6,5),(3,2),(9,5)]]
    for a,b,s in cases:
        target,_=predicted(a,b,s)
        brute,count,valid=brute_extreme(a,b,s)
        assert brute==target,(a,b,s,brute,target)
    print('PRUFER_SPANNING_TREE_EXHAUSTION_EXACT_MATCH_OK',len(cases))
    for a in range(2,35):
        for b in range(2,35):
            s=F(3,2);N=a+b
            actual,_=predicted(a,b,s)
            expected=F(9,16)-F(min(a,b),2*N)-F(N%2,16*N*N)
            assert actual==expected,(a,b,actual,expected)
    print('HALF_INTEGER_MIDPOINT_LAW_OK',33**2)
    for a in range(2,25):
        for b in range(2,25):
            N=a+b
            at1,_=predicted(a,b,F(1));at2,_=predicted(a,b,F(2))
            assert at1==F((N*N)//4,N*N)
            assert at2==F(max(a,b),N)-F(max(a,b)%2,N*N)
    print('EXACT_EQUILATERAL_AND_BIPARTITE_ENDPOINTS_OK',23**2)
    print('ALL_TWO_CLUSTER_SPREAD_CHECKS_OK')

if __name__=='__main__':run()
