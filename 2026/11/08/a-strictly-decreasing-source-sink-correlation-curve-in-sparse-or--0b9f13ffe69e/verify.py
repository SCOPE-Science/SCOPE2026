"""Independent exact checks of source/sink statistics in ordered Bernoulli DAGs.
Run: python3 verify.py
Standard library only.  These finite checks do not prove the asymptotic theorem.
"""
from fractions import Fraction as F
from itertools import product
from math import exp
from random import Random

CHECKS=0
def eq(a,b,description):
    global CHECKS
    if a != b:
        raise AssertionError((description,a,b))
    CHECKS+=1

def finite_check(n,p):
    q=1-p
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    m=len(edges)
    EU=[F(0) for _ in range(n)]
    EV=[F(0) for _ in range(n)]
    EUV=[[F(0) for _ in range(n)] for _ in range(n)]
    E0=F(0); E1=F(0); E00=F(0); E11=F(0); E01=F(0)
    for mask in range(1<<m):
        e=mask.bit_count(); weight=p**e*q**(m-e)
        indeg=[0]*n; outdeg=[0]*n
        for k,(i,j) in enumerate(edges):
            if (mask>>k)&1: outdeg[i]+=1; indeg[j]+=1
        u=[int(d==0) for d in indeg]; v=[int(d==0) for d in outdeg]
        s=sum(u); t=sum(v)
        E0+=weight*s; E1+=weight*t
        E00+=weight*s*s; E11+=weight*t*t; E01+=weight*s*t
        for i in range(n):
            EU[i]+=weight*u[i]
            EV[i]+=weight*v[i]
            for j in range(n):
                EUV[i][j]+=weight*u[i]*v[j]
    mean=(1-q**n)/p
    var=mean-(1-q**(2*n))/(p*(1+q))
    cov=q**(n-1)*(n*p-1+q**n)/p
    eq(E0,mean,f'ES n={n},p={p}')
    eq(E1,mean,f'EK n={n},p={p}')
    eq(E00-E0**2,var,f'VarS n={n},p={p}')
    eq(E11-E1**2,var,f'VarK n={n},p={p}')
    eq(E01-E0*E1,cov,f'Cov n={n},p={p}')
    for j in range(n):
        eq(EU[j],q**j,f'P source j={j}')
        eq(EV[j],q**(n-j-1),f'P sink j={j}')
        for i in range(n):
            expected=(p*q**(n+j-i-2)) if i<j else F(0)
            # Here j is source's index and i is sink's index.
            eq(EUV[j][i]-EU[j]*EV[i],expected,f'Cov(U_{j},V_{i})')

def conditional_martingale_check(n,p,j,old_edges):
    # vertices 0..n-1; reveal edges into target j (0-based).
    q=1-p
    R=[int(all(old_edges.get((i,k),0)==0 for k in range(i+1,j))) for i in range(j)]
    moments=[F(0)]*5 # E dx, E dy, E dx^2, E dy^2, E dx dy
    for bits in product((0,1),repeat=j):
        v=sum(bits); w=p**v*q**(j-v)
        dx=int(not any(bits))-q**j
        dy=q**(n-j-1)*sum(R[i]*((1-bits[i])-q) for i in range(j))
        for a,z in enumerate((dx,dy,dx*dx,dy*dy,dx*dy)):
            moments[a]+=w*z
    exp_vx=q**j*(1-q**j)
    exp_vy=p*q**(2*(n-j-1)+1)*sum(R)
    exp_cov=p*q**(n-1)*sum(R)
    eq(moments[0],0,'conditional martingale dx')
    eq(moments[1],0,'conditional martingale dy')
    eq(moments[2],exp_vx,'conditional variance dx')
    eq(moments[3],exp_vy,'conditional variance dy')
    eq(moments[4],exp_cov,'conditional covariance dx dy')

for n in range(2,6):
    for p in (F(1,4),F(1,3),F(1,2),F(2,3)):
        finite_check(n,p)
finite_check(6,F(1,2))
rng=Random(20260319)
for p in (F(1,4),F(1,2),F(3,4)):
    for j in range(1,7):
        for rep in range(7):
            old={(i,k):rng.randrange(2) for k in range(1,j+1) for i in range(k)}
            conditional_martingale_check(7,p,j,old)

# Numerics: convergence of exact moments to sparse-limit matrix, no proof claim.
for c in (0.25,0.5,1.,2.,4.,8.):
    e=exp(-c)
    a=(1-e)**2/(2*c)
    b=e*(c-1+e)/c
    assert 0<b<a
    for n in (1000,10000):
        p=c/n;q=1-p
        mean=(1-q**n)/p
        var=mean-(1-q**(2*n))/(p*(1+q))
        cov=q**(n-1)*(n*p-1+q**n)/p
        assert abs(var/n-a)<0.015
        assert abs(cov/n-b)<0.015
        CHECKS+=2
    rho=2*e*(c-1+e)/(1-e)**2
    assert 0<rho<1
    CHECKS+=1
rhos=[]
for k in range(1,200):
    c=k/20
    e=exp(-c)
    rhos.append(2*e*(c-1+e)/(1-e)**2)
for a,b in zip(rhos,rhos[1:]):
    assert b<a
    CHECKS+=1
print('PASS:',CHECKS,'exact assertions and controlled numerical checks')
