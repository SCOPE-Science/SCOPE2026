#!/usr/bin/env python3
"""Exact arithmetic checks for overlapping-spacing squared-Gini cross-order covariance."""
import itertools
import math
from fractions import Fraction as F
import random

assertions=0

def check(flag,why):
    global assertions
    assert flag,why
    assertions+=1

def mm(A,B):
    return [[sum(A[i][r]*B[r][j] for r in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def trprod(A,B):
    return sum(A[i][j]*B[j][i] for i in range(len(A)) for j in range(len(A)))

def make_A(n,m):
    N=n-m+1
    B=[[int(i<=j<i+m) for j in range(n)] for i in range(N)]
    col=[sum(row[j] for row in B) for j in range(n)]
    return [[sum(B[h][i]*B[h][j] for h in range(N))-F(col[i]*col[j],N) for j in range(n)] for i in range(n)]

def cov_formula(n,m,k,A,B):
    u=sum(A[i][i] for i in range(n))
    v=sum(B[i][i] for i in range(n))
    c=trprod(A,B)
    d=sum(A[i][i]*B[i][i] for i in range(n))
    moment=(u*v+2*c+6*d)/math.prod(range(n,n+4))
    product=F(u*v,(n*(n+1))**2)
    scale=F(4*n**4,(n-m)*(n-k))
    return scale*(moment-product)

def brute_monomial_cov(n,m,k,A,B):
    # independently integrate the 4th-order Dirichlet monomials.
    f=lambda inds: F(math.prod(math.factorial(inds.count(i)) for i in set(inds)),math.prod(range(n,n+4)))
    Q=F(0)
    for i,j,a,b in itertools.product(range(n),repeat=4):
        Q+=A[i][j]*B[a][b]*f((i,j,a,b))
    tA=sum(A[i][i] for i in range(n));tB=sum(B[i][i] for i in range(n))
    return F(4*n**4,(n-m)*(n-k))*(Q-F(tA*tB,(n*(n+1))**2))

# Exact identity and structural zero-row sums.
for n in range(4,10):
    As={m:make_A(n,m) for m in range(1,n//2+1)}
    for m,A in As.items():
        for row in A: check(sum(row)==0,('row zero',n,m))
    for m in As:
        for k in As:
            val=cov_formula(n,m,k,As[m],As[k]);br=brute_monomial_cov(n,m,k,As[m],As[k])
            check(val==br,('exact Dirichlet integration',n,m,k,val,br))
            check(val>0,('positive sampled range',n,m,k))

# Fixed-order covariance coefficient vs numerical finite n.
def C(m,k):
    p=min(m,k);q=max(m,k)
    S=p*p*q-F(p*(p*p-1),3)
    return 8*(m*k+S)

for m,k in [(1,1),(1,2),(2,3),(2,5),(3,7),(5,8)]:
    val=C(m,k)
    check(val==C(k,m),('coefficient symmetry',m,k))
    if m==k: check(val==F(8*m*(m+1)*(2*m+1),3),('known marginal variance',m))
    for n in [max(40,2*k),max(80,2*k),max(160,2*k)]:
        A=make_A(n,m);B=make_A(n,k)
        cv=cov_formula(n,m,k,A,B)
        check(abs(float(n*cv/val)-1)<0.4,('finite-n convergence',n,m,k,float(n*cv/val)))

# Algebraic overlap identities, direct enumeration over all shifts.
for m in range(1,20):
    for k in range(1,20):
        p=min(m,k);q=max(m,k)
        ct=sum(sum(1 for z in range(m) if h<=z<h+k)**2 for h in range(-k+1,m))
        check(ct==p*p*q-F(p*(p*p-1),3),('overlap sum',m,k))

# Exact correlation kernel sequence and strict bounds.
for m in range(1,20):
    for k in range(1,20):
        corr=float(C(m,k)/(C(m,m)*C(k,k))**F(1,2)) if False else float(C(m,k))/math.sqrt(float(C(m,m)*C(k,k)))
        check(0<corr<=1.0000000001,('correlation',m,k,corr))

# Independent simulation of the actual Dirichlet statistic, not the matrix formula.
random.seed(1729)
n=8; m=1; k=3; count=60000
sx=sy=sxy=0.
for q in range(count):
    exp=[random.expovariate(1) for i in range(n)]
    s=sum(exp);d=[v/s for v in exp]
    def stat(order):
        ns=n-order+1
        v=[n*sum(d[i:i+order]) for i in range(ns)]
        return 2/(ns-1)*(sum(x*x for x in v)-sum(v)**2/ns)
    a=stat(m);b=stat(k)
    sx+=a;sy+=b;sxy+=a*b
sim=sxy/count-sx*sy/count**2
A=make_A(n,m);B=make_A(n,k);theory=float(cov_formula(n,m,k,A,B))
check(abs(sim-theory)<0.13,('Monte Carlo',sim,theory))
print('PASS',assertions,'assertions; exact covariance n=8,m=1,k=3:',theory,'simulation:',sim)
print('Asymptotic covariance n*Cov(m=2,k=3):',float(C(2,3)))
print('Two-stage correlation m/k=1/4:',(3-.25)*math.sqrt(.25)/2)
