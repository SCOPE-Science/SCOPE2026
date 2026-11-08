#!/usr/bin/env python3
"""Reproduce current-transform and marginal-coefficient checks; SciPy >=1.9."""
import math
from scipy.integrate import quad
from scipy.special import i0e, i1e, exp1, erfc


def instantaneous_no_reset(a):
    return float(i0e(2*a))


def integrated_no_reset(a):
    return float(a * (i0e(2*a) + i1e(2*a)))


def survival(a, alpha, t0):
    return 1.0 if a <= t0 else (t0/a)**alpha


def survival_transform_analytic(s, alpha, t0):
    z=s*t0
    head=-math.expm1(-z)/s
    if alpha == 0.5:
        tail=math.sqrt(t0/s)*math.sqrt(math.pi)*erfc(math.sqrt(z))
    elif alpha == 1.0:
        tail=t0*exp1(z)
    elif alpha == 1.5:
        tail=t0**1.5*math.sqrt(s)*(2*math.exp(-z)/math.sqrt(z)-2*math.sqrt(math.pi)*erfc(math.sqrt(z)))
    else:
        raise ValueError('this checker covers the three marginal alpha values')
    return head + tail


def weighted_transform(s, alpha, t0, function):
    head=quad(lambda a: math.exp(-s*a)*function(a),0,t0,epsabs=2e-11,epsrel=1e-11)[0]
    def integrand(u):
        a=math.exp(u)
        return math.exp(-s*a)*(t0/a)**alpha*function(a)*a
    tail=quad(integrand,math.log(t0),math.log(75/s),epsabs=1e-9,epsrel=2e-10,limit=400)[0]
    return head + tail


def transforms(s, alpha, t0):
    qhat=survival_transform_analytic(s,alpha,t0)
    denom=s*qhat
    return (weighted_transform(s,alpha,t0,instantaneous_no_reset)/(s*denom),
            weighted_transform(s,alpha,t0,integrated_no_reset)/denom)


def main():
    count=0
    for a in (0.001,0.01,0.2,1.,5.,100.):
        integral=quad(instantaneous_no_reset,0,a,epsabs=1e-11,epsrel=1e-11)[0]
        assert abs(integral-integrated_no_reset(a))<1e-9*(1+integral)
        count+=1
    for alpha in (0.5,1.,1.5):
        for s in (1e-3,1e-5,1e-7):
            qhat=survival_transform_analytic(s,alpha,1.)
            numerical=weighted_transform(s,alpha,1.,lambda a:1.)
            assert abs(qhat-numerical)/qhat < 1e-8
            count+=1
    G=weighted_transform(1e-12,1.,1.,instantaneous_no_reset)
    G_exact=quad(instantaneous_no_reset,0,1.,epsabs=1e-10)[0]+quad(lambda a:instantaneous_no_reset(a)/a,1.,math.inf,epsrel=1e-10,limit=250)[0]
    assert abs(G_exact-1.103030746080358)<1e-8
    assert abs(G-G_exact)/G_exact < 3e-6
    count+=2
    for alpha in (0.5,1.,1.5):
        deviations=[]
        for s in (1e-3,1e-5,1e-7):
            diff,total=transforms(s,alpha,1.)
            if alpha==0.5:
                asym=(1/(2*math.pi))*s**(-1.5)*math.log(1/s)
                ratio=diff/asym
            elif alpha==1.:
                asym=G_exact/(s*s*math.log(1/s))
                ratio=diff/asym
            else:
                asym=1/(3*math.sqrt(math.pi))*math.log(1/s)/s
                ratio=total/asym
            deviations.append(abs(ratio-1.))
            print('alpha',alpha,'s',s,'Laplace leading coefficient ratio',round(ratio,9))
            assert math.isfinite(ratio) and 0.85<ratio<1.3
            count+=1
        assert deviations[2]<deviations[0]
        count+=1
    print('G(1)=',round(G_exact,12))
    print('PASS:',count,'independent numerical identities and marginal checks')

if __name__=='__main__':
    main()
