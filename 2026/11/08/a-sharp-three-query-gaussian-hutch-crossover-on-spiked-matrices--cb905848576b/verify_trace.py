#!/usr/bin/env python3
"""Reproduce algebraic and numerical checks for Gaussian three-query trace estimation.
Public mathematics only; no external documents or network access required.
Dependencies: sympy, mpmath, numpy.
"""
import sympy as sp
import mpmath as mp
import numpy as np

checks = 0
def check(condition, name):
    global checks
    assert bool(condition), name
    checks += 1

k = sp.symbols('k', positive=True)
y = sp.symbols('y', real=True)
I1 = (2*k+1)/(k+1)**2
I2 = (k*k+3*k+1)/(k+1)**3
R = (k**4+8*k**3+7*k**2+6*k+2)/(k+1)**3
D = (k**5-18*k**3-11*k**2-9*k-3)/(3*(k+1)**3)
p = k**5-18*k**3-11*k**2-9*k-3
check(sp.simplify(3+2*(k-1)*I1+(k-1)**2*I2-R)==0,'residual Frobenius moment identity')
check(sp.simplify((k*k+3)/3-R-D)==0,'variance difference polynomial')
check(sp.simplify(I1.subs(k,1)-sp.Rational(3,4))==0,'isotropic first moment')
check(sp.simplify(I2.subs(k,1)-sp.Rational(5,8))==0,'isotropic second moment')
check(sp.simplify(R.subs(k,1)-3)==0,'isotropic residual norm')
check(sp.limit(R/k,k,sp.oo)==1,'four-dimensional rare-sketch asymptotic coefficient')
check(sp.limit((2*R)/(2*(k*k+3)/3),k,sp.oo)==0,'relative benefit for large spike')
check(p.subs(k,1)<0 and p.subs(k,5)>0,'threshold bracket')
# Exactly one sign change in descending coefficients: Descartes + IVT -> unique positive root.
coeffs=[sp.expand(p).coeff(k,i) for i in range(5,-1,-1)]
signs=[1 if x>0 else -1 for x in coeffs if x!=0]
check(sum(signs[i]!=signs[i+1] for i in range(len(signs)-1))==1,'unique positive crossover by Descartes')

mp.mp.dps=50
for kval in (1,1.5,2,4,5,10,40):
    K=mp.mpf(str(kval))
    moment1=4/mp.pi * mp.quad(lambda z: 1/((1+z*z)**2*(1+K*K*z*z)), [0,1,mp.inf])
    moment2=4/mp.pi * mp.quad(lambda z: 1/((1+z*z)**2*(1+K*K*z*z)**2), [0,1,mp.inf])
    f1=(2*K+1)/(K+1)**2
    f2=(K*K+3*K+1)/(K+1)**3
    check(abs(moment1-f1)<mp.mpf('1e-38'), 'first moment quadrature')
    check(abs(moment2-f2)<mp.mpf('1e-38'), 'second moment quadrature')

root=mp.findroot(lambda z: z**5-18*z**3-11*z*z-9*z-3,(4,5))
check(abs(root-mp.mpf('4.568427040565852286766830357413051273121'))<mp.mpf('1e-34'),'high-precision threshold')
for kval in (1,2,4,5,10,20):
    K=mp.mpf(kval)
    vh=2*(K**4+8*K**3+7*K*K+6*K+2)/(K+1)**3
    vg=2*(K*K+3)/3
    check((vh<vg)==(K>root),'all tested crossover regimes')

# Independent direct finite-dimensional covariance identity, not just its symbolic reduction.
rng = np.random.default_rng(91751)
for kval in (1.0,1.5,2.0,4.0,5.0,10.0):
    A=np.diag([kval,1.,1.,1.])
    for _ in range(30):
        s=rng.normal(size=4)
        q=A@s; q=q/np.linalg.norm(q)
        P=np.eye(4)-np.outer(q,q)
        B=P@A@P
        t=1-q[0]**2
        target=3+2*(kval-1)*t+(kval-1)**2*t*t
        check(abs(np.trace(B@B)-target)<1e-10,'direct 4d matrix identity')
        check(abs(float(q@A@q + np.trace(B))-(kval+3))<1e-10,'conditional unbiasedness')

# Numerically estimate the true estimator variance to check the complete Monte Carlo design.
for kval in (1.,5.,10.):
    sample_size=300000
    s=rng.normal(size=(sample_size,4))
    g=rng.normal(size=(sample_size,4))
    AS=s.copy(); AS[:,0]*=kval
    q=AS/np.linalg.norm(AS,axis=1)[:,None]
    g_res=g - q*np.einsum('ni,ni->n',q,g)[:,None]
    Aq=q.copy();Aq[:,0]*=kval
    Ag=g_res.copy(); Ag[:,0]*=kval
    H=np.einsum('ni,ni->n',q,Aq)+np.einsum('ni,ni->n',g_res,Ag)
    theoretical=2*(kval**4+8*kval**3+7*kval*kval+6*kval+2)/(kval+1)**3
    observed=float(np.var(H,ddof=1))
    check(abs(float(np.mean(H))-(kval+3)) < .06,'empirical unbiasedness')
    check(abs(observed/theoretical-1) < .09,'empirical variance')

print(f'PASS: {checks} checks')
print(f'Unique positive threshold kappa_* = {mp.nstr(root,35)}')
print('Variance Hutch++ at kappa=1,5,10: '+', '.join(str(float(2*R.subs(k,z))) for z in (1,5,10)))
print('Variance 3-probe Gaussian Hutchinson at kappa=1,5,10: '+', '.join(str(float(2*(k*k+3).subs(k,z)/3)) for z in (1,5,10)))
