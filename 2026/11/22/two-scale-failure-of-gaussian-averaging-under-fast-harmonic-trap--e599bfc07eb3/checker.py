"""Reproduce the stationary variance mixture and sharp rare-displacement saddle."""
import math
from scipy.special import betaln, logsumexp
from scipy.integrate import quad
from scipy.optimize import brentq


def setup(alpha, beta, diffusivity):
    assert 0 < alpha < beta and diffusivity > 0
    a, b = 1/(2*beta), 1/(2*alpha)
    z0 = alpha/(alpha+beta)
    lo, hi = diffusivity/beta, diffusivity/alpha
    L = hi-lo
    return a,b,z0,lo,hi,L


def F(alpha,beta,D,y,z):
    a,b,z0,lo,hi,L=setup(alpha,beta,D)
    v=lo+L*z
    h=a*math.log(z0/z)+b*math.log((1-z0)/(1-z))
    return y*y/(2*v)+h


def saddle(alpha,beta,D,y):
    a,b,z0,lo,hi,L=setup(alpha,beta,D)
    if y == 0: return z0
    def dF(z):
        return -a/z+b/(1-z)-L*y*y/(2*(lo+L*z)**2)
    return brentq(dF,z0,1-1e-13,xtol=1e-14)


def asymptotic(alpha,beta,D,y):
    a,b,z0,lo,hi,L=setup(alpha,beta,D)
    z=saddle(alpha,beta,D,y)
    v=lo+L*z
    hpp0=a/z0**2+b/(1-z0)**2
    Fpp=a/z**2+b/(1-z)**2+y*y*L*L/v**3
    W=lambda u:alpha+(beta-alpha)*u
    pref=math.sqrt(hpp0/Fpp) * W(z)/W(z0) * z0*(1-z0)/(z*(1-z)) / math.sqrt(2*math.pi*v)
    posterior=beta*z/W(z)
    return F(alpha,beta,D,y,z),pref,z,posterior,Fpp


def log_density(alpha,beta,D,q,y):
    a,b,z0,lo,hi,L=setup(alpha,beta,D)
    # high-accuracy real-space integral, with log-stabilization
    i,pref,z,pw,Fpp=asymptotic(alpha,beta,D,y)
    norm=math.log(alpha+beta)-math.log(2*alpha*beta)-betaln(a*q,b*q)
    def log_integrand(u):
        if u<=0 or u>=1: return -math.inf
        v=lo+L*u
        return (norm+math.log(alpha+(beta-alpha)*u)+(a*q-1)*math.log(u)
                +(b*q-1)*math.log1p(-u)-0.5*math.log(2*math.pi*v)-q*y*y/(2*v))
    m=log_integrand(z)
    # Integral with split at maximizer; logarithmic compensator prevents underflow.
    def integrand(u):return math.exp(log_integrand(u)-m)
    ans=quad(integrand,0,z,epsabs=1e-12,epsrel=2e-10,limit=300)[0]+quad(integrand,z,1,epsabs=1e-12,epsrel=2e-10,limit=300)[0]
    return m+math.log(ans)


def check():
    total=0
    for alpha,beta,D in [(1.,3.,1.),(.7,5.,2.),(2.,2.2,.4)]:
        a,b,z0,lo,hi,L=setup(alpha,beta,D)
        # exact normalization E[W(Z)]/normalizer via beta moments
        Ez=a/(a+b)
        C=(alpha+beta)/(2*alpha*beta)
        assert abs(C*(alpha+(beta-alpha)*Ez)-1)<1e-12;total+=1
        assert abs(beta*z0/(alpha+(beta-alpha)*z0)-.5)<1e-12;total+=1
        for y in [0.,.4,1.,2.,4.]:
            I,p,z,pw,Fpp=asymptotic(alpha,beta,D,y)
            assert 0<z<1 and 0<=pw<=1 and Fpp>0;total+=3
            if y>0:
                assert z>z0 and pw>.5 and I>y*y/(2*hi) and I<y*y/(2*(2*D/(alpha+beta)));total+=4
            else:
                assert abs(p-1/math.sqrt(2*math.pi*(2*D/(alpha+beta))))<1e-12;total+=1
            # Numerical integrals approach the saddle, including its prefactor.
            for q in (80.,320.,800.):
                if y>3 and q>320: continue
                exact=log_density(alpha,beta,D,q,y)
                approximation=math.log(p)-q*I
                assert abs(exact-approximation)<.09, (alpha,beta,D,y,q,exact,approximation)
                total+=1
        # Small-y fourth-order coefficient, checked with high-order difference quotient.
        c4=-(alpha+beta)*(beta-alpha)**2/(64*D**2)
        y=.05
        I,*_=asymptotic(alpha,beta,D,y)
        first=(alpha+beta)*y*y/(4*D)
        assert abs((I-first)/y**4-c4)<.025*max(1,abs(c4));total+=1
        # large-y selected weak trap scaling
        for y in (30.,50.):
            I,p,z,pw,Fpp=asymptotic(alpha,beta,D,y)
            asymc=D*beta/(alpha**2*(beta-alpha))
            assert abs((1-z)*y*y/asymc-1)<.18;total+=1
    # First loss of relative accuracy of the averaged-trap Gaussian occurs at q**(1/4).
    for alpha,beta,D in [(1.,3.,1.),(.7,5.,2.)]:
        K=(alpha+beta)*(beta-alpha)**2/(64*D**2)
        v0=2*D/(alpha+beta)
        for t in (.8,1.2):
            for q in (800.,2400.):
                x=t*q**.25
                logp=log_density(alpha,beta,D,q,x/math.sqrt(q))
                loggauss=-.5*math.log(2*math.pi*v0)-x*x/(2*v0)
                assert abs((logp-loggauss)-K*t**4)<.15, (alpha,beta,D,q,t)
                total+=1
    print('PASS',total,'deterministic mathematical assertions')

if __name__=='__main__': check()
