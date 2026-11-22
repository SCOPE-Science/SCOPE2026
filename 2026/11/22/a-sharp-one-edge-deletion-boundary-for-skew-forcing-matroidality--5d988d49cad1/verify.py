#!/usr/bin/env python3
"""Reproducible finite checks for an edge-deletion boundary of skew forcing matroidality."""

def near_biclique(a, b):
    n = a+b
    nbrs = [0]*n
    for i in range(a):
        for j in range(a,n):
            if i==0 and j==a:
                continue
            nbrs[i] |= 1<<j
            nbrs[j] |= 1<<i
    return nbrs


def closure(S, adj):
    n=len(adj)
    while True:
        U=((1<<n)-1)^S
        nxt=0
        for v in range(n):
            whites=adj[v]&U
            if whites and whites&(whites-1)==0:
                nxt |= whites
        if not nxt:
            return S
        S |= nxt


def exchange_holds(adj):
    n=len(adj)
    cs=[closure(S,adj) for S in range(1<<n)]
    for S in range(1<<n):
        outside=((1<<n)-1)^cs[S]
        for x in range(n):
            if not (outside>>x)&1:
                continue
            for y in range(n):
                if y==x or not(outside>>y)&1:
                    continue
                if (cs[S|(1<<y)]>>x)&1 and not(cs[S|(1<<x)]>>y)&1:
                    return False
    return True


checked=0
for a in range(1,11):
    for b in range(1,11):
        if a+b>10:continue
        actual=exchange_holds(near_biclique(a,b))
        expected=min(a,b)==1 or (a,b)==(2,2)
        assert actual==expected,(a,b,actual,expected)
        checked+=1
print('EXHAUSTIVE_ALL_SUBSETS_EXCHANGE_PASS graph_instances=',checked)

# Explicit one-way exchange witnesses for all larger bicliques. A is the shore
# with at least three vertices; missing edge is (A[0],B[0]).
witness_count=0
for a in range(3,41):
    for b in range(2,41):
        adj=near_biclique(a,b)
        S=sum(1<<i for i in range(3,a))
        x=0
        y=1
        clS=closure(S,adj)
        cl_y=closure(S|(1<<y),adj)
        cl_x=closure(S|(1<<x),adj)
        assert not ((clS>>x)&1), (a,b,'x already closed')
        assert ((cl_y>>x)&1), (a,b,'x not forced by y')
        assert not ((cl_x>>y)&1), (a,b,'y forced by x')
        witness_count+=1
print('EXPLICIT_EXCHANGE_OBSTRUCTIONS_PASS cases=',witness_count)

# The small-exception claims: all of P4 is in cl(empty); in a star plus an
# isolated endpoint, the center is a loop and the remaining leaves form a
# uniform corank-one matroid, while the isolated endpoint is a coloop.
assert closure(0,near_biclique(2,2))==(1<<4)-1
for b in range(2,14):
    adj=near_biclique(1,b)
    n=b+1
    center=0
    iso=1
    leaves=range(2,n)
    for S in range(1<<n):
        c=closure(S,adj)
        assert bool(c&(1<<iso)) == bool(S&(1<<iso))
        assert (c&(1<<center))!=0
        selected=sum(1 for v in leaves if S&(1<<v))
        for v in leaves:
            expected=bool(S&(1<<v)) or selected>=len(leaves)-1
            assert bool(c&(1<<v))==expected,(b,S,v)
print('EXCEPTIONAL_MATROIDS_FULL_CLOSURE_PASS')
print('VERIFY_OK')
