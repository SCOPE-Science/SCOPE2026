#!/usr/bin/env python3
"""Exact arithmetic checks for trace-sliced binary invertible-matrix convolution.
Runs with Python 3 standard library; matrix-space dimensions n=1,2,3,4.
No floating-point arithmetic occurs in any finite rank/spectrum check.
"""
from math import prod

def qbin(n,k):
    if not 0 <= k <= n:return 0
    return prod(2**(n-j)-1 for j in range(k))//prod(2**(k-j)-1 for j in range(k))

def mixed(n,k,l):
    if k+l>n:return 0
    return qbin(n,k)*qbin(n-k,l)*2**(k*l+n*(n-k-l))

def joint(n,u,v):
    return sum((-1)**(k-u+l-v)*2**((k-u)*(k-u-1)//2+(l-v)*(l-v-1)//2)
               *qbin(k,u)*qbin(l,v)*mixed(n,k,l)
               for k in range(u,n+1) for l in range(v,n-k+1))

def rnk(a,n):
    rows=[(a>>(i*n))&((1<<n)-1) for i in range(n)]
    r=0
    for i in range(n):
        pivot=next((j for j in range(r,n) if (rows[j]>>i)&1),None)
        if pivot is None:continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        for j in range(n):
            if j!=r and ((rows[j]>>i)&1):rows[j]^=rows[r]
        r+=1
    return r

def wht(a):
    n=len(a);h=1
    while h<n:
        for b in range(0,n,2*h):
            for j in range(b,b+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2

def fg(n,r):
    return (-1)**r*2**(n*(n-1)//2)*prod(2**i-1 for i in range(1,n-r+1))

def run(n):
    l=1<<(n*n)
    I=sum(1<<(i*n+i) for i in range(n))
    even=[0]*l;odd=[0]*l
    obs={}
    for a in range(l):
        r=rnk(a,n)
        s=rnk(a^I,n)
        uv=(n-r,n-s)
        obs[uv]=obs.get(uv,0)+1
        if r==n:
            if (a&I).bit_count()%2:odd[a]=1
            else:even[a]=1
    for u in range(n+1):
        for v in range(n+1-u):
            assert obs.get((u,v),0)==joint(n,u,v),(n,u,v)
    assert sum(obs.values())==l
    wht(even);wht(odd)
    for a in range(l):
        r,s=rnk(a,n),rnk(a^I,n)
        assert 2*even[a]==fg(n,r)+fg(n,s)
        assert 2*odd[a]==fg(n,r)-fg(n,s)
        assert (even[a]==0)==((n-r,n-s) in ((0,1),(1,0)))
        assert (odd[a]==0)==(r==s)
    e0=even.count(0);o0=odd.count(0)
    assert e0==2*joint(n,0,1)
    assert o0==sum(joint(n,k,k) for k in range(n//2+1))
    return e0,o0,sum(1 for v in even if v<0),sum(1 for v in odd if v<0)

if __name__=='__main__':
    for n in (1,2,3,4):
        print('n=%d even_nullity=%d odd_nullity=%d negative_even_modes=%d negative_odd_modes=%d'%((n,)+run(n)))
    print('TRACE_SLICE_BINARY_GL_EXACT_CHECKS_OK')
