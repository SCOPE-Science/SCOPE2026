#!/usr/bin/env python3
"""Exact rational sign certificates and numerical checks for a circularized log-score."""
from fractions import Fraction as Q
import math
import random

CHECKS=0

def check(cond, msg):
    global CHECKS
    assert cond,msg
    CHECKS+=1

def log_pos_interval(x,terms=22):
    """Exact rational enclosure of ln(x) for positive rational x, using atanh."""
    x=Q(x); check(x>0,'log positive')
    def primitive(y):
        z=(y-1)/(y+1)
        check(0<=z<=Q(1,3),'scaled argument')
        val=Q(0)
        for j in range(terms):
            val += Q(2)*z**(2*j+1)/(2*j+1)
        err=Q(2)*z**(2*terms+1)/((2*terms+1)*(1-z*z))
        return val,val+err
    k=0; y=x
    while y>=2: y/=2;k+=1
    while y<1: y*=2;k-=1
    lo,hi=primitive(y)
    L,U=primitive(Q(2))
    return (lo+k*L, hi+k*U) if k>=0 else (lo+k*U,hi+k*L)

def plus(a,b):return a[0]+b[0],a[1]+b[1]
def mul_pos(a,c):return a[0]*c,a[1]*c
def mul_neg(a,c):return a[1]*c,a[0]*c

def F_interval(N):
    v=(Q(N*N-2),Q(N*N-2))
    for i in range(1,N):
        v=plus(v,mul_pos(log_pos_interval(Q(i,N)),4*i))
    return v

def inc_interval(N):
    l=log_pos_interval(Q(N+1,N))
    v=(Q(2*N+1),Q(2*N+1))
    return plus(v,mul_neg(l,-2*N*(N+1)))

def H_interval(N):
    inc=inc_interval(N); F=F_interval(N)
    return N*inc[0]-F[1], N*inc[1]-F[0]

for N,expected_sign in [(20,-1),(21,1)]:
    L,U=F_interval(N)
    check(U<0 if expected_sign<0 else L>0,'F sign at boundary')
    print('F',N,'interval',float(L),float(U))
for N,expected_sign in [(54,1),(55,-1)]:
    L,U=H_interval(N)
    check(U<0 if expected_sign<0 else L>0,'H sign at boundary')
    print('H',N,'interval',float(L),float(U))

def collapsed(N):
    return N+1-2/N + (4/N)*sum(i*math.log(i/N) for i in range(1,N))

def beta_form(N):
    # Independent beta-log formula: E(log Beta(a,b)) = H_(a-1)-H_(a+b-1).
    H=[0.0]
    for k in range(1,N):H.append(H[-1]+1/k)
    val=0.0
    for i in range(1,N):
        mu=i/N
        e_log=H[i-1]-H[N-1]
        e_comp=H[N-i-1]-H[N-1]
        val += -2*(mu*(e_log-math.log(mu))+(1-mu)*(e_comp-math.log(1-mu)))
    return val

for N in range(2,201):
    a,b=collapsed(N),beta_form(N)
    check(abs(a-b)<5e-10,'independent beta expectation check')

for N in range(2,55):
    check(collapsed(N+1)>collapsed(N),'expectation increasing through maximum')
for N in range(55,130):
    check(collapsed(N+1)<collapsed(N),'expectation decreasing after maximum')
for N in range(2,21):
    check(collapsed(N)<1,'expectation less than one')
for N in range(21,120):
    check(collapsed(N)>1,'expectation exceeds one')

rng=random.Random(20261115)
def one_circular_score(N):
    raw=[rng.expovariate(1.) for _ in range(N)]
    total=sum(raw)
    d=[z/total for z in raw]
    double=d+d
    cs=[0.0]
    for x in double:cs.append(cs[-1]+x)
    v=0.0
    # Independent literal reconstruction of average pooling, not the collapsed
    # weighted-log-circular identity used to obtain the closed expectation.
    for c in range(N):
        for i in range(1,N):
            mu=i/N
            arc=max(1e-300,min(1.-1e-15,cs[c+i]-cs[c]))
            v += -2/N*(mu*math.log(arc/mu)+(1-mu)*math.log((1-arc)/(1-mu)))
    return v

for N in [2,3,6,20,21,55]:
    reps=15000 if N<=6 else 1400
    vals=[one_circular_score(N) for _ in range(reps)]
    mean=sum(vals)/reps
    var=sum((x-mean)**2 for x in vals)/(reps-1)
    stderr=math.sqrt(var/reps)
    theory=collapsed(N)
    check(abs(mean-theory)<6*stderr+0.003,'independent Dirichlet simulation check')
    print('simulation N',N,'mean',mean,'expected',theory,'SE',stderr)
print('PASSED',CHECKS,'assertions')
