"""Independent GF(5) reconstruction of the Cartier rank at all 625 coefficients.
Requires Python 3 standard library. Run: python3 verify_finite.py
"""
from collections import Counter
from itertools import product
from math import comb

p=5
basis=[(i,j) for j in range(4) for i in range(4) if 5*i+6*j<=18]
def multiply(f,g):
    h=[0]*(len(f)+len(g)-1)
    for i,fi in enumerate(f):
        if fi:
            for j,gj in enumerate(g):h[i+j]=(h[i+j]+fi*gj)%p
    return h

def rank(matrix):
    a=[r[:] for r in matrix]
    n=len(a); cols=len(a[0]); r=0
    for j in range(cols):
        k=next((k for k in range(r,n) if a[k][j]),None)
        if k is None:continue
        a[k],a[r]=a[r],a[k]
        inv=pow(a[r][j],-1,p)
        a[r]=[(x*inv)%p for x in a[r]]
        for k in range(n):
            if k!=r and a[k][j]:
                t=a[k][j]
                a[k]=[(x-t*y)%p for x,y in zip(a[k],a[r])]
        r+=1
        if r==n:break
    return r

counts=Counter()
for a,b,c,d in product(range(p),repeat=4):
    f=[0,d,c,b,a,0,1]
    powers=[[1]]
    for _ in range(3):powers.append(multiply(powers[-1],f))
    mat=[[0]*len(basis) for _ in basis]
    for col,(i,j) in enumerate(basis):
        for m in range(j+1):
            sign=(-1)**m*comb(j,m)
            for row,(r,ell) in enumerate(basis):
                if ell!=j-m:continue
                n=5*r+4-i
                if 0<=n<len(powers[m]):
                    mat[row][col]=(mat[row][col]+sign*powers[m][n])%p
    actual=rank(mat)
    q=(b*b+2*a*a*a+4*a*c)%p
    predicted=0 if (a,b,c)==(0,0,0) else 3 if q==0 else 4
    assert actual==predicted,(a,b,c,d,actual,predicted)
    counts[actual]+=1
assert counts==Counter({4:500,3:120,0:5}),counts
print('CHAR5_CONDUCTOR6_GF5_ALL_625_Q_STRATA_OK',dict(sorted(counts.items())))
