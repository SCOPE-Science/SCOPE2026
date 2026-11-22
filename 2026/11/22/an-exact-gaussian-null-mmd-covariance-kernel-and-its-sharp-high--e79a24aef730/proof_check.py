"""Reproduce numerical checks for the exact Gaussian-null MMD bandwidth-correlation law.
The analytic theorem and all-dimensional regimes require the proof, not finite tests.
Standard library only; executable with Python 3.11 or later.
"""
from decimal import Decimal, localcontext
from math import exp, sqrt, pi
import random

checks=0

def record(condition, label):
    global checks
    checks+=1
    if not condition:
        raise AssertionError(label)

def D(x):
    return Decimal(str(x))

def K(d,a,b):
    """Stable covariance kernel for dimension d; numbers use Decimal."""
    a,b=D(a),D(b)
    p=Decimal(d)/2
    A=1+4*(a+b)
    r=a*b/A
    f=(1-2*((1+12*r).ln()*(-p)).exp()+((1+16*r).ln()*(-p)).exp())
    return (-p*A.ln()).exp()*f

def rho(d,a,b):
    kab=K(d,a,b)
    return kab/(K(d,a,a)*K(d,b,b)).sqrt()

def critical(u,v):
    u,v=D(u),D(v)
    g=lambda t: 1-2*(-6*t).exp()+(-8*t).exp()
    return (-4*(u-v)**2).exp()*g(u*v)/(g(u*u)*g(v*v)).sqrt()

def log_asymptotic(d,a,b):
    """Leading logarithmic normalised-covariance ratio in subcritical regime."""
    return -4*(a-b)**2*d

with localcontext() as ctx:
    ctx.prec=80
    for dim in [1,2,3,5,10,20]:
        for a,b in [('.05','.3'),('.2','1.1'),('1','3'),('0.01','0.02')]:
            q=rho(dim,a,b)
            record(Decimal(0)<q<Decimal(1),f'corr strict {dim,a,b}')
            record(K(dim,a,b)>0, f'positive kernel {dim,a,b}')
            record(abs(rho(dim,a,a)-1)<D('1e-65'),f'normalization {dim,a}')
    u,v=D('.6'),D('1.4')
    cr=critical(u,v)
    record(0<cr<1,'critical nondegenerate')
    for alpha in ['.25','.35']:
        alpha=D(alpha)
        for dim in [2000,5000,20000]:
            a=u/(D(dim)**alpha)
            b=v/(D(dim)**alpha)
            R=rho(dim,a,b)
            leading=log_asymptotic(D(dim),a,b)
            record(R>0 and R<1, f'subcritical {dim,alpha}')
            if dim==20000:
                ratio=R.ln()/leading
                record(D('.3')<ratio<1,f'subcritical log scale direction {alpha}')
    for dim in [20000,100000,1000000]:
        sd=D(dim).sqrt()
        r=rho(dim,u/sd,v/sd)
        record(abs(r-cr)<D('.05'),f'critical limit {dim}')
    for alpha in ['.75','1.0','1.2']:
        aexp=D(alpha)
        d=100000
        r=rho(d,u/(D(d)**aexp),v/(D(d)**aexp))
        record(r>D('.94'),f'supercritical limit {alpha}')

# Deterministic 2-D Simpson quadrature in d=1, independent of Gaussian algebra.
def one_d_center(t,x,y):
    m=lambda z:exp(-t*z*z/(1+2*t))/sqrt(1+2*t)
    return exp(-t*(x-y)**2)-m(x)-m(y)+1/sqrt(1+4*t)
N=200
L=7.0
step=2*L/N
xs=[-L+i*step for i in range(N+1)]
weights=[(1 if i in (0,N) else (4 if i%2 else 2))*step/3 * exp(-x*x/2)/sqrt(2*pi) for i,x in enumerate(xs)]
for a,b in [(0.05,.15),(.3,.9),(1.5,2.4)]:
    total=0.
    for i,x in enumerate(xs):
        for j,y in enumerate(xs):
            total+=weights[i]*weights[j]*one_d_center(a,x,y)*one_d_center(b,x,y)
    exact=float(K(1,str(a),str(b)))
    record(abs(total-exact)<2e-7+2e-4*exact,f'quadrature a={a},b={b}')

# Independent finite-sample simulation for the U-statistic covariance, not a proof.
seed=74192
rng=random.Random(seed)
n=4; dim=3; a=.17; b=.51
trials=40000
mean_a=mean_b=mean_ab=0.
for rep in range(trials):
    X=[[rng.gauss(0,1) for k in range(dim)] for i in range(n)]
    def U(t):
        c=(1+4*t)**(-dim/2)
        ms=[(1+2*t)**(-dim/2)*exp(-t*sum(z*z for z in x)/(1+2*t)) for x in X]
        ss=0.
        for i in range(n):
            for j in range(i+1,n):
                ds=sum((p-q)**2 for p,q in zip(X[i],X[j]))
                ss+=exp(-t*ds)-ms[i]-ms[j]+c
        return 2*ss/(n*(n-1))
    ua,ub=U(a),U(b)
    mean_a+=ua; mean_b+=ub; mean_ab+=ua*ub
emp=mean_ab/trials-(mean_a/trials)*(mean_b/trials)
theory=2*float(K(dim,str(a),str(b)))/(n*(n-1))
record(abs(emp-theory)<.06*theory,f'finite-n empirical covariance: {emp}, expected {theory}')
print('PASS',checks,'checks; example Monte Carlo covariance',emp,'formula',theory)
