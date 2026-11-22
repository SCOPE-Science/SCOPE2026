#!/usr/bin/env python3
"""Exact Walsh and endpoint-projection checks for connected vertex-set codebooks of complete split graphs."""
from math import comb
from fractions import Fraction

def fwht(a):
    a=list(a)
    span=1
    while span<len(a):
        for off in range(0,len(a),span*2):
            for k in range(span):
                u,v=a[off+k],a[off+span+k]
                a[off+k],a[off+span+k]=u+v,u-v
        span*=2
    return a

def connected_split(s,m,mask):
    core=mask&((1<<s)-1)
    leaves=(mask>>s)
    return (core !=0) or (leaves.bit_count()==1)

def expected(s,m,mask):
    t=(mask&((1<<s)-1)).bit_count()
    k=(mask>>s).bit_count()
    return (m-2*k) + ((2**s if t==0 else 0)-1)*(2**m if k==0 else 0)

def kr(n,r,x):
    return sum((-1)**j * comb(x,j)*comb(n-x,r-j) for j in range(r+1) if j<=x and 0<=r-j<=n-x)

def main():
    seen=0
    for s in range(1,5):
        for m in range(2,11):
            if s+m>13:continue
            N=1<<(s+m)
            f=[int(bool(mask) and connected_split(s,m,mask)) for mask in range(N)]
            W=fwht(f)
            assert sum(f)==m+(2**s-1)*2**m
            assert all(w==expected(s,m,k) for k,w in enumerate(W)),(s,m)
            zero=sum(w==0 for w in W)
            assert zero==( (2**s)*comb(m,m//2) if m%2==0 else 0 ),(s,m,zero)
            assert min(abs(w) for w in W if w)==(2 if m%2==0 else 1)
            if m%2==0:
                spectrum=[int(w!=0) for w in W]
                kernel=fwht(spectrum)
                norm=Fraction(sum(map(abs,kernel)),N)
                r=m//2
                target=Fraction(1)+Fraction(comb(m,r),2**r)-Fraction(2*comb(m,r),2**m)
                assert norm==target,(s,m,norm,target)
                assert all(kernel[j]==0 for j in range(N) if (j&((1<<s)-1)))
            seen+=N
    for r in range(1,17):
        n=2*r
        cm=comb(n,r)
        for x in range(n+1):
            k=kr(n,r,x)
            assert k==0 if x%2 else Fraction(k)==Fraction((-1)**(x//2)*cm*comb(r,x//2),comb(n,x))
        assert sum(comb(n,x)*abs(kr(n,r,x)) for x in range(n+1))==2**r*cm
    print(f'PASSED: {seen} complete characters across 4 core sizes and 2..10 leaf sizes; 16 symbolic central-Krawtchouk checks')
    for s,m in [(1,4),(2,4),(1,6),(3,6),(1,8),(4,8)]:
        N=1<<(s+m)
        z=2**s*comb(m,m//2)
        r=m//2
        v=Fraction(1)+Fraction(comb(m,r),2**r)-Fraction(2*comb(m,r),2**m)
        print(f's={s} m={m} rank={N-z} nullity={z} opt_norm={v}')
if __name__=='__main__':main()
