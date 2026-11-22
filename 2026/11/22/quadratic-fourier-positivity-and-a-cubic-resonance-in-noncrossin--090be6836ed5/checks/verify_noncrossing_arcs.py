#!/usr/bin/env python3
"""Exact, dependency-free reconstruction of noncrossing-partition arc spectra.

All coordinates are unordered pairs (i,j), 1 <= i < j <= n, in lexicographic
order. A partition contributes the edges between consecutive members of each
block. The transform is unnormalized, with signs (-1)^(|S intersect arcs|).
"""
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path
import csv


def catalan(n):
    return comb(2*n,n)//(n+1)


def edges(n):
    return [(i,j) for i in range(1,n+1) for j in range(i+1,n+1)]


def restricted_growth_words(n):
    def recur(a,largest):
        if len(a)==n:
            yield tuple(a)
            return
        for label in range(largest+2):
            yield from recur(a+[label],max(largest,label))
    if n:
        yield from recur([0],0)


def crosses(e,f):
    i,j=e; k,l=f
    return (i<k<j<l) or (k<i<l<j)


def via_partitions(n):
    E=edges(n); lookup={e:i for i,e in enumerate(E)}
    masks=set()
    for word in restricted_growth_words(n):
        blocks={b:[] for b in set(word)}
        for i,b in enumerate(word,1):blocks[b].append(i)
        arcs=[(a,b) for block in blocks.values() for a,b in zip(block,block[1:])]
        if any(crosses(e,f) for e,f in combinations(arcs,2)):
            continue
        mask=sum(1<<lookup[e] for e in arcs)
        assert mask not in masks
        masks.add(mask)
    return masks


def via_arc_subsets(n):
    """Entire Boolean edge cube searched, with only local arc constraints."""
    E=edges(n)
    result=set()
    for m in range(1<<len(E)):
        indeg=set();outdeg=set();selected=[];okay=True
        for t,(i,j) in enumerate(E):
            if m>>t&1:
                if i in outdeg or j in indeg:
                    okay=False;break
                if any(crosses((i,j),other) for other in selected):
                    okay=False;break
                outdeg.add(i);indeg.add(j);selected.append((i,j))
        if okay:result.add(m)
    return result


def walsh_vector(support,dim):
    x=[0]*(1<<dim)
    for m in support:x[m]=1
    for bit in range(dim):
        stride=1<<bit
        for base in range(0,len(x),2*stride):
            for j in range(stride):
                i=base+j
                a,b=x[i],x[i+stride]
                x[i],x[i+stride]=a+b,a-b
    return x


def check(n, expected_zeros, degree_first, degree_first_count):
    E=edges(n); support=via_partitions(n)
    assert len(support)==catalan(n)
    if n<=6:
        independent=via_arc_subsets(n)
        assert support==independent, (n,len(support),len(independent))
    W=walsh_vector(support,len(E))
    assert W[0]==catalan(n)
    assert sum(a*a for a in W)==(1<<len(E))*len(support)
    assert all((a-catalan(n))%2==0 for a in W)
    zeros=[s for s,w in enumerate(W) if w==0]
    hist=Counter(s.bit_count() for s in zeros)
    assert len(zeros)==expected_zeros
    assert (min(hist) if hist else None)==degree_first
    if degree_first is not None:assert hist[degree_first]==degree_first_count
    if n==6:
        # Independent direct signed sums for every one of the 32768 characters.
        for s,w in enumerate(W):
            direct=sum(-1 if (s&u).bit_count()%2 else 1 for u in support)
            assert w==direct,(s,w,direct)
        assert all(w>0 for s,w in enumerate(W) if s.bit_count()<=2)
        assert min(abs(w) for w in W if w)==4
        assert hist=={3:25,4:95,5:366,6:960,7:1610,8:1830,
                      9:1785,10:1362,11:720,12:255,13:65,14:10,15:1}
        assert W[7]==0  # arcs (1,2), (1,3), (1,4)
        assert W[106]==-4  # arcs (1,3), (1,5), (2,3), (2,4)
        # The accompanying finite certificate lists exactly all cubic zeros.
        zero_cubic = {tuple(v for t in range(len(E)) for v in E[t]
                            if (mask>>t)&1)
                      for mask in zeros if mask.bit_count()==3}
        with Path(__file__).with_name('cubic_zeros_n6.csv').open(newline='') as fin:
            reader=csv.reader(fin)
            assert next(reader)==['i1','j1','i2','j2','i3','j3']
            recorded={tuple(map(int,row)) for row in reader}
        assert len(recorded)==25 and recorded==zero_cubic
        # Every coefficient is a multiple of four.
        assert all(w%4==0 for w in W)
    if n==5:
        assert all(w>0 for s,w in enumerate(W) if s.bit_count()<=2)
    print('n=',n,'partitions=',len(support),'frequencies=',len(W),
          'zeros=',len(zeros),'rank=',len(W)-len(zeros),
          'degree_zeros=',dict(sorted(hist.items())))


if __name__=='__main__':
    check(2,1,1,1)
    check(3,0,None,0)
    check(4,20,2,6)
    check(5,164,4,16)
    check(6,9084,3,25)
    # Odd Catalan cardinality makes every signed coefficient odd.
    assert catalan(7)==429
    print('All exact checks passed.')
