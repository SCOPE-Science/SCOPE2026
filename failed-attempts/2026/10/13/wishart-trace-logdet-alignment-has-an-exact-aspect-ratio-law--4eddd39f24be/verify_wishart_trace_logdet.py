#!/usr/bin/env python3
import math

# Deterministic numerical replay of the joint-transform identities.

def log_multigamma(a,p):
    if a <= (p-1)/2:
        raise ValueError('outside multivariate-gamma domain')
    return p*(p-1)*0.25*math.log(math.pi) + sum(math.lgamma(a-j/2) for j in range(p))

def trigamma(x):
    # Recurrence to a stable asymptotic region, then Bernoulli expansion.
    s=0.0
    while x < 24.0:
        s += 1.0/(x*x)
        x += 1.0
    z=1.0/x
    z2=z*z
    s += z + 0.5*z2 + (1.0/6.0)*z*z2 - (1.0/30.0)*z*z2*z2 + (1.0/42.0)*z*z2*z2*z2 - (1.0/30.0)*z*z2**4 + (5.0/66.0)*z*z2**5
    return s

def logM(p,nu,s,t):
    return (p*s*math.log(2.0)
            + log_multigamma(nu/2+s,p)-log_multigamma(nu/2,p)
            - p*(nu/2+s)*math.log1p(-2.0*t))

def V(p,nu):
    return sum(trigamma((nu-j+1)/2) for j in range(1,p+1))

def corr(p,nu):
    return math.sqrt(2.0*p/(nu*V(p,nu)))

def run():
    mixed_checks=0
    t2_checks=0
    s2_checks=0
    corr_checks=0
    h=2e-4
    # Moderate grid avoids cancellation while spanning near-boundary and thin cases.
    for p in range(1,13):
        for off in (0.0,1.0,4.0,12.0,40.0):
            nu=p+off
            # nu=p is valid because nu>p-1.
            fpp=logM(p,nu,h,h); fpm=logM(p,nu,h,-h)
            fmp=logM(p,nu,-h,h); fmm=logM(p,nu,-h,-h)
            mixed=(fpp-fpm-fmp+fmm)/(4*h*h)
            assert abs(mixed-2*p) < 4e-4*max(1.0,p)
            mixed_checks+=1

            f0=logM(p,nu,0.0,0.0)
            t2=(logM(p,nu,0.0,h)-2*f0+logM(p,nu,0.0,-h))/(h*h)
            assert abs(t2-2*nu*p) < 3e-3*max(1.0,2*nu*p)
            t2_checks+=1

            s2=(logM(p,nu,h,0.0)-2*f0+logM(p,nu,-h,0.0))/(h*h)
            vv=V(p,nu)
            assert abs(s2-vv) < 5e-4*max(1.0,vv)
            s2_checks+=1

            c=corr(p,nu)
            assert 0.0 < c <= 1.0000001
            corr_checks+=1

    # Aspect-ratio checks at increasing scale.
    aspect_checks=0
    for r in (0.1,0.25,0.5,0.75,0.9):
        target=math.sqrt(r/(-math.log1p(-r)))
        nu=20000
        p=max(1,int(round(r*nu)))
        got=corr(p,nu)
        assert abs(got-target) < 0.004
        aspect_checks+=1

    # Thin and near-square endpoints.
    for nu,p,kind in [(20000,20,'thin'),(20000,100,'thin'),(20000,19990,'square'),(20000,20000,'square')]:
        got=corr(p,nu)
        if kind=='thin': assert got>0.995
        else: assert got<0.37
        aspect_checks+=1

    print('VERIFY_OK '
          f'mixed_checks={mixed_checks} t2_checks={t2_checks} '
          f's2_checks={s2_checks} corr_checks={corr_checks} '
          f'aspect_checks={aspect_checks}')

if __name__=='__main__':
    run()
