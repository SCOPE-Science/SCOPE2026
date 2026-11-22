"""Exact-rational checks for first-neighborhood sparse approximate inverses on trees.
Standard Python only. Reproducibility checks support, but do not replace, the proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

checks = 0

def check(test, message):
    global checks
    checks += 1
    if not test:
        raise AssertionError(message)


def solve(M, b):
    n=len(b)
    a=[[F(x) for x in row]+[F(b[i])] for i,row in enumerate(M)]
    for i in range(n):
        k=next(k for k in range(i,n) if a[k][i])
        a[i],a[k]=a[k],a[i]
        z=a[i][i]
        a[i]=[v/z for v in a[i]]
        for j in range(n):
            if i==j:continue
            z=a[j][i]
            a[j]=[u-z*v for u,v in zip(a[j],a[i])]
    return [a[i][-1] for i in range(n)]


def edges_prufer(code, n):
    if n==1:return []
    deg=[1]*n
    for v in code: deg[v]+=1
    result=[]
    for v in code:
        u=next(i for i in range(n) if deg[i]==1)
        result.append((u,v))
        deg[u]-=1;deg[v]-=1
    u,v=[i for i in range(n) if deg[i]==1]
    result.append((u,v))
    return result


def data_tree(n, edges, mu):
    W=[[F(0) for _ in range(n)] for _ in range(n)]
    for u,v,w in edges:
        W[u][v]=W[v][u]=F(w)
    A=[[-W[i][j] if i!=j else F(mu)+sum(W[i]) for j in range(n)] for i in range(n)]
    return W,A


def sparse_inverse(W,A):
    n=len(A)
    B=[[F(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        J=[j]+[i for i in range(n) if W[j][i]>0]
        G=[[sum(A[k][i]*A[k][h] for k in range(n)) for h in J] for i in J]
        q=[A[j][i] for i in J]
        x=solve(G,q)
        for i,v in zip(J,x):B[i][j]=v
    return B


def formula(W,A,j):
    n=len(A)
    ne=[i for i in range(n) if W[i][j]>0]
    d=[A[i][i] for i in range(n)]
    s={i:sum(W[i][k]**2 for k in range(n) if k!=j) for i in ne}
    r={i:d[i]**2+s[i] for i in ne}
    V=sum((W[i][j]**2/r[i] for i in ne),F(0))
    D=d[j]-sum((W[i][j]**2*d[i]/r[i] for i in ne),F(0))
    E=sum((W[i][j]**2*s[i]/r[i] for i in ne),F(0))
    Z=D**2+(1+V)*E
    out={j:D/Z}
    for i in ne:
        out[i]=W[j][i]*(d[i]*D-E)/(r[i]*Z)
    return out

# Enumerate all labelled unweighted trees through order 5, and compare every column
# to direct normal-equation solves at three positive shifts.
for n in range(1,6):
    for code in product(range(n),repeat=max(n-2,0)):
        es=edges_prufer(code,n)
        for mu in (F(1,3),F(1),F(5,2)):
            W,A=data_tree(n,[(u,v,1) for u,v in es],mu)
            B=sparse_inverse(W,A)
            for j in range(n):
                f=formula(W,A,j)
                for i,x in f.items():
                    check(B[i][j]==x,(n,code,mu,i,j,'formula'))
                    check(x>0,(n,code,mu,i,j,'positivity'))

# All weighted stars under a diverse range of edge weights and shifts.
for n in range(2,9):
    for z in range(12):
        rng=Random(n*100+z)
        edges=[(0,i,F(rng.randint(1,30),rng.randint(1,20))) for i in range(1,n)]
        W,A=data_tree(n,edges,F(rng.randint(1,6),rng.randint(1,7)))
        B=sparse_inverse(W,A)
        for j in range(n):
            for i,x in formula(W,A,j).items():
                check(x==B[i][j],('star formula',n,z,i,j))
                check(x>0,('star positive',n,z,i,j))

# Weighted P4 motif: one entry crosses the unique positive zero of the quartic.
for t in range(1,30):
    W,A=data_tree(4,[(0,1,1),(1,2,t),(2,3,t)],F(1))
    B=sparse_inverse(W,A)
    N=-t**4+6*t**3+21*t**2+14*t+3
    H=13*t**4+44*t**3+85*t**2+48*t+9
    check(B[0][1]==F(N,H),('P4 exact entry',t))
    check((B[0][1]>0)==(t<=8),('P4 integer sign',t))
check(sparse_inverse(*data_tree(4,[(0,1,1),(1,2,9),(2,3,9)],F(1)))[0][1]==F(-7,2445),'exact witness')

# Non-star larger tree with arbitrarily small positive attachments keeps the negative entry.
for n in range(5,9):
    for e in (F(1,1000),F(1,1000000)):
        es=[(0,1,1),(1,2,9),(2,3,9)]+[(k-1,k,e) for k in range(4,n)]
        W,A=data_tree(n,es,F(1))
        B=sparse_inverse(W,A)
        check(B[0][1]<0,('embedded P4 sign',n,e))
        for j in range(n):
            for i,v in formula(W,A,j).items():check(B[i][j]==v,('embedding formula',n,e,i,j))

print(f'PASS {checks} exact-rational assertion groups')
