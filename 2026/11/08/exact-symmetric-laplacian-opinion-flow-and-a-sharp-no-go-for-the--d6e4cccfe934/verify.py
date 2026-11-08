"""Exact finite-state checks of a symmetric-exchange opinion generator.

Standard library only. This verifies identities from the printed mathematical
model, not any external implementation, and supplements the all-size proof.
"""
from fractions import Fraction as F
from itertools import product
import random


def matmul(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]


def generator(w, lam, s):
    n=len(w); states=list(product((0,1), repeat=n)); pos={v:k for k,v in enumerate(states)}
    N=len(states)
    q=[[F(0) for _ in range(N)] for _ in range(N)]
    for col,b in enumerate(states):
        for i in range(n):
            c=list(b);c[i]^=1
            rate=lam[i] * ((1+s[i])/2 if b[i]==1 else (1-s[i])/2)
            q[pos[tuple(c)]][col]+=rate
            q[col][col]-=rate
        for i in range(n):
            for j in range(n):
                if i==j or b[i]==b[j]:continue
                rate=(1-lam[i])*w[i][j]
                c=list(b);c[i],c[j]=c[j],c[i]
                q[pos[tuple(c)]][col]+=rate
                q[col][col]-=rate
    return states,q


def check(w, lam,s):
    n=len(w)
    states,q=generator(w,lam,s)
    assert all(sum(q[i][j] for i in range(len(states)))==0 for j in range(len(states)))
    c=[[F(0) if i==j else (1-lam[i])*w[i][j]+(1-lam[j])*w[j][i] for j in range(n)] for i in range(n)]
    M=[[-c[i][j] if i!=j else lam[i]+sum(c[i]) for j in range(n)] for i in range(n)]
    z=[[F(1-2*b[i]) for b in states] for i in range(n)]
    lhs=matmul(z,q)
    for i in range(n):
        for col,b in enumerate(states):
            expected=lam[i]*s[i]-sum((M[i][j]*z[j][col] for j in range(n)),F(0))
            assert lhs[i][col]==expected,(i,b,lhs[i][col],expected)
    return len(states)


def solve(a,b):
    n=len(a); q=[list(row)+[b[i]] for i,row in enumerate(a)]
    for j in range(n):
        piv=next(k for k in range(j,n) if q[k][j]!=0)
        q[j],q[piv]=q[piv],q[j]
        z=q[j][j];q[j]=[e/z for e in q[j]]
        for k in range(n):
            if k==j:continue
            z=q[k][j]
            q[k]=[q[k][t]-z*q[j][t] for t in range(n+1)]
    return [q[i][-1] for i in range(n)]


def examples():
    W=[[F(0),F(1),F(0)], [F(0),F(0),F(1)], [F(1,2),F(1,2),F(0)]]
    check(W,[F(0)]*3,[F(0)]*3)
    # Left-invariant distribution of the row-stochastic directed FJ flow
    stationary=solve([[W[j][i]-int(i==j) for j in range(3)] for i in range(2)] + [[F(1)]*3],[F(0),F(0),F(1)])
    assert stationary==[F(1,5),F(2,5),F(2,5)],stationary
    x0=[F(1),F(-1),F(-1)]
    exact=sum(x0,F(0))/3
    fj=sum((stationary[i]*x0[i] for i in range(3)),F(0))
    assert (exact,fj)==(F(-1,3),F(-3,5))
    C=[[W[i][j]+W[j][i] for j in range(3)] for i in range(3)]
    assert all(C[i][j]==C[j][i] for i in range(3) for j in range(3))
    W3=[[F(0),F(1),F(0)],[F(0),F(0),F(1)],[F(1),F(0),F(0)]]
    l=F(1,2); anchors=[F(1),F(0),F(-1)]
    check(W3,[l]*3,anchors)
    c=[[F(0) if i==j else (1-l)*(W3[i][j]+W3[j][i]) for j in range(3)] for i in range(3)]
    a=[[l*int(i==j)+(sum(c[i])-c[i][j] if i==j else -c[i][j]) for j in range(3)] for i in range(3)]
    exactanch=solve(a,[l*s for s in anchors])
    fja=[[int(i==j)-(1-l)*W3[i][j] for j in range(3)] for i in range(3)]
    fjanch=solve(fja,[l*s for s in anchors])
    assert exactanch==[F(1,4),F(0),F(-1,4)],exactanch
    assert fjanch==[F(3,7),F(-1,7),F(-2,7)],fjanch
    print('unanchored consensus: exchange =',exact,'directed FJ =',fj)
    print('anchored equilibrium: exchange =', exactanch,'directed FJ =',fjanch)


def randomized():
    rng=random.Random(42049)
    count=0
    for n in (2,3,4,5):
        for rep in range(12):
            w=[[F(0)]*n for _ in range(n)]
            for i in range(n):
                raw=[rng.randint(0,5) if j!=i else 0 for j in range(n)]
                if sum(raw)==0:raw[(i+1)%n]=1
                w[i]=[F(t,sum(raw)) for t in raw]
            lam=[F(rng.randint(0,4),4) for _ in range(n)]
            s=[F(rng.randint(-4,4),4) for _ in range(n)]
            check(w,lam,s)
            count+=1
    print('exact full-chain vs moment identity PASSED',count,'parameter matrices, dimensions 2-5')

if __name__=='__main__':
    examples(); randomized(); print('VERIFICATION PASSED')
