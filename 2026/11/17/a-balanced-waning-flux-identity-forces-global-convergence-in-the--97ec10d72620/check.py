#!/usr/bin/env python3
"""Exact balance and mixed-entropy identities for a prevalence-driven four-class model.

Requires the Python standard library only. This is supplementary finite verification,
not a substitute for the analytic argument.
"""
from fractions import Fraction as Q
from random import Random
from math import sqrt

rng = Random(20261114)
N = 0
for _ in range(2400):
    mu, alpha, delta = (Q(rng.randrange(1,19),rng.randrange(1,12)) for j in range(3))
    sigma = Q(rng.randrange(1,10),10)
    gamma = sigma*delta
    eps = Q(rng.randrange(0,30),rng.randrange(1,13))
    beta = (mu+alpha)*Q(rng.randrange(11,31),10)
    w = [rng.randrange(1,101) for j in range(4)]
    S,I,R,C = (Q(z,sum(w)) for z in w)
    G=1+eps*I
    ds=mu*(1-S)-beta*S*I+gamma*G*C
    di=beta*S*I+sigma*beta*C*I-(mu+alpha)*I
    dr=(1-sigma)*beta*C*I+alpha*I-mu*R-delta*G*R
    dc=delta*G*R-beta*C*I-mu*C-gamma*G*C
    U=R+(1-sigma)*C
    assert ds+di+dr+dc==0
    assert di==I*(beta-mu-alpha-beta*(I+U))
    assert dr+(1-sigma)*dc==alpha*I-(mu+gamma*G)*U
    assert dc==delta*G*U-(beta*I+mu+(gamma+(1-sigma)*delta)*G)*C
    # Positive equilibrium closed form and Lyapunov derivative, float arithmetic
    v=float(1-(mu+alpha)/beta)
    a=float(mu+gamma); b=float(gamma*eps); alf=float(alpha); bf=float(beta)
    if b:
        # cancellation-safe quadratic positive root
        B=a+alf-b*v
        i0=2*a*v/(B+sqrt(B*B+4*b*a*v)) if B>=0 else (-B+sqrt(B*B+4*b*a*v))/(2*b)
    else:
        i0=a*v/(a+alf)
    u0=v-i0
    assert i0>0 and u0>0
    assert abs(alf*i0-(a+b*i0)*u0)<2e-8*max(1,alf*i0)
    coef=bf/(alf-b*u0)
    assert coef>0
    i=float(I);u=float(U)
    diffi=i-i0; diffu=u-u0
    ip=i*(bf*v-bf*i-bf*u)
    up=alf*i-(a+b*i)*u
    dV=diffi*ip/i+coef*diffu*up
    minus= -bf*diffi**2-coef*(a+b*i)*diffu**2
    assert abs(dV-minus)<1e-7*max(1,abs(minus))
    # The critical balance equality is exact, not numerically fitted.
    assert gamma==sigma*delta
    N+=1
print('PASS:',N,'independent rational vector-field and floating entropy-identity trials')
