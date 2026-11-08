"""Exact rational and finite-block tests for a geometric Lyapunov histogram law.

The formulas are proved in RESULT.md. The tests below check algebraic
consequences and independent finite signed-cocycle computations only.
"""
from fractions import Fraction as Q
from math import log, exp

checks = 0

def prefix(g, m, j):
    return g**m * (g**j-1)//(g-1)

def contrast(g, m, j, t):
    return g**m * (1-(-g)**j)//(g+1) + (-1)**j*t

# Independently accumulate signed blocks and compare every finite index.
for g in (2,3,4):
    m=1
    n=q=0
    for j in range(7):
        ell=g**(m+j)
        assert n==prefix(g,m,j)
        for t in range(ell+1):
            assert q==contrast(g,m,j,t)
            checks+=1
            if t<ell:
                q+=(-1)**j
                n+=1

# Verify the claimed normalized exponent bound using stable log-sum-exp.
a,b=log(3),log(2)
alpha,beta=1.3,-0.7
for g in (2,3,4):
    m=1
    n=q=0
    C=max(abs(log(alpha*alpha)),abs(log(beta*beta)),abs(log(alpha*alpha+beta*beta)))
    for j in range(7):
        ell=g**(m+j)
        for _ in range(ell):
            q+=(-1)**j;n+=1
            z=(a-b)*q
            max_z=abs(z)
            if z>=0:
                extra=log(alpha*alpha+beta*beta*exp(-2*max_z))
            else:
                extra=log(beta*beta+alpha*alpha*exp(-2*max_z))
            L=(a+b)/2+(max_z+extra)/(2*n)
            Z=2*(L-(a+b)/2)/(a-b)
            assert abs(Z-abs(q)/n)<=C/((a-b)*n)+1e-12
            checks+=1

# Closed CDF algebra, continuity and strict mid-block separation.
for g in (2,3,4,7):
    c=Q(1,g+1);d=Q(1,g-1);r=Q(g-1,g+1)
    for t in (Q(0),r/8,r/4,r/2,3*r/4,r):
        L=(c-d*t)/(1+t)
        U=(c+d*t)/(1-t)
        G=4*g*t/((g*g-1)*(1-t*t))
        assert 0<=L<=U<=1 and U-L==G
        Gc=(d*G+t*(c+d)/(1+t))/(d+c)
        assert Gc-G==t*(r-t)/(1-t*t)
        checks+=3
    assert Q(4*g*r,(g*g-1)*(1-r*r))==1
    checks+=1
assert Q(4*3*Q(1,4),(3**2-1)*(1-Q(1,4)**2))==Q(2,5)
checks+=1

# At large but finite third-base cutoffs, direct counting approaches two distinct limits.
g=3;m=1;j=11
start=prefix(g,m,j)
stop=start+g**(m+j)
partial=start+g**(m+j)//4
n=q=0
hits_full=hits_partial=0
for i in range(j+1):
    for _ in range(g**(m+i)):
        q+=(-1)**i;n+=1
        qualifies=4*abs(q)<=n
        hits_full+=qualifies
        if n<=partial:
            hits_partial+=qualifies
assert n==stop
full=hits_full/stop
quarter=hits_partial/partial
assert abs(full-0.4)<0.003
assert abs(quarter-7/15)<0.003
checks+=4
print('PASS',checks,'checks')
print('gamma=3 complete block CDF at 1/4',full,'limit 2/5')
print('gamma=3 quarter-phase CDF at 1/4',quarter,'limit 7/15')
