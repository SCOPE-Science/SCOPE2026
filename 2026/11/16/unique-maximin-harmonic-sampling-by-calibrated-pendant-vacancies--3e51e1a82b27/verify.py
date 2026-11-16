"""Standalone numerical and exact-count checks for calibrated pendant-channel covariance.
Requires Python 3 and numpy. Finite tests supplement the analytic theorem.
"""
from itertools import product
from math import sqrt, cos, pi, isclose
import numpy as np

checks = 0

def check(cond, explanation='assertion'):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(explanation)

def rim_measures(n, t=0.5):
    points=[]; weights=[]
    for seq in product((0,1),repeat=n):
        if all(seq[i]*seq[(i+1)%n]==0 for i in range(n)):
            points.append(seq)
            weights.append(t**sum(seq))
    a=np.asarray(points,dtype=float)
    w=np.asarray(weights,dtype=float); w/=sum(w)
    p=w@a
    C=(a*w[:,None]).T@a-np.outer(p,p)
    assert np.max(np.abs(p-p[0])) < 1e-12
    return float(p[0]),C

def formulas(n):
    rho=sqrt(3)-2
    u=rho**n
    p0=(1-1/sqrt(3))/2
    q0=(1+1/sqrt(3))/2
    p=(p0+q0*u)/(1+u)
    s=(1-u)/(6*sqrt(3)*(1+u))+n*u/(3*(1+u)**2)
    other=np.asarray([(1-rho**2)*(1-u)/(6*(1+u)*(1-2*rho*cos(2*pi*j/n)+rho**2)) for j in range(1,n)])
    return p, s, np.r_[s,other]

def blocks(C,p,r):
    n=len(C); q=(1-p)*r*(1-r)
    return np.block([[C,-r*C],[-r*C,r*r*C+q*np.eye(n)]])

def lower(s,c,r):
    q=c*r*(1-r)
    mat=np.array([[s,-r*s],[-r*s,r*r*s+q]])
    return np.linalg.eigvalsh(mat)[0]

def opt(s,c):
    # The unique root in (0,1/2), without cancellation at c=s.
    if abs(c-s)<1.e-12:
        return .4
    roots=np.roots([2*(s-c),c+4*s,-2*s])
    ans=[z.real for z in roots if abs(z.imag)<1.e-10 and 0<z.real<.5]
    assert len(ans)==1
    return ans[0]

for n in range(3,14):
    p,C=rim_measures(n)
    p0,s,ss=formulas(n)
    check(np.max(np.abs(p-p0))<2e-12, ('mean',n))
    ev=np.linalg.eigvalsh(C)
    check(np.max(np.abs(np.sort(ev)-np.sort(ss)))<5e-12,('rim Fourier',n))
    check(abs(ev[0]-s)<5e-12, ('constant mode',n))
    check(np.linalg.norm(C@np.ones(n)-s*np.ones(n),np.inf)<5e-12, ('constant eigenvector',n))
    check(ev[0]>0,('positive rim spectrum',n))
    r=opt(s,1-p)
    check(0<r<.5,('optimal range',n))
    check(abs(2*(s-(1-p))*r*r+((1-p)+4*s)*r-2*s)<1e-12,('quadratic',n))
    B=blocks(C,p,r)
    check(abs(np.linalg.eigvalsh(B)[0]-lower(s,1-p,r))<1e-12,('block min',n))
    check(abs(np.linalg.eigvalsh(B)[0]-max(lower(s,1-p,r+d) for d in [-.000001,0,.000001]))<1e-9,('local max',n))
    for rr in np.linspace(.005,.995,199):
        check(lower(s,1-p,r) >=lower(s,1-p,float(rr))-2.e-13,('global numerical max',n,rr))
    for rr in (.1,.2,.33,.5,.8):
        B2=blocks(C,p,rr)
        check(abs(np.linalg.eigvalsh(B2)[0]-lower(s,1-p,rr))<2e-12,('block spectrum',n,rr))

# Entire sunlet Gibbs law independently: rim weight alpha=t/(1-r), leaf beta=r/(1-r).
for n in range(3,7):
    for r in (.15,.3,.5,.8):
        alpha=.5/(1-r); beta=r/(1-r)
        points=[]; weights=[]
        for X in product((0,1),repeat=n):
            if any(X[i]*X[(i+1)%n] for i in range(n)):continue
            for Y in product((0,1),repeat=n):
                if any(X[i]*Y[i] for i in range(n)):continue
                points.append(X+Y); weights.append(alpha**sum(X)*beta**sum(Y))
        arr=np.array(points,dtype=float)
        w=np.array(weights,dtype=float); w/=sum(w)
        mu=w@arr
        Cov=(arr*w[:,None]).T@arr-np.outer(mu,mu)
        pp,C=rim_measures(n)
        check(np.max(np.abs(Cov-blocks(C,pp,r)))<2e-12, ('independent direct Gibbs',n,r))

# More general stationary Bernoulli vectors: a nontrivial random distribution on all 2^4 words.
for trial in range(15):
    n=4
    rng=np.random.default_rng(153+trial)
    words=np.asarray(list(product((0.,1.),repeat=n)))
    weights=rng.random(len(words));weights=weights/weights.sum()
    # enforce stationarity by averaging every cyclic rotation's original probability
    w=np.zeros(len(words))
    for k in range(n):
        for j,row in enumerate(words):
            index=int(''.join(str(int(x)) for x in np.roll(row,k)),2)
            w[j]+=weights[index]/n
    w/=sum(w)
    mu=w@words
    C=(words*w[:,None]).T@words-np.outer(mu,mu)
    p=mu[0]; s=np.linalg.eigvalsh(C)[0]
    check(np.max(abs(mu-p))<1e-12,'stationary means')
    check(s>0,'positive full support')
    rr=opt(s,1-p)
    check(abs(np.linalg.eigvalsh(blocks(C,p,rr))[0]-lower(s,1-p,rr))<2e-12,'general eigenvalue')
    for test in np.linspace(.01,.99,31):
        check(lower(s,1-p,rr)>=lower(s,1-p,test)-1e-12,'general maximin')

rho=sqrt(3)-2
p_inf=(1-1/sqrt(3))/2
s_inf=1/(6*sqrt(3)); c_inf=1-p_inf
r_inf=opt(s_inf,c_inf)
print('PASS', checks, 'finite assertions')
print('Limit: rim p=%.15f rim smallest Fourier eigenvalue=%.15f'%(p_inf,s_inf))
print('Limit: optimal leaf conditional probability=%.15f'%r_inf)
print('Limit: maximal smallest eigenvalue=%.15f baseline equal-fugacity value=%.15f'%(lower(s_inf,c_inf,r_inf),lower(s_inf,c_inf,.5)))
print('Limit: optimal rim/leaf activities=%.15f %.15f'%(0.5/(1-r_inf),r_inf/(1-r_inf)))
