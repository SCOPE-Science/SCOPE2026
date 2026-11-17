"""Finite-field verification of the square-zero locus in an unequal two-block nilpotent centralizer.
Uses prime fields, with independent matrix multiplication and rank elimination.
Run: python checker.py
"""
from itertools import product
from collections import Counter


def matmul(a,b,q):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n))%q for j in range(n)] for i in range(n)]


def rank(a,q):
    a=[row[:] for row in a]
    n=len(a); piv=0
    for col in range(len(a[0])):
        row=next((i for i in range(piv,n) if a[i][col]%q),None)
        if row is None:continue
        a[row],a[piv]=a[piv],a[row]
        inv=pow(a[piv][col],-1,q)
        a[piv]=[(v*inv)%q for v in a[piv]]
        for j in range(n):
            if j!=piv:
                t=a[j][col]%q
                a[j]=[(a[j][k]-t*a[piv][k])%q for k in range(len(a[0]))]
        piv+=1
        if piv==n:break
    return piv


def centralizer_matrix(a,b,c,d,q):
    n=len(a); x=[[0]*(n+1) for _ in range(n+1)]
    # multiplication by a(t) on k[t]/t^n
    for j in range(n):
        for z in range(n-j): x[j+z][j]=a[z]%q
    x[n-1][n]=b%q
    x[n][0]=c%q; x[n][n]=d%q
    return x


def expected(n,q):
    h=n//2
    ans=Counter({0:1,1:(q-1)*(2*q+1)})
    for r in range(2,h+1): ans[r]=(q-1)*(2*q-1)*q**(r-1)
    if n%2: ans[h+1]=q**h*(q-1)**2
    return ans


def test(n,q):
    N=n+1
    B=[[0]*N for _ in range(N)]
    for i in range(n-1): B[i+1][i]=1
    histogram=Counter()
    for params in product(range(q),repeat=n+3):
        a=params[:n];b,c,d=params[n:]
        X=centralizer_matrix(a,b,c,d,q)
        assert matmul(X,B,q)==matmul(B,X,q)
        if all(x==0 for row in matmul(X,X,q) for x in row):
            histogram[rank(X,q)]+=1
            assert a[0]==d==0
            if n%2:
                h=n//2
                assert all(v==0 for v in a[:h]) and (a[h]*a[h]+b*c)%q==0
            else:
                h=n//2
                assert all(v==0 for v in a[:h]) and b*c%q==0
    theory=expected(n,q)
    assert histogram==theory,(n,q,histogram,theory)
    if n%2: assert sum(histogram.values())==q**(n//2+2)
    else: assert sum(histogram.values())==q**(n//2)*(2*q-1)
    return dict(sorted(histogram.items()))

if __name__=='__main__':
    for q,nmax in [(2,8),(3,5),(5,3)]:
        for n in range(2,nmax+1):
            got=test(n,q)
            print(f'q={q} n={n}: rank multiplicities={got}; total={sum(got.values())}; PASS')
    print('ALL_UNEQUAL_BLOCK_SQUARE_ZERO_CENTRALIZER_TESTS_PASS')
