#!/usr/bin/env python3
"""Exact arithmetic checks for the Dyck-return Walsh convolution theorem.

No external dependencies. Run: python3 dyck_return_verify.py
"""
from math import comb


def catalan(n):
    return comb(2*n, n)//(n+1)


def fine_up_to(N):
    # H=z+z*H^2/(1-2H); equivalently H-z-2H^2+2zH-zH^2=0.
    # Coefficients of z^n for H= sum_{n>=1} f[n-1] z^n.
    h=[0]*(N+1)
    if N>=1: h[1]=1
    for n in range(2,N+1):
        h[n]=sum(2*h[j]*h[n-j] for j in range(1,n))
        if n>=2: h[n]-=2*h[n-1]
        if n>=3: h[n]+=sum(h[j]*h[n-1-j] for j in range(1,n-1))
    return h


def profile_weights(n):
    c=[catalan(j) for j in range(n)]
    out=[]
    for mask in range(1 << max(n-1,0)):
        last=0; value=1
        for j in range(1,n):
            if mask & (1<<(j-1)):
                value*=c[j-last-1];last=j
        value*=c[n-last-1]
        out.append(value)
    return out


def direct_profiles(n):
    counts=[0]*(1<<max(n-1,0))
    def visit(pos,height,mask):
        if pos==2*n:
            assert height==0
            counts[mask]+=1
            return
        if height < 2*n-pos:
            visit(pos+1,height+1,mask)
        if height>0:
            newh=height-1
            newmask=mask
            if newh==0 and pos+1<2*n:
                newmask|=1<<((pos+1)//2-1)
            visit(pos+1,newh,newmask)
    visit(0,0,0)
    return counts


def walsh(vals):
    a=vals[:]; s=1
    while s<len(a):
        for start in range(0,len(a),2*s):
            for j in range(start,start+s):
                x,y=a[j],a[j+s]
                a[j],a[j+s]=x+y,x-y
        s*=2
    return a


def main():
    N=16
    h=fine_up_to(N)
    tests=0
    assert h[:12]==[0,1,0,1,2,6,18,57,186,622,2120,7338];tests+=12
    for n in range(1,N+1):
        weights=profile_weights(n)
        lam=walsh(weights)
        assert sum(weights)==catalan(n);tests+=1
        assert min(lam)==h[n];tests+=1
        assert max(lam)==catalan(n);tests+=1
        if n==2:
            assert lam==[2,0];tests+=1
        elif n>=3:
            assert all(z>0 for z in lam);tests+=len(lam)
        if n<=10:
            via_words=direct_profiles(n)
            for x,y in zip(weights,via_words):
                assert x==y;tests+=1
            via_words_walsh=walsh(via_words)
            for x,y in zip(lam,via_words_walsh):
                assert x==y;tests+=1
        for j in range(n-1):
            # Test exact factorization of character flip (sample all for n<=9).
            if n<=9:
                for freq in range(1<<(n-1)):
                    if freq & (1<<j):
                        continue
                    low=freq&((1<<j)-1)
                    high=(freq>>(j+1))
                    a=walsh(profile_weights(j+1))[low]
                    b=walsh(profile_weights(n-j-1))[high]
                    assert lam[freq]-lam[freq | (1<<j)]==2*a*b
                    tests+=1
    print('PASS',tests,'exact integer assertions; N=',N)

if __name__=='__main__':
    main()
