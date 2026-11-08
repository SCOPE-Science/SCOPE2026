"""Exact finite-field checks for the all-order Mayer homology of a directed multi-diamond.
Theorems about arbitrary parameters are proved separately; these are finite checks.
"""
from collections import Counter

def prime_root(N):
    for p in (17,19,29,31,37,41,43,61,71,73,97,113,127,181,241,337,421,631):
        if (p-1)%N: continue
        for x in range(2,p):
            if pow(x,N,p)!=1: continue
            if all(pow(x,N//d,p)!=1 for d in range(2,N+1) if N%d==0):
                return p,x
    raise ValueError(N)

def rank(rows,p):
    M=[[v%p for v in row] for row in rows]
    if not M:return 0
    R=len(M);C=len(M[0]);h=0
    for j in range(C):
        v=next((i for i in range(h,R) if M[i][j]),None)
        if v is None:continue
        M[h],M[v]=M[v],M[h]
        inv=pow(M[h][j],-1,p)
        M[h]=[(inv*z)%p for z in M[h]]
        for i in range(R):
            if i!=h and M[i][j]:
                t=M[i][j]
                M[i]=[(u-t*z)%p for u,z in zip(M[i],M[h])]
        h+=1
        if h==R:break
    return h

def matrices(m,p,z):
    # Vertices source s=0, middle a_i=1+i, sink t=m+1.
    edges=[(0,i+1) for i in range(m)]+[(i+1,m+1) for i in range(m)]
    D1=[[0]*(2*m) for _ in range(m+2)]
    for j,(u,v) in enumerate(edges):
        D1[u][j]=z;D1[v][j]=1
    # The square differences form a basis of Omega_2.
    # root differential: boundary(s,a,t)=(a,t)+z(s,t)+z^2(s,a).
    D2=[[0]*(m-1) for _ in range(2*m)]
    for j in range(m-1):
        D2[j][j]=z*z;D2[m-1][j]=-(z*z)
        D2[m+j][j]=1;D2[2*m-1][j]=-1
    D12=[[sum(D1[i][k]*D2[k][j] for k in range(2*m))%p for j in range(m-1)] for i in range(m+2)]
    return D1,D2,D12

def expected(m,N,q):
    if N==2:return (1,0,0)
    b0= 1 if q==N-1 else 3 if q==N-2 else m+2
    b1= m-1 if q==1 else m+1 if q==N-1 else 2*m
    b2= m-1 if q>=3 else 0
    return b0,b1,b2

cases=0
for N in range(2,9):
    p,z=prime_root(N)
    for m in range(2,10):
        D1,D2,D12=matrices(m,p,z)
        ranks=(rank(D1,p),rank(D2,p),rank(D12,p))
        assert ranks==(m+1,m-1,(0 if N==2 else m-1)),(N,m,ranks)
        for q in range(1,N):
            r0= (ranks[0] if N-q==1 else ranks[2] if N-q==2 else 0)
            b0=m+2-r0
            b1= (2*m-ranks[0] if q==1 else 2*m)-(ranks[1] if N-q==1 else 0)
            b2= (m-1 - (ranks[1] if q==1 else ranks[2] if q==2 else 0))
            actual=(b0,b1,b2)
            assert actual==expected(m,N,q),(N,m,q,actual,expected(m,N,q))
            cases+=1
print(f'ALL_VERIFY_OK exact_modular_cases={cases} m=2..9 N=2..8 all_q primitive_roots')
