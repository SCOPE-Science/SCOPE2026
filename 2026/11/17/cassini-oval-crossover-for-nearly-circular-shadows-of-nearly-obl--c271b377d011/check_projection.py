"""Numerical reproducibility checks for random planar shadows of near-oblate ellipsoids."""
import numpy as np
from scipy.special import ellipk, ellipe
from scipy.stats import qmc


def phi(t):
    if t <= 0:
        return 0.0
    if t < 1:
        return (ellipe(t*t) - (1-t*t)*ellipk(t*t))/np.pi
    if t == 1:
        return 1/np.pi
    return t*ellipe(1/(t*t))/np.pi


def gap_from_compression(normals, eta, delta, B=3.0):
    normals = np.asarray(normals)
    pole = np.zeros_like(normals)
    pole[:, 2] = 1
    pole[np.abs(normals[:, 2]) > 0.8] = (0, 1, 0)
    u = np.cross(normals, pole)
    u /= np.linalg.norm(u, axis=1)[:, None]
    v = np.cross(normals, u)
    diag = np.array([B+eta, B, B-delta])
    a = (diag * u*u).sum(axis=1)
    b = (diag * v*v).sum(axis=1)
    c = (diag * u*v).sum(axis=1)
    return np.sqrt((a-b)**2+4*c*c)


def formula_gap(normals, eta, delta):
    x, y = normals[:, 0], normals[:, 1]
    return np.sqrt((eta - (eta+delta)*x*x - delta*y*y)**2 + 4*eta*delta*y*y)


def exact_probability_2d(eta, delta, t, m=20):
    # Two hemispheres represented by x,y; the density is 1/(2pi sqrt(1-r^2)).
    radius = np.sqrt((1+t)*eta/delta)
    assert radius < .75
    uv = qmc.Sobol(d=2, scramble=True, seed=219).random_base2(m)
    x = (2*uv[:, 0]-1)*radius
    y = (2*uv[:, 1]-1)*radius
    r2 = x*x+y*y
    gap2 = (eta - (eta+delta)*x*x-delta*y*y)**2 + 4*eta*delta*y*y
    weights = ((r2 < 1) & (gap2 < (eta*t)**2))/np.sqrt(1-r2)
    return 2*radius**2 / np.pi * weights.mean()


def cassini_area(t, m=20):
    radius = np.sqrt(1+t)
    uv = qmc.Sobol(d=2, scramble=True, seed=218).random_base2(m)
    x = (2*uv[:, 0]-1)*radius
    y = (2*uv[:, 1]-1)*radius
    region = ((1-x*x+y*y)**2+4*x*x*y*y) < t*t
    return 4*radius*radius * region.mean()


def main():
    uv = qmc.Sobol(d=2, scramble=True, seed=713).random_base2(14)
    z = 2*uv[:, 0]-1
    angle = 2*np.pi*uv[:, 1]
    norms = np.column_stack((np.sqrt(1-z*z)*np.cos(angle), np.sqrt(1-z*z)*np.sin(angle), z))
    for eta,delta in [(0.4,2.0),(0.2,1.0),(.01,1.5)]:
        err = np.max(abs(gap_from_compression(norms,eta,delta,B=3) - formula_gap(norms,eta,delta)))
        assert err < 3.e-7,err
    for t in [.4, .8, 1.0, 1.4, 2.0]:
        predicted_area = 2*np.pi*phi(t)
        measured = cassini_area(t)
        assert abs(measured/predicted_area - 1) < .006, (t,measured,predicted_area)
    for t in [.4,1.,2.]:
        rel=[]
        for eta in [.2,.05,.0125]:
            p = exact_probability_2d(eta,2,t)
            expected = eta/2*phi(t)
            rel.append(abs(p/expected-1))
        assert rel[-1] < .003,(t,rel)
        assert rel[-1] < rel[0],(t,rel)
    for t in [.001,.003,.01]:
        assert abs(phi(t)/(t*t/4)-1) < .0001
    for t in [200,500]:
        assert abs(phi(t)/(t/2)-1) < 1e-5
    assert abs(phi(1)-1/np.pi) < 1e-14
    print('ELLIPSOID_CASSINI_CROSSOVER_CHECKS_OK')

if __name__=='__main__':
    main()
