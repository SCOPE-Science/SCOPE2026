#!/usr/bin/env python3
"""Standard-library exact-rational verification of a two-row Markov Kaczmarz law.
Run: python verify_markov.py
"""
from fractions import Fraction as F
from math import sqrt


def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]

def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def scale(t,A):
    return [[t*A[i][j] for j in range(2)] for i in range(2)]

def outer(x):
    return [[x[i]*x[j] for j in range(2)] for i in range(2)]

def trace(A):
    return A[0][0]+A[1][1]

def quad(v,A):
    return sum(v[i]*A[i][j]*v[j] for i in range(2) for j in range(2))

def risk(c,p,a,b):
    t=c*c
    return (a+b+2*t*(p*a+(1-p)*b))/(1+t)

def transition_rate(c,alpha,beta):
    z=(2-alpha-beta)**2-4*((1-alpha)*(1-beta)-alpha*beta*c**4)
    return (float(2-alpha-beta)+sqrt(float(z)))/2

def opt_rate(c,p):
    z=abs(float(2*p-1)); t=float(c**4)
    return (z+sqrt(t+(1-t)*z*z))/(1+z)

def opt_risk_at_rate(c,r,a,b):
    t=float(c**4)
    z=(r*r-t)/(2*r-r*r-t)
    return float(a+b-c*c*abs(a-b)/(1+c*c)*z)

def verify(c,s,p,k,a,b):
    assert c*c+s*s==1
    alpha=(1-p)*k;beta=p*k
    assert 0<alpha<=1 and 0<beta<=1
    # Two-state chain reversibility: stationary masses pi_1=p, pi_2=1-p.
    assert p*alpha==(1-p)*beta
    u1=[F(1),F(0)]; v1=[F(0),F(1)]
    u2=[c,s];v2=[-s,c]
    P1=outer(v1);P2=outer(v2)
    c2=c*c
    q1=(b+c2*a)/(1+c2)
    q2=(a+c2*b)/(1+c2)
    S1=add(scale(q1,P1),scale(a,outer(u1)))
    S2=add(scale(q2,P2),scale(b,outer(u2)))
    # Reverse row transitions equal the forward transitions for two states.
    assert S1==add(scale((1-alpha)*quad(v1,S1)+alpha*quad(v1,S2),P1),scale(a,outer(u1)))
    assert S2==add(scale(beta*quad(v2,S1)+(1-beta)*quad(v2,S2),P2),scale(b,outer(u2)))
    Q=add(scale(p,S1),scale(1-p,S2))
    assert trace(Q)==risk(c,p,a,b)
    assert risk(c,F(1,2),a,b)==a+b
    # The homogeneous two-state conditional energy transfer is M.
    M=[[1-alpha,beta*c2],[alpha*c2,1-beta]]
    assert M[0][0]+M[1][1]==2-k
    det=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    assert det==1-k+alpha*beta*(1-c**4)
    rate=transition_rate(c,alpha,beta)
    iid=(1+sqrt(float(1-4*p*(1-p)*(1-c**4))))/2
    assert abs(rate-(1-float(k)*(1-iid)))<1e-12
    best=opt_rate(c,p)
    assert rate+1e-12>=best
    if k==1/max(p,1-p):
        assert abs(rate-best)<1e-12
        denom=2*best-best*best-float(c**4)
        z=(best*best-float(c**4))/denom
        assert abs(z-float(abs(2*p-1)))<1e-10
    # All feasible (p,k) at rate r are dominated in noise risk
    # by the rate-constrained optimal stationary frequency.
    assert float(risk(c,p,a,b))+1e-9>=opt_risk_at_rate(c,rate,a,b)
    return rate

n=0
triples=[(3,4,5),(5,12,13),(8,15,17),(7,24,25),(20,21,29)]
ps=[F(1,6),F(1,5),F(1,4),F(1,3),F(1,2),F(2,3),F(3,4),F(4,5),F(5,6)]
vs=[F(1,4),F(1),F(2),F(4),F(7)]
for C,S,H in triples:
    c,s=F(C,H),F(S,H)
    for p in ps:
        kmax=1/max(p,1-p)
        for k in [kmax*F(1,4),kmax*F(1,2),kmax*F(3,4),kmax]:
            for a in vs:
                for b in vs:
                    verify(c,s,p,k,a,b)
                    n+=1

# Exact benchmark: row normals (1,0),(3/5,4/5), stationary p=3/4.
c,s,p,a,b=F(3,5),F(4,5),F(3,4),F(1),F(4)
k=F(4,3);alpha=F(1,3);beta=F(1)
assert risk(c,p,a,b)==F(313,68)
assert risk(c,F(1,2),a,b)==5
rate=(25+2*sqrt(217))/75
iid=(25+sqrt(217))/50
assert abs(transition_rate(c,alpha,beta)-rate)<1e-14
assert rate < iid
assert abs(opt_risk_at_rate(c,rate,a,b)-float(F(313,68)))<1e-12
assert opt_rate(c,F(1,2))==float(c*c)
print('PASS: %d exact-rational Markov stationarity/spectrum instances;' %n)
print('        rate and constrained risk cross-checks, sharp endpoint example')
print('example: risk=%s, optimized Markov factor=%.12f, iid factor=%.12f' %(F(313,68),rate,iid))
