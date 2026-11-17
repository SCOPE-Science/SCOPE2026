"""Finite identity checks for the Ricker boundary-cycle threshold.
The analytic argument is in RESULT.md; these checks do not replace its proof.
"""
from fractions import Fraction as F
from math import log, exp, sqrt, tanh, isclose
from random import Random

# Symbolic rational witness: L=log(2), x=kL, gamma=1/(2L), beta=3/(7L).
def qw(k):
    return F(1, 2) + F(3, 7) * F(k, 1) / (1 + F(k, 2))
assert qw(2) == F(13, 14)
assert qw(4) == F(15, 14)
assert qw(3) == F(71, 70)
assert qw(2) * qw(4) == F(195, 196)
assert qw(3) > 1 > qw(2) * qw(4)
L = log(2)
r = 3*L
u, v = 2*L, 4*L
assert isclose(u*exp(r-u),v,rel_tol=1e-14)
assert isclose(v*exp(r-v),u,rel_tol=1e-14)
lambda_prey = (1-u)*(1-v)
assert 0 < lambda_prey < 1

# Check the exact Jensen-deficit identity with rational inputs.
rng=Random(29)
for _ in range(300):
    s=F(rng.randrange(1,19),20)
    gam=F(rng.randrange(1,18),9)
    rr=F(rng.randrange(21,61),10)
    tt=F(rng.randrange(1,16),10)
    beta=F(rng.randrange(1,40),13)
    assert tt < rr
    q=lambda x:s+beta*x/(1+gam*x)
    diff=q(rr)**2-q(rr-tt)*q(rr+tt)
    explicit=(beta*tt**2*(2*s*gam+beta+2*gam*(s*gam+beta)*rr)
        / ((1+gam*rr)**2 * ((1+gam*rr)**2-(gam*tt)**2)))
    assert diff == explicit and diff > 0

# Check strictly positive window and its small-amplitude coefficient for several parameter choices.
def values(t,s,gamma):
    rr=t/tanh(t/2)
    u=rr-t; v=rr+t
    hu=u/(1+gamma*u); hv=v/(1+gamma*v)
    be=(1-s)*(1+gamma*rr)/rr
    bc=(-s*(hu+hv)+sqrt(s*s*(hu+hv)**2+4*hu*hv*(1-s*s)))/(2*hu*hv)
    return rr,be,bc,(1-u)*(1-v)
for s,g in ((.25,.2),(.5,.7),(.8,3)):
    for t in (.01,.1,.3,.6):
        rr,be,bc,lp=values(t,s,g)
        assert 2<rr and be<bc and -1<lp<1
        beta=(be+bc)/2
        u=rr-t;v=rr+t
        q=lambda x:s+beta*x/(1+g*x)
        assert q(rr)>1 and q(u)*q(v)<1
    t=.005
    rr,be,bc,_=values(t,s,g)
    coefficient=3*(1-s)*(4*g+1-s)/(8*(1+2*g))
    assert abs((bc-be)/(rr-2)-coefficient) < .001
print('RICKER_BOUNDARY_TWO_CYCLE_CHECK_OK')
