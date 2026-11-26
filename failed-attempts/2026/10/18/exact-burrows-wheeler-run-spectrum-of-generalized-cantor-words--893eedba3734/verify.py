#!/usr/bin/env python3
"""Reproducible finite checks of the base-uniform Cantor-word BWT theorem."""
from collections import defaultdict
from itertools import groupby


def by_substitution(base, depth):
    w = '1'
    for _ in range(depth):
        w = ''.join('1'+'0'*(base-2)+'1' if c == '1' else '0'*base for c in w)
    return w


def by_digit_criterion(base, depth):
    out = []
    for n in range(base**depth):
        m=n
        good=True
        while m:
            m,d=divmod(m,base)
            if d!=0 and d!=base-1:
                good=False
                break
        out.append('1' if good else '0')
    return ''.join(out)


def cyclic_sa_doubling(w):
    n=len(w)
    if n==1:return [0]
    rank=[ord(c)-48 for c in w]
    step=1
    while step<n:
        pos=sorted(range(n),key=lambda i:(rank[i],rank[(i+step)%n]))
        new=[0]*n
        distinct=0
        for i,j in zip(pos,pos[1:]):
            if (rank[i],rank[(i+step)%n]) != (rank[j],rank[(j+step)%n]):
                distinct+=1
            new[j]=distinct
        rank=new
        if distinct==n-1:break
        step*=2
    assert len(set(rank))==n
    return sorted(range(n),key=rank.__getitem__)


def cyclic_sa_direct(w):
    return sorted(range(len(w)),key=lambda i:w[i:]+w[:i])


def ordered_gap_groups(base,depth,w,sa):
    m=len(w); groups=defaultdict(list)
    hh=[0]*m
    count=0
    for i in range(2*m-1,-1,-1):
        if w[i%m]=='0':count+=1
        else:count=0
        if i<m:hh[i]=count
    for i in sa:
        if w[i]=='0':
            groups[hh[i]].append(w[(i-1)%m])
    for h,seq in groups.items():
        eligible=[j for j in range(depth) if h==(base-2)*base**j]
        if eligible:
            j=eligible[0]; a=2**(depth-j-1)-1
            assert ''.join(seq)=='1'*a+'0'*a+'1',(base,depth,h,''.join(seq))
        else:
            assert all(ch=='0' for ch in seq)
    return ''.join(''.join(groups[h]) for h in sorted(groups,reverse=True))


def verify_one(base,k,independent=False):
    w=by_substitution(base,k)
    assert w==by_digit_criterion(base,k)
    sa=cyclic_sa_doubling(w)
    if independent:assert sa==cyclic_sa_direct(w)
    bwt=''.join(w[(i-1)%len(w)] for i in sa)
    runs=len(list(groupby(bwt)))
    ones= [len(list(g)) for c,g in groupby(bwt) if c=='1']
    if k>=2:
        assert runs==4*k,(base,k,runs)
        assert ones==[1]+[v for t in range(1,k) for v in (2**t-1,1)]+[1]
        assert bwt[0]=='1' and bwt[-1]=='0'
        assert len(list(groupby(w)))==2**(k+1)-1
    zpart=bwt[:len(w)-w.count('1')]; opart=bwt[len(w)-w.count('1'):]
    assert ordered_gap_groups(base,k,w,sa)==zpart
    assert opart.count('1')==1
    if k>=2:assert opart[0]=='0' and opart[-1]=='0'
    return (len(w),runs)


def main():
    cases=0;independently_sorted=0;maxlen=0
    for base in range(3,10):
        for k in range(1,12):
            n=base**k
            if n>60000:break
            independently=(n<=2187)
            verify_one(base,k,independently)
            independently_sorted+=independently
            cases+=1;maxlen=max(maxlen,n)
    print('VERIFY_OK generalized_Cantor_BWT base=3..9 k>=2 exact_4k cases=%s direct_rotation_sort_cases=%s independent_digit_generator_and_gap_partition max_word_length=%s'%(cases,independently_sorted,maxlen))

if __name__=='__main__':main()
