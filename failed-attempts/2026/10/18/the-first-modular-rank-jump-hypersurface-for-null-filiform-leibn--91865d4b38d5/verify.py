"""Finite-field matrix and derivation-identity tests for null-filiform Leibniz algebras."""
from itertools import product
from collections import Counter
from random import Random

def mul(a,b,q):
    if q==4:
        z=0
        for i in range(2):
            for j in range(2):
                if a&(1<<i) and b&(1<<j): z ^= 1<<(i+j)
        if z&4: z^=7
        return z
    return a*b%q

def add(a,b,q): return a^b if q==4 else (a+b)%q

def sub(a,b,q): return a^b if q==4 else (a-b)%q

def inv(a,q):
    for v in range(1,q):
        if mul(a,v,q)==1:return v
    raise ValueError('not a field')

def derive_matrix(a,q):
    n=len(a);D=[[0]*n for _ in range(n)]
    for j in range(n):
        D[j][j]=mul((j+1)%q if q!=4 else (j+1)%2,a[0],q)
        for i in range(j+1,n):D[i][j]=a[i-j]
    return D

def matrix_rank(A,q):
    n=len(A);m=len(A[0]);R=[x[:] for x in A];r=0
    for j in range(m):
        p=next((i for i in range(r,n) if R[i][j]),None)
        if p is None:continue
        R[r],R[p]=R[p],R[r]
        v=inv(R[r][j],q)
        R[r]=[mul(v,x,q) for x in R[r]]
        for i in range(n):
            if i!=r and R[i][j]:
                c=R[i][j]
                R[i]=[sub(x,mul(c,y,q),q) for x,y in zip(R[i],R[r])]
        r+=1
        if r==n:break
    return r

def certificate(a,p,q):
    n=len(a);a1=a[0]
    if not a1:return 0
    u=[1]
    for j in range(1,p):
        s=0
        for r in range(1,j+1):s=add(s,mul(a[r],u[j-r],q),q)
        denom=mul(a1,j%p,q)
        u.append(sub(0,mul(inv(denom,q),s,q),q))
    c=0
    for r in range(1,p+1):c=add(c,mul(a[r],u[p-r],q),q)
    return c

def expected(a,p,q):
    n=len(a)
    if not a[0]:
        for r in range(1,n):
            if a[r]:return n-r
        return 0
    return n-2 if certificate(a,p,q)==0 else n-1

def check_derivation(a,q):
    n=len(a);D=derive_matrix(a,q)
    # [e_i,e_j]=e_{i+1} if j=0 and i<n-1 (0-based).
    for i in range(n):
        for j in range(n):
            left=[0]*n
            if j==0 and i<n-1:left=[D[k][i+1] for k in range(n)]
            right=[0]*n
            if j==0:
                for k in range(1,n):right[k]=D[k-1][i]
            for k in range(1,n):right[k]=add(right[k],mul(D[0][j], int(i==k-1),q),q)
            assert left==right,(q,a,i,j,left,right)

def run():
    for q,p,n in ((2,2,4),(4,2,4),(3,3,6)):
        obs=Counter()
        for a in product(range(q),repeat=n):
            r=matrix_rank(derive_matrix(a,q),q)
            assert r==expected(a,p,q),(q,a,r,expected(a,p,q))
            obs[r]+=1
            if q==2:check_derivation(a,q)
        th={0:1}
        for k in range(1,n-2):th[k]=(q-1)*q**(k-1)
        th[n-2]=(q-1)*(q+1)*q**(n-3)
        th[n-1]=(q-1)*q**(n-1)
        assert dict(obs)==th,(q,obs,th)
        print('EXHAUSTIVE',q,n,dict(sorted(obs.items())))
    p=q=5;n=2*p; rng=Random(123456789)
    for _ in range(3000):
        a=[rng.randrange(q) for _ in range(n)]
        assert matrix_rank(derive_matrix(a,q),q)==expected(a,p,q)
    print('SAMPLED',q,n,3000)
    print('VERIFY_OK')

if __name__=='__main__':run()
