"""Numerical supplementary checks for stochastic salinity excursion law.
Scientific parameters only; exact proof is in RESULT.md.
"""
import math
import random
from scipy.special import hyperu, gammaincc, gamma
from scipy.integrate import quad


def laplace_theory(a, lam, c, h, s):
    A = a * s / (lam + s)
    z = (lam + s) * h / c
    u = hyperu(A, a, z)
    uz = -A * hyperu(A+1, a+1, z)
    return lam / (lam+s) * u / (u-uz)


def mean_theory(a, lam, c, h):
    x = lam*h/c
    return math.exp(x) * gamma(a+1) * gammaincc(a+1, x) / (lam*x**a)


def mean_integral(a, lam, c, h):
    x = lam*h/c
    return quad(lambda t: math.exp(-t)*(1+t/x)**a,0, math.inf, epsabs=1e-11)[0]/lam


def experiment(a, lam, c, h, s, n=30000, seed=42):
    rng=random.Random(seed)
    means=[]; vals=[]; extra=0
    for _ in range(n):
        pos=h; time=0.; first=True
        for j in range(100000):
            dt=rng.expovariate(lam)
            time+=dt; pos+=c*dt
            R=rng.random()**(1/a)
            pos*=R
            if pos<h:
                break
            if first: extra+=1
            first=False
        else: raise AssertionError('unexpected excessive jump count')
        means.append(time); vals.append(math.exp(-s*time))
    m=sum(means)/n
    ex=sum(vals)/n
    sdm=(sum((v-m)**2 for v in means)/n)**.5/(n**.5)
    sde=(sum((v-ex)**2 for v in vals)/n)**.5/(n**.5)
    expected_m=mean_theory(a,lam,c,h)
    expected_ex=laplace_theory(a,lam,c,h,s)
    assert abs(m-expected_m)<7*sdm+0.001, (m,expected_m,sdm)
    assert abs(ex-expected_ex)<7*sde+0.0005, (ex,expected_ex,sde)
    assert abs(mean_integral(a,lam,c,h)-expected_m)<1e-8
    assert 0 < expected_ex < lam/(lam+s)  # strictly longer than first Poisson waiting time
    first_fail=extra/n
    upper=a*c/(lam*h)
    assert first_fail<=upper+0.01
    return dict(a=a,lam=lam,c=c,h=h,s=s,n=n,mean_mc=m,mean_exact=expected_m,mean_se=sdm,laplace_mc=ex,laplace_exact=expected_ex,laplace_se=sde,first_fail=first_fail,first_fail_bound=upper)


def check():
    cases=[(1,0.7,2.0,1.5,0.5),(2.5,1.3,0.8,2.2,1.0),(0.45,2.2,1.2,0.9,1.3),(1.8,1.5,0.6,12,2.0)]
    for i,args in enumerate(cases):
        print(experiment(*args,n=30000,seed=20261120+i),flush=True)
    # Analytic properties: exact mean monotone via positive integral representation;
    # numerical check only corroborates strict inequalities over a grid.
    for a in [0.3,1,2,5]:
        vals=[mean_theory(a,1.3,0.7,h) for h in [0.3,0.6,1,2,3,5,8,15]]
        assert all(v1>v2>1/1.3 for v1,v2 in zip(vals,vals[1:]))
    print('all supplementary checks passed')

if __name__=='__main__':check()
