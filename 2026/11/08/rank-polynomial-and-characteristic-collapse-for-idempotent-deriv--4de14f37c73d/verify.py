"""Finite-field checks for the rank census of idempotent derivations of bipartite graph Lie algebras.

Uses direct linear equations for the central-to-generator block, independent of
projector-eigenspace dimension counting. Only prime fields are tested here.
"""
from itertools import product
from math import prod
from collections import defaultdict


def mm(X,Y,p):
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y)))%p for j in range(len(Y[0]))] for i in range(len(X))]

def rank(M,p):
    M=[list(map(lambda x:x%p,row)) for row in M]
    if not M: return 0
    h=len(M);w=len(M[0]);s=0
    for j in range(w):
        k=next((k for k in range(s,h) if M[k][j]),None)
        if k is None: continue
        M[s],M[k]=M[k],M[s]
        inv=pow(M[s][j],-1,p)
        M[s]=[(v*inv)%p for v in M[s]]
        for i in range(h):
            if i!=s and M[i][j]:
                c=M[i][j]
                M[i]=[(a-c*b)%p for a,b in zip(M[i],M[s])]
        s+=1
        if s==h:break
    return s

def proj_matrices(size,p):
    out=[]
    for data in product(range(p),repeat=size*size):
        M=[list(data[i*size:(i+1)*size]) for i in range(size)]
        if mm(M,M,p)==M:out.append(M)
    return out

def gauss(n,k,q):
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))

def expected(a,b,q):
    dct=defaultdict(int)
    for i in range(a+1):
        for j in range(b+1):
            if q%2 and i*j:continue
            s=i*(b-j)+(a-i)*j
            t=i+j
            power=(a+b-t)*s+t*(a*b-s)
            count=(gauss(a,i,q)*q**(i*(a-i)) * gauss(b,j,q)*q**(j*(b-j))*q**power)
            dct[t+s]+=count
    return dict(dct)

def matrices(a,b,q):
    N=a+b;K=a*b
    hist=defaultdict(int)
    A_list=proj_matrices(a,q)
    B_list=proj_matrices(b,q)
    for A in A_list:
      for B in B_list:
        T=[[0]*N for _ in range(N)]
        for i in range(a):
          for j in range(a): T[i][j]=A[i][j]
        for i in range(b):
          for j in range(b): T[a+i][a+j]=B[i][j]
        S=[[0]*K for _ in range(K)]
        for i in range(a):
          for j in range(b):
            col=i*b+j
            for k in range(a): S[k*b+j][col]=(S[k*b+j][col]+A[k][i])%q
            for l in range(b): S[i*b+l][col]=(S[i*b+l][col]+B[l][j])%q
        if mm(S,S,q)!=S:continue
        # Construct the K*N linear equations in the K*N unknown central shears.
        # For phi=matrix unit at position (u,v), use S*phi+phi*T-phi.
        L=[[0]*(K*N) for _ in range(K*N)]
        for u in range(K):
          for v in range(N):
            col=u*N+v
            for i in range(K):
              for j in range(N):
                val=(S[i][u]*(j==v)+(i==u)*T[v][j]-(i==u and j==v))%q
                L[i*N+j][col]=val
        nullity=K*N-rank(L,q)
        # Actual operator rank of diagonal representative, computed by elimination.
        D=[[0]*(N+K) for _ in range(N+K)]
        for i in range(N):
          for j in range(N):D[i][j]=T[i][j]
        for i in range(K):
          for j in range(K):D[N+i][N+j]=S[i][j]
        assert mm(D,D,q)==D
        hist[rank(D,q)]+=q**nullity
    return dict(hist),len(A_list),len(B_list)

if __name__=='__main__':
    for a,b,q in [(2,2,2),(2,2,3),(2,2,5),(2,3,2)]:
        observed, na, nb=matrices(a,b,q)
        predicted=expected(a,b,q)
        assert observed==predicted,(a,b,q,observed,predicted)
        print('RANK_HIST_OK',a,b,q,'projectors',na,nb,'ranks',observed)
    print('VERIFY_OK')
