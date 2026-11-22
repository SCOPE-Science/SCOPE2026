"""Reproduce numerical checks for Euclidean rare-diameter tails in planar Lame disks.
Dependencies: Python 3, numpy and scipy. All constants below have analytic proofs
in RESULT.md; finite diagnostics do not certify the infinite limits.
"""
import math
import numpy as np
from scipy.special import gamma
from scipy.integrate import quad
from scipy.stats import qmc

PI = math.pi

def area(p):
    return 4 * gamma(1 + 1 / p)**2 / gamma(1 + 2 / p)

def fixed_coefficient(p):
    return (p**(2/p) * gamma(1 + 2/p) /
            ((1 + 2/p)*(2 + 2/p)*gamma(1 + 1/p)**2))

def H(t):
    c, s = abs(math.cos(t)), abs(math.sin(t))
    return -(c*c*math.log(max(c, 1e-300)) +
             s*s*math.log(max(s, 1e-300))) / 2

def crossover(lam):
    return (16/(15*PI**2) *
            quad(lambda t: max(0, 1-2*lam*H(t))**2.5,
                 0, 2*PI, points=[PI*k/4 for k in range(1,8)],
                 epsabs=1e-11, limit=250)[0])

def fixed_estimate(p, eps, U):
    # Deterministic importance sampling in four near-opposite axial tip boxes.
    M = 1.5 if p <= 1 else 2
    u, w = M*U[:,0], M*U[:,1]
    vcap = np.maximum((1-(1-eps*u)**p)/eps, 0)**(1/p)
    wcap = np.maximum((1-(1-eps*w)**p)/eps, 0)**(1/p)
    v, z = (2*U[:,2]-1)*vcap, (2*U[:,3]-1)*wcap
    length_sq = (2-eps*(u+w))**2 + eps**(2/p)*(v-z)**2
    ok = length_sq > (2-eps)**2
    return 4/area(p)**2 * M*M * np.mean(4*vcap*wcap*ok)

def critical_estimate(lam, eps, U):
    # Integrate exact finite-p radial point inclusion with polar quadrature.
    p = 2-lam*eps
    M = 1 + lam*math.log(2)/4 + 0.1
    theta = 2*PI*U[:,0]
    u, w = M*U[:,1], M*U[:,2]
    z = 4*U[:,3]-2
    t2 = theta + PI + math.sqrt(eps)*z
    r1, r2 = 1-eps*u, 1-eps*w
    x1 = r1**p*(abs(np.cos(theta))**p+abs(np.sin(theta))**p)
    x2 = r2**p*(abs(np.cos(t2))**p+abs(np.sin(t2))**p)
    length_sq = (r1-r2)**2 + 2*r1*r2*(1+np.cos(math.sqrt(eps)*z))
    ok = (x1 <= 1)&(x2 <= 1)&(length_sq > (2-eps)**2)
    return 2*PI*M*M*4*np.mean(ok*r1*r2)/area(p)**2

if __name__ == '__main__':
    assert abs(area(2)-PI)<1e-12
    assert abs(area(1)-2)<1e-12
    assert abs(fixed_coefficient(1)-1/6)<1e-12
    assert abs(fixed_coefficient(2/3)-64/(405*PI))<1e-12
    assert abs(crossover(0)-32/(15*PI))<1e-12
    assert abs(H(PI/4)-math.log(2)/4)<1e-14
    assert all(crossover(a)>crossover(b) for a,b in [(0,1),(1,2),(2,5)])
    U = qmc.Sobol(d=4, scramble=True, seed=2026).random_base2(m=18)
    for p in (2/3, 1):
        c = fixed_coefficient(p)
        est = fixed_estimate(p, 0.005, U)
        print('Fixed p', p, 'predicted', c, 'scaled estimate', est, 'ratio',est/c)
        assert abs(est/c-1)<0.035
    for lam in (0,1,2,5):
        expected = crossover(lam)
        actual = critical_estimate(lam, .002, U)
        print('Critical lambda',lam,'predicted',expected,'scaled estimate',actual,'ratio', actual/expected)
        assert abs(actual/expected-1)<0.04
    print('PASS: exact special constants, monotonicity, and 6 Sobol integral comparisons')
