"""Exact diagnostics for the unicyclic habitat fragmentation variance theorem.

Python 3 standard library only. Computations are integer polynomial identities;
they supplement the general combinatorial proof.
"""
from collections import defaultdict
from itertools import combinations
from math import comb

EXAMPLE_A=((0,1),(0,2),(0,3),(3,4),(3,5),(4,5))
EXAMPLE_B=((0,2),(1,2),(1,3),(1,4),(2,4),(3,5))


def components(n, edges, mask):
    adjacent=[[] for _ in range(n)]
    for u,v in edges:
        adjacent[u].append(v);adjacent[v].append(u)
    seen=0; count=0
    for u in range(n):
        if not ((mask>>u)&1) or ((seen>>u)&1):
            continue
        count+=1
        seen|=1<<u
        stack=[u]
        while stack:
            v=stack.pop()
            for w in adjacent[v]:
                if ((mask>>w)&1) and not ((seen>>w)&1):
                    seen|=1<<w;stack.append(w)
    return count


def cycle_vertices(n,edges):
    # Repeatedly trim leaves; the surviving 2-core is the unique cycle.
    adjacent=[set() for _ in range(n)]
    for u,v in edges:
        adjacent[u].add(v);adjacent[v].add(u)
    todo=[v for v in range(n) if len(adjacent[v])<=1]
    while todo:
        u=todo.pop()
        for v in tuple(adjacent[u]):
            adjacent[v].remove(u)
            if len(adjacent[v])==1:
                todo.append(v)
        adjacent[u].clear()
    return frozenset(v for v in range(n) if adjacent[v])


def connected(n,edges):
    return components(n,edges,(1<<n)-1)==1


def polynomial_moments(n,edges):
    first=[0]*(n+1);second=[0]*(n+1)
    for mask in range(1<<n):
        k=mask.bit_count(); cc=components(n,edges,mask)
        for j in range(n-k+1):
            b=(-1)**j*comb(n-k,j)
            first[k+j]+=cc*b;second[k+j]+=cc*cc*b
    squared=[0]*(2*n+1)
    for i,a in enumerate(first):
        for j,b in enumerate(first):
            squared[i+j]+=a*b
    return first,[second[k] if k<=n else 0 for k in range(2*n+1)],\
        [(second[k] if k<=n else 0)-squared[k] for k in range(2*n+1)]


def predicted(n,edges,cyc):
    degrees=[0]*n
    for u,v in edges: degrees[u]+=1;degrees[v]+=1
    ell=len(cyc)
    wedges=sum(d*(d-1)//2 for d in degrees)
    h=sum(degrees[v]-2 for v in cyc)
    mean=[0]*(n+1);mean[1]+=n;mean[2]-=n;mean[ell]+=1
    variance=[0]*(2*n+1)
    terms=((1,n),(2,-4*n),(3,4*n+2*wedges),(4,-n-2*wedges),
           (ell,1),(2*ell,-1),(ell+1,-2*(ell+h)),(ell+2,2*(ell+h)))
    for k,value in terms: variance[k]+=value
    return tuple(sorted(degrees)),ell,h,mean,variance


def run():
    count=0; total=0; checked=0
    small_groups=defaultdict(set)
    for n in range(3,7):
        for edges in combinations(combinations(range(n),2),n):
            if not connected(n,edges):
                continue
            cyc=cycle_vertices(n,edges)
            assert len(cyc)>=3
            degrees,ell,h,mean,variance=predicted(n,edges,cyc)
            m1,m2,v=polynomial_moments(n,edges)
            assert m1==mean,(n,edges,'mean')
            assert v==variance,(n,edges,'variance')
            checked+=1;count+=2
            if n<=5:
                small_groups[n,degrees,ell].add(h)
    assert all(len(hs)==1 for hs in small_groups.values())
    a=predicted(6,EXAMPLE_A,cycle_vertices(6,EXAMPLE_A))
    b=predicted(6,EXAMPLE_B,cycle_vertices(6,EXAMPLE_B))
    assert a[:2]==b[:2] and (a[2],b[2])==(1,2)
    assert [x-y for x,y in zip(a[4],b[4])]==[0,0,0,0,2,-2]+[0]*7
    assert len(a[4])==13
    print('PASS: exact mean and variance polynomials for',checked,'labeled connected unicyclic graphs on 3..6 vertices')
    print('PASS: each degree-multiset/cycle-length class on 3..5 vertices has one h value')
    print('PASS: six-vertex example has variance gap 2*p^4*(1-p)')
    print('CHECKED polynomial equalities:',count)


if __name__=='__main__':
    run()
