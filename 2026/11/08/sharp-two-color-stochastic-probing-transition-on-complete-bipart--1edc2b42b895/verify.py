"""Exact rational checks for two-color trace probing of complete bipartite resolvents.

Run: python verify.py . Requires only Python standard library.
These finite checks supplement, not replace, the proof in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb

checks=0

def check(cond, desc='exact identity'):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(desc)

def inverse(M):
    n=len(M)
    C=[list(row)+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(M)]
    for i in range(n):
        j=next(j for j in range(i,n) if C[j][i])
        C[j],C[i]=C[i],C[j]
        k=C[i][i]; C[i]=[z/k for z in C[i]]
        for j in range(n):
            if j!=i:
                k=C[j][i]
                C[j]=[x-k*y for x,y in zip(C[j],C[i])]
    return [row[n:] for row in C]

def matrix(m,n,mu):
    N=m+n
    M=[[Q(0) for _ in range(N)] for _ in range(N)]
    for i in range(m):
        M[i][i]=mu+n
        for j in range(m,N):
            M[i][j]=M[j][i]=Q(-1)
    for j in range(m,N):
        M[j][j]=mu+m
    return M

def predicted(m,n,mu,i,j):
    c=Q(1)/(mu*(mu+m+n))
    if i<m and j<m:
        return (Q(int(i==j))/(mu+n)+n*c/(mu+n))
    if i>=m and j>=m:
        return (Q(int(i==j))/(mu+m)+m*c/(mu+m))
    return c

def cut(m,n,mu,x,y):
    a=(Q(n)/(mu+n))**2
    b=(Q(m)/(mu+m))**2
    return a*x*(m-x)+b*y*(n-y)+n*x+m*y-2*x*y

def variance(m,n,mu,x,y):
    c=Q(1)/(mu*(mu+m+n))
    a=(Q(n)/(mu+n))**2; b=(Q(m)/(mu+m))**2
    total=a*comb(m,2)+b*comb(n,2)+m*n
    return 4*c*c*(total-cut(m,n,mu,x,y))

def direct_variance(B,m,n,x,y):
    # The canonical color assignment uses x left and y right vertices in color 1.
    color=[int(i<x) for i in range(m)]+[int(i-m<y) for i in range(m,m+n)]
    return 4*sum(B[i][j]**2 for i in range(m+n) for j in range(i+1,m+n) if color[i]==color[j])

# Independently invert the full shifted Laplacian and enumerate every two-color partition.
for m,n in product(range(1,6),repeat=2):
    for mu in (Q(1,3),Q(1),Q(7,2)):
        B=inverse(matrix(m,n,mu))
        for i in range(m+n):
            for j in range(m+n):
                check(B[i][j]==predicted(m,n,mu,i,j), f'inverse blocks m={m} n={n}')
        c=Q(1)/(mu*(mu+m+n))
        a=(Q(n)/(mu+n))**2; b=(Q(m)/(mu+m))**2
        allcuts=[cut(m,n,mu,x,y) for x in range(m+1) for y in range(n+1)]
        largest=max(allcuts)
        edge=max([cut(m,n,mu,x,0) for x in range(m+1)]+[cut(m,n,mu,0,y) for y in range(n+1)])
        check(largest==edge, 'edge extremum')
        check((largest>m*n)==(a*(m-1)>n or b*(n-1)>m), 'sharp transition')
        for x in range(m+1):
            for y in range(n+1):
                check(direct_variance(B,m,n,x,y)==variance(m,n,mu,x,y),'variance identity')
                if 0<x<m and 0<y<n:
                    check(cut(m,n,mu,x,y)<largest, 'no interior maximizer')

# Verify the exact integer optimizer and phase inequalities for larger parameter grids.
for m,n in product(range(1,20),repeat=2):
    for mu in (Q(1,20),Q(1,2),Q(1),Q(5),Q(100)):
        a=(Q(n)/(mu+n))**2; b=(Q(m)/(mu+m))**2
        xs=[cut(m,n,mu,x,0) for x in range(m+1)]
        ys=[cut(m,n,mu,0,y) for y in range(n+1)]
        mx=max(xs+ys)
        check(mx==max(cut(m,n,mu,x,y) for x in range(m+1) for y in range(n+1)),'exact edge reduction')
        check((mx>m*n)==(a*(m-1)>n or b*(n-1)>m),'sharp full phase')
        check(not (a*(m-1)>n and b*(n-1)>m),'one winning side')

check(variance(10,1,Q(1),7,0)==Q(1,4),'star optimal variance')
check(variance(10,1,Q(1),10,0)==Q(5,16),'star conventional variance')
print(f'EXACT_CHECKS_PASSED={checks}')
print('STAR_K_10_1_mu_1: optimal=1/4, conventional=5/16, reduction=20%.')
print('The finite verifications supplement the parameter-uniform proof.')
