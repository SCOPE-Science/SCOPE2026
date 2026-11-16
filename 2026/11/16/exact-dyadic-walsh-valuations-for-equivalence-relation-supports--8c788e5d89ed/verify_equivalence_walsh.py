#!/usr/bin/env python3
"""Independent integer checks for Fourier congruences on set-partition equivalence vectors.
Run with Python 3.9 or newer: python verify_equivalence_walsh.py
"""
from array import array
from math import comb


def bell(n):
    b=[1]
    for t in range(n):
        b.append(sum(comb(t,j)*b[j] for j in range(t+1)))
    return b


def mul_state(v):
    return [((r*v[r])+v[(r-1)%8])%8 for r in range(8)]


def state_after(n):
    v=[1]+[0]*7
    for _ in range(n):v=mul_state(v)
    return v


def matrix_period_certificate():
    e=[1]+[0]*7
    d=[(a-b)%8 for a,b in zip(state_after(24),e)]
    assert d == [4,0,0,0,4,0,0,0], d
    x=d[:]
    for _ in range(6):
        assert sum(x)%8==0
        x=mul_state(x)
    assert x==d
    # Thus sum(M^(n+24)e0-M^n e0)=0 for every n>=0.
    b=bell(96)
    assert all(b[n+24]%8==b[n]%8 for n in range(73))
    assert [b[i]%8 for i in range(24)] == [
        1,1,2,5,7,4,3,5,4,3,7,2,5,5,2,1,3,4,7,1,4,7,3,2]
    for n in range(2,72):
        for m in range(4):
            residue=(b[n]-2*m*b[n-1]+4*comb(m,2)*b[n-2])%8
            if n%12 in (5,8):
                assert residue==(4 if m%2==0 else (6 if n%12==5 else 2))
            elif n%12==11:
                assert residue==(2 if m%2==0 else 4)
            elif n%12==2:
                assert residue==(2 if m%2==0 else 0)
            else:
                assert residue%2==1


def partition_support(n):
    edges=[(a,b) for a in range(n) for b in range(a+1,n)]
    result=[]
    blocks=[]
    def rec(v):
        if v==n:
            block_of=[-1]*n
            for j,blk in enumerate(blocks):
                for k in blk:block_of[k]=j
            mask=sum((1<<k) for k,(a,b) in enumerate(edges) if block_of[a]==block_of[b])
            result.append(mask)
            return
        for j in range(len(blocks)):
            blocks[j].append(v);rec(v+1);blocks[j].pop()
        blocks.append([v]);rec(v+1);blocks.pop()
    rec(0)
    assert len(set(result))==len(result)
    return result


def walsh_in_place(a):
    width=1
    while width<len(a):
        for start in range(0,len(a),2*width):
            for j in range(start,start+width):
                p,q=a[j],a[j+width]
                a[j],a[j+width]=p+q,p-q
        width*=2


def exhaustive():
    coefficients=0
    B=bell(7)
    for n in range(2,8):
        e=n*(n-1)//2
        a=array('i',[0])*(1<<e)
        positions=partition_support(n)
        assert len(positions)==B[n]
        for mask in positions:a[mask]=1
        walsh_in_place(a)
        bad=0
        min_abs=None
        for freq,w in enumerate(a):
            m=freq.bit_count()
            expected=(B[n]-2*m*B[n-1]+4*comb(m,2)*B[n-2])%8
            assert w%8==expected, (n,freq,w,expected)
            if n>=3:assert w!=0,(n,freq)
            if w==0:bad+=1
            else:min_abs=abs(w) if min_abs is None else min(min_abs,abs(w))
        if n==2:assert bad==1
        elif n%3==2:assert min_abs>=2
        coefficients+=len(a)
        print('n',n,'Bell',len(positions),'coefficients',len(a),'zeros',bad,'minimum_nonzero',min_abs)
    return coefficients


def formula_partition_dp(n,mask):
    # Independently evaluates character sums by a first-block recurrence,
    # without listing partitions or applying any Fourier transform.
    adj=[0]*n;k=0
    for i in range(n):
        for j in range(i+1,n):
            if mask & (1<<k):adj[i]|=1<<j;adj[j]|=1<<i
            k+=1
    M=1<<n
    parity=[0]*M
    for s in range(1,M):
        v=(s&-s).bit_length()-1;t=s&(s-1)
        parity[s]=parity[t]^((adj[v]&t).bit_count()&1)
    f=[0]*M;f[0]=1
    for s in range(1,M):
        first=s&-s;rest=s^first
        t=rest;total=0
        while True:
            block=t|first
            total+=(-1 if parity[block] else 1)*f[s^block]
            if not t:break
            t=(t-1)&rest
        f[s]=total
    return f[-1]


def spot_check():
    # An independently structured recurrence on nontrivial graphs at n=8.
    n=8;B=bell(8);e=n*(n-1)//2
    masks=[0,(1<<e)-1]
    x=123456789
    for _ in range(1024):
        x=(1664525*x+1013904223)&0xffffffff
        masks.append(x&((1<<e)-1))
    for mask in masks:
        val=formula_partition_dp(n,mask)
        m=mask.bit_count()
        assert val%8==(B[n]-2*m*B[n-1]+4*comb(m,2)*B[n-2])%8
        assert val!=0
    return len(masks)


def main():
    matrix_period_certificate()
    count=exhaustive()
    samples=spot_check()
    print('EQUIVALENCE_PARTITION_FOURIER_MOD8_PASS coefficients=',count,'independent_n8_samples=',samples)

if __name__=='__main__':main()
