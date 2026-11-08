#!/usr/bin/env python3
"""Independent exact identities and reproducible finite checks for a Gaussian
trace-subtraction covariance risk law. Only Python standard library required.
Finite checks illustrate, but do not establish, asymptotic assertions.
"""
from fractions import Fraction as F
from math import sqrt, exp, erf
import random


def inverse2(a,b,c):
    """Inverse of [[a,b],[b,c]]."""
    determinant=a*c-b*b
    return (c/determinant,-b/determinant,a/determinant)


def trace_correction(kappa, eps=F(0)):
    """Compute exact Schur/boundary scalars for a 3-by-3 SPD family."""
    gamma=F(1,4)
    t11,t12,t22=inverse2(F(1),eps,kappa)
    c11,c12,c22=inverse2(F(3,4),eps,kappa)
    # e1^T T^{-2}e1 = ||T^{-1}e1||^2.
    a1=t11
    a2=t11*t11+t12*t12
    correction=gamma*a2/(1-gamma*a1)
    # u=normalize(S^{-1}e1); sigma_u=(S^{-1}e1)^T S^{-1}(S^{-1}e1) / ||S^{-1}e1||^2.
    p2=c11*c11+c12*c12
    p3=c11*(c11*c11+2*c12*c12)+c22*c12*c12
    sigma_u=p3/p2
    omega_exact=c11+c22-sigma_u
    return correction,sigma_u,omega_exact,(t11,t12,t22)


for k in (1,2,3,10,100,1000):
    k=F(k)
    correction,sigma,omega,Tinv=trace_correction(k)
    assert correction==F(1,3)
    assert sigma==F(4,3)
    assert omega==1/k
    assert Tinv==(1,F(0),1/k)
    for eps in (F(1,100), F(1,1000)):
        if eps*eps < F(3,4)*k:
            corr2,sig2,ome2,tinv2=trace_correction(k,eps)
            assert ome2>0
            assert corr2>0 and sig2>0


def two_node_lanczos_inverse_qf(u,v,kappa):
    norm=sqrt(u*u+v*v)
    x,y=u/norm,v/norm
    alpha=x*x+kappa*y*y
    rx,ry=(1-alpha)*x,(kappa-alpha)*y
    beta=sqrt(rx*rx+ry*ry)
    if beta<1e-12: return norm*norm/alpha
    x2,y2=rx/beta,ry/beta
    alpha2=x2*x2+kappa*y2*y2
    return norm*norm*alpha2/(alpha*alpha2-beta*beta)

rng=random.Random(29092026)
checks=0
for k in (1,2,5,10,100):
    for _ in range(600):
        u,v=rng.gauss(0,1),rng.gauss(0,1)
        exact=u*u+v*v/k
        computed=two_node_lanczos_inverse_qf(u,v,k)
        assert abs(computed-exact)<2e-9*max(1.,abs(exact)),(k,computed,exact)
        checks+=1


def p_n2(k):
    if k==1: return 1-2/exp(1)
    return 1-(k*exp(-1)-exp(-k))/(k-1)

for k in (1,2,10,100):
    ntrials=100000
    count=0
    for _ in range(ntrials):
        x=rng.gammavariate(1,2)
        y=rng.gammavariate(1,2)
        count+=(x+y/k<2)
    empirical=count/ntrials
    assert abs(empirical-p_n2(k))<0.013,(k,empirical,p_n2(k))
    checks+=ntrials

# Exact formula arises by cancellation of a known Schur/boundary correction.
for k in (1,5,30):
    correction,sigma,omega,Tinv=trace_correction(F(k))
    for _ in range(100):
        z1,z2=rng.gauss(0,1),rng.gauss(0,1)
        estimated_trace=z1*z1+z2*z2/k
        estimated_bulk=estimated_trace+float(correction)-float(sigma)
        assert abs(estimated_bulk-(estimated_trace-1))<1e-12
        checks+=1

# Finite numerical probes of central limit critical window, not an asymptotic proof.
for tau in (0.5,1,2):
    N=2500
    k=sqrt(N)/tau
    runs=25000
    failures=sum(rng.gammavariate(N/2,2)+rng.gammavariate(N/2,2)/k<N for _ in range(runs))
    observed=failures/runs
    predicted=(1+erf(-tau/2))/2 # Phi(-tau/sqrt(2))
    assert abs(observed-predicted)<0.02,(tau,observed,predicted)
    checks+=runs

# Boundary-probe exactness at epsilon=0 extends continuously to irreducible SPD matrices.
for k in (2,10,100):
    eps=F(1,100000)
    correction,sigma,omega,(t11,t12,t22)=trace_correction(F(k),eps)
    c0,s0,w0,_=trace_correction(F(k))
    assert abs(float(omega-w0))<1e-6
    for _ in range(200):
        z1,z2=rng.gauss(0,1),rng.gauss(0,1)
        qf=float(t11)*z1*z1+2*float(t12)*z1*z2+float(t22)*z2*z2
        est=qf+float(correction-sigma)
        lim=z1*z1+z2*z2/k-1
        assert abs(est-lim)<1e-3
        checks+=1

print('VERIFY_OK',checks,'finite checks; analytic proofs in RESULT.md')
