#!/usr/bin/env python3
"""Independent cyclic gap-word enumeration; no infection simulation.
Enumerates all gap strings for a candidate maximum white-set size by a restricted composition search.
Checks direct graph acyclicity, gap characterization, and exact time census for n up to 32.
"""
from collections import Counter

def acyclic(S,n):
    parent=list(range(n))
    S=set(S)
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    for i in S:
        for h in (1,2):
            j=(i+h)%n
            if j in S:
                a,b=root(i),root(j)
                if a==b:return False
                parent[a]=b
    return True

def search_gaps(n,m):
    # Enumerate all integer compositions with cyclic exclusion of neighboring 1s.
    # Large gaps > 4 cannot occur at optimum, but include up to n to verify the bound separately.
    def rec(prefix,remain):
        slots=m-len(prefix)
        if slots==0:
            if remain==0 and not (prefix[0]==prefix[-1]==1) and max(prefix)>=3:
                yield tuple(prefix)
            return
        if remain < slots:return
        for x in range(1,remain-slots+2):
            if prefix and prefix[-1]==x==1:continue
            yield from rec(prefix+[x],remain-x)
    return rec([],n)

def expected(n):
    k=n//3
    if n%3==0:return Counter({k:n*k})
    if n%3==1:return Counter({k:n})
    result=Counter({k:n*(k*k+k+2)//2})
    for t in range((k+1)//2,k):
        if 2*t<k:continue
        result[t]=n//2 if 2*t==k else n
    return result

def composition_time(g):
    # Segments broken at gaps >= 3: path vertex count is number of gaps from one break to the next.
    m=len(g);cuts=[i for i,x in enumerate(g) if x>=3]
    assert cuts
    if len(cuts)==1:return (m+1)//2
    assert len(cuts)==2
    a=(cuts[1]-cuts[0])%m; b=m-a
    return max((a+1)//2,(b+1)//2)

if __name__=='__main__':
    for n in range(5,33):
        m=(2*(n-1))//3
        census=Counter()
        rooted=0
        for gaps in search_gaps(n,m):
            assert sum(gaps)==n
            assert max(gaps)<=4
            S=[0];pos=0
            for g in gaps[:-1]:pos+=g;S.append(pos)
            assert len(S)==m and S[-1]<n
            assert acyclic(S,n), (n,gaps)
            census[composition_time(gaps)]+=n
            rooted+=1
        assert all(count%m==0 for count in census.values()),(n,census,m)
        census=Counter({t:c//m for t,c in census.items()})
        assert census==expected(n),(n,census,expected(n))
        print(f'n={n} rooted_gap_strings={rooted} census={dict(sorted(census.items()))} PASS')
    print('PASS: gap certificates 5..32')
