"""Exact checks of multipartite spanning-tree degree covariance and extremal theorem.
Run: python3 verify.py. Python standard library only.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def partitions(n, top=None):
    top=n if top is None else top
    if n==0:
        yield ()
    else:
        for j in range(min(n,top),1-1,-1):
            for rem in partitions(n-j,j):
                yield (j,)+rem


def pruefer_edges(code,n):
    deg=[1]*n
    for i in code:deg[i]+=1
    edges=[]
    for i in code:
        v=next(j for j in range(n) if deg[j]==1)
        edges.append((v,i))
        deg[v]-=1;deg[i]-=1
    a,b=[j for j in range(n) if deg[j]==1]
    edges.append((a,b))
    return edges


def experiment(parts):
    n=sum(parts);r=len(parts)
    side=[]
    for i,s in enumerate(parts):side.extend([i]*s)
    cnt=Counter();cov_s=[0]*n;cross=[[0]*n for _ in range(n)]
    total=0
    for code in product(range(n),repeat=n-2):
        edges=pruefer_edges(code,n)
        if any(side[u]==side[v] for u,v in edges):continue
        deg=[1]*n
        for j in code:deg[j]+=1
        excess=tuple(x-1 for x in deg)
        cnt[excess]+=1
        total+=1
        for u in range(n):cov_s[u]+=deg[u]
        for u in range(n):
            for v in range(u+1,n):cross[u][v]+=deg[u]*deg[v]
    assert total==n**(r-2)*__import__('math').prod((n-s)**(s-1) for s in parts)
    # Independently multiply the expected vertex-degree polynomial.
    dist=Counter({(0,)*n:1})
    streams=[list(range(n))]*(r-2)
    for i,s in enumerate(parts):
        for j in range(s-1):streams.append([v for v in range(n) if side[v]!=i])
    for choices in streams:
        nxt=Counter()
        for state,mult in dist.items():
            for v in choices:
                state2=list(state);state2[v]+=1
                nxt[tuple(state2)]+=mult
        dist=nxt
    assert dist==cnt,(parts,'degree polynomial mismatch')
    maximum=Fraction(n-3,4)+Fraction(1,n*n)
    for u in range(n):
        for v in range(u+1,n):
            actual=Fraction(cross[u][v],total)-Fraction(cov_s[u]*cov_s[v],total*total)
            predicted=-Fraction(r-2,n*n)
            for i,s in enumerate(parts):
                if i!=side[u] and i!=side[v]:
                    predicted-=Fraction(s-1,(n-s)**2)
            assert actual==predicted,(parts,u,v,actual,predicted)
            assert -maximum<=actual<=0,(parts,u,v,actual)
            if actual==-maximum:
                assert tuple(sorted(parts))==(1,1,n-2) and side[u]!=side[v] and parts[side[u]]==parts[side[v]]==1
    return total,len(cnt),n*(n-1)//2


def main():
    tests=0;trees=0;states=0;pairs=0
    for n in range(3,8):
        for parts in partitions(n):
            if len(parts)<2:continue
            t,s,p=experiment(parts)
            tests+=1;trees+=t;states+=s;pairs+=p
    # Larger distinctive extremal, balanced, and bipartite examples.
    for parts in [(6,1,1),(3,3,2),(4,4),(5,2,1)]:
        t,s,p=experiment(parts)
        tests+=1;trees+=t;states+=s;pairs+=p
    print('PASS configurations=',tests,'trees=',trees,'polynomial_coefficients=',states,'pair_covariances=',pairs)

if __name__=='__main__':main()
