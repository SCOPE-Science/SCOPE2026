"""Independent finite checks for a stationary fractional wash-off covariance law.
All numerical checks are diagnostic; the theorem is proved analytically.
"""
from fractions import Fraction as Q
from random import Random
from math import sqrt


def formula(mu, vf, cu2, mean_u=Q(1)):
    d = mu*(2-mu)-vf
    assert 0 < d
    xmean = mean_u/mu
    x2 = mean_u**2*((2-mu)/mu+cu2)/d
    varx = x2-xmean*xmean
    vary = (mu*mu+vf)*x2-mean_u*mean_u
    cov1 = mean_u**2 * (cu2*mu*mu*(1-mu)-vf*(1+cu2*mu))/d
    return xmean, x2, varx, vary, cov1


def independently_derived(mu, vf, cu2, mean_u=Q(1)):
    f2=mu*mu+vf
    xmean=mean_u/mu
    u2=mean_u*mean_u*(1+cu2)
    x2=(2*(1-mu)*mean_u*xmean+u2)/(1-(1-2*mu+f2))
    cov1=mu*(mu-f2)*x2+mu*mu*mean_u*xmean-mean_u**2
    return xmean,x2,cov1


def run_exact():
    checks=0
    for mi in range(1,10):
        mu=Q(mi,10)
        for vi in range(0,11):
            vf=mu*(1-mu)*Q(vi,11)
            for ci in range(0,21):
                c=Q(ci,4)
                for ai in (Q(1,3), Q(1), Q(7,2)):
                    vals=formula(mu,vf,c,ai)
                    independent=independently_derived(mu,vf,c,ai)
                    assert vals[0]==independent[0] and vals[1]==independent[1]
                    assert vals[4]==independent[2]
                    assert vals[4] * (c*mu*mu*(1-mu)-vf*(1+c*mu))>=0
                    assert vals[2]>=0 and vals[3]>=0
                    checks+=5
    # Exponential interstorm additions; symmetric beta wash-off efficiency.
    cases = [(Q(2), Q(1,14), Q(5,7)),
             (Q(1), Q(0), Q(1)),
             (Q(1,2), Q(-1,10), Q(7,5))]
    for alpha, expected_c1, expected_vy in cases:
        varf=Q(1,4*(2*alpha+1))
        _,_,_,vy,c1=formula(Q(1,2),varf,Q(1))
        assert c1==expected_c1 and vy==expected_vy
        checks+=2
    assert Q(1,12)==Q(1)*Q(1,2)**2*(1-Q(1,2))/(1+Q(1)*Q(1,2))
    checks+=1
    print('exact rational checks:',checks)


def empirical(alpha, count=240000):
    rng=Random(int(alpha*100)+23)
    x=2.0
    observations=[]
    for i in range(count+6000):
        f=rng.betavariate(alpha,alpha)
        y=f*x
        x=(1-f)*x+rng.expovariate(1.0)
        if i>=6000: observations.append(y)
    n=len(observations)
    m=sum(observations)/n
    var=sum((y-m)**2 for y in observations)/n
    c1=sum((observations[i]-m)*(observations[i+1]-m) for i in range(n-1))/(n-1)
    return m,var,c1

if __name__=='__main__':
    run_exact()
    for alpha,expect in [(2.0,1/14),(1.0,0.0),(0.5,-0.1)]:
        mean,var,c1=empirical(alpha)
        print('alpha',alpha,'mean',round(mean,5),'variance',round(var,5),'lag1',round(c1,5),'theory',round(expect,5))
        assert abs(mean-1)<0.025
        assert abs(c1-expect)<0.035
    print('All independent diagnostics passed')
