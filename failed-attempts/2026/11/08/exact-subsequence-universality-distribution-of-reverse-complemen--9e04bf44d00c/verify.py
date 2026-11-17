#!/usr/bin/env python3
"""Exact diagnostic for reverse-complement symmetry and subsequence universality.
The finite test is independent of the symbolic all-length proof.
"""
from itertools import product
from collections import Counter
from math import comb, factorial

def idx_rest(word, q):
    seen=set(); k=0; start=0
    for i, a in enumerate(word):
        seen.add(a)
        if len(seen)==q:
            k+=1; start=i+1; seen.clear()
    return k,word[start:]

def B(s,N):
    # onto words using a fixed set of exactly s letters
    out=[0]*(N+1)
    for n in range(N+1):
        out[n]=sum((-1)**(s-j)*comb(s,j)*j**n for j in range(s+1))
    return out

def polynomial_prediction(q,N):
    m=q//2
    bs=[B(s,N) for s in range(q)]
    T=[sum(comb(q,s)*bs[s][n] for s in range(q)) for n in range(N+1)]
    R=[sum(comb(m,s-m)*2**(q-s)*bs[s][n] for s in range(m,q)) for n in range(N+1)]
    # Each arch = q choices of missing last letter * onto words using other q-1.
    A=[0]*(N+1)
    for n in range(1,N+1):
        A[n]=q*bs[q-1][n-1]
    # recurrence F=(T+(u-1)R)+u^2 A F
    out=[Counter() for _ in range(N+1)]
    for n in range(N+1):
        if T[n]-R[n]:out[n][0]+=T[n]-R[n]
        if R[n]:out[n][1]+=R[n]
        for j in range(1,n+1):
            for k,c in out[n-j].items():out[n][k+2]+=A[j]*c
    return out

def direct_universal(word,q,k):
    # independent of arch factorization; bounded diagnostic only
    if not k:return True
    for target in product(range(q),repeat=k):
        j=0
        for x in word:
            if x==target[j]:
                j+=1
                if j==k:break
        else:return False
    return True

total=0; cells=0; direct=0
for q,N in [(2,12),(4,8),(6,6),(8,5)]:
    pred=polynomial_prediction(q,N)
    for n in range(N+1):
        actual=Counter()
        for half in product(range(q),repeat=n):
            whole=half+tuple(a^1 for a in half[::-1])
            j,_=idx_rest(whole,q)
            k,tail=idx_rest(half,q)
            expected=2*k+int(len(set(tail)|{a^1 for a in tail})==q)
            if j!=expected:
                raise AssertionError(('structural',q,n,half,j,expected))
            if q<=4 and n<=4 and j<=3:
                if not direct_universal(whole,q,j) or direct_universal(whole,q,j+1):
                    raise AssertionError(('subsequence',q,n,half,j))
                direct+=1
            actual[j]+=1;total+=1
        if actual!=pred[n]:
            raise AssertionError(('GF',q,n,actual,pred[n]))
        cells+=len(actual)
    print('q=',q,'N=',N,'total=',sum(q**n for n in range(N+1)),
          'sample_last=',dict(sorted(pred[N].items())))
# Exact shortest universal anti-palindromes: q*(t) symbols, t arches.
for q in (2,4,6,8):
    m=q//2
    for t in range(1,6):
        N=q*t//2
        pred=polynomial_prediction(q,N)[N][t]
        closed=factorial(q)**(t//2)*(1 if t%2==0 else 2**m*factorial(m))
        assert pred==closed,(q,t,pred,closed)
print(f'VERIFY_OK halfwords={total} nonzero_cells={cells} direct_subsequence_cases={direct} shortest_profiles=20')
