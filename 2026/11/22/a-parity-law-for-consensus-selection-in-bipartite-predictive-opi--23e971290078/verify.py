#!/usr/bin/env python3
"""Exact rational verification of a bipartite peer-prediction invariance theorem.
No external packages required. Checks are finite diagnostics, not an infinite proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def mm(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))] for i in range(len(A))]
def mv(A,v): return [sum((z*w for z,w in zip(row,v)),F(0)) for row in A]
def rv(v,A): return [sum((v[i]*A[i][j] for i in range(len(v))),F(0)) for j in range(len(A[0]))]
def add(A,B): return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]
def gauss(A,b):
    X=[list(row)+[v] for row,v in zip(A,b)]; n=len(A)
    for j in range(n):
        pivot=next(i for i in range(j,n) if X[i][j]); X[j],X[pivot]=X[pivot],X[j]
        d=X[j][j]; X[j]=[z/d for z in X[j]]
        for i in range(n):
            if i!=j:
                fac=X[i][j]
                X[i]=[u-fac*v for u,v in zip(X[i],X[j])]
    return [row[-1] for row in X]
def connected(m,n,edges):
    nbr=[set() for _ in range(m+n)]
    for i,j in edges: nbr[i].add(m+j);nbr[m+j].add(i)
    seen={0};todo=[0]
    while todo:
        for z in nbr[todo.pop()]:
            if z not in seen:seen.add(z);todo.append(z)
    return len(seen)==m+n

def test(m,n,edges,a,b,K,rep,weights=None):
    N=m+n;D=[F(0) for _ in range(N)];A=[[F(0) for j in range(N)] for i in range(N)]
    for index,(i,j) in enumerate(edges):
        wt=F(1) if weights is None else weights[index]
        A[i][m+j]+=wt;A[m+j][i]+=wt;D[i]+=wt;D[m+j]+=wt
    W=[[A[i][j]/D[i] for j in range(N)] for i in range(N)]
    alpha=[a]*m+[b]*n
    Z=[[alpha[i]*W[i][j] for j in range(N)] for i in range(N)]
    B=[[F(i==j)*(1-alpha[i]) for j in range(N)] for i in range(N)]
    Psi=eye(N); f=eye(N)
    # FJ evolution matrix from xinit to xK (not ordinary Z^K)
    for _ in range(K): f=add(B,mm(Z,f))
    Psi=f
    E=sum(D[:m]);assert E==sum(D[m:]);
    t=(a*b)**((K-1)//2)
    if K%2==0:
        w=b*(1-a)/(a*(1-b)+b*(1-a))
    else:
        num=b*(1-a)+t*a*b*(1-b)
        den=a*(1-b)+b*(1-a)+t*a*b*(2-a-b)
        w=num/den
    pi=[w*D[i]/E if i<m else (1-w)*D[i]/E for i in range(N)]
    assert sum(pi)==1
    assert rv(pi,Psi)==pi, (m,n,a,b,K,rv(pi,Psi),pi)
    assert mv(Psi,[F(1)]*N)==[F(1)]*N
    inn=[F((i*7+rep*11)%13,12) for i in range(N)]
    beta=F(3,7)
    rhs=mv(Psi,[(1-beta)*v for v in inn])
    x=gauss([[F(i==j)-beta*Psi[i][j] for j in range(N)] for i in range(N)],rhs)
    assert sum((pi[i]*x[i] for i in range(N)),F(0))==sum((pi[i]*inn[i] for i in range(N)),F(0))
    # For high susceptibility exact rational equilibrium must almost be consensus (not check bound here).
    return 1

def main():
    rng=Random(434343)
    count=0
    for m in range(1,5):
      for n in range(1,5):
        all_edges=list(product(range(m),range(n)))
        graphs=[]
        if len(all_edges)<=8:
            for mask in range(1,1<<len(all_edges)):
                e=[x for j,x in enumerate(all_edges) if mask>>j&1]
                if connected(m,n,e):graphs.append(e)
        else:
            for _ in range(30):
                e=[x for x in all_edges if rng.random()<.63]
                if connected(m,n,e):graphs.append(e)
        for e in graphs[:50]:
          for a,b in [(F(1,5),F(4,5)),(F(2,3),F(1,4)),(F(1,2),F(1,2))]:
            for K in range(1,7): count+=test(m,n,e,a,b,K,count)
    # Additional exact tests on weighted and irregular bipartite networks.
    for m,n in [(2,3),(3,4),(4,4)]:
      all_edges=list(product(range(m),range(n)))
      for rep in range(24):
        edges=[(i,j) for i,j in all_edges if rng.random()<.72]
        if not connected(m,n,edges):continue
        weights=[F(rng.randrange(1,6),rng.randrange(1,5)) for _ in edges]
        for K in (1,2,3,4,5,6):
          count+=test(m,n,edges,F(2,7),F(5,9),K,rep,weights)
    a,b=F(1,5),F(4,5)
    w1=b/(a+b);w2=b*(1-a)/(a*(1-b)+b*(1-a))
    t=a*b
    w3=(b*(1-a)+t*a*b*(1-b))/(a*(1-b)+b*(1-a)+t*a*b*(2-a-b))
    assert (w1,w2,w3)==(F(4,5),F(16,17),F(224,245))
    print('PASS:',count,'exact stationary-measure and fixed-point identities on connected bipartite graphs; star hub weights',w1,w2,w3)
if __name__=='__main__':main()
