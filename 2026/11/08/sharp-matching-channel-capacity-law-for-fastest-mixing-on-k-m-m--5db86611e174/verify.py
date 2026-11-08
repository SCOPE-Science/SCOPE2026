"""Exact-rational spot checks for a matched-channel bipartite Markov-chain theorem.

Run with Python 3 standard library: python3 verify.py.
These finite checks are supplements to, not substitutes for, the all-order proof.
"""
from fractions import Fraction as F

CHECKS = 0

def check(cond, message):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(message)

def optimal(m, a):
    assert m >= 2 and F(0) <= a <= F(1)
    threshold = F(2, 3*m)
    if a <= threshold:
        b = F(2) * (1 - 2*a) / (3*m - 4)
        c = F(m - 2) + m*a
        c /= 3*m - 4
        rho = F(m) * (1 - 2*a) / (3*m - 4)
    else:
        b = F(2) * (1 - a) / (3*m - 2)
        c = F(m) * (1 - a) / (3*m - 2)
        rho = (F(m-2) + 2*m*a)/(3*m-2)
    return b,c,rho

def objective(m,a,b):
    c = 1 - a - (m-1)*b
    assert b >= 0 and c >= 0
    return max(abs(2*c-1),abs(c+a-b),abs(c-a+b))

def matrix(m,a,b,c):
    n = 2*m
    P=[[F(0) for j in range(n)] for i in range(n)]
    for i in range(n): P[i][i] = c
    for i in range(m):
        for j in range(m):
            P[i][m+j]=P[m+j][i] = a if i == j else b
    return P

def matvec(P,v):
    return [sum(pij*vj for pij,vj in zip(row,v)) for row in P]

def spectral_certificate(m,a,b,c):
    P=matrix(m,a,b,c)
    check(all(v>=0 for row in P for v in row), 'negative entry')
    check(all(sum(row)==1 for row in P),'not stochastic')
    u=[F(1)]*(2*m)
    check(matvec(P,u)==u,'constant eigenspace')
    signs=[F(1)]*m+[F(-1)]*m
    check(matvec(P,signs)==[(2*c-1)*v for v in signs],'bipartition eigenspace')
    for i in range(m-1):
        w=[F(0)]*m
        w[i]=F(1);w[-1]=F(-1)
        vplus=w+w
        vminus=w+[-x for x in w]
        check(matvec(P,vplus)==[(c+a-b)*v for v in vplus], 'plus eigenspace')
        check(matvec(P,vminus)==[(c-a+b)*v for v in vminus], 'minus eigenspace')

cases=0
for m in range(2,13):
    t=F(2,3*m)
    values={F(0),F(1),t,F(1,10),F(1,5),F(1,3),F(1,2),F(7,10),t/2,(1+t)/2}
    for a in sorted(values):
        if not (0<=a<=1): continue
        b,c,rho=optimal(m,a)
        check(c+a+(m-1)*b==1,'mass identity')
        check(b>=0 and c>=0,'feasibility')
        check(objective(m,a,b)==rho,'attained spectrum')
        rlow=F(m)*(1-2*a)/(3*m-4)
        rhigh=(F(m-2)+2*m*a)/(3*m-2)
        check(rho==max(rlow,rhigh),'piecewise envelope')
        spectral_certificate(m,a,b,c)
        for k in range(121):
            trial_b=F(k,120)*(1-a)/(m-1)
            check(objective(m,a,trial_b)>=rho,'finite trial contradicts lower bound')
            cases+=1
# Interval theorem: optimum is projected matching probability
for m in range(2,13):
    t=F(2,3*m)
    for ell in [F(0),F(1,10),F(1,4),F(1,2)]:
        for high in [F(1,4),F(1,2),F(3,4),F(1)]:
            if ell>high: continue
            a=max(ell,min(t,high))
            rho=optimal(m,a)[2]
            for k in range(121):
                trial=ell+(high-ell)*F(k,120)
                check(optimal(m,trial)[2]>=rho,'interval projection failure')
print('PASS exact-rational tests:',CHECKS,'checks; feasible b comparisons:',cases)
