"""Finite checks of exact extremizer count and asymptotic normalized tie count.
All arithmetic involving kernels and floors is integer-exact.
"""
import math
from functools import lru_cache


def cube_root_floor(n):
    if n<=0: return 0
    x=int(round(n**(1/3)))
    while (x+1)**3<=n: x+=1
    while x**3>n: x-=1
    return x

def mobius_squarefree(N):
    sq=bytearray([1])*(N+1)
    for p in range(2,int(math.isqrt(N))+1):
        if all(p%t for t in range(2,math.isqrt(p)+1)):
            for n in range(p*p,N+1,p*p): sq[n]=0
    return sq

def count_ties(N):
    lim=math.isqrt(N)
    sq=mobius_squarefree(lim)
    count=0
    for u in range(1,lim+1):
        if not sq[u]:continue
        vmax=min(math.isqrt(N//u), N//(u*u))
        for v in range(1,vmax+1):
            if not sq[v] or math.gcd(u,v)!=1:continue
            r=u*v*v; rstar=u*u*v
            if cube_root_floor(N//r)==cube_root_floor(N//rstar):count+=1
    assert count%2==1
    return (count-1)//2

def kthfree_kernel(n):
    if n==1:return 1
    r=1; p=2
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        r*=p**(e%3)
        p+=1
    if n>1:r*=n
    return r

def max_indep_bruteforce(N):
    edges=[]
    kernels=[kthfree_kernel(i) for i in range(1,N+1)]
    for i in range(N):
        for j in range(i+1,N):
            if kthfree_kernel((i+1)*(j+1))==1:edges.append((i,j))
    best=-1; count=0
    for mask in range(1<<N):
        bits=mask.bit_count()
        if bits<best:continue
        if any((mask>>i)&1 and (mask>>j)&1 for i,j in edges):continue
        if bits>best:best=bits;count=0
        count+=1
    return best,count

def analytic_extremal_max_size(N):
    classes={}
    for i in range(1,N+1):
        r=kthfree_kernel(i)
        classes[r]=classes.get(r,0)+1
    def star(r):
        u=1;d=2
        while d*d<=r:
            e=0
            while r%d==0:r//=d;e+=1
            if e:u*=d**(3-e)
            d+=1
        if r>1:u*=r*r
        return u
    val=0; used=set()
    for r,c in classes.items():
        if r in used:continue
        s=star(r);used.add(r);used.add(s)
        if s==r:val+=1
        else:val+=max(c,classes.get(s,0))
    return val

for N in range(1,17):
    sz,count=max_indep_bruteforce(N)
    formula=cube_root_floor(N)*(1<<count_ties(N))
    assert count==formula and sz==analytic_extremal_max_size(N),(N,sz,count,formula)
print('BRUTE_FORCE_COMPLETE_CUBE_PRODUCT_GRAPH_OK N=1..16')
for N in (100,1000,10000,100000,1000000,10000000):
    b=count_ties(N)
    print('TIE_COUNT',N,b,'NORMALIZED',format(b/N**(2/3),'.9f'))
sieve=bytearray([1])*100000
sieve[0:2]=bytes([0,0])
for p in range(2,math.isqrt(99999)+1):
    if sieve[p]:
        for m in range(p*p,100000,p): sieve[m]=0
rho=1.0
for p in range(2,100000):
    if sieve[p]: rho*=(1-1/p)**2*(1+2/p)
print('PREDICTED_TIE_NORMALIZATION',format(rho*(math.pi**2-9)/2,'.9f'))
print('FINITE_CHECKS_ONLY_TRUE; INFINITE_PROOF_SEPARATE_TRUE; INDEPENDENT_AUDIT_FALSE')
