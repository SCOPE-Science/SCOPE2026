"""Standard-library integer certificates for weighted Petersen capture."""
from itertools import combinations
from fractions import Fraction

V=list(combinations(range(5),2))
TRIPLE=[(0,1),(0,2),(0,8),(1,1),(1,2),(1,8),(2,1),(2,8),(3,1),(3,8)]
FIVE=[(0,0),(0,1),(0,2),(0,4),(0,5),(1,0),(1,1),(1,2),(1,4),(2,0)]

def matrix(t):
    a=[[int(set(u).isdisjoint(w)) for w in V] for u in V]
    a[0][7]=a[7][0]=t
    return a

def columns(t, requested):
    a=matrix(t)
    powers=[[int(i==j) for i in range(10)] for j in range(10)]
    vectors={}
    for k in range(max(e[0] for e in requested)+1):
        for j in range(10): vectors[k,j]=powers[j][:]
        powers=[[sum(a[i][h]*powers[j][h] for h in range(10)) for i in range(10)] for j in range(10)]
    return [[vectors[k,j][i] for k,j in requested] for i in range(10)]

def det(mat):
    a=[r[:] for r in mat]; n=len(a); sign=1; old=1
    assert len(a)==n and all(len(row)==n for row in a)
    for k in range(n-1):
        if a[k][k]==0:
            i=next((i for i in range(k+1,n) if a[i][k]),None)
            if i is None: return 0
            a[k],a[i]=a[i],a[k];sign=-sign
        piv=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=piv*a[i][j]-a[i][k]*a[k][j]
                assert numerator%old==0
                a[i][j]=numerator//old
        for i in range(k+1,n): a[i][k]=0
        old=piv
    return sign*a[n-1][n-1]

def rank(mat):
    a=[[Fraction(z) for z in row] for row in mat]
    n=len(a);m=len(a[0]);row=0
    for c in range(m):
        p=next((r for r in range(row,n) if a[r][c]),None)
        if p is None: continue
        a[row],a[p]=a[p],a[row]
        inv=a[row][c]
        a[row]=[z/inv for z in a[row]]
        for r in range(n):
            if r!=row and a[r][c]:
                mul=a[r][c]
                a[r]=[a[r][j]-mul*a[row][j] for j in range(m)]
        row+=1
        if row==n: break
    return row

# Each selected Krylov column H(t)^k e_i has polynomial entries of degree <=k.
# Sum of the selected k is 13; hence its determinant has degree at most 13.
# Fourteen distinct exact evaluations therefore prove the cubic determinant identity.
assert sum(k for k,j in TRIPLE)==13
for t in range(-6,8):
    assert det(columns(t,TRIPLE))==-2*(t-1)**3,(t,det(columns(t,TRIPLE)))
assert rank(columns(1, [(k,j) for k in range(3) for j in [1,2,8]]))==7
assert det(columns(1,FIVE))==-2
assert rank(columns(2,TRIPLE))==10
print('INDEPENDENT_INTEGER_PETERSEN_CERTIFICATE_PASSED: 14 evaluations, rank, unweighted minor')
