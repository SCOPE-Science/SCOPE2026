"""Exact integral certificate for the reduced MacLane triple-point blowup boundary.
Dependencies: Python 3 standard library only.
"""
from itertools import product
from math import prod

def det_bareiss(a):
    a=[row[:] for row in a]; n=len(a); sign=1; prev=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next(j for j in range(k+1,n) if a[j][k]); a[k],a[j]=a[j],a[k];sign=-sign
        d=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                x=a[i][j]*d-a[i][k]*a[k][j]
                assert x%prev==0
                a[i][j]=x//prev
            a[i][k]=0
        prev=d
    return sign*a[-1][-1]

def smith(a):
    a=[row[:] for row in a];n=len(a)
    U=[[int(i==j) for j in range(n)] for i in range(n)]
    V=[[int(i==j) for j in range(n)] for i in range(n)]
    def rowadd(i,j,q):
        for t in (a,U):
            t[i]=[x+q*y for x,y in zip(t[i],t[j])]
    def row_swap(i,j):
        a[i],a[j]=a[j],a[i]; U[i],U[j]=U[j],U[i]
    def coladd(i,j,q):
        for t in (a,V):
            for row in t:row[i]+=q*row[j]
    def col_swap(i,j):
        for t in (a,V):
            for row in t:row[i],row[j]=row[j],row[i]
    for k in range(n):
        pivot=min(((abs(a[i][j]),i,j) for i in range(k,n) for j in range(k,n) if a[i][j]!=0),default=None)
        if pivot is None:continue
        row_swap(k,pivot[1]);col_swap(k,pivot[2])
        limit=0
        while True:
            limit+=1;assert limit<2000
            again=False
            for i in range(k+1,n):
                if a[i][k]:
                    q=a[i][k]//a[k][k]
                    rowadd(i,k,-q)
                    if a[i][k]:row_swap(i,k)
                    again=True
                    break
            if again:continue
            for j in range(k+1,n):
                if a[k][j]:
                    q=a[k][j]//a[k][k]
                    coladd(j,k,-q)
                    if a[k][j]:col_swap(j,k)
                    again=True
                    break
            if again:continue
            bad=next(((i,j) for i in range(k+1,n) for j in range(k+1,n) if a[i][j]%a[k][k]),None)
            if bad:
                rowadd(k,bad[0],1)
                continue
            break
        if a[k][k]<0:rowadd(k,k,-2)
    for i in range(n):
        for j in range(n):assert (i==j) or a[i][j]==0
    for i in range(n-1):assert a[i][i] and a[i+1][i+1]%a[i][i]==0
    return [a[i][i] for i in range(n)],U,V

def matmul(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]

pts=[(i,j) for i in range(3) for j in range(3) if (i,j)!=(0,0)]
lines=set()
for a,b in product(range(3),repeat=2):
    if (a,b)==(0,0):continue
    for c in range(3):
        support=frozenset((x,y) for x,y in pts if (a*x+b*y-c)%3==0)
        if len(support)>=2:lines.add(support)
triples=sorted((p for p in lines if len(p)==3),key=lambda x:sorted(x))
doubles=sorted((p for p in lines if len(p)==2),key=lambda x:sorted(x))
assert (len(triples),len(doubles))==(8,4)
assert all(sum(p in t for t in triples)==3 and sum(p in d for d in doubles)==1 for p in pts)
assert all(sum({x,y}.issubset(t) for t in triples+doubles)==1 for x in pts for y in pts if x<y)
N=16; A=[[0]*N for _ in range(N)]
def edge(i,j):
    A[i][i]+=1;A[j][j]+=1;A[i][j]-=1;A[j][i]-=1
for j,t in enumerate(triples):
    for p in t:edge(pts.index(p),8+j)
for t in doubles:edge(*(pts.index(p) for p in sorted(t)))
assert sum(A[i][i] for i in range(N))//2==28
assert all(A[i][i]==4 for i in range(8))
assert all(A[i][i]==3 for i in range(8,16))
assert sum(A[0])==0 and all(sum(r)==0 for r in A)
B=[row[:-1] for row in A[:-1]]
D,U,V=smith(B)
assert D==[1]*9+[2,6,12,12,48,48],D
assert matmul(matmul(U,B),V)==[[D[i] if i==j else 0 for j in range(15)] for i in range(15)]
assert abs(det_bareiss(U))==abs(det_bareiss(V))==1
assert det_bareiss(B)==prod(D)==3981312
assert det_bareiss([r[1:] for r in A[1:]])==prod(D)
assert len(pts)+len(triples)==16 and 28-16+1==13
print('MACLANE_STABLE_BOUNDARY_INTEGRAL_COMPONENT_GROUP_OK')
print('Smith:',D,'order:',prod(D),'genus:',13)
