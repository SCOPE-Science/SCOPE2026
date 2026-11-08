#!/usr/bin/env python3
"""Direct dynamic-programming tests of the top-two run law.
Usage: python3 verify.py
"""
from itertools import product
from functools import lru_cache

def lps_length(word):
    n=len(word)
    if n==0: return 0
    d=[[0]*n for _ in range(n)]
    for i in range(n): d[i][i]=1
    for span in range(2,n+1):
        for i in range(n-span+1):
            j=i+span-1
            d[i][j]=(2+(d[i+1][j-1] if span>2 else 0)) if word[i]==word[j] else max(d[i+1][j],d[i][j-1])
    return d[0][-1]

def is_subsequence(s,w):
    it=iter(w)
    return all(any(x==c for x in it) for c in s)

def all_best_palindromes(w):
    n=len(w)
    @lru_cache(None)
    def f(i,j):
        if i>j:return frozenset(('',))
        if i==j:return frozenset((w[i],))
        best=set(f(i+1,j))|set(f(i,j-1))
        if w[i]==w[j]:
            best.update(w[i]+v+w[j] for v in f(i+1,j-1))
        L=max(map(len,best))
        return frozenset(v for v in best if len(v)==L)
    return f(0,n-1)

cases=0; witness=0; counted=0
for q in range(2,6):
    for lengths in product(range(1,5),repeat=q):
        block=''.join(chr(97+i)*lengths[i] for i in range(q))
        ranks=sorted(lengths,reverse=True)
        A,B=ranks[:2]
        for k in range(1,5):
            word=block*k
            observed=lps_length(word)
            expected=k*A+(k-1)*B
            assert observed==expected,('LPS counterexample',q,lengths,k,observed,expected)
            cases+=1
            maxletter=chr(97+lengths.index(A))
            secondletter=chr(97+next(i for i,a in enumerate(lengths) if i!=lengths.index(A) and a==B))
            construction=(maxletter*A+secondletter*B)*(k-1)+maxletter*A
            assert construction==construction[::-1] and is_subsequence(construction,word)
            assert len(construction)==expected
            witness+=1

for q in (2,3):
    for lengths in product((1,2,3),repeat=q):
        for k in (1,2,3):
            block=''.join(chr(97+i)*lengths[i] for i in range(q))
            word=block*k
            if len(word)>24: continue
            top=max(lengths); t=lengths.count(top)
            solutions=all_best_palindromes(word)
            if t==1:
                sec=max(a for a in lengths if a!=top)
                r=lengths.count(sec)
                assert len(solutions)==r**(k//2),('count',lengths,k,len(solutions),r**(k//2))
                assert all(len(x)==k*top+(k-1)*sec for x in solutions)
            counted+=1
print('PASS: length profiles=',cases,'explicit witnesses=',witness,'small exact optimizer enumerations=',counted)
