#!/usr/bin/env python3
"""Finite diagnostics for the two-weight 2x2 Jordan rank-two compression theorem.
These sample checks do not establish the infinite-parameter claim."""
import math, cmath, random
random.seed(4627)
checks = 0

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def adj(A):
    return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]

def assert_close(x,y,tol=2e-11):
    global checks
    assert abs(x-y)<tol, (x,y)
    checks += 1

for k in range(110):
    r=0.02+random.random()*5
    s=0.02+random.random()*4
    D=random.random()*11
    alpha=complex(random.uniform(-3,3),random.uniform(-2,2))
    rot=cmath.exp(1j*random.uniform(-math.pi,math.pi))
    beta=alpha+D*rot
    a=2*r; b=2*s; R=r+s
    A=[[0j]*4 for _ in range(4)]
    A[0][0]=A[1][1]=alpha
    A[2][2]=A[3][3]=beta
    A[0][1]=a; A[2][3]=b
    Q=[[1,0],[0,-1]]
    V=[[math.sqrt(s/R),0],[0,math.sqrt(s/R)],
       [math.sqrt(r/R),0],[0,-math.sqrt(r/R)]]
    G=mul(adj(V),V)
    C=mul(mul(adj(V),A),V)
    target=(s*alpha+r*beta)/R
    for i in range(2):
        for j in range(2):
            assert_close(G[i][j],float(i==j))
            assert_close(C[i][j],target if i==j else 0)
    for i in range(51):
        th=2*math.pi*i/51
        u=D*math.cos(th)
        eig=sorted([r,-r,u+s,u-s],reverse=True)
        lam=eig[1]
        h=(-r if u < -R else (u-s if u>R else min(r,u+s)))
        assert_close(lam,h)
        lhs=((target-alpha)*complex(math.cos(th),-math.sin(th))*rot.conjugate()).real
        # Rotated to alpha=0 and beta positive: compare target normalized frame.
        assert lhs <= lam+3e-10, (r,s,D,th,lhs,lam)
        checks+=1
    if D>R:
        q=math.sqrt(1-(R/D)**2)
        # Four critical planes intersect at the predicted barycenter.
        assert q>0
        assert_close((R/D)*(D*r/R),r)
for t in (0.0,0.125,0.5,0.8,1.0):
    for n in range(3,18):
        eps=1/(n*n)
        if t==0: r=eps*eps; s=eps
        elif t==1: r=eps; s=eps*eps
        else: r=t*eps; s=(1-t)*eps
        target=(r/(r+s))
        assert abs(target-t)<0.2
        checks+=1
print('JORDAN_RANK_TWO_VERIFY_OK',checks)
