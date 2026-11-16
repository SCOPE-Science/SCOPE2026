#!/usr/bin/env python3
"""Reproduce exact first-harmonic Grassmannian-cap polynomial identities.

Requires Python 3, SymPy, NumPy, SciPy.  The exact identities are
symbolic; random numerical checks are corroborative, not proofs.
"""
import sympy as S
import numpy as np
from scipy.special import betainc

n,k,x = S.symbols('n k x', integer=True, positive=True)
a = k/S.Integer(2)
b = (n-k)/S.Integer(2)
C = 2*k*(n-k)/(n*(n-1)*(n+2))
qA=(n+2)*(n*x-k)**2/(2*k*(n-k))
qV=n*(n+2)*x*(1-x)/(k*(n-k))
qT=n*(n+2)*(k*(n-k-1)+2*(k-n+1)*x+(n-2)*x*x)/(k*(n-k)*(n-2)*(n+1))

def eq(a,b):
    d=S.factor(a-b)
    if d!=0: raise AssertionError(d)

# Reconstruct the conditional distributions, including the random
# orthogonal rank-(k-1) projector in dimension n-2.
qT_from_cond=S.factor((2/((n-1)*(n+1))*(1-x-(k-1)/(n-2))**2
                +2*(k-1)*(n-k-1)/((n-2)**2*(n+1)))/C)
eq(qT,qT_from_cond)

# E[X^j] for X ~ Beta(k/2,(n-k)/2), exact rational function.
def moment(j):
    return S.rf(a,j)/S.rf(a+b,j)
def expected(poly):
    p=S.Poly(S.cancel(poly),x)
    return S.factor(sum(coef*moment(deg[0]) for deg,coef in p.terms()))
for q in (qA,qV,qT): eq(expected(q), 1)

# Integration by parts with Beta(a,b) density.
F=lambda A,B: a*A+((a+1)*B-(a+b)*A)*x-(a+b+1)*B*x*x
threshold_AB=S.factor((k*(n+2)-2*n)/(n*(n-2)))
threshold_AV=k/n
threshold_VT=S.factor((n-k-1)/(n-2))
K_AV=n*(n+2)/(k*(n-k))
K_AT=n*(n-1)*(n+2)/(k*(n-k)*(n+1))
K_VT=2*n*(n+2)/(k*(n-k)*(n+1))
# If w is normalized Beta density, D=w*x*(1-x), then
# integral_x^1 (q_i-q_j) w = D*K*(x-threshold), signs as below.
eq(qA-qV, F(K_AV*threshold_AV, -K_AV))
eq(qA-qT, F(K_AT*threshold_AB, -K_AT))
eq(qV-qT, F(-K_VT*threshold_VT, K_VT))
# Earlier F(A,B) is (1/w) d[x(1-x)w(A+Bx)]/dx.
# Antiderivative of the gap is -D*(A+Bx), so sign factors above.

eq(S.factor(threshold_AV-threshold_AB),2*(n-2*k)/(n*(n-2)))
eq(S.factor(threshold_VT-threshold_AV),(n-1)*(n-2*k)/(n*(n-2)))
eq(S.factor(threshold_VT-threshold_AB),(n+1)*(n-2*k)/(n*(n-2)))
# The boundary gap is scalar vs vector, giving a simple pole.
qA_at_1=S.factor(qA.subs(x,1))
qV_slope=S.factor(-S.diff(qV,x).subs(x,1))
eq(S.factor((qA_at_1/qV_slope)*(b+1)/b), (n-k)*(n-k+2)/(2*n))

# The complement involution P -> I-P makes the middle-rank
# s>=1/2 cap energy exactly one half for every f_A.
for q in (qA,qV,qT):
    eq(S.factor(q.subs({n:2*k,x:1-x})-q.subs(n,2*k)),0)
print('SYMBOLIC_BETA_NORMALIZATION_AND_GAP_IDENTITIES_PASS')

# Independent seeded Haar projection check: compare full Gram operator
# with theoretical spectrum, rather than sampling only 3 test functions.
def integrals(n0,k0,t0):
    A=k0/2.;B=(n0-k0)/2.
    c0=2*k0*(n0-k0)/(n0*(n0-1)*(n0+2))
    m0=k0/n0
    # beta tails; use scipy regularized incomplete beta
    def J(j):
        from scipy.special import poch
        return poch(A,j)/poch(A+B,j)*(1-betainc(A+j,B,t0))
    qa=lambda s:(n0+2)*(n0*s-k0)**2/(2*k0*(n0-k0))
    qv=lambda s:n0*(n0+2)*s*(1-s)/(k0*(n0-k0))
    qt=lambda s:n0*(n0+2)*(k0*(n0-k0-1)+2*(k0-n0+1)*s+(n0-2)*s*s)/(k0*(n0-k0)*(n0-2)*(n0+1))
    qs=[]
    for coeff in [np.polynomial.polynomial.polyfit([0,.5,1],[qa(0),qa(.5),qa(1)],2),
                  np.polynomial.polynomial.polyfit([0,.5,1],[qv(0),qv(.5),qv(1)],2),
                  np.polynomial.polynomial.polyfit([0,.5,1],[qt(0),qt(.5),qt(1)],2)]:
        qs.append(sum(coeff[j]*J(j) for j in range(3)))
    return qs

def basis(n0):
    mats=[]
    for i in range(n0):
        for j in range(i+1,n0):
            E=np.zeros((n0,n0));E[i,j]=E[j,i]=1/np.sqrt(2)
            mats.append(E)
    for i in range(1,n0):
        E=np.zeros((n0,n0))
        E[:i,:i]+=np.eye(i)/np.sqrt(i*(i+1))
        E[i,i]=-i/np.sqrt(i*(i+1))
        mats.append(E)
    return np.array(mats)

def check_sample(n0,k0,t0,count,seed):
    rg=np.random.default_rng(seed)
    h=basis(n0)
    M=len(h)
    empirical=np.zeros((M,M))
    step=4096
    for off in range(0,count,step):
        g=rg.standard_normal((min(step,count-off),n0,k0))
        Q=np.linalg.qr(g)[0]
        P=Q@np.swapaxes(Q,1,2)
        v=np.einsum('bij,tij->bt',P,h,optimize=True)
        v[P[:,0,0]<t0,:]=0
        empirical+=v.T@v
    empirical/=count
    c0=2*k0*(n0-k0)/(n0*(n0-1)*(n0+2))
    empirical/=c0
    got=np.linalg.eigvalsh(empirical)
    la,lv,lt=integrals(n0,k0,t0)
    want=np.sort([la]+[lv]*(n0-1)+[lt]*(M-n0))
    err=np.max(np.abs(got-want))
    if err>.045:raise AssertionError((n0,k0,t0,err,got,want))
    print('HAAR_CONSISTENCY',n0,k0,t0,'max_abs',round(float(err),6))
for args in [(4,2,.38,60000,351),(6,2,.41,60000,352),(7,3,.53,60000,353)]:
    check_sample(*args)
print('FIRST_GRASSMANNIAN_THREE_BRANCH_SPECTRUM_PASS')
