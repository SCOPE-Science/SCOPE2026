#!/usr/bin/env python3
"""Independent exact radix-3 Fourier verification of proper K_{m,n} ternary colorings.

Run with Python 3; no third-party dependencies. Entries use the integer pair
(a,b) for a+b*omega, where omega^2+omega+1=0.
"""
from math import comb

def omega(z):
    a,b = z
    return -b,a-b

def omega2(z):
    a,b = z
    return b-a,-a

def add(*zs):
    return sum(x for x,y in zs),sum(y for x,y in zs)

def transform(m,n):
    d=m+n
    N=3**d
    arr=[]
    for k in range(N):
        t=k
        a=[]
        for _ in range(d):
            a.append(t%3);t//=3
        good=all(a[i]!=a[j] for i in range(m) for j in range(m,d))
        arr.append((int(good),0))
    step=1
    for _ in range(d):
        for first in range(0,N,3*step):
            for j in range(step):
                i=first+j
                a,b,c=arr[i],arr[i+step],arr[i+2*step]
                arr[i]=add(a,b,c)
                arr[i+step]=add(a,omega(b),omega2(c))
                arr[i+2*step]=add(a,omega2(b),omega(c))
        step*=3
    return arr

def predicted(m,n,freq):
    alpha,beta=freq[:m],freq[m:]
    ta,tb=alpha.count(0),beta.count(0)
    za=(-1)**(m-ta)*2**ta
    zb=(-1)**(n-tb)*2**tb
    sa,sb=sum(alpha)%3,sum(beta)%3
    return 3*(int((sa+sb)%3==0)*(za+zb+1)-3*int(sa==sb==0))

def extra(m,n):
    if m%2 or n%2:
        return 0
    U=lambda r:(2**r+2)//3
    V=lambda r:(2**r-1)//3
    B=lambda r:r*(2**(r-1)-2)//3
    D=lambda r:r*(2**(r-1)+1)//3
    E=lambda r:comb(r,2)*(2**(r-2)+2)//3
    return U(m)*U(n)+E(m)*B(n)+B(m)*E(n)+2*(V(m)*D(n)+D(m)*V(n))

def check(m,n):
    out=transform(m,n)
    d=m+n
    pos=[]
    for k,val in enumerate(out):
        t=k; freq=[]
        for _ in range(d):
            freq.append(t%3);t//=3
        w=predicted(m,n,freq)
        assert val==(w,0), ('multiplier',m,n,k,val,w)
        if w:pos.append(abs(w))
    rank=3**(d-1)-extra(m,n)
    minpos=9 if m%2==n%2==0 else 3
    maxpos=3*(2**m+2**n-2)
    assert len(pos)==rank,(m,n,'rank',len(pos),rank)
    assert min(pos)==minpos,(m,n,'min',min(pos),minpos)
    assert max(pos)==maxpos,(m,n,'max',max(pos),maxpos)
    return m,n,rank,3**d-rank,minpos,maxpos

if __name__=='__main__':
    cases=0
    for m in range(1,7):
        for n in range(1,7):
            if m+n>9:continue
            result=check(m,n)
            print('m={} n={} rank={} nullity={} gap={} max={}'.format(*result))
            cases+=1
    print('VERIFY_OK cases={} exact full DFT m+n<=9'.format(cases))
