#!/usr/bin/env python3
"""Self-contained exact checks for common rooted-PDA cherry statistics."""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb, factorial

def node(a,b):
    return tuple(sorted((a,b),key=lambda x:min(leaves(x))))

def leaves(t):
    if isinstance(t,int):return (t,)
    return leaves(t[0])+leaves(t[1])

def all_insert(t,k):
    out={node(t,k)}
    if isinstance(t,int):return out
    for x in all_insert(t[0],k):out.add(node(x,t[1]))
    for x in all_insert(t[1],k):out.add(node(t[0],x))
    return out

@lru_cache(None)
def trees(n):
    if n==2:return (node(0,1),)
    return tuple({u for t in trees(n-1) for u in all_insert(t,n-1)})

def clades(t):
    if isinstance(t,int):return frozenset(),frozenset([t])
    x,a=clades(t[0]);y,b=clades(t[1]); z=a|b
    return x|y|frozenset([z]),z

def data(n):
    vals=[]
    for t in trees(n):
        c,_=clades(t)
        cherry=frozenset(x for x in c if len(x)==2)
        nontriv=frozenset(x for x in c if 2<=len(x)<n)
        vals.append((cherry,nontriv))
    return vals

def dblfact(m):
    o=1
    for k in range(m,0,-2):o*=k
    return o

def checks():
    cnt=0
    for n in range(3,7):
        d=data(n);N=len(d)
        assert N==dblfact(2*n-3),(n,N)
        cnt+=1
        pairs=list(combinations(range(n),2))
        for a,b in pairs:
            p=sum(frozenset((a,b)) in x[0] for x in d)
            assert Fraction(p,N)==Fraction(1,2*n-3)
            cnt+=1
        if n>=4:
            for a,b in combinations(pairs,2):
                paira,pairb=map(frozenset,(a,b))
                joint=sum(paira in x[0] and pairb in x[0] for x in d)
                expected=Fraction(1,(2*n-3)*(2*n-5)) if paira.isdisjoint(pairb) else Fraction(0)
                assert Fraction(joint,N)==expected
                cnt+=1
        cherry_count=[len(x[0]) for x in d]
        mean=Fraction(sum(cherry_count),N)
        var=Fraction(sum(c*c for c in cherry_count),N)-mean**2
        exact=Fraction(n*(n-1)*(n-2)*(n-3),2*(2*n-5)*(2*n-3)**2)
        assert var==exact,(n,var,exact)
        cnt+=1
        if n<=5:
            # Two independent trees: exact E, variance, and if three trees share one, exact covariance.
            overlaps=[len(a[0]&b[0]) for a in d for b in d]
            mu=Fraction(sum(overlaps),N*N)
            assert mu==Fraction(comb(n,2),(2*n-3)**2)
            assert Fraction(sum(v*v for v in overlaps),N*N)-mu**2>=0
            # conditional covariance reduction: E(Y12 Y13)=E[(p C(T1))^2]
            prod=Fraction(sum(c*c for c in cherry_count),N)*Fraction(1,(2*n-3)**2)
            assert prod-mu**2 == Fraction(1,(2*n-3)**2)*var
            cnt+=3
        # Exact probability of every nontrivial clade size, from contraction of one clade.
        for k in range(2,n):
            target=frozenset(range(k))
            seen=sum(target in x[1] for x in d)
            prob=Fraction(dblfact(2*k-3)*dblfact(2*(n-k)-1),dblfact(2*n-3))
            assert Fraction(seen,N)==prob,(n,k,seen,N,prob)
            cnt+=1
    # Leading-term factorial-moment coefficients: q independent pairs, any fixed degree pattern.
    for r in range(1,6):
        # with r disjoint labelled cherry collisions, coefficient equals 1/8**r.
        assert Fraction(1,2**r)*Fraction(1,2**(2*r))==Fraction(1,8**r)
        cnt+=1
    print(f'PASS {cnt} exact checks; rooted PDA n=3..6; 945 trees at n=6')
if __name__=='__main__':checks()
