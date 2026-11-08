#!/usr/bin/env python3
"""Check exact Walsh spectrum of spanning-tree incidence vectors of K_{2,n}."""
from math import comb
from collections import Counter

def trees(n):
    for j in range(n):
        others=[i for i in range(n) if i != j]
        for choices in range(1<<(n-1)):
            mask=(3<<(2*j))
            for k,i in enumerate(others):
                mask |= 1 << (2*i+((choices>>k)&1))
            yield mask

def fwht(a):
    step=1
    while step<len(a):
        for offset in range(0,len(a),2*step):
            for k in range(offset,offset+step):
                u,v=a[k],a[k+step]
                a[k],a[k+step]=u+v,u-v
        step*=2
    return a

def theory(n):
    h=Counter()
    h[0]=(1<<n)*((1<<n)-n-1)
    h[1<<(n-1)]+=n*(1<<n)
    for j in range(n+1):
        h[(1<<(n-1))*abs(n-2*j)] += comb(n,j)
    return h

for n in range(2,9):
    counts=Counter(trees(n))
    assert len(counts)==n*(1<<(n-1)) and set(counts.values())=={1}
    signal=[0]*(1<<(2*n))
    for t in counts:signal[t]=1
    spectrum=fwht(signal)
    h=Counter(map(abs,spectrum)); pred=theory(n)
    assert h==pred,(n,h,pred)
    assert spectrum[0]==n*(1<<(n-1))
    norm_num=sum(abs(v) for v in spectrum)
    num= n*(1<<(2*n-1)) + n*comb(n-1,(n-1)//2)*(1<<n)
    assert norm_num==num,(n,norm_num,num)
    support=(n+1)*(1<<n) - (comb(n,n//2) if n%2==0 else 0)
    assert sum(c for k,c in h.items() if k>0)==support
    assert sum(v*v for v in spectrum)==(1<<(2*n))*len(counts)
    print('n',n,'total_trees',len(counts),'nonzero',support,'spectral_norm',f'{norm_num}/{1<<(2*n)}','levels',sorted(h.items()))
print('THETA_K2N_FULL_FOURIER_CERTIFICATE_PASS')
