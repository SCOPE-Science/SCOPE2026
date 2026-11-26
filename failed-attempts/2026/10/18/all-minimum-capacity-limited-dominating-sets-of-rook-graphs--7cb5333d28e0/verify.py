#!/usr/bin/env python3
"""Exhaustive, graph-neighbourhood verification of minimum k-limited dominating sets on small rook boards.
No external packages required. Run: python3 verify.py
"""
from math import comb


def capacity_surjections(a, b, t):
    """Number of functions from b labelled items to a labelled targets, every nonempty fibre >= t."""
    t = max(1, t)
    dp = [0] * (b + 1)
    dp[0] = 1
    for _ in range(a):
        new = [0] * (b + 1)
        for u in range(b + 1):
            if dp[u] == 0:
                continue
            new[u] += dp[u]
            for s in range(t, b - u + 1):
                new[u+s] += dp[u] * comb(u+s,s)
        dp = new
    return dp[b]


def expected(m,n,k):
    assert 2 <= m <= n and k >= 1
    if m == n:
        if k < n-1:
            return n*(n-k), 2*comb(n,k)
        t = max(1,2*n-1-k)
        return n, 2*capacity_surjections(n,n,t) - (1 if k >= 2*n-2 else 0)*factorial(n)
    if k < m:
        return n*(m-k), comb(m,k)
    if k < n-1:
        c = m*(n-k)
        t = n+m-1-k
        if c < n:
            return c, comb(n,n-k)
        if c > n:
            return n, capacity_surjections(m,n,t)
        return n, comb(n,n-k) + capacity_surjections(m,n,t)
    t = max(1,m+n-1-k)
    return m, capacity_surjections(n,m,t)


def factorial(n):
    ans=1
    for a in range(2,n+1):ans*=a
    return ans


def matches_structural(m,n,k,mask):
    rr=[sum((mask>>(i*n+j))&1 for j in range(n)) for i in range(m)]
    cc=[sum((mask>>(i*n+j))&1 for i in range(m)) for j in range(n)]
    if m == n:
        if k < n-1:
            return (sorted(rr) == [0]*k + [n]*(n-k) or
                    sorted(cc) == [0]*k + [m]*(m-k))
        t=max(1,2*n-1-k)
        return ((all(x == 1 for x in rr) and all(x == 0 or x>=t for x in cc)) or
                (all(x == 1 for x in cc) and all(x == 0 or x>=t for x in rr)))
    if k < m:
        return sorted(rr) == [0]*k + [n]*(m-k)
    if k < n-1:
        c = m*(n-k)
        t = m+n-1-k
        return ((c <= n and sorted(cc) == [0]*k+[m]*(n-k)) or
                (c >= n and all(x==1 for x in cc) and all(x == 0 or x>=t for x in rr)))
    t=max(1,m+n-1-k)
    return all(x==1 for x in rr) and all(x==0 or x>=t for x in cc)


def direct_graph_check(m,n):
    nn=m*n
    neigh=[]
    for i in range(m):
        for j in range(n):
            neigh.append(sum(1 << (a*n+b) for a in range(m) for b in range(n)
                             if (a==i) != (b==j)))
    maxdeg=m+n-2
    opt=[nn+1]*(maxdeg+1)
    num=[0]*(maxdeg+1)
    struct=[0]*(maxdeg+1)
    full=(1<<nn)-1
    for mask in range(1,1<<nn):
        # All omitted vertices must see a selected neighbour.
        outside=full^mask
        temp=outside
        ok=True
        while temp:
            v=(temp&-temp).bit_length()-1
            temp &= temp-1
            if neigh[v]&mask == 0:
                ok=False
                break
        if not ok:continue
        min_capacity=0
        temp=mask
        while temp:
            v=(temp&-temp).bit_length()-1
            temp&=temp-1
            min_capacity=max(min_capacity, (neigh[v]&outside).bit_count())
        sz=mask.bit_count()
        for k in range(max(1,min_capacity),maxdeg+1):
            if sz<opt[k]:
                opt[k]=sz
                num[k]=0
                struct[k]=0
            if sz==opt[k]:
                num[k]+=1
                if matches_structural(m,n,k,mask):struct[k]+=1
    for k in range(1,maxdeg+1):
        e,c=expected(m,n,k)
        assert (opt[k],num[k],struct[k])==(e,c,c), (
            m,n,k, 'brute',(opt[k],num[k],struct[k]),'expected',(e,c,c))
    return maxdeg

if __name__=='__main__':
    boards=[(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5)]
    checks=0
    for m,n in boards:
        c=direct_graph_check(m,n)
        checks+=c
        print('PASS',f'{m}x{n}',f'capacity_cases={c}',f'all_subsets={1<<(m*n)}')
    print('VERIFIED',len(boards),'boards',checks,'positive-capacity cases')
    print('Example 3x6 at k=4:',expected(3,6,4))
    print('Example 4x4 at k=5:',expected(4,4,5))
