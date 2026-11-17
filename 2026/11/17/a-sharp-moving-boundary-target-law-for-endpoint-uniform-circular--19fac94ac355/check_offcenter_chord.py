"""Independent numerical checks for the boundary-target uniform-endpoint chord law.

Run: python check_offcenter_chord.py
Requires Python >= 3.10, numpy and scipy. These tests do not certify infinite limits.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipk

PI = math.pi


def exact_interception(radius, epsilon):
    assert 0 <= radius <= 1-epsilon
    def integrand(theta):
        c = radius*math.cos(theta)
        return math.asin(c+epsilon)-math.asin(c-epsilon)
    v, e = quad(integrand, 0, PI/2, epsabs=2e-13, epsrel=2e-13, limit=300)
    return (2/PI**2)*v


def boundary_prediction(lam, epsilon):
    g = (lam+1)*math.log(lam+1)
    if lam>1: g-=(lam-1)*math.log(lam-1)
    return (2*epsilon/PI**2)*(math.log(1/epsilon)+math.log(8)+1-g/2)


def independent_endpoint_frequency(r, epsilon, n, seed):
    rng = np.random.default_rng(seed)
    a = rng.uniform(0, 2*PI, n)
    b = rng.uniform(0, 2*PI, n)
    xa, ya = np.cos(a), np.sin(a)
    xb, yb = np.cos(b), np.sin(b)
    dx, dy = xb-xa, yb-ya
    dist = np.abs(dx*(-ya)-dy*(r-xa))/np.hypot(dx,dy)
    return float(np.mean(dist <= epsilon))


def run():
    for r in (0.0, 0.45, 0.82):
        e=1e-4
        v=exact_interception(r,e)/e
        k=4*ellipk(r*r)/PI**2
        assert abs(v-k) < 1e-7, (r,v,k)
        print('FIXED_INTERIOR_INTENSITY',r,v,k)
    for lam in (1.0, 2.0, 5.0):
        residuals=[]
        for e in (0.01, 0.001, 0.0001):
            a=exact_interception(1-lam*e,e)
            p=boundary_prediction(lam,e)
            assert abs(a-p) < (2.0*e*e*math.log(1/e) + 1e-11), (lam,e,a,p)
            residuals.append((a-p)/e)
            print('BOUNDARY_MATCH',lam,e,a,p)
        assert abs(residuals[-1])<abs(residuals[0])
    for lam in (1.0, 3.0):
        e=0.01;r=1-lam*e
        expected=exact_interception(r,e)
        observed=independent_endpoint_frequency(r,e,1600000,20261111+int(lam))
        sigma=math.sqrt(expected*(1-expected)/1600000)
        assert abs(observed-expected)<5*sigma, (lam, observed,expected,sigma)
        print('INDEPENDENT_CARTESIAN_ENDPOINTS',lam,observed,expected,sigma)
    print('OFFCENTER_BOUNDARY_CHORD_CHECKS_OK')

if __name__=='__main__':run()
