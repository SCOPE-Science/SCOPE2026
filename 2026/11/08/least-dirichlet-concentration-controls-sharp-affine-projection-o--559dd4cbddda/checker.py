#!/usr/bin/env python3
"""Self-contained finite exact and numerical checks for affine Dirichlet projection formulas."""
from fractions import Fraction as Q
from math import comb, factorial, gamma, exp, pi
from itertools import combinations
from scipy.special import betainc, gammaln
from scipy.integrate import quad
import sympy as sp

def beta_cdf_int(a,b,t):
    # regularized incomplete beta for positive integers via binomial tail.
    return sum(Q(comb(a+b-1,j)) * t**j * (1-t)**(a+b-1-j)
               for j in range(a,a+b))

def norm_int(a,T):
    t=Q(a,T+1)
    return 1+2*(T*beta_cdf_int(a,T-a,t)-(T+1)*beta_cdf_int(a+1,T-a,t))

def norm_real(a,T):
    t=a/(T+1)
    return 1+2*(T*betainc(a,T-a,t)-(T+1)*betainc(a+1,T-a,t))

checks=0
# Verify Gram matrix inverse and kernel, all integer positive parameters for N=2..5.
for n in range(2,6):
    from itertools import product
    for alpha in product((1,2,3),repeat=n):
        T=sum(alpha)
        G=sp.Matrix(n,n,lambda i,j: sp.Rational(alpha[i]*(alpha[j]+(1 if i==j else 0)),T*(T+1)))
        Gi=sp.Matrix(n,n,lambda i,j: sp.Rational(T*(T+1),alpha[i])*int(i==j)-T)
        assert G*Gi==sp.eye(n)
        vals=[norm_int(a,T) for a in alpha]
        assert all(v>1 for v in vals)
        assert max(vals)==norm_int(min(alpha),T)
        for i,j in combinations(range(n),2):
            if alpha[i]<alpha[j]:assert vals[i]>vals[j]
            if alpha[i]==alpha[j]:assert vals[i]==vals[j]
        checks+=1
# Numerically integrate abs exact beta for noninteger a,T, including near zero.
checks_numerical=0
for T in (0.8,1.3,3.2,12.0):
    prev=None
    for aa in [0.08,0.17,0.27,0.41,0.65,0.87]:
        a=T*aa
        b=T-a
        norm=norm_real(a,T)
        beta_const=sp.beta(a,b).evalf(20)
        integral=quad(lambda y: abs(T*((T+1)*y/a-1))*
             (y**(a-1)*(1-y)**(b-1))/float(beta_const),
             0,1,points=[a/(T+1)],epsabs=5e-9,limit=300)[0]
        assert abs(norm-integral)<2e-7,(T,a,norm,integral)
        if prev is not None:assert prev>norm+1e-8,(T,a,prev,norm)
        prev=norm
        checks_numerical+=1
# Gamma limit for fixed a, total concentration T to infinity.
checks_asymptotic=0
for a in (0.5,1.,2.,3.):
    target=2*a**(a-1)*exp(-a)/gamma(a)
    errors=[]
    for T in (100.,1000.,10000.):
        val=norm_real(a,T)/T
        errors.append(abs(val-target))
    assert errors[-1]<3e-4 and errors[-1]<errors[0],(a,errors)
    checks_asymptotic+=1
# Recover known uniform-volume one-simplex norm exactly, but do not re-audit source.
for n in range(2,15):
    t=Q(n,n+1)
    assert norm_int(1,n)==2*n*t**(n-1)-1
    checks+=1
print('DIRICHLET_EXACT_GRAM_AND_BETA_CHECKS_PASSED',checks)
print('DIRICHLET_NONINTEGER_QUADRATURE_AND_STRICT_ORDER_CHECKS_PASSED',checks_numerical)
print('DIRICHLET_GAMMA_SCALING_CHECKS_PASSED',checks_asymptotic)
print('ALL_AFFINE_DIRICHLET_CHECKS_PASSED')
