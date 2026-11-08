"""Numerical cross-checks for the local distance-histogram law of flat Klein bottles.

Run: python3 verify_klein.py. All proofs are analytic; finite tests are diagnostic.
"""
import math
import numpy as np
from scipy.integrate import quad


def lens(r, d):
    if d >= 2.0*r:
        return 0.0
    if d <= 0:
        return math.pi*r*r
    z = min(1.0, d/(2.0*r))
    theta = math.acos(z)
    if theta < 0.01:
        # theta-sin(theta)cos(theta) = 2 theta^3/3 - 2 theta^5/15 + 4 theta^7/315 + ...
        delta = (2/3)*theta**3 - (2/15)*theta**5 + (4/315)*theta**7
    else:
        delta = theta - math.sin(theta)*math.cos(theta)
    return 2*r*r*delta


def local_deficit(a, b, r):
    hor = lens(r, a)
    if 2*r <= b:
        return hor
    upper = math.sqrt((2*r-b)*(2*r+b))
    glide = 2*quad(lambda u: lens(r, math.sqrt(b*b+u*u)), 0, upper,
                   epsabs=1e-13, epsrel=1e-12)[0]/a
    return hor+glide


def paired_cdf(a, b, r, samples=350000, seed=1047):
    rng = np.random.default_rng(seed)
    p = rng.random((samples,2))*np.array([a,b]); q = rng.random((samples,2))*np.array([a,b])
    dist2 = np.full(samples, np.inf)
    for m in range(-2,3):
        for k in range(-2,3):
            dx = p[:,0]-(q[:,0]+m*a)
            dy = p[:,1]-(q[:,1]+2*k*b)
            dist2 = np.minimum(dist2,dx*dx+dy*dy)
            dx = p[:,0]-(m*a-q[:,0])
            dy = p[:,1]-(q[:,1]+(2*k+1)*b)
            dist2 = np.minimum(dist2,dx*dx+dy*dy)
    return float(np.mean(dist2 <= r*r))


def main():
    errors = []
    for a,b in [(2.,3.),(3.,2.),(2.,2.)]:
        t=min(a,b)/2
        for eps in [0.16,0.08,0.04,0.02,0.01,0.005]:
            j=local_deficit(a,b,t+eps)
            power=1.5 if a<=b else 2.
            coef=8*math.sqrt(a)/3 if a<=b else 2*math.pi*b/a
            ratio=(j-(2*math.pi*b/a*eps**2 if a==b else 0))/(coef*eps**power)
            errors.append((a,b,eps,ratio))
        radius=t+0.13
        expected=(math.pi*radius**2-local_deficit(a,b,radius))/(a*b)
        sampled=paired_cdf(a,b,radius)
        assert abs(expected-sampled)<0.004, (a,b,expected,sampled)
        assert abs((math.pi*(t/2)**2)/(a*b)-paired_cdf(a,b,t/2))<0.004
    for a,b,eps,ratio in errors:
        if eps==0.005:
            assert 0.985 < ratio < 1.018, (a,b,eps,ratio)
    print('VERIFICATION_OK distance_pair_sampling=6 local_coefficients=18 small_epsilon_ratios=',
          [(a,b,round(r,8)) for a,b,e,r in errors if e==0.005])

if __name__=='__main__':
    main()
