"""Independent numerical checks of Gaussian shrinkage e-value formulas.

Only standard Python and NumPy are needed. Run: python checker.py
The analytic Gaussian-integral proof is in RESULT.md; quadrature checks are not proofs.
"""
import math
import numpy as np
from numpy.polynomial.hermite import hermgauss

checks=0

def check(condition, description):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(description)

def close(x,y,tol=1e-9):
    return abs(x-y) <= tol*max(1,abs(y))

def gauss2(f, order=90):
    # Standard normal integrals, using the Gauss-Hermite Gaussian density transform
    z,w=hermgauss(order)
    z=z*math.sqrt(2)
    w=w/math.sqrt(math.pi)
    x=z[:,None]; y=z[None,:]
    return np.sum(w[:,None]*w[None,:]*f(x,y))

def raw_moment(q,lam,d,m,k):
    h=q*(q-1)*k*lam**2/m
    return (1-h)**(-d/2) if h < 1-1e-14 else float('inf')

def mixed_moment(lam,d):
    return (1-lam**2)**(-d) if lam<1 else float('inf')

def log_growth(lam,d,m,k,mu2):
    return k*(lam*mu2-.5*lam**2*(mu2+d/m))

# Quadrature from first principles with independent standard normals X,Y:
# E1=exp(lambda X Y -lambda² X²/2), E2=exp(lambda X Y -lambda² Y²/2).
for lam in [0.1,0.25,0.35,0.5]:
    for q in [1,2,3]:
        if q*(q-1)*lam**2>=0.72:
            continue
        quadr=gauss2(lambda x,y: np.exp(q*lam*x*y-.5*q*lam**2*x*x))
        check(close(quadr,raw_moment(q,lam,1,1,1),3e-8),f'one-fold q={q} lambda={lam}')
    cross=gauss2(lambda x,y: np.exp(2*lam*x*y-.5*lam**2*(x*x+y*y)))
    check(close(cross,mixed_moment(lam,1),3e-8),f'cross lambda={lam}')

# Independent high-dimensional limits plus the sharp L2 swap gap.
for c in [0.35,1.,1.5]:
    vals=[]
    for d in [1000,2000,4000,8000]:
        lam=c/math.sqrt(d)
        a=raw_moment(2,lam,d,1,1)
        b=mixed_moment(lam,d)
        gap=2*(a-b)
        vals.append(d*gap)
        check(a>=b>1, 'positive cross-covariance and swap gap')
        check(a>0 and b>0, 'positive moments')
        # convergence of each moment to lognormal second moment
        check(abs(a-math.exp(c*c)) < 2*math.exp(c*c)*c**4/d, 'lognormal moment limit bound')
    target=math.exp(c*c)*c**4
    check(abs(vals[-1]/target-1)<0.01,'sharp L2 difference asymptotic')

# Verify the exact quadratic expected-log-growth criterion and the sharp
# balanced-split signal crossover by algebraic substitutions.
rt=math.sqrt(2)+1
for r in [0., .2, 1., rt-1e-7, rt,rt+1e-7, 4., 20.]:
    lamstar=r/(1+r)
    check(close(lamstar,0 if r==0 else 1-1/(1+r)),'oracle stationary point')
    check((lamstar<1/math.sqrt(2))==(r<rt),'safe-oracle threshold')
    check(log_growth(lamstar,2,4,4,r*2/4)>=log_growth(max(0,lamstar-.01),2,4,4,r*2/4)-1e-12,'oracle left comparison')
    check(log_growth(lamstar,2,4,4,r*2/4)>=log_growth(min(1,lamstar+.01),2,4,4,r*2/4)-1e-12,'oracle right comparison')

# Monte Carlo against independent random normal observations; no reuse of
# quadrature inputs or symbolic expansion.
rng=np.random.default_rng(302711)
nmc=300000
m,k,d=5,7,3
mu=np.array([0.35,-0.6,0.45])
lam=.28
train=mu+rng.standard_normal((nmc,d))/math.sqrt(m)
testsum=k*mu+math.sqrt(k)*rng.standard_normal((nmc,d))
logs=lam*np.sum(train*testsum,axis=1)-.5*k*lam**2*np.sum(train*train,axis=1)
est=logs.mean(); exact=log_growth(lam,d,m,k,np.dot(mu,mu))
check(abs(est-exact)<0.015,'alternative mean log growth Monte Carlo')

# Strict diverging moment at boundary from the nonpositive Gaussian precision.
for lam in [1/math.sqrt(2),.8,1.]:
    check(math.isinf(raw_moment(2,lam,1,1,1)),'strict L2 boundary')

print(f'PASS: {checks} deterministic quadrature, asymptotic, boundary, and simulation assertions')
