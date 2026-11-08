#!/usr/bin/env python3
"""Independent finite checker for a support classification of onto maps.
Uses the definition of shattering for all subsets of the incidence grid.
The unrestricted statements are established mathematically, not by this search.
"""
from itertools import product
from collections import Counter
from math import comb, factorial


def stirling2(s, d):
    old=[1]
    for x in range(1,s+1):
        new=[0]*(x+1)
        for k in range(1,x+1):
            new[k]=(old[k-1] if k-1<len(old) else 0) + k*(old[k] if k<len(old) else 0)
        old=new
    return old[d] if d<len(old) else 0


def predicted(n,q,mask):
    rows=0; colors=set(); s=mask.bit_count()
    for i in range(n):
        x=(mask>>(i*q))&((1<<q)-1)
        if x.bit_count()>1:return False
        if x:
            rows+=1
            colors.add(x.bit_length()-1)
    return (rows<n and s-len(colors)<=n-q)


def concepts(n,q):
    return [sum(1<<(i*q+a) for i,a in enumerate(t)) for t in product(range(q),repeat=n) if len(set(t))==q]


def check_pair(n,q):
    C=concepts(n,q)
    size=n*q
    cnt=Counter()
    count=0
    for S in range(1<<size):
        s=S.bit_count()
        # If a support is too large even hypothesis counting makes it impossible.
        actual= s<=len(C).bit_length()-1 and len({c&S for c in C})==(1<<s)
        expected=predicted(n,q,S)
        assert actual==expected,(n,q,S,actual,expected)
        if actual:cnt[s]+=1
        count+=1
    poly={}
    for s in range(n):
        total=sum(factorial(q)//factorial(q-d)*stirling2(s,d)
                    for d in range(max(0,s-n+q),min(q,s)+1))
        poly[s]=comb(n,s)*total
    assert all(cnt[k]==poly.get(k,0) for k in set(cnt)|set(poly)),(n,q,cnt,poly)
    assert max(cnt)==n-1 and cnt[n-1]==n*factorial(q)*(stirling2(n-1,q-1)+stirling2(n-1,q))
    return count, sum(cnt.values()), cnt


def check_exchange_counterexamples():
    for q in range(3,6):
        for n in range(q,9):
            if n==q:
                A={(i,i) for i in range(q-1)}
                B={(0,1),(1,0)}|{(i,i) for i in range(2,q-1)}
                e=(0,0)
            else:
                # 0-based rows, colors: e uses q-2; A-e uses all 0..q-3
                e=(0,q-2)
                A={e}|{(i,(i-1)%(q-2)) for i in range(1,n-1)}
                B={(i,(i-1)%(q-1)) for i in range(1,n-1)}|{(n-1,0)}
            def bit(X):return sum(1<<(i*q+j) for i,j in X)
            assert len(A)==len(B)==n-1 and predicted(n,q,bit(A)) and predicted(n,q,bit(B)),(n,q,A,B)
            assert e in A-B
            assert all(not predicted(n,q,bit((A-{e})|{b})) for b in B-A),(n,q,A,B)


def main():
    rounds=0; supports=0; shattered=0
    for n in range(2,6):
        for q in range(2,min(n,4)+1):
            if (n,q)==(5,4):continue
            a,b,c=check_pair(n,q)
            rounds+=1; supports+=a; shattered+=b
            print('checked',n,q,'supports',a,'shattered',b,'f-vector',dict(sorted(c.items())))
    check_exchange_counterexamples()
    print('SURJECTION_SUPPORT_CLASSIFICATION_PASS',rounds,supports,shattered,'nonmatroid_witness_pairs',sum(9-q for q in range(3,6)))

if __name__=='__main__':main()
