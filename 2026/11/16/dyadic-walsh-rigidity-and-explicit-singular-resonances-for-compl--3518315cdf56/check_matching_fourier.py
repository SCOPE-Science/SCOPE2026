#!/usr/bin/env python3
"""Exact checks for signed matching Walsh arithmetic. Requires Python 3 and NumPy."""
import itertools
from functools import lru_cache
import numpy as np


def involution_counts(N):
    out = [1, 1]
    for n in range(2, N + 1):
        out.append(out[n-1] + (n-1)*out[n-2])
    return out


def valuation(n):
    return (n & -n).bit_length()-1


def edges(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]


def matching_masks(n):
    ed = edges(n)
    lookup={e:i for i,e in enumerate(ed)}
    @lru_cache(None)
    def rec(vs):
        if not vs:
            return (0,)
        a=vs[0]
        ret=list(rec(vs[1:]))
        for idx,b in enumerate(vs[1:]):
            ebit=1<<lookup[(a,b)]
            leftover=vs[1:idx+1]+vs[idx+2:]
            ret += [k|ebit for k in rec(leftover)]
        return tuple(ret)
    return rec(tuple(range(n)))


def fwht_coefficients(n):
    count=1<<len(edges(n))
    a=np.zeros(count,dtype=np.int64)
    ms=matching_masks(n)
    a[list(ms)]=1
    for j in range(len(edges(n))):
        size=1<<j
        view=a.reshape(-1,2,size)
        left=view[:,0,:].copy()
        right=view[:,1,:].copy()
        view[:,0,:]=left+right
        view[:,1,:]=left-right
    return a, len(ms)


def alpha(n):
    q,r=divmod(n,4)
    return q+(r>=2)


def direct_signed_matching(n, H):
    ed=edges(n)
    neg=set(H)
    signs={(a,b): (-1 if (a,b) in neg else 1) for a,b in ed}
    @lru_cache(None)
    def rec(vs):
        if not vs:
            return 1
        a=vs[0]
        total=rec(vs[1:])
        for i,b in enumerate(vs[1:]):
            total+=signs[(a,b)]*rec(vs[1:i+1]+vs[i+2:])
        return total
    return rec(tuple(range(n)))


def coefficient_via_matching_number(n,H,I):
    neg=set(H)
    @lru_cache(None)
    def rec(vs):
        if not vs:
            return (1,)
        a=vs[0]
        arr=list(rec(vs[1:]))
        for i,b in enumerate(vs[1:]):
            if (a,b) in neg:
                sub=rec(vs[1:i+1]+vs[i+2:])
                if len(arr)<len(sub)+1:
                    arr.extend([0]*(len(sub)+1-len(arr)))
                for j,c in enumerate(sub):arr[j+1]+=c
        return tuple(arr)
    return sum((-2)**k*v*I[n-2*k] for k,v in enumerate(rec(tuple(range(n)))))


def square_witness(s):
    n=s*s+2
    r=n-2
    plus=(r+s)//2
    ts=[1]*plus+[-1]*(r-plus)
    H={(0,1)}
    for k,t in enumerate(ts,2):
        if t==-1:H.add((0,k))
        if t==1:H.add((1,k))
    return n,H


def check():
    I=involution_counts(70)
    for n in range(2,71):
        q,r=divmod(n,4)
        target=q+([0,0,1,2][r])
        assert valuation(I[n])==target,(n,I[n])
    count_checked=0
    total_zeros={}
    for n in range(2,8):
        coeff,num=fwht_coefficients(n)
        assert num==I[n]
        a=alpha(n)
        normalized=coeff//(1<<a)
        assert np.all(coeff % (1<<a)==0)
        even_edge_count=np.fromiter((i.bit_count()%2 for i in range(len(coeff))), dtype=np.int8,count=len(coeff))
        r=n%4
        expected= np.full(len(coeff),1,dtype=np.int8) if r in (0,1) else (1-even_edge_count if r==2 else even_edge_count)
        assert np.array_equal(normalized%2, expected), n
        assert np.any(normalized%2==1)
        if n%4 in (0,1):assert np.all(coeff!=0)
        if n%4 in (2,3):assert np.count_nonzero(coeff)>=len(coeff)//2
        zeros=int(np.count_nonzero(coeff==0))
        total_zeros[n]=zeros
        if n<=6:
            # Disjoint-set inclusion-exclusion is independent of the FWHT implementation.
            for h in range(len(coeff)):
                H={e for j,e in enumerate(edges(n)) if h>>j&1}
                assert coefficient_via_matching_number(n,H,I)==int(coeff[h]),(n,h)
        else:
            for h in [0,1,2,3,17,67,251,994,1777,91001,1000001,2097151]:
                H={e for j,e in enumerate(edges(n)) if h>>j&1}
                assert coefficient_via_matching_number(n,H,I)==int(coeff[h]),(n,h)
        count_checked+=len(coeff)
        print(f'n={n} matchings={num} frequencies={len(coeff)} zeros={zeros} 2_content={1<<a}')
    for s in range(1,5):
        n,H=square_witness(s)
        assert len(H)==(n-1)
        coeff=direct_signed_matching(n,H)
        assert coeff==0, (n,coeff)
        print(f'square_witness n={n} value={coeff}')
    assert total_zeros[6]==6825 and total_zeros[7]==269577
    print(f'ALL_MATCHING_WALSH_DYADIC_PASS frequencies={count_checked} n6_zeros=6825 n7_zeros=269577')

if __name__=='__main__':check()
