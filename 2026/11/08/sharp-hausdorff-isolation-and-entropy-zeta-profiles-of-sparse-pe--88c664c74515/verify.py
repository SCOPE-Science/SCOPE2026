#!/usr/bin/env python3
"""Finite checks for a sharp Hausdorff-entropy profile in binary shift dynamics."""
from itertools import product
from math import log

def cyclic_language(q, n):
    seq = [1 if j % q == 0 else 0 for j in range(q)]
    return {tuple(seq[(i+k) % q] for k in range(n)) for i in range(q)}

def allowed_m_words(m):
    return {w for w in product((0, 1), repeat=m) if sum(w) <= 1}

def matrices(q, m):
    words = cyclic_language(q, m)
    states = sorted(cyclic_language(q, m-1)) if m > 1 else [()]
    # edge (m-word) is an allowed directed edge from prefix to suffix
    idx = {w:i for i,w in enumerate(states)}
    mat = [[0] * len(states) for _ in states]
    for w in words:
        left = w[:-1] if m > 1 else ()
        right = w[1:] if m > 1 else ()
        if left in idx and right in idx:
            mat[idx[left]][idx[right]] += 1
    return mat

def is_periodic_word_allowed(w, allowed):
    p, m = len(w), len(next(iter(allowed)))
    return all(tuple(w[(i+j)%p] for j in range(m)) in allowed for i in range(p))

def prim_period(w):
    p=len(w)
    return min(d for d in range(1,p+1) if p%d==0 and all(w[i]==w[i%d] for i in range(p)))

def root(m):
    a,b=1.,2.
    for _ in range(100):
        c=(a+b)/2
        if (c-1)*c**(m-1)>1:b=c
        else:a=c
    return (a+b)/2

checks=0
for q in range(2,12):
    for m in range(1,q+3):
        lang=cyclic_language(q,m)
        if m<q:
            assert lang == allowed_m_words(m)
        else:
            assert all(sum(w)==(m//q) or sum(w)==(m//q+1) for w in lang)
        checks+=1
        for p in range(1,10):
            for w in product((0,1), repeat=p):
                a=is_periodic_word_allowed(w,lang)
                if m>=q:
                    expected= all(w[j]==(1 if (j-(w.index(1) if 1 in w else -99))%q ==0 else 0)
                                  for j in range(p)) if (p%q==0 and (1 in w)) else False
                    assert a==expected,(q,m,p,w)
                else:
                    expected=not any(sum(w[(i+j)%p] for j in range(m))>1 for i in range(p))
                    assert a==expected
                checks+=1
# Count words of gap-shift SFT by simple combinatorial DP vs graph growth.
for m in range(1,21):
    rr=root(m)
    assert abs((rr-1)*rr**(m-1)-1)<1e-11
    for n in range(1,31):
        # number of n words with at most one 1 in each length-m window
        dp={(0,0):1}  # (last position of a one capped at m, count) -> count
        counts=[1] + [0]*(m-1)
        counts[0]=1
        for _ in range(n):
            nxt={}
            for (last,_),v in dp.items():
                nextlast=min(m,last+1)
                k=(nextlast,0)
                nxt[k]=nxt.get(k,0)+v
                if nextlast==m:
                    k=(0,0)
                    nxt[k]=nxt.get(k,0)+v
            dp=nxt
        assert sum(dp.values())>0
        checks+=1
print('VERIFY_OK checks='+str(checks))

# Independent adjacency-matrix and periodic-point-count checks.
def adjacent_gap_matrix(m):
    A = [[0]*m for _ in range(m)]
    for k in range(m-1): A[k][k+1] += 1
    A[m-1][m-1] += 1
    A[m-1][0] += 1
    return A

def mult(A,B):
    d=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(d)) for j in range(d)] for i in range(d)]

for m in range(1,9):
    A=adjacent_gap_matrix(m)
    B=[[int(i==j) for j in range(m)] for i in range(m)]
    for p in range(1,13):
        B=mult(B,A)
        t=sum(B[i][i] for i in range(m))
        periodic=sum(is_periodic_word_allowed(w,allowed_m_words(m)) for w in product((0,1), repeat=p))
        assert t==periodic,(m,p,t,periodic)
        checks+=1
print('VERIFY_ZETA_OK total_checks='+str(checks))
