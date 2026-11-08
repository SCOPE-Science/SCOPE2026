"""Independent checks of the diameter law for planar shadows of a regular tetrahedron.

Requires Python 3, NumPy and SciPy. Reproducible fixed random seed.
"""
from math import pi, sqrt
import numpy as np
from scipy.integrate import quad

TMAX = 1 / sqrt(5)
DMIN = sqrt(12 / 5)
DMAX = sqrt(8 / 3)


def gap_survival(t):
    """Exact spherical quadrature, split at the change of the active gap."""
    if t <= 0:
        return 1.0
    if t >= TMAX:
        return 0.0
    ymin = t / sqrt(1 - t*t)
    ymax = (1 - t*sqrt(2 - t*t)) / (1 - t*t)
    change = 1 - 3*t / (sqrt(3*(1 - 2*t*t)) + 3*t)
    def primitive(y, z):
        return z / ((1 + y*y)*sqrt(1 + y*y + z*z))
    def lower(y):
        z = (y - t*sqrt((2-t*t)*y*y + 1-t*t))/(1-t*t)
        return primitive(y, max(0., z))
    def upper(y):
        zsq = ((1-y)/t)**2 -1-y*y
        return primitive(y, sqrt(max(0., zsq)))
    a = quad(lower, ymin, change, epsabs=1e-13, epsrel=1e-12)[0]
    b = quad(upper, change, ymax, epsabs=1e-13, epsrel=1e-12)[0]
    return (12/pi)*(a+b)


def diameter_cdf(r):
    if r <= DMIN:
        return 0.0
    if r >= DMAX:
        return 1.0
    return gap_survival(sqrt(2-3*r*r/4))


def run():
    rng = np.random.default_rng(641327)
    n = 900_000
    normals = rng.normal(size=(n,3))
    normals /= np.linalg.norm(normals,axis=1)[:,None]
    ordered = np.sort(np.abs(normals),axis=1)[:,::-1]
    gaps = np.minimum(ordered[:,0]-ordered[:,1],ordered[:,1]-ordered[:,2])
    predicted_sq = (8-4*gaps*gaps)/3
    verts = np.asarray([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=float)/sqrt(3)
    sampled = normals[:90000]
    direct = []
    for i in range(4):
        for j in range(i+1,4):
            edge = verts[i]-verts[j]
            direct.append(np.sum(edge*edge)-(sampled@edge)**2)
    observed_sq = np.max(direct,axis=0)
    assert np.max(np.abs(observed_sq-predicted_sq[:len(sampled)])) < 1e-12
    assert gaps.max() < TMAX
    for t in [0.02, 0.06, 0.12, 0.2, 0.29, 0.38, 0.43]:
        truth = gap_survival(t)
        estimate = np.mean(gaps>=t)
        assert abs(estimate-truth)<0.003, (t, estimate, truth)
    near0 = [0.01,0.001,0.0001]
    c0 = [ (1-gap_survival(t))/t for t in near0]
    assert abs(c0[-1]-3*sqrt(2))<0.001
    lower = [0.01,0.002,0.0001]
    c1 = [gap_survival(TMAX-h)/h**2 for h in lower]
    assert abs(c1[-1]-25*sqrt(5)/(3*pi))<0.002
    for s in np.linspace(DMIN+0.001, DMAX-0.001, 13):
        assert 0<diameter_cdf(float(s))<1
    assert abs(diameter_cdf(DMIN))<1e-12
    assert abs(diameter_cdf(DMAX)-1)<1e-12
    print('TETRAHEDRAL_SHADOW_DIAMETER_OK',n,len(sampled),len(near0),len(lower))

if __name__=='__main__':
    run()
