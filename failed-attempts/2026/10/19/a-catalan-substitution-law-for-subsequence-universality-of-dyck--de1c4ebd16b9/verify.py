#!/usr/bin/env python3
"""Finite, reproducible checks of Dyck-word subsequence-universality enumeration.

No finite check is used as a proof of the infinite generating function.
Python 3 standard library only.
"""
from collections import defaultdict
from itertools import product
from math import comb


def catalan(j):
    return comb(2*j, j)//(j+1)


def formula(n,k):
    if n==k==0: return 1
    if k==0 or n<k: return 0
    return sum((-1)**(k-j)*catalan(j)*comb(j,k-j)*comb(n-k+j-1,j-1)
               for j in range((k+1)//2,k+1))


def dyck(n, w='', height=0):
    if len(w)==2*n:
        if height==0: yield w
        return
    if w.count('0')<n: yield from dyck(n,w+'0',height+1)
    if height>0: yield from dyck(n,w+'1',height-1)


def is_subseq(pattern,word):
    i=0
    for a in word:
        if i<len(pattern) and a==pattern[i]: i+=1
    return i==len(pattern)


def direct_index(w):
    for k in range(len(w)//2+1):
        if not all(is_subseq(''.join(p),w) for p in product('01',repeat=k)):
            return k-1
    return len(w)//2


def arch_index(w):
    seen=set();k=0
    for symbol in w:
        seen.add(symbol)
        if len(seen)==2:
            k+=1; seen.clear()
    return k


def transfer_distribution(n):
    # states (height, partial arch seen state, completed arches).
    # partial state: 0 none, 1 seen 0, 2 seen 1.
    states={(0,0,0):1}
    for step in range(2*n):
        nxt=defaultdict(int)
        for (height,s,k),v in states.items():
            if height<n:
                nxt[(height+1, (1 if s!=2 else 0), k+(s==2))]+=v
            if height>0:
                nxt[(height-1, (2 if s!=1 else 0), k+(s==1))]+=v
        states=nxt
    out=defaultdict(int)
    for (height,s,k),v in states.items():
        if height==0: out[k]+=v
    return out


def main():
    for n in range(0,9):
        table=defaultdict(int)
        for w in dyck(n):
            d=direct_index(w) if n<=8 else None
            a=arch_index(w)
            assert d==a, ('arch',n,w,d,a)
            table[d]+=1
        assert sum(table.values())==catalan(n)
        assert all(table.get(k,0)==formula(n,k) for k in range(n+1)),('brute',n,table)
    print('Direct subsequence tests, arch indices and formula: n=0..8 PASS')
    for n in range(0,28):
        table=transfer_distribution(n)
        assert sum(table.values())==catalan(n)
        for k in range(n+1):
            assert table.get(k,0)==formula(n,k),('transfer',n,k,table.get(k,0),formula(n,k))
    print('Independent height/arch-state transfer and formula: n=0..27 PASS')
    for k in range(1,18):
        vals=[formula(n,k) for n in range(k,k+2*k+3)]
        diff=vals[:]
        for _ in range(k-1):
            diff=[b-a for a,b in zip(diff,diff[1:])]
        assert set(diff)=={catalan(k)},('finite difference',k,diff)
    print('Catalan fixed-index finite differences: k=1..17 PASS')
    for n in range(1,28):
        assert formula(n,n)==1
        if n>=2: assert formula(n,n-1)==2**(n-1)-1
    print('Sharp top two index layers: n=1..27 PASS')
    print('ALL FINITE CHECKS PASSED (infinite proof is in RESULT.md)')


if __name__=='__main__': main()
