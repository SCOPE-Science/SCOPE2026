"""Independent finite enumeration and exact arithmetic for a leaf/cycle law on labeled unicyclic graphs."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, factorial, exp, pi, sqrt


def theory(n):
    w = {}
    g = {}
    for k in range(3,n+1):
        # choose cycle vertices, cyclic arrangements, rooted forests
        forest = k*n**(n-k-1) if k<n else 1
        # forest product is integral for k<n
        count = comb(n,k)*factorial(k-1)//2 * forest
        w[k]=count
        m=n-k
        g[k] = Fraction(m*(n-1)**(m-1), n**(m-1)) if m else Fraction(0)
    return w,g


def enumerate_graphs(n):
    edges = list(combinations(range(n),2))
    stats = defaultdict(lambda:[0,0])
    for which in combinations(range(len(edges)),n):
        adj=[set() for _ in range(n)]
        for t in which:
            a,b=edges[t]
            adj[a].add(b); adj[b].add(a)
        seen={0}; stack=[0]
        while stack:
            for x in adj[stack.pop()]:
                if x not in seen:
                    seen.add(x); stack.append(x)
        if len(seen)<n: continue
        L=sum(len(a)==1 for a in adj)
        degree=[len(a) for a in adj]
        stack=[i for i in range(n) if degree[i]==1]
        while stack:
            v=stack.pop()
            if degree[v]!=1: continue
            degree[v]=0
            for u in adj[v]:
                if degree[u]:
                    degree[u]-=1
                    if degree[u]==1: stack.append(u)
        k=sum(d>0 for d in degree)
        assert k>=3
        stats[k][0]+=1;stats[k][1]+=L
    return stats


def exact_finite():
    assertions=0
    for n in range(3,8):
        observed=enumerate_graphs(n)
        w,g=theory(n)
        assert set(observed)==set(w); assertions+=1
        for k in w:
            assert observed[k][0]==w[k],(n,k,observed[k],w[k]);assertions+=1
            assert Fraction(observed[k][1],observed[k][0])==g[k],(n,k);assertions+=1
        assert sum(w.values()) == sum(observed[k][0] for k in observed);assertions+=1
    for n in range(4,75):
        w,g=theory(n)
        assert all(g[k]>g[k+1] for k in range(3,n));assertions+=1
        W=sum(w.values())
        EL=sum(w[k]*g[k] for k in w)/W
        EK=Fraction(sum(k*w[k] for k in w),W)
        ELK=sum(k*w[k]*g[k] for k in w)/W
        assert ELK-EL*EK<0; assertions+=1
        # verify leaf decrement from exact finite formula
        q=Fraction(n-1,n)
        for k in range(3,n):
            assert g[k+1]-g[k]==-Fraction(k,n)*q**(n-k-2);assertions+=1
    return assertions


def limit_estimate(n):
    q=1-1/n
    b=1.
    Z=EK=0.
    H=HK=0.
    g0= n*q**(n-1)
    for k in range(1,n+1):
        b*= (n-k+1)/n
        if k<3: continue
        s=k/sqrt(n)
        h=(n-k)*q**(n-k-1)-g0 if k<n else -g0
        Z+=b; EK+=b*s; H+=b*h;HK+=b*h*s
    return (HK/Z-H*EK/Z**2)

if __name__=='__main__':
    count=exact_finite()
    target=-sqrt(2/pi)/(2*exp(1))
    xs={n:limit_estimate(n) for n in (80,300,1000,3000,10000)}
    print('exact assertions',count)
    print('predicted limit',target)
    print('scaled covariances',xs)
    assert abs(xs[10000]-target)<0.007
    print('all checks passed')
