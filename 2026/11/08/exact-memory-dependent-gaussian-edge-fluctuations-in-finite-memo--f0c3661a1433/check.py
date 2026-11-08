#!/usr/bin/env python3
"""Exact finite-state checks for a binary finite-memory reinforced graph model.

Requires only Python 3 standard library. Execute: python3 check.py
The finite enumeration checks algebraic identities, not the functional CLT.
"""
from fractions import Fraction as F
from itertools import product

N_CHECKS = 0

def check(truth, note):
    global N_CHECKS
    N_CHECKS += 1
    if not truth:
        raise AssertionError(note)

def rising(x, m, d):
    z=F(1)
    for j in range(m):
        z *= x+j*d
    return z

def solve(A, rhs):
    n=len(A)
    a=[list(A[i])+[rhs[i]] for i in range(n)]
    for c in range(n):
        pivot=next((r for r in range(c,n) if a[r][c]),None)
        if pivot is None: raise ArithmeticError('singular linear system')
        a[pivot],a[c]=a[c],a[pivot]
        d=a[c][c]
        for j in range(c,n+1): a[c][j]/=d
        for r in range(n):
            if r!=c:
                d=a[r][c]
                for j in range(c,n+1): a[r][j] -= d*a[c][j]
    return [a[i][-1] for i in range(n)]

def inspect(M,rho,delta):
    states=list(product((0,1),repeat=M))
    idx={s:i for i,s in enumerate(states)}
    dim=len(states)
    P=[[F(0) for _ in range(dim)] for _ in range(dim)]
    pi=[]
    for i,s in enumerate(states):
        c=sum(s)
        pi.append(rising(rho,c,delta)*rising(1-rho,M-c,delta)/rising(F(1),M,delta))
        probability=(rho+delta*c)/(1+M*delta)
        for new,prob in ((0,1-probability),(1,probability)):
            P[i][idx[s[1:]+(new,)]]+=prob
        check(sum(P[i])==1,('transition',M,s))
    check(sum(pi)==1,('stationary normalized',M))
    for j in range(dim):
        check(sum(pi[i]*P[i][j] for i in range(dim))==pi[j],('stationary',M,j))
    avg=sum(pi[i]*states[i][-1] for i in range(dim))
    check(avg==rho,('mean',M))
    v=rho*(1-rho)
    c=v*delta/(1+delta)
    for d in range(1,M):
        pair=sum(pi[i]*(states[i][-1]-rho)*(states[i][-1-d]-rho) for i in range(dim))
        check(pair==c,('lag covariance',M,d))
    f=[F(s[-1])-rho for s in states]
    # Centered resolvent H=I-P+1*pi, with g solving Hg=f.
    H=[[F(int(i==j))-P[i][j]+pi[j] for j in range(dim)] for i in range(dim)]
    g=solve(H,f)
    for i in range(dim):
        check(sum(H[i][j]*g[j] for j in range(dim))==f[i],('Poisson solve',M,i))
    longvar=2*sum(pi[i]*f[i]*g[i] for i in range(dim))-sum(pi[i]*f[i]**2 for i in range(dim))
    D=1+2*M*delta + F(M*(M-1))*delta**2/(1+delta)
    check(longvar==v*D,('exact covariance-sum coefficient',M,longvar,v*D))
    a=delta/(1+M*delta)
    innovation_variance=sum(pi[i]*((rho+delta*sum(states[i]))/(1+M*delta))*(1-(rho+delta*sum(states[i]))/(1+M*delta)) for i in range(dim))
    check(innovation_variance/(1-M*a)**2==v*D,('innovation coefficient',M))
    # The exact vertex-edge count is an age-weighted sum: t-1 per universal draw.
    # Its expectation follows from one-step means and makes a separate normalization check.
    for n in range(2,M+5):
        check(sum((t-1)*rho for t in range(1,n+1))==rho*F(n*(n-1),2),('edge expectation',M,n))

for M in range(1,5):
    for rho,delta in ((F(2,5),F(3,2)),(F(1,3),F(1,2)),(F(5,7),F(2,3))):
        inspect(M,rho,delta)
print(f'PASS: {N_CHECKS} exact arithmetic assertions across 12 Markov chains, memory 1..4.')
