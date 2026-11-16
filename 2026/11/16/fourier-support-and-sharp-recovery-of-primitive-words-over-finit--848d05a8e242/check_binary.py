"""Independent exhaustive binary Walsh comparison for full-period words."""
from math import gcd
from itertools import combinations

def primes(n):
    return [p for p in range(2,n+1) if n%p==0 and all(p%d for d in range(2,int(p**.5)+1))]

def popcount(x): return x.bit_count()

def is_full(x,n):
    return all(any(((x>>i)&1)!=((x>>((i+d)%n))&1) for i in range(n)) for d in range(1,n) if n%d==0)

def fwht(a):
    a=a[:]; m=len(a); h=1
    while h<m:
        for i in range(0,m,2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h]
                a[j],a[j+h]=u+v,u-v
        h*=2
    return a

def C(x,n,d):
    return all(sum((x>>j)&1 for j in range(i,n,d))%2==0 for i in range(d))

def mob(k):
    if k==1: return 1
    z=0; t=k
    for p in range(2,t+1):
        if p*p>t: break
        if t%p==0:
            t//=p;z+=1
            if t%p==0:return 0
            while t%p==0:t//=p
    if t>1:z+=1
    return -1 if z%2 else 1

def formula(n):
    from math import prod
    m=n//prod(primes(n))
    return 2**(n-m)

for n in range(2,16):
    f=[int(is_full(x,n)) for x in range(1<<n)]
    w=fwht(f)
    rank=sum(v!=0 for v in w)
    expected=formula(n)
    assert rank==expected,(n,rank,expected)
    for k,v in enumerate(w):
        rhs=sum(mob(n//d)*(2**d if C(k,n,d) else 0) for d in range(1,n+1) if n%d==0)
        assert rhs==v,(n,k,v,rhs)
        from math import prod
        assert (v!=0)==C(k,n,n//prod(primes(n))),(n,k,v)
    from math import prod
    m=n//prod(primes(n))
    assert min(abs(z) for z in w if z)==2**m
    assert max(abs(z) for z in w)==sum(f)
    print('n=',n,'primitive=',sum(f),'rank=',rank,'zeros=',2**n-rank,'min=',2**m,'max=',sum(f))
print('all binary checks passed')
