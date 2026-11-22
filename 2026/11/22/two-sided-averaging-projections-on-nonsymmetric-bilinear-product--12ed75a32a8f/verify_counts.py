from itertools import product
from math import prod

def gb(n,r,q):
    if r<0 or r>n:return 0
    a=prod(q**(n-i)-1 for i in range(r));b=prod(q**(r-i)-1 for i in range(r))
    return a//b

def gl(d,q):return prod(q**d-q**i for i in range(d))

def Ir(n,r,q):
    return sum(gb(n,s,q)*gb(n-s,t,q)*gb(s,r-t,q)*gb(t,r-s,q)*gl(s+t-r,q) for s in range(n+1) for t in range(n-s+1) if s<=r and t<=r and s+t>=r)

def census(n,q):
    res={}
    for r in range(n+1):res[r]=Ir(n,r,q)*q**(r*(2*n-r+1))
    for j in range(n+1):res[2*j+1]=res.get(2*j+1,0)+gb(n,j,q)*q**(j*(n-j)+2*(n-j))
    return res

# enumerate RREF subspaces for fixed n over prime field
def subspaces(d,q):
    for r in range(d+1):
        for piv in __import__('itertools').combinations(range(d),r):
            pos=[(i,j) for i in range(r) for j in range(piv[i]+1,d) if j not in piv]
            for vals in product(range(q),repeat=len(pos)):
                rows=[[0]*d for _ in range(r)]
                for i,p in enumerate(piv):rows[i][p]=1
                for (i,j),v in zip(pos,vals):rows[i][j]=v
                yield rows

def iso_dim_counts(n,q,a):
    h=[0]*(n+1)
    for rows in subspaces(2*n,q):
        r=len(rows)
        ok=all((sum(rows[i][k]*rows[j][n+k]+a*rows[i][n+k]*rows[j][k] for k in range(n)))%q==0 for i in range(r) for j in range(r))
        if ok:
            assert r<=n
            h[r]+=1
    return h
def central_idempotents(n,q):
    assert n==2
    count=[0]*(n+1)
    for flat in product(range(q), repeat=n*n):
        A=[[flat[i*n+j] for j in range(n)] for i in range(n)]
        if all(sum(A[i][k]*A[k][j] for k in range(n))%q==A[i][j] for i in range(n) for j in range(n)):
            r=0 if all(v==0 for v in flat) else 2 if (A[0][0]*A[1][1]-A[0][1]*A[1][0])%q else 1
            count[r]+=1
    return count

if __name__=='__main__':
    for q,n,a in [(5,1,2),(5,2,2),(7,1,2)]:
        hs=iso_dim_counts(n,q,a)
        f=[Ir(n,r,q) for r in range(n+1)]
        print(q,n,'actual and predicted isotropic subspaces',hs,f,'rank',census(n,q),'total',sum(census(n,q).values()))
        assert hs==f
    c=central_idempotents(2,5)
    assert c==[1,30,1], c
    # Lifts are functionals annihilating the projected image.
    expected={1:5**4,3:30*5**2,5:1}
    assert expected=={1:625,3:750,5:1}
    assert census(2,5)=={0:1,1:23125,2:125000,3:750,5:1}
    print('RREF_ISOTROPIC_AND_CENTRAL_IDEMPOTENT_COUNTS_VERIFIED')
