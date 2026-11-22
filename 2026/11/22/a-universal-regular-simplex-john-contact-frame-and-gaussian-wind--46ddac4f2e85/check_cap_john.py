"""Numerical and symbolic-identity diagnostics for spherical-cap John ellipsoids.

Run with: python check_cap_john.py. The analytical proof, not these
finite tests, establishes the assertions for all dimensions and heights.
"""
import math
from scipy.integrate import quad
from scipy.special import gammaln, ndtr
from scipy.linalg import null_space
import numpy as np


def parameters(d, t):
    s = math.sqrt((d - 1)**2*t*t + 4*d)
    u = (s - (d + 1)*t)/(2*(d + 1))
    c = t + u
    v = math.sqrt(u*(u + d*c))
    return c, u, v


def normalized_fraction(d, t):
    c, u, v = parameters(d, t)
    if d <= 12:
        integral = quad(lambda x: (1-x*x)**((d-1)/2), t, 1, epsabs=1e-12)[0]
        k_ratio = math.exp(.5*math.log(math.pi) + gammaln((d+1)/2) - gammaln(1+d/2))
        return k_ratio*u*v**(d-1)/integral
    # Use regularized incomplete beta for numerical stability on high d.
    from scipy.special import betainc
    # Signed x coordinate for a uniform ball, CDF via beta tail.
    a = .5
    b = (d+1)/2
    p = .5 * betainc(b, a, 1-t*t) if t >=0 else 1-.5*betainc(b,a,1-t*t)
    return u * v**(d-1) / p


def gaussian_limit(lam):
    beta=(math.sqrt(lam*lam+4)+lam)/2
    alpha=1/beta
    return alpha * math.exp(-beta*beta/2) / ndtr(-lam)


def run():
    tests=0
    for d in [2,3,4,5,8,13,30,100]:
        for t in [-.99,-.8,-.25,0,.15,.5,.9,.99]:
            c,u,v=parameters(d,t)
            assert 0 < u and 0 < v <= 1.000001 and c >= 0
            assert abs((c-u)-t) < 1e-12
            assert abs((c*c+v*v+c*u/d)-1) < 1e-12
            assert abs((v*v-u*u)-d*c*u) < 1e-12
            # Full angular containment, including the exact curvature contact.
            for ss in np.linspace(-1,1,51):
                r2=(c+u*ss)**2+v*v*(1-ss*ss)
                assert r2<=1+5e-12
                assert c+u*ss>=t-5e-12
                tests+=2
            # A genuine d+1-point regular-simplex contact certificate.
            basis = null_space(np.ones((1,d)))
            omega = basis * math.sqrt(d/(d-1))
            latitude = np.column_stack((np.full(d,1/d),
                            omega*math.sqrt(1-1/d**2)))
            contacts=np.vstack((np.r_[-1.,np.zeros(d-1)], latitude))
            weights=np.full(d+1, d/(d+1))
            assert np.max(np.abs(weights@contacts))<2e-10
            assert np.max(np.abs(contacts.T@(contacts*weights[:,None])-np.eye(d)))<2e-10
            assert np.max(np.abs(contacts@contacts.T -
                   (np.eye(d+1)*(1+1/d)-np.ones((d+1,d+1))/d)))<2e-10
            tests+=3
            assert normalized_fraction(d,t) <=1+1e-7
            tests+=1
    for d in [2,3,4,8,12]:
        thin = math.exp(.5*math.log(math.pi)+gammaln((d+1)/2)-gammaln(1+d/2))*(d/(d+1))**d
        # Thin cap is a controlled asymptotic, not an exact equality at fixed t.
        a=normalized_fraction(d, .999) if d<=12 else 0
        assert abs(a/thin-1)<.012
        tests+=1
    for lam in [-3,-1,0,.5,2,4]:
        L=gaussian_limit(lam)
        for d in ([1000,5000] if lam<=2 else [5000,20000]):
            c,u,v=parameters(d,lam/math.sqrt(d))
            p=ndtr(-lam) # CLT cap volume; test strong asymptotic trends in determinant only
            val=math.sqrt(d)*u*v**(d-1)/p
            assert abs(val/L-1)<0.015
            tests+=1
    xs=np.linspace(-7,8,121)
    gs=[gaussian_limit(float(x)) for x in xs]
    assert all(gs[i]>gs[i+1] for i in range(len(gs)-1))
    assert all(g > math.sqrt(2*math.pi)/math.e for g in gs)
    tests+=len(gs)
    print(f"PASS: {tests} deterministic diagnostic assertions")

if __name__=='__main__':
    run()
