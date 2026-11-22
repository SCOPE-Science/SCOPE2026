#!/usr/bin/env python3
"""Direct finite-state and asymptotic checks for rooted biclique reset entropy.
All reported state-space checks use direct rational transition-matrix solves.
The infinitude of sizes/rates is established by the accompanying proof.
"""
from fractions import Fraction
from math import log, sqrt

CHECKS = 0

def check(condition, context=''):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(context)

def close(x, y, tol=2e-11):
    check(abs(float(x)-float(y)) < tol, (x,y))

def solve_linear(M, b):
    n=len(b)
    x=[list(row)+[v] for row,v in zip(M,b)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if x[i][j]), None)
        check(pivot is not None,'singular')
        x[j],x[pivot]=x[pivot],x[j]
        piv=x[j][j]
        x[j]=[v/piv for v in x[j]]
        for i in range(n):
            if i!=j and x[i][j]:
                t=x[i][j]
                x[i]=[v-t*w for v,w in zip(x[i],x[j])]
    return [row[-1] for row in x]

def matrix_entropy(a,b,r,root_in_A=True):
    # A={0,...,a-1}, B={a,...,a+b-1}; root 0 or a
    N=a+b; root=0 if root_in_A else a
    T=[[Fraction(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        T[i][root]+=r
        neigh=list(range(a,N)) if i<a else list(range(a))
        for j in neigh:
            T[i][j]+=(1-r)/len(neigh)
    # Direct invariant-law linear solve: (T^t-I) pi = 0; replace last row.
    A=[[T[j][i]-(1 if i==j else 0) for j in range(N)] for i in range(N)]
    A[-1]=[Fraction(1)]*N
    B=[Fraction(0)]*(N-1)+[Fraction(1)]
    pi=solve_linear(A,B)
    for x in pi:check(x>=0)
    check(sum(pi)==1)
    for j in range(N):check(sum(pi[i]*T[i][j] for i in range(N))==pi[j])
    entropy=0.
    for i in range(N):
        for p in T[i]:
            if p:entropy-=float(pi[i])*float(p)*log(float(p))
    return entropy,pi

def K(a,r):
    q=1-r
    if r==0:return 0.
    if r==1:return log(a)
    return log(q)+(r+q/a)*log1p_robust(a*r/q)

def log1p_robust(x):
    from math import log1p
    return log1p(x)

def formula(a,b,r):
    if r==0:return .5*log(a*b)
    if r==1:return 0.
    q=1-r
    H=-r*log(r)-q*log(q)
    return (H+q*log(a*b)-q*K(a,r))/(2-r)

def gain_limit(alpha,beta,c):
    if c==0:return 0.
    return .5*(c*(2-log(c*sqrt(alpha*beta)))-(c+1/alpha)*log1p_robust(alpha*c))

def c_star(alpha,beta):
    # solve alpha*c^2+c = 1/sqrt(alpha*beta)
    return 2/sqrt(alpha*beta)/(1+sqrt(1+4*alpha/sqrt(alpha*beta)))

def test():
    for a in range(1,5):
        for b in range(1,5):
            for rn,rd in [(0,1),(1,11),(1,4),(2,5),(3,4),(1,1)]:
                r=Fraction(rn,rd)
                direct,_=matrix_entropy(a,b,r)
                close(direct,formula(a,b,float(r)))
                if a!=b and 0<r<1:
                    other,_=matrix_entropy(a,b,r,False)
                    close(other,formula(b,a,float(r)))
                    check((direct>other)==(a<b), (a,b,r,direct,other))
                if 0<r<1:
                    # Independent divergence KL of nonroot-target row from uniform on A.
                    prob=[float(r)+(1-float(r))/a]+[(1-float(r))/a]*(a-1)
                    kval=sum(p*log(p*a) for p in prob if p)
                    close(kval,K(a,float(r)))
    for alpha,beta in [(1.,1.),(1.,2.),(2.,1.),(.7,3.),(3.,.7)]:
        c=c_star(alpha,beta)
        close(c*(1+alpha*c)*sqrt(alpha*beta),1,1e-13)
        check(gain_limit(alpha,beta,c)>0)
        check(gain_limit(alpha,beta,c)>gain_limit(alpha,beta,c*.8))
        check(gain_limit(alpha,beta,c)>gain_limit(alpha,beta,c*1.2))
        for n in [1000,3000,10000,30000]:
            a=round(alpha*n);b=round(beta*n)
            g=n*(formula(a,b,c/n)-.5*log(a*b))
            check(abs(g-gain_limit(alpha,beta,c))< 20*log(n)/n, (n,alpha,beta,g))
            # direct global grid near scaling, cannot certify global optimum
            candidates=[i*.025 for i in range(1,201)]
            values=[formula(a,b,x/n) for x in candidates]
            cgrid=candidates[max(range(len(values)),key=lambda i:values[i])]
            check(abs(cgrid-c)<.025, (cgrid,c))
    golden=(sqrt(5)-1)/2
    close(c_star(1.,1.),golden)
    close(gain_limit(1.,1.,golden),golden-.5*log(1+golden))
    print('CHECKS_OK',CHECKS)

if __name__=='__main__':test()
