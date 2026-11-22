#!/usr/bin/env python3
"""Direct GF(2) checks for cubic exterior multiplication."""
from itertools import combinations
from collections import Counter
from math import comb

def masks(n,j):
    return [sum(1<<i for i in c) for c in combinations(range(n),j)]

def rank_binary(columns):
    pivots={}
    for col in columns:
        w=col
        while w:
            p=w.bit_length()-1
            if p in pivots: w^=pivots[p]
            else:
                pivots[p]=w
                break
    return len(pivots)

def multiplication_rank_profile(n,cubic):
    f3=masks(n,3)
    pairs=tuple(f3[i] for i in range(len(f3)) if (cubic>>i)&1)
    result=[]
    for j in range(n+1):
        source=masks(n,j)
        target={v:i for i,v in enumerate(masks(n,j+3))} if j+3<=n else {}
        cols=[]
        for a in source:
            b=0
            for z in pairs:
                if not (a&z): b^=1<<target[a|z]
            cols.append(b)
        result.append(rank_binary(cols))
    return tuple(result)

def gauss(n,k,q):
    if not 0<=k<=n:return 0
    numerator=1
    denominator=1
    for i in range(k):
        numerator*=q**(n-i)-1
        denominator*=q**(k-i)-1
    return numerator//denominator

def expected(n,s):
    # Polynomial division by 1+t^2
    a=[comb(n-1,i) for i in range(n)]
    for j in range(n-1-2*s+1): a[j+s]-=(2**s)*comb(n-1-2*s,j)
    r=[0]*n
    for i in range(n):
        r[i]=a[i]-(r[i-2] if i>=2 else 0)
    assert r[-1]==0
    return tuple(r)+(0,)

def cubic_from_terms(n,terms):
    ix={m:i for i,m in enumerate(masks(n,3))}
    c=0
    for term in terms:
        m=sum(1<<i for i in term)
        c ^= 1<<ix[m]
    return c

def main():
    # Exhaust the 2^20 cubic elements in six generators by computing the
    # 6-column V->Lambda^4 V map, then verify multiplier ranks on examples.
    n=6
    three=masks(n,3)
    four={v:i for i,v in enumerate(masks(n,4))}
    base=[[0]*len(three) for _ in range(n)]
    for v in range(n):
        for i,z in enumerate(three):
            if not z&(1<<v): base[v][i]=1<<four[z|(1<<v)]
    look=[]
    for v in range(n):
        blocks=[]
        for start,stop in ((0,7),(7,14),(14,20)):
            tab=[0]*(1<<(stop-start))
            for x in range(1,len(tab)):
                low=x&(-x)
                tab[x]=tab[x^low]^base[v][start+low.bit_length()-1]
            blocks.append(tab)
        look.append(blocks)
    observed=Counter()
    for x in range(1<<20):
        columns=[b[0][x&127]^b[1][(x>>7)&127]^b[2][x>>14] for b in look]
        r=rank_binary(columns)
        observed[r]+=1
    expected_counts={0:1,3:gauss(6,3,2),5:gauss(6,1,2)*(2**10-1-gauss(5,2,2))}
    expected_counts[6]=(1<<20)-sum(expected_counts.values())
    assert dict(observed)==expected_counts, (observed,expected_counts)
    print('GF2 six-dimensional wedge-annihilator ranks:',dict(sorted(observed.items())))
    # All possible nonzero 3-form types in n=6 are represented.
    types={3:[(0,1,2)],5:[(0,1,2),(0,3,4)],6:[(0,1,2),(3,4,5)]}
    for wr,terms in types.items():
        profile=multiplication_rank_profile(6,cubic_from_terms(6,terms))
        assert sum(profile)==2+2*wr,(wr,profile)
        if wr==3:assert profile==expected(6,1)
        if wr==5:assert profile==expected(6,2)
        print('n=6 wedge rank',wr,'graded exterior multiplier ranks:',profile)
    for n in range(5,9):
        for s in range(1,(n-1)//2+1):
            terms=[(0,2*i+1,2*i+2) for i in range(s)]
            profile=multiplication_rank_profile(n,cubic_from_terms(n,terms))
            target=expected(n,s)
            assert profile==target,(n,s,profile,target)
            assert sum(profile)==2**(n-2)-2**(n-s-2)
            print('divisible cubic n=%d s=%d rank=%d verified'%(n,s,sum(profile)))
    print('CUBIC_EXTERIOR_DIRECT_GF2_PASS')
if __name__=='__main__':main()
