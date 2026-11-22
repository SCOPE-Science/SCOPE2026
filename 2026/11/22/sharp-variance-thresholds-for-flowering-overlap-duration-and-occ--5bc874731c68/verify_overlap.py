"""Supplementary numerical checks for the Gaussian phenology-overlap theorem.

The analytic proof is separate. This script is not a proof of the
for-all-parameter assertions.
"""
import math
import random

SQRT2 = math.sqrt(2)
INVROOT2PI = 1/math.sqrt(2*math.pi)

def phi(y):
    return math.exp(-y*y/2)*INVROOT2PI

def cdf(y):
    return 0.5*math.erfc(-y/SQRT2)

def gs(x,s):
    return math.exp(-x*x/(2*s))/math.sqrt(2*math.pi*s)

def probability(L,d,s):
    if s == 0:
        return float(d<L)
    return cdf((L-d)/math.sqrt(s))-cdf((-L-d)/math.sqrt(s))

def overlap_exact(L,d,s):
    if s == 0:
        return max(0,L-d)
    z=math.sqrt(s)
    # Gaussian mass and moment between a and b for N(d,s)
    def mass(a,b):
        return cdf((b-d)/z)-cdf((a-d)/z)
    def mom(a,b):
        return d*mass(a,b)+s*(gs(a-d,s)-gs(b-d,s))
    return L*mass(-L,L)+mom(-L,0)-mom(0,L)

def overlap_quadrature(L,d,s,terms=2000):
    if s == 0: return max(0,L-d)
    step=2*L/terms
    return step/3*sum((1 if i in (0,terms) else 4 if i%2 else 2)
           * (L-abs(-L+i*step))*gs(-L+i*step-d,s)
           for i in range(terms+1))

def derivative(L,d,s):
    return .5*(gs(d-L,s)-2*gs(d,s)+gs(d+L,s))

def logcosh(u):
    u=abs(u)
    return u+math.log1p(math.exp(-2*u))-math.log(2)

def optimal_overlap_variance(L,d):
    if 2*d<=L: return 0.
    a=2*d/L
    def h(z): return logcosh(a*z)-z
    lo=1e-14
    hi=1.
    while h(hi)<0: hi*=2
    for _ in range(180):
        mid=(hi+lo)/2
        if h(mid)>0: hi=mid
        else: lo=mid
    return L*L/(2*((hi+lo)/2))

def optimal_probability_variance(L,d):
    if d<=L: return None
    return 2*d*L/math.log((d+L)/(d-L))

def test():
    rng=random.Random(20261121)
    count=0
    for _ in range(200):
        L=rng.uniform(.5,2.)
        d=rng.uniform(0,3*L)
        s=rng.uniform(.05*L*L,3*L*L)
        exact=overlap_exact(L,d,s)
        quad=overlap_quadrature(L,d,s,terms=2000)
        assert abs(exact-quad)<1e-7*L, (L,d,s,exact,quad)
        h=1e-5*s
        finite_diff=(overlap_exact(L,d,s+h)-overlap_exact(L,d,s-h))/(2*h)
        assert abs(finite_diff-derivative(L,d,s))<2e-7/L,(L,d,s,finite_diff,derivative(L,d,s))
        count+=2
    for _ in range(1000):
        L=rng.uniform(.4,2.1)
        d=rng.uniform(.01,3*L)
        opt=optimal_overlap_variance(L,d)
        if d<=L/2:
            for s in [(.04+.2*j)*L*L for j in range(1,9)]:
                assert derivative(L,d,s)<0
                count+=1
        else:
            assert opt>0
            for s in [opt*.32, opt*.77, opt*1.25,opt*2.5]:
                assert (derivative(L,d,s)>0) == (s<opt)
                count+=1
        if d>L:
            other=optimal_probability_variance(L,d)
            assert other<opt<d*d, (L,d,opt,other)
            count+=1
    s=optimal_overlap_variance(1,.75)
    assert abs(math.sqrt(s)-.6081417030881335)<1e-9
    assert abs(overlap_exact(1,.75,s)-.3244756341048125)<1e-9
    assert abs(probability(1,.75,s)-.6574926974280855)<1e-9
    p=optimal_probability_variance(1,1.5)
    assert abs(math.sqrt(p)-1.3652856124924322)<1e-9
    q=optimal_overlap_variance(1,1.5)
    assert abs(math.sqrt(q)-1.441557116882646)<1e-9
    print('PASS', count, 'supplementary analytic/quadrature/finite-difference/sign checks')
    print('L=1 d=.75: sigma_F=', math.sqrt(s), 'Fmax=', overlap_exact(1,.75,s), 'P-at-F=', probability(1,.75,s))
    print('L=1 d=1.5: sigma_P=', math.sqrt(p),'sigma_F=',math.sqrt(q))

if __name__=='__main__': test()
