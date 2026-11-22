"""Exact finite-chain checks of a renewal-reset stationary bias bound.
The unrestricted theorem follows from the analytic balance proof; these
checks test normalization, clocks, periodic boundaries and sharpness.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random

ZERO=F(0); ONE=F(1)
def mul(v,P):
    n=len(P)
    return [sum(v[i]*P[i][j] for i in range(n)) for j in range(n)]
def powers(v,P,m):
    out=[v]
    for _ in range(m): out.append(mul(out[-1],P))
    return out

def clock(P,root,dist,pi):
    n=len(P)
    assert sum(dist.values(),ZERO)==1
    assert all(isinstance(k,int) and k>=1 and v>0 for k,v in dist.items())
    mu=sum((F(k)*w for k,w in dist.items()),ZERO)
    e=[ONE if i==root else ZERO for i in range(n)]
    z=powers(e,P,max(dist))
    p=[ZERO]*n; terminal=[ZERO]*n
    for L,w in dist.items():
        for k in range(L):
            for j in range(n):p[j]+=w*z[k][j]/mu
        for j in range(n):terminal[j]+=w*z[L][j]
    q=ONE-terminal[root]
    pp=mul(p,P)
    for j in range(n):
        assert p[j]-pp[j]==(e[j]-terminal[j])/mu
    assert sum(p,ZERO)==ONE
    assert sum(terminal,ZERO)==ONE
    tv=sum((abs(p[j]-pi[j]) for j in range(n)),ZERO)/2
    assert 2*mu*tv>=q
    assert (tv==0)==(q==0)
    return p,mu,q,tv

def undirected(n,es):
    a=[[0]*n for _ in range(n)]
    for i,j in es: a[i][j]=a[j][i]=1
    degree=list(map(sum,a))
    if 0 in degree:return None
    seen={0};queue=[0]
    for v in queue:
        for w in range(n):
            if a[v][w] and w not in seen: seen.add(w);queue.append(w)
    if len(seen)!=n:return None
    P=[[F(a[i][j],degree[i]) for j in range(n)] for i in range(n)]
    pi=[F(degree[i],sum(degree)) for i in range(n)]
    return P,pi,degree

def is_hub_star(n,es,root):
    return all((min(i,j)==root or max(i,j)==root) for i,j in es) and len(es)==n-1

def test_graphs():
    checks=0; graph_count=0
    for n in range(2,6):
        edges=list(combinations(range(n),2))
        for bits in range(1,1<<len(edges)):
            es=[e for j,e in enumerate(edges) if bits>>j&1]
            obj=undirected(n,es)
            if obj is None:continue
            P,pi,deg=obj;graph_count+=1
            for root in range(n):
                for L in (2,3,4,5,6):
                    p,mu,q,tv=clock(P,root,{L:ONE},pi)
                    assert (tv==0)==(is_hub_star(n,es,root) and L%2==0)
                    checks+=1
    return graph_count,checks

def test_random_directed():
    rng=Random(1711);checks=0
    # Positive rational matrices: irreducible and aperiodic.
    for n in (2,3,4,5):
        for _ in range(30):
            rows=[]
            for i in range(n):
                weights=[rng.randint(1,9) for _ in range(n)]
                rows.append([F(w,sum(weights)) for w in weights])
            # Solve stationarity exactly with Gaussian elimination over rationals.
            A=[[rows[j][i]-(ONE if i==j else ZERO) for j in range(n)] for i in range(n)]
            A[-1]=[ONE]*n
            b=[ZERO]*(n-1)+[ONE]
            for k in range(n):
                pivot=next(i for i in range(k,n) if A[i][k])
                A[k],A[pivot]=A[pivot],A[k];b[k],b[pivot]=b[pivot],b[k]
                pivotval=A[k][k];A[k]=[t/pivotval for t in A[k]];b[k]/=pivotval
                for i in range(n):
                    if i==k:continue
                    fac=A[i][k]
                    A[i]=[A[i][j]-fac*A[k][j] for j in range(n)]
                    b[i]-=fac*b[k]
            pi=b
            for root in (0,n-1):
                for dist in ({1:F(1,2),4:F(1,2)},{2:F(2,3),6:F(1,3)}):
                    p,mu,q,tv=clock(rows,root,dist,pi)
                    assert tv>0 and q>0
                    checks+=1
    return checks

def test_sharp():
    checks=0
    for m in range(1,9):
        obj=undirected(m+1,[(0,i) for i in range(1,m+1)])
        P,pi,_=obj
        for dist in ({3:F(1,4),6:F(3,4)},{2:ONE},{5:ONE},{2:F(3,5),7:F(2,5)}):
            p,mu,q,tv=clock(P,0,dist,pi)
            assert tv==q/(2*mu)
            assert q==sum((v for k,v in dist.items() if k%2),ZERO)
            checks+=1
    n=3
    P=[[ONE if j==(i+1)%n else ZERO for j in range(n)] for i in range(n)]
    pi=[F(1,n)]*n
    for L in range(1,15):
        p,mu,q,tv=clock(P,0,{L:ONE},pi)
        assert (tv==0)==(L%3==0)
        checks+=1
    return checks

if __name__=='__main__':
    a,b=test_graphs();c=test_random_directed();d=test_sharp()
    print('PASS',a,'connected undirected graphs;',b,'undirected root-clock exact assertions;',c,'positive directed root-clock assertions;',d,'sharpness/periodic assertions; total',b+c+d)
