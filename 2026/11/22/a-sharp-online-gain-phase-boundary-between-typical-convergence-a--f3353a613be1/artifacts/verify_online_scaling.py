#!/usr/bin/env python3
"""Exact-rational checks for a two-curvature out-of-sample ratio-feedback step."""
from fractions import Fraction as F

def expectation(vals, weights):
    return sum((v*w for v,w in zip(vals,weights)), F(0))

def verify(a, b, low_probability, eta):
    assert F(0)<a<b and F(0)<low_probability<1
    assert F(0)<eta<F(1)/(2*b*b)
    law = [(a,low_probability),(b,1-low_probability)]
    mu = expectation([x for x,p in law],[p for x,p in law])
    nu = expectation([x*x for x,p in law],[p for x,p in law])
    sigma2 = nu-mu*mu
    center=1/mu
    q = 1-2*eta*mu*mu
    var = eta*nu*sigma2/(mu*mu*(mu*mu-eta*nu*nu))
    assert var>0 and F(0)<q<1
    joint=[(x,z,px*pz) for x,px in law for z,pz in law]
    def step(p,x,z):
        # Gradient of (z/x)*(1-p*x)^2 is -2*z*(1-p*x).
        return p+2*eta*z*(1-p*x)
    # First/second moments under the affine update, evaluating all four pairs exactly.
    first=expectation([step(center,x,z) for x,z,w in joint], [w for x,z,w in joint])
    assert first==center
    noise_second=expectation([(step(center,x,z)-center)**2 for x,z,w in joint], [w for x,z,w in joint])
    assert noise_second==4*eta*eta*nu*sigma2/(mu*mu)
    slope_first=expectation([1-2*eta*x*z for x,z,w in joint],[w for x,z,w in joint])
    slope_second=expectation([(1-2*eta*x*z)**2 for x,z,w in joint],[w for x,z,w in joint])
    assert slope_first == q
    assert slope_second==1-4*eta*mu*mu+4*eta*eta*nu*nu
    assert var == slope_second*var+noise_second
    # Centering confirms there is no hidden covariance term: E[Y] = 0.
    long_run=var*(1+q)/(1-q)
    predicted=nu*sigma2*(1-eta*mu*mu)/(mu**4*(mu*mu-eta*nu*nu))
    assert long_run==predicted
    small_eta=nu*sigma2/(mu**6)
    assert small_eta>0
    # Variance strictly grows with eta, and the integrated average variance grows too.
    for eta2 in (eta/2,eta*F(3,4)):
        assert eta2*nu*sigma2/(mu*mu*(mu*mu-eta2*nu*nu)) < var
        integrated=nu*sigma2*(1-eta2*mu*mu)/(mu**4*(mu*mu-eta2*nu*nu))
        assert small_eta<integrated<long_run
    # Valid finite sequence of sample pairs: projection remains inactive.
    p=(1/a+1/b)/2
    x=F(1)
    for t in range(128):
        aa,bb,_ = joint[(t*t+3*t+1)%4]
        x=(1-p*aa)*x
        p=step(p,aa,bb)
        assert 1/b<p<1/a and x!=0
    prospective = expectation([ (1-a*center)**2, (1-b*center)**2 ], [low_probability,1-low_probability]) + nu*var
    assert prospective == sigma2/(mu*mu-eta*nu*nu)
    return mu,nu,center,var,q,long_run,small_eta

if __name__ == '__main__':
    inputs=[(F(1),F(2),F(1,2),F(1,16)),
            (F(2),F(5),F(1,3),F(1,100)),
            (F(1,5),F(7,5),F(3,4),F(1,8)),
            (F(3),F(4),F(2,7),F(1,64))]
    results=[]
    for args in inputs:
        results.append(verify(*args))
    assert results[0] == (F(3,2),F(5,2),F(2,3),F(10,1071),F(23,32),F(550,9639),F(40,729))
    for item in results:
        print('mean_A=%s E_A2=%s target=%s var=%s corr=%s integrated=%s eta_to_zero=%s' % item)
    # Sharp stationary prospective-error phase with uniform equal-probability curvature endpoints.
    b=F(10);eta=F(1,225);mu=(1+b)/2;nu=(1+b*b)/2
    sigma2=nu-mu*mu
    eta_crit=4*b/(1+b*b)**2
    eta_max=F(1)/(2*b*b)
    prospective=sigma2/(mu*mu-eta*nu*nu)
    assert eta_crit<eta<eta_max
    assert prospective==F(18225,17024)>1
    assert sigma2/(mu*mu)==F(81,121)<1
    assert eta*nu*sigma2/(mu*mu*(mu*mu-eta*nu*nu)) == F(8181,1029952)
    def f(t): return t**4-8*t**3+2*t*t+1
    assert f(F(7739,1000))<0<f(F(7740,1000))
    assert f(F(1))<0 and f(F(8))>0
    # For b>1, f' changes from negative to positive once at 3+sqrt(8).
    # Thus the root bracket is the unique b>1 where a nonempty expansion window begins.
    assert prospective>1 and F(9,11)<1
    print('PASS: phase window b=10, eta=1/225, prospective factor 18225/17024; root in (7.739,7.740)')
    print('PASS: exact four-pair moment recurrences, variance identities, autocorrelation, and 512 finite steps')
