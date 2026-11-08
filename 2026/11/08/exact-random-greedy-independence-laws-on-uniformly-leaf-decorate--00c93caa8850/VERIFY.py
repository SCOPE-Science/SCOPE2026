"""Standalone exact checks for the decorated-path random greedy independent-set law.
Run with: python3 VERIFY.py
No external modules required.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial


def plus(a,b,mult=1):
    out=a.copy()
    for k,x in b.items():out[k]=out.get(k,Q(0))+mult*x
    return {k:v for k,v in out.items() if v}


def product(a,b):
    out={}
    for k,v in a.items():
        for j,w in b.items():out[k+j]=out.get(k+j,Q(0))+v*w
    return out


def shift(a,k):return {i+k:x for i,x in a.items()}


def family(n,q):
    ans=[{0:Q(1)}]
    for m in range(1,n+1):
        out={}
        for i in range(1,m+1):
            out=plus(out,shift(product(ans[i-1],ans[m-i]),q),q)
            left=max(i-2,0);right=max(m-i-1,0)
            out=plus(out,shift(product(ans[left],ans[right]),1+q*(i>1)+q*(i<m)))
        ans.append({k:v/((q+1)*m) for k,v in out.items()})
    return ans


def direct(n,q):
    """Independent arbitrary-graph recursion by first still-available vertex."""
    nn=n*(q+1); closed=[1<<i for i in range(nn)]
    for i in range(n):
        u=i*(q+1)
        for j in range(1,q+1):
            v=u+j;closed[u]|=1<<v;closed[v]|=1<<u
        if i+1<n:
            v=(i+1)*(q+1);closed[u]|=1<<v;closed[v]|=1<<u
    @lru_cache(None)
    def polynomial(mask):
        if not mask:return {0:Q(1)}
        value={};bits=mask
        while bits:
            bit=bits&-bits;bits-=bit;vertex=bit.bit_length()-1
            value=plus(value,shift(polynomial(mask&~closed[vertex]),1))
        return {k:v/mask.bit_count() for k,v in value.items()}
    return polynomial((1<<nn)-1)


def expected_core(n,q):
    a=Q(1,q+1)
    return sum((n-j)*(-2)**j*a**(j+1)/factorial(j+1) for j in range(n))


def run():
    assertions=0
    for q in range(1,7):
        polys=family(17,q)
        for n in range(1,18):
            P=polys[n]
            assert sum(P.values())==1;assert all(p>0 for p in P.values());assert all(0<=x<=q*n for x in P)
            assertions+=3
            if q==1: assert P=={n:Q(1)}
            else: assert set(P)=={q*n-(q-1)*k for k in range((n+1)//2+1)}
            assertions+=1
            if q>=2: assert P[q*n]==Q(q,q+1)**n
            assertions+=1
            mean=sum(k*p for k,p in P.items())
            assert mean==q*n-(q-1)*expected_core(n,q); assertions+=1
            # Check every u-coefficient of the Riccati equation independently.
            r={}
            for j in range(n):
                r=plus(r,shift(product(polys[j],polys[n-1-j]),q),q)
            if n==1:r=plus(r,{1:Q(1)})
            if n>=2:r=plus(r,shift(polys[n-2],q+1),2)
            if n>=3:
                for j in range(n-2):
                    r=plus(r,shift(product(polys[j],polys[n-3-j]),2*q+1))
            assert {k:v for k,v in r.items() if v}=={k:v*((q+1)*n) for k,v in P.items()}; assertions+=1
            if n*(q+1)<=16:
                assert P==direct(n,q); assertions+=1
    print('VERIFY_OK',assertions,'exact checks')

if __name__=='__main__':run()
