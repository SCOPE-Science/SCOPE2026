"""Compute the independent cyclic-run polynomial and count wheel majority 2-cycles."""
from math import comb
from collections import defaultdict

def R(m):
    z=defaultdict(int)
    z[(0,0)]+=1
    z[(m,m)]+=1
    for k in range(2,m):
        for r in range(1,min(k//2,m-k)+1):
            numerator=m*comb(k-r-1,r-1)*comb(m-k-1,r-1)
            assert numerator%r==0
            z[(k,k-r)]+=numerator//r
    return dict(z)

def square(poly):
    a=defaultdict(int)
    for (k,e),v in poly.items():
        for (l,f),w in poly.items():
            a[(k+l,e+f)]+=v*w
    return dict(a)

def A(n):
    p=R(n) if n%2 else square(R(n//2))
    return sum(c for (k,e),c in p.items() if 2*k>n and 2*e<n)

# A second construction, finite bitstring tests on the step-two graph,
# independently checks the binomial run polynomial.
def direct(n):
    total=0
    for x in range(1<<n):
        k=x.bit_count()
        if 2*k<=n:continue
        e=0
        good=True
        for i in range(n):
            if ((x>>i)&1):
                l=(x>>((i-2)%n))&1
                r=(x>>((i+2)%n))&1
                if not (l or r):good=False;break
                e+=r
        if good and 2*e<n:total+=1
    return total

if __name__=='__main__':
    for n in range(3,20):
        a=A(n)
        assert a==direct(n), (n,a,direct(n))
        print(n,2,2*(a+2*(n%2==0)),a,2*(n%2==0))
    for m in range(2,16):
        assert sum(R(m).values())==sum(
            int(all(not ((x>>i)&1) or ((x>>((i-1)%m))&1) or ((x>>((i+1)%m))&1)
                    for i in range(m))) for x in range(1<<m)),m
    print('RUN_POLYNOMIAL_OK')
