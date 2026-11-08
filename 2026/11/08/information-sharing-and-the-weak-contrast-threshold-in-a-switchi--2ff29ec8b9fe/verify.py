#!/usr/bin/env python3
"""Finite diagnostic checks for the Gaussian scale-mixture information theorem.
Requires NumPy and SciPy. Run: python verify.py
The theorem's infinite-population limits rely on the proof, not these checks.
"""
import math
import numpy as np
from scipy.special import beta, digamma, gammaln, roots_legendre, logsumexp
from scipy.integrate import quad

NTEST=0
def check(p, explanation):
    global NTEST
    NTEST += 1
    if not p:
        raise AssertionError(explanation)

def mixing_shape(a,b,mu1,mu2):
    c,e=1/mu1,1/mu2
    J=c*beta(a,b+1)+e*beta(a+1,b)
    return lambda u: u**(a-1)*(1-u)**(b-1)*(c*(1-u)+e*u)/J

def log_gamma_density(t,k):
    z=np.asarray(t)
    a=k/2
    return a*(np.log(a)+z-np.exp(np.clip(z,-50,50)))-gammaln(a)

def entropy_log_noise(k):
    a=k/2
    return a+gammaln(a)-a*digamma(a)

def entropy_mixed(k,a=1,b=1,mu1=2,mu2=1,step=.002,quadnodes=160):
    x,wt=roots_legendre(quadnodes)
    u=(x+1)/2
    wt=wt/2*mixing_shape(a,b,mu1,mu2)(u)
    wt=wt/wt.sum()
    v=np.log((1-u)/mu1+u/mu2)
    st=np.sqrt(2/k)
    t=np.arange(v.min()-max(18*st,3), v.max()+max(18*st,3),step)
    p=np.zeros(len(t))
    for j in range(0,len(t),128):
        lg=log_gamma_density(t[j:j+128,None]-v[None,:],k)+np.log(wt)[None,:]
        p[j:j+128]=np.exp(logsumexp(lg,axis=1))
    area=np.trapezoid(p,t)
    h=-np.trapezoid(p*np.log(np.maximum(p,1e-300)),t)
    return h,area

def information(n,delta,alpha=1.,beta_=1.,step=.016):
    # Mu_2=1, Mu_1=1+delta; rates 2*mu_i*fixed alpha_i
    u,v=roots_legendre(140)
    u=(u+1)/2
    w=v/2*mixing_shape(alpha,beta_,1+delta,1)(u)
    w=w/w.sum()
    def hg(k):
        signal=np.sqrt(k)*np.log1p(delta*u)
        t=np.arange(-18,signal.max()+18,step)
        p=np.zeros(len(t))
        for j in range(0,len(t),100):
            z=(t[j:j+100,None]-signal[None,:])/np.sqrt(k)
            lg=log_gamma_density(z,k)-.5*np.log(k)+np.log(w)[None,:]
            p[j:j+100]=np.exp(logsumexp(lg,axis=1))
        check(abs(np.trapezoid(p,t)-1)<1e-7,'scaled convolution mass')
        return -np.trapezoid(p*np.log(np.maximum(p,1e-300)),t)
    def hnoise(k): return entropy_log_noise(k)+.5*np.log(k)
    return 2*(hg(n)-hnoise(n))-(hg(2*n)-hnoise(2*n))

def profile(c,a=1.,b=1.,step=.016):
    uu,ww=roots_legendre(160);uu=(uu+1)/2
    ww=ww/2*uu**(a-1)*(1-uu)**(b-1)/beta(a,b)
    ww=ww/ww.sum()
    def hsig(tau):
        t=np.arange(-18,tau+18,step)
        p=np.zeros(len(t))
        for i in range(0,len(t),80):
            z=t[i:i+80,None]-tau*uu[None,:]
            p[i:i+80]=np.exp(logsumexp(-z*z/4-.5*np.log(4*np.pi)+np.log(ww)[None,:],axis=1))
        check(abs(np.trapezoid(p,t)-1)<1e-7,'Gaussian channel mass')
        return -np.trapezoid(p*np.log(np.maximum(p,1e-300)),t)
    return 2*hsig(c)-hsig(np.sqrt(2)*c)-.5*np.log(4*np.pi*np.e)

# Mixing law is normalized and respects the stationary variance moment equations.
for mu1,mu2,la1,la2 in [(2,1,4,2),(3,1,2,3),(4,2,5,1),(1.5,1,1,1)]:
    a,b=la1/(2*mu1),la2/(2*mu2)
    q=mixing_shape(a,b,mu1,mu2)
    check(abs(quad(q,0,1,epsabs=1e-10)[0]-1)<1e-9,'mix law normalized')
    Emix=quad(lambda u:q(u)*((1-u)/mu1+u/mu2),0,1,epsabs=1e-10)[0]
    ph=la2/(la1+la2);pl=1-ph
    # Solve the stationary first-moment equations for variance times state indicator.
    mat=np.array([[2*mu1+la1,-la2],[-la1,2*mu2+la2]])
    right=np.array([2*ph,2*pl])
    cond=np.linalg.solve(mat,right)
    check(abs(Emix-cond.sum())<1e-9,'stationary variance mixture agrees with moment generator')

for k in [2,3,4,8,16,32,64,128,512,2048]:
    check(np.isfinite(entropy_log_noise(k)),'log Gamma noise entropy finite')
    approx=.5*np.log(4*np.pi*np.e/k)
    if k>=512:
        check(abs(entropy_log_noise(k)-approx)<.002,'Stirling log-Gamma entropy')

# Direct block information via the joint squared-statistic density, compared with
# the three-entropy exact decomposition (not based on the same integral).
k=8
h1,m1=entropy_mixed(k,step=.004)
h2,m2=entropy_mixed(2*k,step=.004)
check(abs(m1-1)<1e-7 and abs(m2-1)<1e-7,'convolution normalized')
I_exact=2*(h1-entropy_log_noise(k))-(h2-entropy_log_noise(2*k))
xx,ww=roots_legendre(150);uu=(xx+1)/2;ww=ww/2*mixing_shape(1,1,2,1)(uu)
ww=ww/ww.sum()
w=np.log(.5+.5*uu)
grid=np.arange(-8,5,.025)
A=np.exp(log_gamma_density(grid[:,None]-w[None,:],k))
Pmarg=A@ww
Pjoint=(A*ww[None,:])@A.T
Pprod=Pmarg[:,None]*Pmarg[None,:]
I_direct=np.sum(Pjoint*np.log(np.maximum(Pjoint,1e-300)/np.maximum(Pprod,1e-300)))*(.025**2)
check(abs(I_direct-I_exact)<2e-3,'direct block-MI integral equals three-entropy identity')

# Fixed-contrast leading constant, including its exact Jacobian factor.
hW=-quad(lambda u: mixing_shape(1,1,2,1)(u)*np.log(mixing_shape(1,1,2,1)(u)*(.5+.5*u)/.5),0,1,epsabs=1e-11)[0]
constant=hW-.5*np.log(8*np.pi*np.e)
check(abs(hW+0.4429273733850231)<2e-10,'reference log-variance entropy')
for n in [32,128,512,2048]:
    a1,m1=entropy_mixed(n,step=.002)
    a2,m2=entropy_mixed(2*n,step=.002)
    info=2*(a1-entropy_log_noise(n))-(a2-entropy_log_noise(2*n))
    check(info>=-2e-8,'MI nonnegative')
    if n>=512:
        check(abs(info-.5*np.log(n)-constant)<.25,'fixed contrast finite-n approaches constant')

# Shrinking-contrast crossover: finite-n densities vs Beta/Gaussian limit.
for c in [.5,1,2]:
    target=profile(c)
    check(target>0,'positive nonzero contrast MI')
    for n in [128,512,2048]:
        val=information(n,c/np.sqrt(n))
        check(val>=-1e-8,'finite-n MI nonnegative')
        check(abs(val-target)<.004 if c<=1 else abs(val-target)<.004,'weak-contrast convergence diagnostic')

# Small-signal quartic coefficient; large-signal logarithmic trend.
coef=(1/12)**2/8
check(abs(profile(.25)-coef*.25**4)<2e-7,'quartic near-zero coefficient')
for c in [0,.5,1,2,4]:
    check(profile(c)>=-1e-8,'Gaussian profile nonnegative')

print('PASS:',NTEST,'finite assertions')
print('Direct MI (n=8):',I_direct,'entropy formula:',I_exact)
print('h(log V):',hW,'large-n equal-block constant:',constant)
print('Beta(1,1) c=2 crossover MI:',profile(2))
