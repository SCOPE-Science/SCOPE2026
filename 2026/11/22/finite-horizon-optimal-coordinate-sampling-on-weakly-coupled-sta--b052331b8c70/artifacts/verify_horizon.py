"""Independent matrix recurrences and numerical asymptotic checks for finite-horizon coordinate descent."""
from fractions import Fraction as F
from itertools import product
from math import sqrt
import numpy as np
from scipy.optimize import minimize_scalar

checks=0

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return [list(x) for x in zip(*A)]
def add(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(A,k):return [[k*x for x in row] for row in A]
def ident(n):return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def sub(A,B):return add(A,scale(B,-1))
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def outer(x,y):return [[a*b for b in y] for a in x]

# Exact rational test for four leaves and root coupling epsilon=3/5.
m=4; n=m+1; eps=F(3,5)
v0=[-F(3,10)]*m+[F(4,5)]
V=[v0]+[[F(int(i==j)) for i in range(m)]+[F(0)] for j in range(m)]
V=tr(V)
G=mul(tr(V),V)
assert all(G[i][i]==1 for i in range(n));checks+=n
assert all(G[i][j]==0 for i in range(1,n) for j in range(1,n) if i!=j);checks+=m*(m-1)
assert all(G[0][i]==-F(3,10) for i in range(1,n));checks+=m
p=F(2,7);q=(1-p)/m;probs=[p]+[q]*m
I=ident(n)
P=[outer([V[k][i] for k in range(n)],[V[k][i] for k in range(n)]) for i in range(n)]
J=[sub(I,Pi) for Pi in P]
Q=[]
for i in range(n):
    Ei=ident(n)
    for j in range(n):Ei[i][j]-=G[i][j]
    Q.append(Ei)
Fmat=ident(n); Emat=G
for t in range(1,9):
    Fmat=sum_matrices=[scale(mul(mul(J[i],Fmat),J[i]),probs[i]) for i in range(n)]
    Fmat=sum_matrices[0]
    for e in sum_matrices[1:]:Fmat=add(Fmat,e)
    mats=[scale(mul(mul(tr(Q[i]),Emat),Q[i]),probs[i]) for i in range(n)]
    Emat=mats[0]
    for e in mats[1:]:Emat=add(Emat,e)
    other=mul(mul(tr(V),Fmat),V)
    assert Emat==other, ('energy matrices differ',t)
    checks+=n*n
    if t==2:
        delta=eps*eps
        a=-2*p+p*p-delta*p*q
        b=-2*q+q*q-delta*p*q/m
        c=2*p*q
        S=ident(n); S[-1][-1]=0
        U=P[0]
        expected=add(add(add(I,scale(U,a)),scale(S,b)),scale(add(mul(U,S),mul(S,U)),c))
        assert expected==Fmat
        checks+=n*n

# Floating-point finite-horizon exact matrix recurrence and weak-coupling optima.
def risk(m,eps,p,T):
    q=(1-p)/m;n=m+1
    V=np.eye(n)
    V[:m,0]=-eps/sqrt(m)
    V[m,0]=sqrt(1-eps*eps)
    # columns 1,..,m must be leaf basis vectors, and the final row is hub complement
    for j in range(m):
        V[:,j+1]=0
        V[j,j+1]=1
    probs=np.r_[p,np.full(m,q)]
    X=np.eye(n)
    J=[np.eye(n)-np.outer(V[:,i],V[:,i]) for i in range(n)]
    for _ in range(T):
        X=sum(probs[i]*(J[i]@X@J[i]) for i in range(n))
    return np.linalg.eigvalsh(X)[-1]

def kt(m,T):
    return (m-1)*sqrt(m)/(m+1)**2*sum((1-1/m)**j for j in range(T))/T

for m in [2,3,4,7]:
    for T in [1,2,3,5]:
        for eps in [0.002,0.0005]:
            u=1/(m+1)
            r=minimize_scalar(lambda p:risk(m,eps,p,T),bounds=(u-0.008,u+0.008),method='bounded',options={'xatol':3e-14})
            assert r.success
            kobs=(r.x-u)/eps
            assert abs(kobs-kt(m,T))<0.014, (m,T,eps,kobs,kt(m,T))
            checks+=1
        if T>1:
            assert kt(m,T)<kt(m,1)
            checks+=1
# Cross-check the full asymmetric-probability first-order star operator, not just equal leaves.
for m in [2,3,5]:
    n=m+1;u=1/n;r=1-u;s=(m-1)/n
    z=np.array([.5]+[(-.5/m)+.11*((-1)**i) for i in range(m)])
    z[1:]-=np.mean(z[1:])+.5/m
    assert abs(sum(z))<1e-12
    for T in [1,2,3,5]:
        eps=0.0001
        V=np.eye(n)
        V[:,0]=0
        V[0,0]=sqrt(1-eps*eps)
        V[1:,0]=-eps/sqrt(m)
        probs=np.full(n,u)+eps*z
        P=[np.outer(V[:,i],V[:,i]) for i in range(n)]
        X=np.eye(n)
        for _ in range(T):
            X=sum(probs[i]*((np.eye(n)-P[i])@X@(np.eye(n)-P[i])) for i in range(n))
        a=T*r**(T-1);h=r**T-s**T
        B=-a*np.diag(z)
        B[0,1:]+=h/sqrt(m);B[1:,0]+=h/sqrt(m)
        observed=(X-r**T*np.eye(n))/eps
        assert np.max(np.abs(observed-B))<.003, (m,T,np.max(np.abs(observed-B)))
        checks+=n*n

print(f'PASS: {checks} exact rational/matrix and numerical asymptotic assertions')
