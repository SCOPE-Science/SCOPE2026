"""Exact finite checks for spanning-tree Walsh spectra of complete split graphs.

Requires Python 3 standard library only. General statements are proved separately;
finite enumeration is a consistency check, not an infinite proof.
"""
from itertools import product
from collections import Counter
from math import comb
from heapq import heapify, heappop, heappush
from random import Random

CHECKS = 0

def eq(a, b):
    global CHECKS
    CHECKS += 1
    assert a == b, (a, b)

def graph_edges(m, n):
    return [(i, j) for i in range(m) for j in range(i+1, m)] + [
        (i, j) for j in range(m, m+n) for i in range(m)]

def bareiss(a):
    a = [list(row) for row in a]
    q = len(a)
    if q == 0:
        return 1
    sign = 1
    prior = 1
    for k in range(q-1):
        if not a[k][k]:
            p = next((i for i in range(k+1,q) if a[i][k]), None)
            if p is None:
                return 0
            a[k], a[p] = a[p], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, q):
            for j in range(k+1, q):
                num = a[i][j]*pivot - a[i][k]*a[k][j]
                assert num % prior == 0
                a[i][j] = num // prior
        for i in range(k+1,q):
            a[i][k] = 0
        prior = pivot
    return sign*a[-1][-1]

def signed_tree_sum(m,n,signs):
    edges = graph_edges(m,n)
    eq(len(edges),len(signs))
    size = m+n
    root = m-1  # a core vertex
    indices = [i for i in range(size) if i != root]
    loc = {v:k for k,v in enumerate(indices)}
    a = [[0]*(size-1) for _ in range(size-1)]
    for (u,v),s in zip(edges,signs):
        if u != root:a[loc[u]][loc[u]] += s
        if v != root:a[loc[v]][loc[v]] += s
        if u != root and v != root:
            a[loc[u]][loc[v]] -= s
            a[loc[v]][loc[u]] -= s
    return bareiss(a)

def tree_prufer(word, size):
    d = [1]*size
    for x in word:d[x] += 1
    leaves = [i for i in range(size) if d[i]==1]
    heapify(leaves)
    result = []
    for x in word:
        leaf = heappop(leaves)
        result.append(tuple(sorted((leaf,x))))
        d[leaf]-=1
        d[x]-=1
        if d[x] == 1:heappush(leaves,x)
    result.append(tuple(sorted(leaves)))
    return result

def support(m,n):
    size=m+n
    es=graph_edges(m,n)
    dic={e:i for i,e in enumerate(es)}
    counts=[0]*(1<<len(es))
    for seq in product(range(size),repeat=size-2):
        tree=tree_prufer(seq,size)
        if any(e not in dic for e in tree):continue
        mask=sum(1<<dic[e] for e in tree)
        counts[mask]+=1
    eq(sum(counts), (m+n)**(m-1)*m**(n-1))
    eq(max(counts),1)
    return counts

def fwht(a):
    a=a[:]
    h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def signs_from_mask(e, mask):
    return tuple(-1 if (mask>>i)&1 else 1 for i in range(e))

def check_full(m,n):
    es=graph_edges(m,n)
    walsh=fwht(support(m,n))
    zeros=0; minval=None
    for mask,t in enumerate(walsh):
        signs=signs_from_mask(len(es),mask)
        eq(t,signed_tree_sum(m,n,signs))
        eq(t%2,((m+n)**(m-1)*m**(n-1))%2)
        if (m%2==1 and n%2==1):eq(t%(1<<(m-1)),0)
        zeros+=(t==0)
        if t: minval=abs(t) if minval is None else min(minval,abs(t))
    if n%2==0:
        eq(zeros,0)
        if m==3:eq(minval,1)
    else:
        assert zeros>0
    if (m,n)==(3,1):eq(zeros,30)
    if (m,n)==(3,3):eq(zeros,1088)
    if m==3 and n%2==1:eq(minval,4)
    if (m,n)==(5,1):eq(minval,16)
    print('full m=%d n=%d edge=%d trees=%d zero=%d minabs=%d'%(m,n,len(es),sum(support(m,n)),zeros,minval))

def odd_seed(m):
    p=(m+1)//2
    core=[1]*comb(m,2)
    leaf=[1]*p+[-1]*(m-p)
    return tuple(core+leaf)

def pair(signs,m,vec):
    assert len(vec)==m and all(abs(x)==1 for x in vec)
    return signs+tuple(vec)+tuple(-x for x in vec)

def even_three_seed():
    m=3
    return tuple([1,1,1]+[1,1,-1]+[1,-1,1])

for m,n in [(3,1),(3,2),(3,3),(3,4),(5,1)]:
    check_full(m,n)
for m in [3,5,7,9]:
    start=odd_seed(m)
    eq(signed_tree_sum(m,1,start),0)
    signs=start
    for k in range(1,4):
        vec=tuple(1 if i<k%m+1 else -1 for i in range(m))
        signs=pair(signs,m,vec)
        eq(signed_tree_sum(m,2*k+1,signs),0)
    if m==3:
        s=even_three_seed()
        eq(signed_tree_sum(m,2,s),-1)
        for k in range(1,4):
            s=pair(s,m,(1,1,-1))
            eq(abs(signed_tree_sum(m,2+2*k,s)),1)
        s=(1,1,1,1,-1,-1)
        eq(abs(signed_tree_sum(m,1,s)),4)
        for k in range(1,4):
            s=pair(s,m,(1,1,-1))
            eq(abs(signed_tree_sum(m,1+2*k,s)),4)
rng=Random(91903)
for m in [3,5,7]:
    for n in [1,2,3]:
        for trial in range(15):
            s=tuple(rng.choice((-1,1)) for _ in graph_edges(m,n))
            v=tuple(rng.choice((-1,1)) for _ in range(m))
            d=sum(v)
            eq(signed_tree_sum(m,n+2,pair(s,m,v)),-d*d*signed_tree_sum(m,n,s))
print('PASS exact integer checks:',CHECKS)
