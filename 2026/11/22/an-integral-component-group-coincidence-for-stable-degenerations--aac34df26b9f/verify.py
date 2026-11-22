"""Exact standard-library certificate for marked order-four three-net incidence graphs."""
from itertools import permutations
from collections import Counter

def reduced_squares():
    ps = list(permutations(range(4)))
    return [((0,1,2,3),a,b,c) for a in ps for b in ps for c in ps
            if a[0]==1 and b[0]==2 and c[0]==3
            and all(len({r[j] for r in ((0,1,2,3),a,b,c)})==4 for j in range(4))]

def laplacian(s):
    A=[[0]*28 for _ in range(28)]
    for i in range(4):
        for j in range(4):
            t=12+4*i+j
            for v in (i,4+j,8+s[i][j]):
                A[t][t]+=1; A[v][v]+=1; A[t][v]-=1; A[v][t]-=1
    return [row[:-1] for row in A[:-1]]

def determinant(A):
    a=[r[:] for r in A]; n=len(a); sign=1; old=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next(j for j in range(k+1,n) if a[j][k]);a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                z=a[i][j]*pivot-a[i][k]*a[k][j]
                assert z%old==0
                a[i][j]=z//old
        for i in range(k+1,n):a[i][k]=0
        old=pivot
    return sign*a[-1][-1]

def valuations(A,p,N=14):
    mod=p**N;a=[[x%mod for x in r] for r in A];n=len(a);out=[]
    for k in range(n):
        best=None
        for i in range(k,n):
            for j in range(k,n):
                z=a[i][j]
                if z:
                    e=0
                    while z%p==0:e+=1;z//=p
                    if best is None or e<best[0]: best=(e,i,j)
        assert best is not None,'insufficient precision'
        e,i,j=best
        a[i],a[k]=a[k],a[i]
        for r in a:r[j],r[k]=r[k],r[j]
        pivot=a[k][k];u=pivot//(p**e); inv=pow(u,-1,mod)
        for i in range(k+1,n):
            factor=((a[i][k]//(p**e))*inv)%mod
            for j in range(k,n):a[i][j]=(a[i][j]-factor*a[k][j])%mod
        for j in range(k+1,n):
            factor=((a[k][j]//(p**e))*inv)%mod
            for i in range(k,n):a[i][j]=(a[i][j]-factor*a[i][k])%mod
        out.append(e)
    return sorted(out)

def intercalates(s):
    z=0
    for i in range(4):
        for j in range(i+1,4):
            for a in range(4):
                for b in range(a+1,4):
                    z+=s[i][a]==s[j][b] and s[i][b]==s[j][a]
    return z

squares=reduced_squares();assert len(squares)==4
assert sorted(intercalates(s) for s in squares)==[4,4,4,12]
for s in squares:
    A=laplacian(s)
    assert determinant(A)==2**29*3**6
    assert valuations(A,2)==[0]*18+[1]+[3]*6+[5]*2
    assert valuations(A,3)==[0]*21+[1]*6
print('ORDER_FOUR_NET_ALL_FOUR_REDUCED_INTEGRAL_CRITICAL_GROUPS_OK')
