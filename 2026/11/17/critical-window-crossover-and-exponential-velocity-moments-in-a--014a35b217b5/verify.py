"""Finite, standalone numerical corroboration of a cubic-center asymptotic theorem.

Run: python verify.py
Requires only Python 3.10+ standard library. This program is not a proof of an infinite limit.
"""
from math import cos, sin, sqrt, exp, expm1, pi, isfinite


def simpson(f, left=0., right=pi/2, n=65536):
    if n % 2:
        raise ValueError('even n required')
    step=(right-left)/n
    s=f(left)+f(right)
    for j in range(1,n):
        s+=(4 if j&1 else 2)*f(left+j*step)
    return s*step/3


def inspect(alpha, beta, A, q):
    d=1/beta-alpha/(beta*beta)
    v0=sqrt(1+alpha*A*A)

    def v(theta):
        if theta==0: return 0.0
        s=A*A*sin(theta)**2
        Y=(alpha*A*A/beta+d)*expm1(beta*s)+alpha*s/beta
        assert Y>0
        return sqrt(Y)/A

    def base(theta):
        if theta==0:
            return 1/v0
        return sin(theta)/v(theta)
    J=simpson(base)
    T=4*J
    targetT=2*pi/(A*A*sqrt(alpha*beta))
    if q==1:
        m=1/J
        targetM=2*sqrt(alpha*beta)*A*A/pi
    else:
        def integrand(theta):
            if theta==0: return 0.0
            return sin(theta)*v(theta)**(q-1)
        m=simpson(integrand)/J
        gamma=sqrt(alpha/beta)
        if q<1:
            targetM=gamma**q/cos(pi*q/2)
        else:
            targetM=gamma**q*A*sqrt(2*beta/(pi*(q-1)))*exp(beta*(q-1)*A*A/2)
    return T/targetT,m/targetM,T,m


def main():
    for alpha,beta,A in ((1.,1.,5.),(.5,3.,5.),(2.,.7,5.)):
        for q in (0.,.5,1.,1.5):
            rt,rm,T,m=inspect(alpha,beta,A,q)
            assert isfinite(T) and T>0 and isfinite(m) and m>0
            assert abs(rt-1)<.09, (alpha,beta,A,q,'period',rt)
            assert abs(rm-1)<.20, (alpha,beta,A,q,'moment',rm)
        # Exact geometric identity: average absolute speed = four horizontal half-amplitudes / T.
        _,_,T,M1=inspect(alpha,beta,A,1.)
        assert abs(M1-(4/T))<1e-7
    # The order-one window interpolates between the distinct fixed-order regimes.
    for alpha, beta, A in ((1.,1.,5.), (.5,3.,5.), (2.,.7,5.)):
        for lam in (-2.,0.,2.):
            order=1+lam/(A*A)
            _,_,_,observed=inspect(alpha,beta,A,order)
            profile=simpson(lambda u: exp(beta*lam*(1-u*u)/2),0.,1.,8192)
            expected=(2*sqrt(alpha*beta)/pi)*A*A*profile
            assert abs(observed/expected-1)<.13,(alpha,beta,lam,observed/expected)
    # The squared-speed graph must obey the original first-order equation exactly.
    for alpha,beta,A,s in ((1.,1.,2.,.1),(.5,3.,2.,.7),(2.,.7,3.,1.4)):
        d=1/beta-alpha/(beta*beta)
        y2=(alpha*A*A/beta+d)*expm1(beta*s)+alpha*s/beta
        deriv=(alpha*A*A+beta*d)*exp(beta*s)+alpha/beta
        assert abs(deriv-(1+alpha*(A*A-s)+beta*y2)) < 1e-9*max(1,abs(deriv))
    print('CUBIC_CENTER_CAUCHY_MOMENT_CHECK_OK')


if __name__=='__main__':
    main()
