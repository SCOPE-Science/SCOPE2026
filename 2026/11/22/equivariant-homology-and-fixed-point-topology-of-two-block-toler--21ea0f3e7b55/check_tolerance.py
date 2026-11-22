#!/usr/bin/env python3
"""Finite independent chain and equivariant checks for two-block tolerance complexes.
Scientific formulas are proved separately for all orders; this script checks small orders.
"""
from itertools import combinations
from math import comb

def faces(a,b,t):
    n=a+b
    return [m for m in range(1<<n) if min((m&((1<<a)-1)).bit_count(),(m>>a).bit_count())<=t]

def rank_bitvectors(vectors):
    basis={}
    for x in vectors:
        while x:
            k=x.bit_length()-1
            if k in basis:x^=basis[k]
            else:
                basis[k]=x
                break
    return len(basis)

def betti_mod2(a,b,t):
    fs=faces(a,b,t)
    bysize={k:[m for m in fs if m.bit_count()==k] for k in range(a+b+1)}
    ranks={}
    for size in range(2,a+b+1):
        dst={m:i for i,m in enumerate(bysize[size-1])}
        cols=[]
        for f in bysize[size]:
            m=f; vec=0
            while m:
                bit=m&-m;m-=bit
                vec^=1<<dst[f^bit]
            cols.append(vec)
        ranks[size]=rank_bitvectors(cols)
    return {size-1:len(items)-ranks.get(size,0)-ranks.get(size+1,0)-(1 if size==1 else 0)
            for size,items in bysize.items() if size and len(items)-ranks.get(size,0)-ranks.get(size+1,0)-(1 if size==1 else 0)}

def trace_reduced_chain(a,b,t,p):
    assert sorted(p)==list(range(a+b))
    result=-1 # empty simplex, reduced degree -1
    for f in faces(a,b,t):
        if not f:continue
        selected=[i for i in range(a+b) if f>>i&1]
        permuted=[p[i] for i in selected]
        if set(selected)!=set(permuted):continue
        inv=sum(permuted[i]>permuted[j] for i in range(len(permuted)) for j in range(i+1,len(permuted)))
        result+=(-1)**(len(selected)-1+inv)
    return result

def swap(n):return [i+n if i<n else i-n for i in range(2*n)]

def run():
    counts=0
    for a in range(2,6):
      for b in range(2,6):
       for t in range(1,min(a,b)+1):
        expected={} if t>=min(a,b) else {2*t:comb(a-1,t)*comb(b-1,t)}
        got=betti_mod2(a,b,t)
        assert got==expected,(a,b,t,got,expected)
        counts+=1
    swap_checks=[]
    for n in range(2,6):
      for t in range(1,n):
        r=comb(n-1,t)
        tr=(-1)**(t+1)*r
        got=trace_reduced_chain(n,n,t,swap(n))
        assert got==tr,(n,t,got,tr)
        # fixed space has orbit-vertex faces precisely sets of size <=t.
        fixed_counts=[comb(n,k) for k in range(t+1)]
        assert sum((-1)**(k-1)*fixed_counts[k] for k in range(t+1))==tr
        swap_checks.append((n,t,got))
    print('PASS mod2 all induced two-block cases:',counts)
    print('PASS reduced Lefschetz signs and fixed orbit Euler:',len(swap_checks))
    print('swap_trace_examples:',swap_checks)
if __name__=='__main__':run()
