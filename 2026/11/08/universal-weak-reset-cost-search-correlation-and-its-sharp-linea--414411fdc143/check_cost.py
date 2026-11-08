#!/usr/bin/env python3
"""Independent numerical reconstruction for a Brownian reset-cost/first-passage theorem.
The primary proof is analytic; these tests are finite-parameter cross-checks only.
"""
import math
from scipy.integrate import quad
from scipy.special import gamma

def cost_power(beta, r, a=1., D=1.):
    k=math.sqrt(r/D)
    def L(z):
        return quad(lambda y:(a-y)**z*math.sinh(k*y), 0., a,epsabs=1e-12)[0]
    def Lprime(z):
        return quad(lambda y:(a-y)**z*y*math.cosh(k*y), 0., a,epsabs=1e-12)[0]
    def H(n):
        z=n*beta
        minus=math.exp(-k*a)/(D*k)*L(z)
        plus=math.exp(-k*a)*math.sinh(k*a)*gamma(z+1)/(D*k**(z+2))
        return minus+plus
    h1=H(1);h2=H(2)
    minus=math.exp(-k*a)/(D*k)*L(beta)
    plus=math.exp(-k*a)*math.sinh(k*a)*gamma(beta+1)/(D*k**(beta+2))
    dplus=plus*(a/math.tanh(k*a)-a-(beta+2)/k)
    dminus=math.exp(-k*a)/(D*k)*((-a-1/k)*L(beta)+Lprime(beta))
    minus_Bprime_over_B=-(dplus+dminus)/(2*D*k*h1)
    b1=r*h1;b2=r*h2
    f=math.exp(-k*a);g=k*a
    ec=b1/f
    vc=b2/f+(b1/f)**2
    vt=(math.expm1(2*g)-g*math.exp(g))/r**2
    et=math.expm1(g)/r
    cov=ec*(et-g/(2*r)+minus_Bprime_over_B)
    return dict(meanT=et,meanC=ec,varT=vt,varC=vc,cov=cov,corr=cov/math.sqrt(vc*vt),slope=r*minus_Bprime_over_B)

def limit(beta):
    return (beta+1)*gamma(beta+1)/(2*math.sqrt(gamma(2*beta+1)))

if __name__=='__main__':
    n=0
    for beta in [0.,0.25,0.5,1.,1.5,2.,3.]:
        for r in [0.02, 0.002, 0.0002, 0.00002]:
            x=cost_power(beta,r)
            assert 0<x['corr']<1, (beta,r,x)
            assert x['cov']>0
            assert x['varT']>0 and x['varC']>0
            assert abs(x['slope']-(beta+1)/2) < 0.15, (beta,r,x['slope'])
            if r<=0.00002:
                assert abs(x['corr']-limit(beta))<0.04,(beta,r,x['corr'],limit(beta))
            n+=5
        print('beta',beta,'limit',round(limit(beta),9),'observed r=2e-5',round(cost_power(beta,2e-5)['corr'],9))
    assert abs(limit(1.)-1/math.sqrt(2))<1e-14
    assert all(limit(x)<limit(1.) for x in [i/10 for i in range(0,10)]+[i/10 for i in range(11,101)])
    print('passed',n+101,'cost-time correlation cross-checks')

# A separate Laplace-kernel quadrature also handles non-power regularly varying costs.
def cost_general(beta, r, a=1., D=1., logfactor=True):
    k=math.sqrt(r/D)
    def cc(u):
        return u**beta*(1+math.log1p(u) if logfactor else 1.)
    def L(n):
        return quad(lambda y: cc(a-y)**n*math.sinh(k*y),0,a,epsabs=1e-11)[0]
    def Lp():
        return quad(lambda y: cc(a-y)*y*math.cosh(k*y),0,a,epsabs=1e-11)[0]
    def M(n, extra=0):
        return quad(lambda z: z**extra*cc(z/k)**n*math.exp(-z),0,100,epsabs=1e-10)[0]/k**(extra+1)
    minus1=math.exp(-k*a)/(D*k)*L(1)
    plus1=math.exp(-k*a)*math.sinh(k*a)/(D*k)*M(1)
    h1=minus1+plus1
    h2=math.exp(-k*a)/(D*k)*L(2)+math.exp(-k*a)*math.sinh(k*a)/(D*k)*M(2)
    dhplus=plus1*(a/math.tanh(k*a)-a-1/k) -math.exp(-k*a)*math.sinh(k*a)/(D*k)*M(1,extra=1)
    dhminus=math.exp(-k*a)/(D*k)*((-a-1/k)*L(1)+Lp())
    rate=-(dhplus+dhminus)/(2*D*k*h1)
    g=k*a; f=math.exp(-g); b1=r*h1;b2=r*h2
    ec=b1/f; vc=b2/f+ec*ec
    vt=(math.expm1(2*g)-g*math.exp(g))/r**2
    cov=ec*(math.expm1(g)/r-g/(2*r)+rate)
    return cov/math.sqrt(vc*vt),r*rate

if __name__=='__main__':
    for beta in [0.0, 0.75, 1.0, 2.0]:
        vals=[]
        for r in [1e-3,1e-5,1e-7]:
            cv,slope=cost_general(beta,r)
            assert cv>0 and cv<1
            assert abs(slope-(beta+1)/2)<0.22
            vals.append(cv)
        assert abs(vals[-1]-limit(beta)) < 0.060,(beta,vals)
        print('slowly-varying beta',beta,'rho sequence', [round(x,6) for x in vals],'limit',round(limit(beta),6))
    print('passed 12 slowly varying cost quadratures and 12 derivative checks')

# Cross-differentiate the joint renewal transform directly, independently
# of the closed covariance formula used by cost_power().
def direct_mixed_covariance(beta, r, a=1.0, D=1.0):
    def H(q):
        k=math.sqrt(q/D)
        left=quad(lambda y: (a-y)**beta*math.sinh(k*y), 0,a)[0]
        return math.exp(-a*k)/(D*k)*(left+math.sinh(a*k)*gamma(beta+1)/k**(beta+1))
    def cost_laplace_weighted(s):
        q=r+s
        f=math.exp(-a*math.sqrt(q/D))
        A=r*(1-f)/q
        return f*r*H(q)/(1-A)**2
    h=1e-5*r
    # The derivative is -E[T exp(-sT) C] at the origin.
    etc=-(cost_laplace_weighted(h)-cost_laplace_weighted(-h))/(2*h)
    ex=cost_power(beta,r,a,D)
    derived=etc-ex['meanT']*ex['meanC']
    return derived,ex['cov']

if __name__=='__main__':
    for beta in [0.,0.5,1.,2.]:
        for r in [0.03,0.2,1.]:
            direct, formula=direct_mixed_covariance(beta,r)
            assert abs(direct-formula)<3e-5*max(1.,abs(formula)),(beta,r,direct,formula)
    print('passed 12 independently cross-differentiated joint-transform covariance checks')

if __name__=='__main__':
    for aa,DD in [(0.3,2.0),(2.5,0.75),(5.0,3.0)]:
        for beta in (0.0,0.75,1.0,2.5):
            x=cost_power(beta,1e-6,aa,DD)
            assert abs(x['corr']-limit(beta))<0.01
            independent,formula=direct_mixed_covariance(beta,0.1,aa,DD)
            assert abs(independent-formula)<1e-4*max(1.,abs(formula))
    print('passed 12 non-unit length/diffusivity asymptotics and 12 mixed-derivative checks')
