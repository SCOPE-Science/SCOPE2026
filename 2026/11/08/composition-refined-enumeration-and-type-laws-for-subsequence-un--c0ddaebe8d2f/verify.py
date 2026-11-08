#!/usr/bin/env python3
"""Standalone integer tests of composition-refined subsequence universality.

Requires only the Python standard library.  Reconstructs the multivariate
arch-series coefficients from composition sums and independently tests direct
subsequence containment on complete finite word sets.
"""
from itertools import product
from collections import defaultdict
from math import comb, factorial

def index_direct(word,q):
    ans=0
    for k in range(1,len(word)//q+1):
        yes=True
        for s in product(range(q),repeat=k):
            pos=0
            for c in word:
                if c==s[pos]:
                    pos+=1
                    if pos==k:
                        break
            if pos<k:
                yes=False
                break
        if not yes:
            break
        ans=k
    return ans

def index_greedy(word,q):
    seen=set(); k=0
    for c in word:
        seen.add(c)
        if len(seen)==q:
            k+=1;seen.clear()
    return k

def multi_indices(q,n):
    if q==1:
        for j in range(n+1): yield (j,)
    else:
        for j in range(n+1):
            for tail in multi_indices(q-1,n-j):yield (j,)+tail

def coefficient_table(q,n):
    # Count all possible first-exhausting arches and incomplete remainders
    # via their independent multinomial coefficients.
    A={};R={};facs=[factorial(i) for i in range(n+1)]
    for v in multi_indices(q,n):
        length=sum(v)
        multi=facs[length]
        multi//=__import__("math").prod(facs[vi] for vi in v)
        if min(v)==0: R[v]=multi
        if min(v)>=1 and length>=q:
            # Last letter j occurs once: its earlier occurrences must be zero.
            # Each eligible j contributes all permutations of the remaining letters.
            count=0
            for j in range(q):
                if v[j]!=1:continue
                denom=1
                for i in range(q):
                    if i!=j:denom*=facs[v[i]]
                count+=facs[length-1]//denom
            if count:A[v]=count
    zero=(0,)*q
    prev={zero:1}
    out=defaultdict(int)
    for k in range(n//q+1):
        for a,va in prev.items():
            for b,vb in R.items():
                c=tuple(x+y for x,y in zip(a,b))
                if sum(c)<=n: out[c,k]+=va*vb
        nxt=defaultdict(int)
        for a,va in prev.items():
            for b,vb in A.items():
                c=tuple(x+y for x,y in zip(a,b))
                if sum(c)<=n:nxt[c]+=va*vb
        prev=nxt
    return out

def moments(a,b):
    if not a or not b:return 0
    return sum((a+b-2*j)*comb(a+b-2*j-2,a-j-1) for j in range(min(a,b)))

def maximum_count(a,b):
    lo=min(a,b);hi=max(a,b)
    return sum(comb(lo,j)*comb(hi-lo+j,j) for j in range(lo+1))

sizes={2:13,3:8,4:7}
word_tests=0;index_tests=0;cells=0
for q,nmax in sizes.items():
    tab=coefficient_table(q,nmax)
    for n in range(nmax+1):
        direct=defaultdict(int)
        for w in product(range(q),repeat=n):
            k=index_direct(w,q)
            assert k==index_greedy(w,q),(q,w,k)
            t=tuple(w.count(i) for i in range(q))
            direct[t,k]+=1
            word_tests+=1
            index_tests+=1
        for t in multi_indices(q,n):
            if sum(t)!=n:continue
            assert sum(direct[t,k] for k in range(n//q+1)) == factorial(n)//__import__('math').prod(factorial(j) for j in t)
            for k in range(n//q+1):
                assert direct[t,k]==tab[t,k],(q,t,k,direct[t,k],tab[t,k])
                cells+=1
            if q==2:
                a,b=t
                assert direct[t,min(t)]==maximum_count(a,b),(t,maximum_count(a,b))
                assert sum(k*direct[t,k] for k in range(n//2+1))==moments(a,b),(t,'moment')
    print(f'PASS q={q}, n=0..{nmax}')
print(f'VERIFY_OK words={word_tests}, direct_indices={index_tests}, coefficient_cells={cells}; extreme and first-moment identities tested')
