"""Standalone exact checks for a finite neutral nonlinear social-imitation chain.

Run with Python >= 3.10; standard library only.
"""
from fractions import Fraction as Q
from math import comb, lgamma, log, exp, pi


def rates(N, m, i):
    x = Q(i, N)
    # Independent binomial exposure samples, followed by a neutral 1/2 Fermi event.
    ex = sum(Q(comb(m,k),1)*x**k*(1-x)**(m-k)*Q(k*k,m*m)
             for k in range(m+1))
    ey = sum(Q(comb(m,k),1)*x**k*(1-x)**(m-k)*Q((m-k)**2,m*m)
             for k in range(m+1))
    return (1-x)*ex/2, x*ey/2


def formula(N,m):
    weights=[Q(1)]
    for j in range(1,N):
        weights.append(weights[-1]*Q(m*(N-j)+j,m*j+N-j))
    S=sum(weights)
    return [Q(0)]+[sum(weights[:i])/S for i in range(1,N)]+[Q(1)],weights


def solve(A,b):
    n=len(b); mat=[list(A[i])+[b[i]] for i in range(n)]
    for j in range(n):
        row=next(i for i in range(j,n) if mat[i][j])
        mat[j],mat[row]=mat[row],mat[j]
        pivot=mat[j][j]; mat[j]=[v/pivot for v in mat[j]]
        for i in range(n):
            if i==j:continue
            coef=mat[i][j]
            mat[i]=[mat[i][t]-coef*mat[j][t] for t in range(n+1)]
    return [mat[i][-1] for i in range(n)]

checks=0
for N in range(2,24):
    for m in range(1,12):
        u,weights=formula(N,m)
        assert weights[0]==weights[-1]==1
        assert u[0]==0 and u[N]==1
        for i in range(1,N):
            plus,minus=rates(N,m,i)
            assert plus>0 and minus>0
            assert plus*(u[i+1]-u[i])==minus*(u[i]-u[i-1])
            if m>=2:
                assert minus/plus==Q(m*(N-i)+i,m*i+N-i)
            checks+=1
        assert all(u[i]+u[N-i]==1 for i in range(N+1))
        if N>=3 and m>=2:
            assert Q(1,2**(N-1)) < u[1] < Q(1,N)
            if m>2:
                assert u[1] < formula(N,m-1)[0][1]
        if m==1:
            assert all(u[i]==Q(i,N) for i in range(N+1))

# Independent absorption linear systems, not reuse of recursive differences.
for N in range(2,10):
    for m in range(1,8):
        A=[[Q(0) for j in range(N-1)] for i in range(N-1)]
        b=[Q(0) for j in range(N-1)]
        for i in range(1,N):
            p,q=rates(N,m,i)
            A[i-1][i-1]=p+q
            if i>=2:A[i-1][i-2]=-q
            if i<N-1:A[i-1][i]=-p
            if i==N-1:b[i-1]=p
        sol=solve(A,b)
        assert [Q(0)]+sol+[Q(1)]==formula(N,m)[0]
        checks+=1

# Analytic saddlepoint predictions checked against independent log-Gamma sums.
for m in (2,3,5,9):
    a=1/(m-1)
    I=(1+a)*log(1+a)+a*log(a)-2*(a+.5)*log(a+.5)
    assert 0<I<log(2)
    for N in (99,100,199,200,499,500):
        logs=[lgamma((1+a)*N)+lgamma(1+a*N)-lgamma((1+a)*N-k)
              -lgamma(a*N+k+1) for k in range(N)]
        z=max(logs)
        actual=-z-log(sum(exp(w-z) for w in logs))
        approx=-N*I+.5*log((1+a)/(pi*N*a*(a+.5)))
        assert abs(exp(actual-approx)-1)<.01, (m,N,actual,approx)
        checks+=1

print('VERIFY_OK',checks,'exact transitions, systems, asymptotic instances')
