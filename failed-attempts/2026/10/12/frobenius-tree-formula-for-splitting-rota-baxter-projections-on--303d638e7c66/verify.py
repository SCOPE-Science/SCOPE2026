#!/usr/bin/env python3
"""Exhaustive small-field checks for splitting Rota--Baxter projections."""
from itertools import combinations

IRREDUCIBLES = {1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101}

def gfmul(a,b,d):
    mask=(1<<d)-1; poly=IRREDUCIBLES[d]
    z=0
    while b:
        if b&1:z^=a
        b >>= 1; a <<= 1
        if a&(1<<d):a^=poly
    return z&mask

def multiplication(degrees):
    n=sum(degrees); fields=[]; shift=0
    for d in degrees:
        fields.append((d,shift,(1<<d)-1));shift+=d
    N=1<<n
    return [[sum(gfmul((x>>s)&mask,(y>>s)&mask,d)<<s for d,s,mask in fields)
             for y in range(N)] for x in range(N)]

def all_subspaces(n):
    N=1<<n
    levels={frozenset([0])}
    result=set(levels)
    for _ in range(n):
        nex=set()
        for sub in levels:
            for v in range(1,N):
                if v not in sub:
                    nex.add(frozenset(sub | {x^v for x in sub}))
        levels=nex-result
        result |= levels
    return [frozenset(s) for s in result]

def count_splittings(degrees, full_check=False):
    n=sum(degrees); N=1<<n; mult=multiplication(degrees)
    subs=all_subspaces(n)
    closed=[s for s in subs if all(mult[x][y] in s for x in s for y in s)]
    count=0
    for U in closed:
        for V in closed:
            if len(U)*len(V)!=N or U.intersection(V)!={0}:continue
            count+=1
            if full_check:
                P={x^y:x for x in U for y in V}
                assert len(P)==N
                assert all(P[P[x]]==P[x] for x in range(N))
                assert all(mult[P[x]][P[y]] == P[mult[P[x]][y] ^ mult[x][P[y]] ^ mult[x][y]] for x in range(N) for y in range(N))
    return count,len(subs),len(closed)

def expected(degrees):
    from collections import Counter
    r=Counter(degrees); result=1
    for d,m in r.items():
        s=sum(e*n for e,n in r.items() if e<d and d%e==0)
        result*=(2+s)*(2+s+d*m)**(m-1)
    return result

TESTS=[(1,),(2,),(3,),(1,1),(1,2),(2,2),(1,1,1),(1,1,2),(1,3),(1,1,1,1),(1,1,1,2),(2,3),(1,4),(1,2,2),(2,2,1)]
if __name__=='__main__':
    for ds in TESTS:
        count,subspaces,subalgebras=count_splittings(ds,full_check=sum(ds)<=4)
        target=expected(ds)
        assert count==target,(ds,count,target)
        print(f'degrees={ds!s:16} direct_sum_pairs={count:4d} expected={target:4d} subspaces={subspaces:3d} subalgebras={subalgebras:3d}')
    print('VERIFY_OK')
