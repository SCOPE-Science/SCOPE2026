"""Exact integer verification of rooted-forest root-support Walsh formulas.

The finite checks supplement, rather than replace, the proofs supplied with the result.
Standard-library only; run: python verify.py
"""
from math import comb
from itertools import product

checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1


def multiplier(m, n, x, y):
    assert m >= 2 and n >= 2 and 0 <= x <= m and 0 <= y <= n
    alpha = (n + 1) ** (m - x) * (n - 1) ** x
    beta = (m + 1) ** (n - y) * (m - 1) ** y
    u = m * (n - 1) + 2 * x
    v = n * (m - 1) + 2 * y
    delta = (n * n - 1) * (m * m - 1)
    num = alpha * beta * (delta - u * v)
    check(num % delta == 0)
    return num // delta


def bareiss(a):
    a = [row[:] for row in a]
    N = len(a)
    sign = 1
    prior = 1
    for k in range(N-1):
        if a[k][k] == 0:
            q = next((i for i in range(k+1,N) if a[i][k] != 0), None)
            if q is None:
                return 0
            a[k], a[q] = a[q], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1,N):
            for j in range(k+1,N):
                num = a[i][j]*pivot-a[i][k]*a[k][j]
                check(num%prior==0)
                a[i][j]=num//prior
            a[i][k]=0
        prior=pivot
    return sign*a[N-1][N-1]


def determinant_multiplier(m,n,x,y):
    N=m+n
    mat=[[0]*N for _ in range(N)]
    for i in range(m):
        mat[i][i]=n+(-1 if i<x else 1)
        for j in range(m,N):mat[i][j]=-1
    for j in range(m,N):
        mat[j][j]=m+(-1 if j<m+y else 1)
        for i in range(m):mat[j][i]=-1
    return bareiss(mat)


def distribution_by_forests(m,n):
    N=m+n
    edges=[(i,j) for i in range(m) for j in range(m,N)]
    weights=[0]*(1<<N)
    for emask in range(1<<len(edges)):
        parent=list(range(N))
        def find(x):
            while x!=parent[x]:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        valid=True
        for k,(u,v) in enumerate(edges):
            if (emask>>k)&1:
                u0=find(u);v0=find(v)
                if u0==v0:
                    valid=False;break
                parent[u0]=v0
        if not valid:continue
        comps={}
        for v in range(N):comps.setdefault(find(v),[]).append(v)
        for roots in product(*comps.values()):
            mask=sum(1<<r for r in roots)
            weights[mask]+=1
    return weights


def walsh(vec):
    v=vec[:]
    k=1
    while k<len(v):
        for i in range(0,len(v),2*k):
            for j in range(k):
                a=v[i+j];b=v[i+j+k]
                v[i+j]=a+b;v[i+j+k]=a-b
        k*=2
    return v


def main():
    for m,n in [(2,2),(2,3),(2,4),(3,2),(3,3),(3,4)]:
        counts=distribution_by_forests(m,n)
        spectral=walsh(counts)
        check(sum(counts)==multiplier(m,n,0,0))
        for mask,z in enumerate(spectral):
            x=(mask&((1<<m)-1)).bit_count()
            y=(mask>>m).bit_count()
            check(z==multiplier(m,n,x,y))
            check(z==determinant_multiplier(m,n,x,y))
    for m in range(2,12):
        for n in range(2,12):
            zeros=0
            for x in range(m+1):
                for y in range(n+1):
                    z=multiplier(m,n,x,y)
                    u=m*(n-1)+2*x
                    v=n*(m-1)+2*y
                    goal=(n*n-1)*(m*m-1)
                    check((z==0)==(u*v==goal))
                    if z==0:zeros+=comb(m,x)*comb(n,y)
            if m%2==n%2==0:check(zeros==0)
            if n==m+1:check(zeros==1)
            if m==n:
                expected=comb(m,(m-1)//2)**2 if m%2 else 0
                check(zeros==expected)
    for d in range(2,151):
        check(sum(comb(d,x)*comb(d,y) for x in range(d+1) for y in range(d+1)
                  if (d*(d-1)+2*x)*(d*(d-1)+2*y)==(d*d-1)**2)
              == (comb(d,(d-1)//2)**2 if d%2 else 0))
        n=d+1
        check(sum(comb(d,x)*comb(n,y) for x in range(d+1) for y in range(n+1)
                  if (d*(n-1)+2*x)*(n*(d-1)+2*y)==(n*n-1)*(d*d-1))==1)
    print(f'PASS {checks} exact integer assertions')

if __name__=='__main__':main()
