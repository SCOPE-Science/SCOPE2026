#!/usr/bin/env python3
"""Exact Walsh and endpoint kernel checks for winner-free tournaments."""
from itertools import combinations
from fractions import Fraction
from math import comb

def butterfly(a):
    a=list(a)
    h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h]
                a[j],a[j+h]=u+v,u-v
        h*=2
    return a

def source_masks(n):
    edges=list(combinations(range(n),2))
    stars=[0]*n
    winner=[0]*n
    for t,(i,j) in enumerate(edges):
        stars[i] |= 1<<t; stars[j] |= 1<<t
        winner[i] |= 1<<t
    return edges,stars,winner

def check(n):
    edges,star,winners=source_masks(n)
    E=len(edges); N=1<<E; B=1<<(E-n+1)
    s=[0]*N
    for x in range(N):
        if not any((x & star[v])==winners[v] for v in range(n)):
            s[x]=1
    assert sum(s)==N-n*B
    w=butterfly(s)
    mask=[0]*N
    for u in range(N):
        if not u:
            expected=N-n*B
        elif u.bit_count()==1:
            expected=0
        else:
            r=[v for v in range(n) if u & ~star[v]==0]
            expected=-B * (1-2*((u&winners[r[0]]).bit_count()%2)) if r else 0
        assert w[u]==expected,(n,u,w[u],expected)
        mask[u]=int(w[u]!=0)
    assert sum(mask)==1+n*(2**(n-1)-n)
    F=butterfly(mask)
    sample=0
    for z,f in enumerate(F):
        ed=z.bit_count()
        isolated=sum((z & star[v])==0 for v in range(n))
        th=(1<<(n-1))*isolated+4*ed-n*n+1
        assert f==th,(n,z,f,th)
        sample+=abs(f)
    assert max(abs(z) for z in w)==N-n*B
    assert min(abs(z) for z in w if z)==B
    return (sum(s),sum(mask),Fraction(sample,N))

def graph_no_isolate(n,k):
    return sum((-1)**j * comb(n,j) * comb(comb(n-j,2),k) if k<=comb(n-j,2) else 0 for j in range(n+1))

def exact_formula(n):
    E=comb(n,2)
    val=0
    for j in range(n+1):
        r=n-j
        for k in range(comb(r,2)+1):
            val+=comb(n,j)*graph_no_isolate(r,k)*abs(2**(n-1)*j+4*k-n*n+1)
    return Fraction(val,2**E)

if __name__=='__main__':
    for n in range(3,7):
        a=check(n)
        b=exact_formula(n)
        assert a[2]==b, (n,a,b)
        print(n,'count rank exact_Lambda=',a)
    for n in (7,8,9,10,12,15,20):
        x=exact_formula(n)
        print(n, 'exact_Lambda=',x,'float=',float(x),'ratio=',float(x)/n)
    print('NO_CONDORCET_TOURNAMENT_WALSH_PASS')
