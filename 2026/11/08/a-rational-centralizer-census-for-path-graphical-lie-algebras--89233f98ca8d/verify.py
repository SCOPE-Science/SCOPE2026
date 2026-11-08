#!/usr/bin/env python3
"""Independent exact enumeration of centralizer subspaces for path graph Lie algebras."""
from collections import defaultdict
from itertools import product

def add(a,b,q): return (a^b) if q==4 else (a+b)%q
def neg(a,q): return a if q==4 else (-a)%q
def mul(a,b,q):
    if q!=4:return (a*b)%q
    x=0
    while b:
        if b&1:x^=a
        a<<=1
        if a&4:a^=7
        b>>=1
    return x

def inv(a,q):
    for b in range(1,q):
        if mul(a,b,q)==1:return b
    raise ValueError(a)

def rref(rows,q):
    if not rows:return ()
    x=[row[:] for row in rows];m=len(x);n=len(x[0]);r=0
    for col in range(n):
        piv=next((j for j in range(r,m) if x[j][col]),None)
        if piv is None:continue
        x[r],x[piv]=x[piv],x[r]
        z=inv(x[r][col],q)
        x[r]=[mul(v,z,q) for v in x[r]]
        for k in range(m):
            if k!=r and x[k][col]:
                fac=neg(x[k][col],q)
                x[k]=[add(a,mul(fac,b,q),q) for a,b in zip(x[k],x[r])]
        r+=1
        if r==m:break
    return tuple(tuple(v) for v in x[:r])

def direct(n,q):
    distinct=set()
    for a in product(range(q),repeat=n):
        rows=[]
        for i in range(n-1):
            row=[0]*n
            row[i]=neg(a[i+1],q);row[i+1]=a[i]
            rows.append(row)
        distinct.add(rref(rows,q))
    return len(distinct)

def descriptor(n,q):
    d={}
    for s in range(1<<n):
        B=Z=0;i=0;weight_exp=0
        while i<n:
            if s>>i&1:
                j=i
                while j<n and (s>>j&1):j+=1
                if j-i>=2:
                    B|=((1<<(j-i))-1)<<i
                    weight_exp+=j-i-1
                i=j
            else:
                if (i and s>>(i-1)&1) or (i+1<n and s>>(i+1)&1):Z|=1<<i
                i+=1
        if (B,Z) in d:assert d[B,Z]==weight_exp
        d[B,Z]=weight_exp
    return sum((q-1)**k for k in d.values())

def predicted(n,q):
    b=[]
    N={0:1,1:1-q,2:q,3:-q,4:1}
    for i in range(n+1):
        prev=lambda j:b[j] if 0<=j<len(b) else 0
        b.append(N.get(i,0)+q*prev(i-1)-(q-2)*prev(i-2)-prev(i-4)+prev(i-5))
    return b[n]

def main():
    checked=0
    for q,maxn in [(2,8),(3,7),(4,6),(5,5)]:
        for n in range(0,maxn+1):
            a=predicted(n,q)
            assert a==descriptor(n,q),(q,n,a,descriptor(n,q))
            if n<=maxn:
                c=direct(n,q)
                assert a==c,(q,n,a,c)
            checked+=1
    for q in (2,3,4,5,7,11):
        for n in range(18):
            assert predicted(n,q)==descriptor(n,q),(q,n)
    print('VERIFY_OK',checked,'independent finite-field centralizer censuses and symbolic-descriptor checks')
if __name__=='__main__':main()
