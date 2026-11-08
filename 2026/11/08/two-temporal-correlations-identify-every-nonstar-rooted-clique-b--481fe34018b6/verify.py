"""Exact finite-graph checks for two-lag identification in synchronous noisy voting.
Run: python verify.py (Python 3.9 or newer; standard library only).
Finite calculations test the formulas; the all-size monotonicity is proved in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations


def graph(m, s):
    vertices = 1 + m*s
    adj = [set() for _ in range(vertices)]
    for i in range(m):
        blade = range(1+i*s, 1+(i+1)*s)
        for u in blade:
            adj[0].add(u); adj[u].add(0)
        for u,v in combinations(blade, 2):
            adj[u].add(v); adj[v].add(u)
    return adj


def solve(A, b):
    n = len(b)
    a = [list(A[i]) + [b[i]] for i in range(n)]
    for j in range(n):
        piv = next(i for i in range(j,n) if a[i][j])
        a[j],a[piv]=a[piv],a[j]
        d=a[j][j]
        a[j]=[v/d for v in a[j]]
        for i in range(n):
            if i!=j and a[i][j]:
                t=a[i][j]; a[i]=[a[i][k]-t*a[j][k] for k in range(n+1)]
    return [a[i][-1] for i in range(n)]


def full_pair_correlations(adj,c):
    edges=list(combinations(range(len(adj)),2))
    ix={e:i for i,e in enumerate(edges)}
    n=len(edges);A=[[F(i==j) for j in range(n)] for i in range(n)]
    rhs=[F(0) for _ in range(n)]
    for i,(u,v) in enumerate(edges):
        for x in adj[u]:
            for y in adj[v]:
                w=c*c/F(len(adj[u])*len(adj[v]))
                if x==y:rhs[i]+=w
                else:A[i][ix[tuple(sorted((x,y)))]]-=w
    sol=solve(A,rhs)
    return lambda u,v: F(1) if u==v else sol[ix[tuple(sorted((u,v)))]]


def reduced(m,s,c):
    q=c*c
    # Equations in C (=hub-to-outer), B (=same blade), D (=different blades).
    A=[
      [1-q/F(s),-q*F((s-1)**2,m*s*s),-q*F((m-1)*(s-1),m*s)],
      [-q*F(2*(s-1),s*s),1-q*F(s*s-3*s+3,s*s),F(0)],
      [-q*F(2*(s-1),s*s),F(0),1-q*F((s-1)**2,s*s)],
    ]
    b=[q*F(s-1,m*s*s),q*F(s-1,s*s),q*F(1,s*s)]
    return solve(A,b)


def recover(r1,r2,c):
    q=c*c; h=r1/c
    s=(1-h)/(r2/q-h)
    assert s.denominator==1
    t=int(s)
    B=q*(t-1)*(1+2*h)/(t*t-q*(t*t-3*t+3))
    D=q*(1+2*(t-1)*h)/(t*t-q*(t-1)**2)
    m=q*(t-1)*(1+(t-1)*B-t*D)/(t*t*h-q*t*h-q*t*(t-1)*D)
    return (m,t)


def checks():
    cases=0
    for c in (F(1,2),F(2,3),F(4,5)):
      for s in (2,3,4):
        prior=None
        for m in (1,2,3):
            adj=graph(m,s)
            C,B,D=reduced(m,s,c)
            corr=full_pair_correlations(adj,c)
            assert C==corr(0,1)
            assert B==corr(1,2)
            if m>1: assert D==corr(1,1+s)
            if prior is not None:assert prior>C
            prior=C
            # Compute temporal correlations independently from one- and two-step
            # random-walk transition probabilities at the observed vertex.
            p1=c*sum(corr(0,u)/len(adj[0]) for u in adj[0])
            p2=c*c*sum(corr(0,v)/F(len(adj[0])*len(adj[u]))
                      for u in adj[0] for v in adj[u])
            assert p1==c*C
            assert p2==c*c*(F(1,s)+F(s-1,s)*C)
            assert recover(p1,p2,c)==(m,s)
            assert 0<C<1 and 0<=B<1 and 0<=D<1
            cases+=1
    for c in (F(1,2),F(2,3)):
        for m in (1,2,4):
            adj=graph(m,1);corr=full_pair_correlations(adj,c)
            p1=c*sum(corr(0,u)/len(adj[0]) for u in adj[0])
            p2=c*c*sum(corr(0,v)/F(len(adj[0])*len(adj[u]))
                      for u in adj[0] for v in adj[u])
            assert p1==0 and p2==c*c
            cases+=1
    print('VERIFY_OK: %d exact graph/noise cases' % cases)

if __name__=='__main__':checks()
