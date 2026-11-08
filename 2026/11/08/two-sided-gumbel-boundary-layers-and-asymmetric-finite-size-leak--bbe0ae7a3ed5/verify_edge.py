#!/usr/bin/env python3
"""Independent finite-N and limiting-integral diagnostics for two-sided extreme edges.

Uses ordinary double-precision SciPy integration. This is not an infinite proof.
Run: python verify_edge.py
"""
import math
from dataclasses import dataclass
from scipy.integrate import quad
from scipy.special import beta as beta_fn, gamma, log_ndtr

@dataclass(frozen=True)
class Parameters:
    mu1: float
    mu2: float
    D: float
    r1: float
    r2: float

    def constants(self):
        assert self.mu1 > self.mu2 > 0 and self.D > 0 and self.r1 > 0 and self.r2 > 0
        v0, v1 = self.D/self.mu1, self.D/self.mu2
        delta = v1-v0
        p, q = self.r1/(2*self.mu1), self.r2/(2*self.mu2)
        vbar = v0+delta*p/(p+q)
        B = beta_fn(p,q)
        A0 = (v0/(vbar*B))*(v0/delta)**p
        A1 = (v1/(vbar*B))*(v1/delta)**q
        return v0,v1,delta,p,q,vbar,B,A0,A1

def gumbel(t):
    return math.exp(-math.exp(-t)) if t > -25 else 0.

def leading_profiles(P,t):
    _,_,_,p,q,_,_,A0,A1=P.constants()
    lo=A0*quad(lambda s:s**(p-1)*gumbel(t-s),0,70,epsabs=2e-11,limit=350)[0]
    hi=A1*quad(lambda s:s**(q-1)*(-math.expm1(-math.exp(-t-s))),0,70,epsabs=2e-11,limit=350)[0]
    return lo,hi

def mixing_density(P,u):
    v0,v1,delta,p,q,vbar,B,_,_=P.constants()
    return (v0+delta*u)*u**(p-1)*(1-u)**(q-1)/(vbar*B)

def conditional_cdf(N,x,v):
    z=x/math.sqrt(v)
    value=N*log_ndtr(z)
    return math.exp(value) if value > -745 else 0.0

def conditional_tail(N,x,v):
    value=N*log_ndtr(x/math.sqrt(v))
    return -math.expm1(value) if value > -745 else 1.0

def exact_edge(P, log10N, t, raw=False):
    N=10.0**log10N
    L=log10N*math.log(10)
    v0,v1,delta,_,_,_,_,_,_=P.constants()
    a=math.sqrt(2*L)-(math.log(L)+math.log(4*math.pi))/(2*math.sqrt(2*L))
    b=1/math.sqrt(2*L)
    xlo=math.sqrt(v0)*(math.sqrt(2*L) if raw else a+b*t)
    xhi=math.sqrt(v1)*(math.sqrt(2*L) if raw else a+b*t)
    def low(u):
        return mixing_density(P,u)*conditional_cdf(N,xlo,v0+delta*u)
    def high(u):
        return mixing_density(P,u)*conditional_tail(N,xhi,v0+delta*u)
    lowvalue=quad(low,0,1,points=[.001,.01,.05,.25,.5,.9],epsabs=2e-10,limit=300)[0]
    highvalue=quad(high,0,1,points=[.05,.5,.9,.99,.999],epsabs=2e-10,limit=300)[0]
    return lowvalue,highvalue


def edge_hidden_means(P, log10N, t):
    N=10.0**log10N
    L=log10N*math.log(10)
    v0,v1,delta,p,q,_,_,_,_=P.constants()
    a=math.sqrt(2*L)-(math.log(L)+math.log(4*math.pi))/(2*math.sqrt(2*L))
    b=1/math.sqrt(2*L)
    xlo=math.sqrt(v0)*(a+b*t)
    xhi=math.sqrt(v1)*(a+b*t)
    def low(u): return mixing_density(P,u)*conditional_cdf(N,xlo,v0+delta*u)
    def high(u): return mixing_density(P,u)*conditional_tail(N,xhi,v0+delta*u)
    zlo=quad(low,0,1,points=[.001,.01,.05,.25],epsabs=2e-10)[0]
    zhi=quad(high,0,1,points=[.9,.99,.999],epsabs=2e-10)[0]
    elo=quad(lambda u:(L*delta*u/v0)*low(u),0,1,points=[.001,.01,.05],epsabs=2e-10)[0]/zlo
    ehi=quad(lambda u:(L*delta*(1-u)/v1)*high(u),0,1,points=[.9,.99,.999],epsabs=2e-10)[0]/zhi
    theorylo=quad(lambda s:s**p*gumbel(t-s),0,70,epsabs=2e-11)[0]/quad(lambda s:s**(p-1)*gumbel(t-s),0,70,epsabs=2e-11)[0]
    theoryhi=quad(lambda s:s**q*(-math.expm1(-math.exp(-t-s))),0,70,epsabs=2e-11)[0]/quad(lambda s:s**(q-1)*(-math.expm1(-math.exp(-t-s))),0,70,epsabs=2e-11)[0]
    return elo,ehi,theorylo,theoryhi

def close(x,y,rel):
    assert math.isfinite(x) and math.isfinite(y) and abs(x/y-1)<rel,(x,y,abs(x/y-1))

assertions=0
for P in (Parameters(3,1,1,3,2), Parameters(5,2,.8,2,5)):
    v0,v1,delta,p,q,vbar,B,A0,A1=P.constants()
    check=quad(lambda u:mixing_density(P,u),0,1,epsabs=1e-11)[0]
    close(check,1,2e-10);assertions+=1
    for t in (-1.,0.,1.):
        x,y=leading_profiles(P,t)
        assert x>0 and y>0;assertions+=2
        for log10N in (8,16,24):
            lo,hi=exact_edge(P,log10N,t)
            L=log10N*math.log(10)
            # Leading convergence is only logarithmic; use conservative tolerance.
            close(L**p*lo,x,.65);close(L**q*hi,y,.65)
            assertions+=2
    observedlo,observedhi,theorylo,theoryhi=edge_hidden_means(P,16,0.)
    close(observedlo,theorylo,.5);close(observedhi,theoryhi,.5)
    assertions+=2
    for log10N in (8,16,24):
        lo,hi=exact_edge(P,log10N,0,raw=True)
        L=log10N*math.log(10)
        low_asym=A0/p*(math.log(L)/(2*L))**p
        high_asym=A1*gamma(q)/math.sqrt(4*math.pi)*L**(-q-.5)
        close(lo,low_asym,.65);close(hi,high_asym,.65)
        assertions+=2
print(f'PASS: {assertions} numerical/integral diagnostic assertions; analytic proofs are in RESULT.md.')
