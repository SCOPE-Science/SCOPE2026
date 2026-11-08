#!/usr/bin/env python3
"""Finite exact checks for the joint-degree covariance formulas of two correlated uniform-attachment trees.

The checks support, but do not replace, the asymptotic martingale argument.
Run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import product

K = 7
checks = 0

def check(x, y):
    global checks
    assert x == y, (x, y)
    checks += 1

def at(a, i, j):
    return a[i][j] if i >= 0 and j >= 0 else F(0)

def coefficient_tables(alpha):
    p = [F(1, 2**(i+1)) for i in range(K+1)]
    q = [[F(0) for _ in range(K+1)] for _ in range(K+1)]
    S = [[F(0) for _ in range(K+1)] for _ in range(K+1)]
    C = [[F(0) for _ in range(K+1)] for _ in range(K+1)]
    h = [[F(0) for _ in range(K+1)] for _ in range(K+1)]
    for i,j in product(range(K+1),repeat=2):
        q[i][j] = (int(i==0 and j==0) + (1-alpha)*(at(q,i-1,j)+at(q,i,j-1)) + alpha*at(q,i-1,j-1))/(3-alpha)
        h[i][j] = q[i][j] - p[i]*p[j]
    for i,j in product(range(K+1),repeat=2):
        S[i][j] = alpha*(at(h,i,j)-at(h,i-1,j)-at(h,i,j-1)+at(h,i-1,j-1))
        C[i][j] = (S[i][j]+at(C,i-1,j)+at(C,i,j-1))/3
    return p,q,S,C

def multiply(a,b):
    ret = [[F(0) for _ in range(K+1)] for _ in range(K+1)]
    for i,j in product(range(K+1),repeat=2):
        if not a[i][j]: continue
        for k,l in product(range(K+1-i),range(K+1-j)):
            ret[i+k][j+l] += a[i][j]*b[k][l]
    return ret

def sparse(terms):
    a=[[F(0) for _ in range(K+1)] for _ in range(K+1)]
    for (i,j),v in terms.items(): a[i][j]=v
    return a

for alpha in [F(0),F(1,5),F(1,3),F(1,2),F(4,5),F(1)]:
    p,q,S,C = coefficient_tables(alpha)
    # The simplified four-factor rational generating function.
    denom = sparse({(0,0):F(3),(1,0):F(-1),(0,1):F(-1)})
    for factor in [sparse({(0,0):F(2),(1,0):F(-1)}),
                   sparse({(0,0):F(2),(0,1):F(-1)}),
                   sparse({(0,0):3-alpha,(1,0):alpha-1,(0,1):alpha-1,(1,1):-alpha})]:
        denom = multiply(denom,factor)
    numerator=multiply(sparse({(0,0):F(1),(1,0):F(-2),(2,0):F(1)}),
                       sparse({(0,0):F(1),(0,1):F(-2),(0,2):F(1)}))
    lhs=multiply(denom,C)
    for i,j in product(range(K+1),repeat=2):
        check(lhs[i][j],alpha*(1+alpha)*numerator[i][j])
    a=alpha
    check(q[0][0],1/(3-a))
    check(q[0][1],(1-a)/(3-a)**2)
    check(q[1][0],(1-a)/(3-a)**2)
    check(q[1][1],(2-a+a*a)/(3-a)**3)
    check(C[0][0],a*(a+1)/(12*(3-a)))
    check(C[0][1],-a*(a+1)*(15-a)/(72*(3-a)**2))
    check(C[1][0],-a*(a+1)*(15-a)/(72*(3-a)**2))
    check(C[1][1],a*(a+1)*(5*a*a-18*a+297)/(432*(3-a)**3))
    check(C[0][0]*C[1][1]-C[0][1]**2,a*a*(a+1)**2*(a*a+3*a+18)/(1296*(3-a)**4))
    if a==1:
        check(C[0][0],F(1,12))
        check(C[0][1],F(-7,72))
        check(C[1][1],F(71,432))
    if a==0:
        for i,j in product(range(K+1),repeat=2): check(C[i][j],0)

# Enumerate all parent pairs exactly to confirm the one-step joint innovation law.
# A chosen parent of child-count k causes generating increment 1+(z-1)z^k.
for alpha in [F(0),F(1,3),F(1,2),F(1)]:
    for d1,d2 in [( (0,),(0,)), ((1,0),(0,1)), ((2,1,0,0),(1,0,1,1)), ((0,1,0,2,1),(1,2,1,0,0))]:
        n=len(d1)
        for k,l in product(range(3),repeat=2):
            # Z_k increment: 1_{k=0}+1_{parent has k-1 children}-1_{parent has k children}.
            def inc(d,idx,k):
                return int(k==0)+int(d[idx]==k-1)-int(d[idx]==k)
            def mean(d,k):
                return F(1 if k==0 else 0)+sum((int(v==k-1)-int(v==k) for v in d),0)/F(n)
            cov=F(0)
            for i,j in product(range(n),repeat=2):
                mass=(alpha/F(n) if i==j else F(0))+(1-alpha)/F(n*n)
                cov+=mass*(inc(d1,i,k)-mean(d1,k))*(inc(d2,j,l)-mean(d2,l))
            g1=[int(v==k-1)-int(v==k) for v in d1]
            g2=[int(v==l-1)-int(v==l) for v in d2]
            theor=alpha*(sum(x*y for x,y in zip(g1,g2))/F(n) - sum(g1)*sum(g2)/F(n*n))
            check(cov,theor)

print('VERIFIED',checks,'exact rational assertions')
