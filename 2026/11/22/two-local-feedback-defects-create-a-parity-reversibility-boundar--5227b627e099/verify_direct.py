#!/usr/bin/env python3
"""Independent bit-matrix checks of the cyclic two-defect update and all-period ranks."""
from verify_transfer import smith, kernel_dim_period, pmul

def mul(A,B,n):
    out=[]
    for row in A:
        z=0
        while row:
            v=(row&-row).bit_length()-1
            z^=B[v];row&=row-1
        out.append(z)
    return out

def rank(A,n):
    a=A[:];r=0
    for c in range(n):
        j=next((j for j in range(r,n) if (a[j]>>c)&1),None)
        if j is None:continue
        a[r],a[j]=a[j],a[r]
        for k in range(n):
            if k!=r and (a[k]>>c)&1:a[k]^=a[r]
        r+=1
    return r

def matrix(n,d):
    return [(1<<((i-1)%n))^(1<<((i+1)%n))^((1<<i) if i==0 or i==d else 0) for i in range(n)]

def direct(n,d,k,m):
    A=matrix(n,d);I=[1<<i for i in range(n)]
    powers=[I]
    for i in range(k+m):powers.append(mul(powers[-1],A,n))
    B=[powers[k+m][i]^powers[k][i] for i in range(n)]
    return n-rank(B,n)

def simulate(n,d):
    A=matrix(n,d);N=1<<n
    def move(x):return sum(((x&r).bit_count()%2)<<i for i,r in enumerate(A))
    observed={}
    for s in range(N):
        seen={};cur=s;t=0
        while cur not in seen:
            seen[cur]=t;t+=1;cur=move(cur)
        depth=seen[cur];period=t-depth
        observed[depth,period]=observed.get((depth,period),0)+1
    from math import lcm
    def factor_mobius(a):
        primes=[];q=a;v=2
        while v*v<=q:
            if q%v==0:
                q//=v;primes.append(v)
                if q%v==0:return 0
            while q%v==0:q//=v
            v+=1
        if q>1:primes.append(q)
        return (-1)**len(primes)
    for k in range(0,max(i for i,j in observed)+1):
        for m in set(p for i,p in observed):
            num=0
            for a in range(1,m+1):
                if m%a==0:
                    mu=factor_mobius(m//a)
                    if mu:
                        num+=mu*((1<<kernel_dim_period(n,d,k,a)) - ((1<<kernel_dim_period(n,d,k-1,a)) if k else 0))
            assert observed.get((k,m),0)==num,(n,d,k,m,observed.get((k,m),0),num)
    return sum(observed.values())

def check():
    cnt=0
    for n in range(3,19):
        for d in range(1,n//2+1):
            A=matrix(n,d);assert n-rank(A,n)==(0 if n%2==0 and d%2==1 else (2 if n%2==0 else 1))
            for k in range(0, min(n,5)+1):
                for m in (1,2,3,4,5,7,8,12):
                    a=direct(n,d,k,m);b=kernel_dim_period(n,d,k,m)
                    assert a==b,(n,d,k,m,a,b)
            cnt+=1
    for n in (3,4,5,6,7,8,9,10):
        for d in range(1,n//2+1):assert simulate(n,d)==2**n
    for n,d in ((7,1),(9,2),(15,1),(17,2)):
        A=matrix(n,d);I=[1<<i for i in range(n)];B=I
        for k in range(1,n+1):
            B=mul(B,A,n)
            if k==n-1:assert rank(B,n)==1,(n,d)
            if k==n:assert rank(B,n)==0,(n,d)
    print('DIRECT PASS:',cnt,'small matrices, all-period rank checks; exhaustive temporal histograms for n<=10; sharp nilpotence witnesses.')

if __name__=='__main__':check()
