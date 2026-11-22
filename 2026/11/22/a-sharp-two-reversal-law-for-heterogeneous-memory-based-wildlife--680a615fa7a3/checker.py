"""Reproduce exact two-switch recapture hazard calculations (standard Python)."""
import math
import random
from fractions import Fraction as Q


def log_ratio(rho, x0, s, a, w2, sigma2, log_gain):
    V = w2 + sigma2*(1-rho*rho)
    m = s + (x0-s)*rho
    return log_gain + (2*a*m)/V


def quadratic(rho, x0, s, a, w2, sigma2, log_gain):
    V = w2+sigma2*(1-rho*rho)
    return log_gain*V+2*a*(s+(x0-s)*rho)


def two_switch_criterion(x0, s, a, w2, sigma2, eta):
    if eta==0: return False
    qa=-eta*sigma2
    qb=2*a*(x0-s)
    qc=eta*(w2+sigma2)+2*a*s
    vertex=-qb/(2*qa)
    if not 0 < vertex < 1: return False
    F0=qc;F1=qa+qb+qc; Fv=qa*vertex*vertex+qb*vertex+qc
    return qa*F0 > 0 and qa*F1 > 0 and qa*Fv < 0


def roots(x0,s,a,w2,sigma2,eta):
    A=-eta*sigma2;B=2*a*(x0-s);C=eta*(w2+sigma2)+2*a*s
    if A==0:
        return [-C/B] if B else []
    disc=B*B-4*A*C
    if disc<0: return []
    d=math.sqrt(disc)
    return sorted([(-B-d)/(2*A),(-B+d)/(2*A)])

# Exact rational evidence for a natural OU-kernel competitor pair.
a=Q(1);w2=Q(1,10);sigma2=Q(1);x0=Q(23,160);s=Q(103,160);eta=Q(-1)
A=-eta*sigma2;B=2*a*(x0-s);C=eta*(w2+sigma2)+2*a*s
assert (A,B,C)==(Q(1),Q(-1),Q(3,16))
assert A*Q(1,4)**2+B*Q(1,4)+C==0
assert A*Q(3,4)**2+B*Q(3,4)+C==0
assert A*Q(1,2)**2+B*Q(1,2)+C==Q(-1,16)
assert A*0+B*0+C==Q(3,16)
assert A+B+C==Q(3,16)
assert s>0 and x0>0 and x0<s<a
assert two_switch_criterion(float(x0),float(s),1,.1,1,-1)
r = roots(float(x0),float(s),1,.1,1,-1)
assert all(abs(u-v)<1e-12 for u,v in zip(r,[.25,.75]))
# Time moves from rho=1 to rho=0, so preference + -> - -> +.
for rho,expect in [(.95,1),(.9,1),(.5,-1),(.2,1),(.05,1)]:
    L=log_ratio(rho,float(x0),float(s),1,.1,1,-1)
    assert L*expect>0

rng=random.Random(20261119)
assertions=17
for i in range(20000):
    x0=rng.uniform(-3,3);s=rng.uniform(-3,3)
    a=rng.uniform(.01,3);w2=rng.uniform(.01,3)
    sig2=rng.uniform(.01,4);eta=rng.uniform(-4,4)
    rho=rng.random()
    V=w2+sig2*(1-rho*rho)
    plus=math.log(0.8)+eta-.5*(a-(s+(x0-s)*rho))**2/V
    minus=math.log(0.8)-.5*(-a-(s+(x0-s)*rho))**2/V
    L=log_ratio(rho,x0,s,a,w2,sig2,eta)
    assert math.isclose(plus-minus,L,rel_tol=2e-12,abs_tol=2e-12)
    assertions+=1
    assert math.isclose(quadratic(rho,x0,s,a,w2,sig2,eta),V*L,rel_tol=2e-12,abs_tol=2e-12)
    assertions+=1
    if abs(eta)>1e-6:
        rr=[x for x in roots(x0,s,a,w2,sig2,eta) if 0<x<1]
        good=two_switch_criterion(x0,s,a,w2,sig2,eta)
        assert good == (len(rr)==2 and abs(rr[0]-rr[1])>1e-8)
        assertions+=1
print('PASS', assertions, 'formula, root and criterion assertions')
print('Exact polynomial coefficients: 1,-1,3/16')
print('First tie time = log(4/3)/kappa; second tie time = log(4)/kappa')
