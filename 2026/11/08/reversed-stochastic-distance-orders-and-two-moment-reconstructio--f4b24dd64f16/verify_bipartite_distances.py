"""Reproduce exact distance-law checks on unit-length complete bipartite metric graphs."""
import random, math
from collections import deque

def cdf(x,p,q):
    n=p+q; P=p*q
    if x<=0:return 0.
    if x<=1:return (2*x+(n-4)*x*x/2)/P
    if x<=2:
        u=2-x
        return 1-((n-2)*u*u/2+(P-n+1)*(2*u-u*u))/P
    return 1.

def exact_distance(p,q,ei,ej,s,t):
    # independent graph shortest-path algorithm, not using the three-type formula
    edges=[(a,p+b) for a in range(p) for b in range(q)]
    (a,b),(c,d)=edges[ei],edges[ej]
    if ei==ej:return abs(s-t)
    n=p+q
    z=[[math.inf]*n for i in range(n)]
    for i in range(n):z[i][i]=0
    for i,j in edges:z[i][j]=z[j][i]=1.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                z[i][j]=min(z[i][j],z[i][k]+z[k][j])
    return min(s+t+z[a][c],s+1-t+z[a][d],1-s+t+z[b][c],2-s-t+z[b][d])

def test():
    rand=random.Random(951037)
    for p,q in [(1,2),(1,7),(2,2),(2,3),(2,7),(3,3),(3,5),(5,5)]:
        m=p*q; samples=15000
        distances=[]
        for _ in range(samples):
            i=rand.randrange(m); j=rand.randrange(m)
            distances.append(exact_distance(p,q,i,j,rand.random(),rand.random()))
        for t in [.25,.5,.75,1,1.25,1.5,1.75]:
            observed=sum(d<=t for d in distances)/samples
            theoretical=cdf(t,p,q)
            if abs(observed-theoretical)>0.031:raise AssertionError((p,q,t,observed,theoretical))
        mean=sum(distances)/samples
        want=5/3-2*(p+q)/(3*p*q)
        if abs(mean-want)>0.034:raise AssertionError((p,q,mean,want))
    # exact mass and first moment checks by symbolic integration, if installed
    import sympy as sp
    x=sp.symbols('x', real=True)
    for p,q in [(1,5),(2,2),(2,7),(3,4),(10,12)]:
        P=p*q; n=p+q
        f0=(2+(n-4)*x)/P
        f1=((n-2)*(2-x)+2*(P-n+1)*(x-1))/P
        assert sp.simplify(sp.integrate(f0,(x,0,1))+sp.integrate(f1,(x,1,2))-1)==0
        mean=sp.integrate(x*f0,(x,0,1))+sp.integrate(x*f1,(x,1,2))
        second=sp.integrate(x*x*f0,(x,0,1))+sp.integrate(x*x*f1,(x,1,2))
        assert sp.simplify(mean-(sp.Rational(5,3)-sp.Rational(2*n,3*P)))==0
        assert sp.simplify(second-(sp.Rational(17,6)-sp.Rational(5*n-2,3*P)))==0
        gap=sp.simplify(6*second+8-15*mean)
        assert sp.simplify(gap-sp.Rational(4,P))==0
        assert sp.simplify(sp.Rational(4,1)/gap-P)==0
        assert sp.simplify(2*(5-3*mean)/gap-n)==0
    for n in range(4,30):
        products=[p*(n-p) for p in range(1,n//2+1)]
        assert all(a<b for a,b in zip(products,products[1:]))
        for x in [.05,.7,1.1,1.8]:
            values=[cdf(x,p,n-p) for p in range(1,n//2+1)]
            assert all(a>b for a,b in zip(values,values[1:]))
        # In contrast, the probability of vertex distance at most one rises with P.
        vertex_cdfs=[(n+2*P)/(n*n) for P in products]
        assert all(a<b for a,b in zip(vertex_cdfs,vertex_cdfs[1:]))
    print('COMPLETE_BIPARTITE_METRIC_DISTANCE_OK configurations=8 samples=120000')
    print('SYMBOLIC_CDF_MOMENT_INVERSE_AND_REVERSED_STOCHASTIC_ORDER_OK')
if __name__=='__main__':test()
