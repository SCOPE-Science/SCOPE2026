"""Independent finite checks for the random-mapping component-size covariance theorem.
This is a finite verifier, not a proof of the asymptotic assertions.
Run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, exp, sqrt, pi, e, log

checks = 0

def chk(got, want, context):
    global checks
    checks += 1
    assert got == want, (context, got, want)

def mu(n):
    if n == 0:
        return F(0)
    a = F(1)
    ans = F(1)
    for j in range(2,n+1):
        a *= F(n-j+1,n)
        ans += a/j
    return ans

def component_count_and_sizes(mapping):
    n=len(mapping)
    parent=list(range(n))
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for i,j in enumerate(mapping):
        a,b=root(i),root(j)
        parent[a]=b
    size={}
    for v in range(n):
        r=root(v)
        size[r]=size.get(r,0)+1
    counts=[0]*(n+1)
    for s in size.values():
        counts[s]+=1
    return len(size),counts

def connected_count(r):
    return factorial(r-1)*sum(F(r**i,factorial(i)) for i in range(r))

def expected_x(n,r):
    return F(comb(n,r)*connected_count(r)*(n-r)**(n-r), n**n) if n!=r else F(connected_count(r),n**n)

for n in range(2,7):
    ksum=0
    xs=[0]*(n+1)
    xk=[0]*(n+1)
    for mapping in product(range(n), repeat=n):
        k,sz=component_count_and_sizes(mapping)
        ksum+=k
        for r in range(1,n+1):
            xs[r]+=sz[r]
            xk[r]+=k*sz[r]
    d=n**n
    chk(F(ksum,d),mu(n),('mean-components',n))
    for r in range(1,n+1):
        ex=expected_x(n,r)
        chk(F(xs[r],d),ex,('mean-count',n,r))
        cov=F(xk[r],d)-F(ksum*xs[r],d*d)
        chk(cov,ex*(1+mu(n-r)-mu(n)),('covariance',n,r))
        assert (cov>0 if r==1 else cov<0 if r==n else True)
        checks+=1

for n in range(2,81):
    diffs=[1+mu(n-r)-mu(n) for r in range(1,n+1)]
    assert diffs[0]>0 and diffs[-1]<0
    checks+=2
    for r in range(1,n):
        assert diffs[r]<diffs[r-1], (n,r)
        checks+=1

# Independent floating-point evaluation of the precise crossover on large n.
def mu_float(n):
    if n==0: return 0.
    term,ans=1.,1.
    for j in range(2,n+1):
        term *= (n-j+1)/n
        ans += term/j
        if j>100*sqrt(n) and term<1e-35:break
    return ans

A=sqrt(pi/2)/3
c=(2/3)*sqrt(pi/2)*exp(-2)*(e-1)
for n in (1000, 10000, 100000):
    mean=mu_float(n)
    lo,hi=1,n
    while lo<hi:
        mid=(lo+hi)//2
        if 1+mu_float(n-mid)-mean<=0: hi=mid
        else: lo=mid+1
    r=lo
    target=(1-exp(-2))*n+c*sqrt(n)
    assert abs(r-target)<3, (n,r,target)
    checks+=1
print('PASS:',checks,'exact symbolic, finite exhaustive, and numerical assertions')
