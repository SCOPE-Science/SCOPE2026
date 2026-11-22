#!/usr/bin/env python3
"""Exact finite checks of the two-step Stern (0,1) gcd law."""
from functools import lru_cache
from math import gcd

@lru_cache(None)
def P(n):
    if n == 0: return (0,)
    if n == 1: return (1,)
    def square_arg(a):
        out = [0] * (2 * len(a) - 1)
        for j, v in enumerate(a): out[2*j] = v
        return out
    if n % 2 == 0:
        q = square_arg(P(n // 2))
    else:
        a = square_arg(P(n // 2))
        b = square_arg(P(n // 2 + 1))
        q = [0] * max(len(a) + 1, len(b))
        for j, c in enumerate(a): q[j+1] += c
        for j, c in enumerate(b): q[j] += c
    while len(q)>1 and q[-1]==0: q.pop()
    return tuple(q)

def R(r):
    d=1<<(r-1)
    return sum(1 << (d - (1 << j)) for j in range(r))

def evaluate(a,t):
    z=0
    for c in a[::-1]: z=z*t+c
    return z

def sylvester_resultant(a,b):
    # Low-to-high arrays; determinant of conventional high-to-low Sylvester matrix.
    a=a[::-1]; b=b[::-1]
    d=len(a)-1; e=len(b)-1
    size=d+e
    m=[]
    for sh in range(e): m.append([0]*sh+list(a)+[0]*(e-1-sh))
    for sh in range(d): m.append([0]*sh+list(b)+[0]*(d-1-sh))
    sign=1; old=1
    for k in range(size-1):
        if m[k][k]==0:
            j=next((j for j in range(k+1,size) if m[j][k]!=0),None)
            if j is None: return 0
            m[k],m[j]=m[j],m[k]; sign=-sign
        piv=m[k][k]
        for i in range(k+1,size):
            v=m[i][k]
            for j in range(k+1,size):
                u=m[i][j]*piv-v*m[k][j]
                assert u%old==0
                m[i][j]=u//old
            m[i][k]=0
        old=piv
    return sign*m[-1][-1]

def gcd_degree_mod_p(a,b,p):
    def trim(u):
        while u and u[-1]%p==0: u.pop()
        return u
    a=trim(list(a)); b=trim(list(b))
    while b:
        inv=pow(b[-1],-1,p)
        while len(a)>=len(b):
            c=(a[-1]*inv)%p; k=len(a)-len(b)
            for j in range(len(b)): a[k+j]=(a[k+j]-c*b[j])%p
            trim(a)
        a,b=b,a
    return len(a)-1

checks=0
for r in range(2,9):
    d=1<<(r-1); n=(1<<r)+1
    a=P(n); b=P(n+2); val=R(r)
    expected=[1 if j in ({0,1}|{1<<i for i in range(1,r)}) else 0 for j in range(d+1)]
    assert list(a)==expected
    rhs=[0]*(len(a)+1)
    for j,c in enumerate(a): rhs[j]+=c; rhs[j+1]+=c
    rhs[1]-=1; rhs[2]-=2
    assert list(b)==rhs
    assert val.bit_count()==r and val%2==1
    assert val==sum((1<<(d-(1<<j))) for j in range(r))
    for t in list(range(-19,97))+[999,10000,1000003]:
        f=evaluate(a,t); g=evaluate(b,t)
        assert gcd(f,g)==gcd(2*t+1,val), (r,t)
        checks+=1
    if r<=5:
        assert sylvester_resultant(a,b)==val, r
        for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]:
            assert (gcd_degree_mod_p(a,b,p)>0)==(val%p==0), (r,p)
            checks+=1
        if r<=4:
            for t in range(val):
                assert gcd(evaluate(a,t),evaluate(b,t))==gcd(2*t+1,val)
                checks+=1
print('VERIFY_OK',checks,'exact finite comparisons; 4 Sylvester determinants; 7 polynomial identities')
