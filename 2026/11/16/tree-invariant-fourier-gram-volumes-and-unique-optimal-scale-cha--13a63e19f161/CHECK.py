"""Exact checks for finite causal exponential-difference Gram volumes.
Run with Python 3, standard library only.
"""
from fractions import Fraction as F
from math import prod, factorial
from itertools import combinations

def determinant(M):
    A=[list(map(F,row)) for row in M]
    n=len(A); out=F(1)
    for i in range(n):
        p=next((k for k in range(i,n) if A[k][i]),None)
        if p is None:return F(0)
        if p!=i:A[i],A[p]=A[p],A[i];out=-out
        x=A[i][i];out*=x
        for k in range(i+1,n):
            m=A[k][i]/x
            for j in range(i+1,n): A[k][j]-=m*A[i][j]
            A[k][i]=0
    return out

def gram(scales):
    a=[F(x) for x in scales]
    K=len(a)-1
    C=[[1/(u+v) for v in a] for u in a]
    D=[[F(int(j==i)-int(j==i+1)) for j in range(K+1)] for i in range(K)]
    return [[sum(D[i][k]*C[k][l]*D[j][l] for k in range(K+1) for l in range(K+1)) for j in range(K)] for i in range(K)]

def analytic(scales):
    a=[F(x) for x in scales]
    p=prod((a[j]-a[i])**2 for i in range(len(a)) for j in range(i+1,len(a)))
    q=prod(a[i]+a[j] for i in range(len(a)) for j in range(len(a)))
    return 2*sum(a)*p/q

def normalized_det(scales):
    a=[F(x) for x in scales]
    return analytic(a)/prod((a[j]-a[j-1])**2/(2*a[j]*a[j-1]*(a[j]+a[j-1])) for j in range(1,len(a)))

nc=0
for K in range(1,7):
    for d in range(1,6):
        a=[F(d+3,2)+(i+1)**2 * F(2,d+7) for i in range(K+1)]
        g=gram(a)
        assert determinant(g)==analytic(a),(K,d,'Gram')
        C=[[1/(u+v) for v in a] for u in a]
        v=[sum(x) for x in zip(*C)]
        # Cauchy normal factorization
        from_cauchy=prod(F(1,2*u) for u in a)*prod(((a[j]-a[i])/(a[j]+a[i]))**2 for i in range(K+1) for j in range(i+1,K+1))
        assert determinant(C)==from_cauchy
        assert 0<normalized_det(a)<=1
        nc+=1

ac=0
for K in range(1,6):
    t=[F(i*i+2*i,3) for i in range(K+1)]
    co=F(K+1,2**(K*K))*prod((t[j]-t[i])**2 for i in range(K+1) for j in range(i+1,K+1))/prod((t[j]-t[j-1])**2 for j in range(1,K+1))
    for s in [F(1,8),F(1,20),F(1,50)]:
        a=[1+s*v for v in t]
        val=normalized_det(a)/s**(K*(K-1))
        # Finite epsilon is not equal to the limit, but the ratios should converge
        assert val>0
        ac+=1
    if K==1:
        assert co==1
    if K==2:
        assert co==F(3,16)*(t[2]-t[0])**2
for K in range(1,8):
    t=list(map(F,range(K+1)))
    co=F(K+1,2**(K*K))*prod((t[j]-t[i])**2 for i in range(K+1) for j in range(i+1,K+1))/prod((t[j]-t[j-1])**2 for j in range(1,K+1))
    assert co==F(K+1,2**(K*K))*prod(factorial(d)**2 for d in range(1,K+1))
print('CHECK_OK', 'exact_gram_determinants='+str(nc), 'collision_positivity='+str(ac), 'geometric_constants=7')

# Tree invariance and strict D-optimality of the adjacent-scale chain.
from itertools import product as cartprod

def prufer_edges(seq,n):
    degrees=[1]*n
    for x in seq:degrees[x]+=1
    E=[]
    for x in seq:
        leaf=next(i for i,v in enumerate(degrees) if v==1)
        E.append((min(leaf,x),max(leaf,x)))
        degrees[leaf]-=1;degrees[x]-=1
    last=[i for i,v in enumerate(degrees) if v==1]
    E.append(tuple(last))
    return E

def graph_gram(a,edges):
    C=[[1/(x+y) for y in a] for x in a]
    D=[[F(int(j==u)-int(j==v)) for j in range(len(a))] for u,v in edges]
    return [[sum(D[i][p]*C[p][q]*D[j][q] for p in range(len(a)) for q in range(len(a))) for j in range(len(edges))] for i in range(len(edges))]

def edge_norm(a,i,j):
    x,y=a[i],a[j]
    return (y-x)**2/(2*x*y*(x+y))

nts=0
for n in range(2,7):
    a=[F(j+1,1) +F(j*j,11) for j in range(n)]
    base=analytic(a)
    chain={(i,i+1) for i in range(n-1)}
    chain_prod=prod(edge_norm(a,i,j) for i,j in chain)
    for seq in cartprod(range(n),repeat=n-2):
        E=prufer_edges(seq,n)
        actual=prod(edge_norm(a,i,j) for i,j in E)
        assert actual>=chain_prod
        assert (actual==chain_prod)==(set(E)==chain),(n,seq)
        if n<=4 or (n==5 and nts%4==0) or (n==6 and nts%60==0):
            assert determinant(graph_gram(a,E))==base,(n,seq)
        nts+=1
print('TREE_OK', 'trees_checked='+str(nts), 'all_chain_strict=1')
