"""Reproducible diagnostics for spherical-cap pole containment.

Run with Python 3.10+, NumPy, SciPy. The analytic proof does not rely on this script.
"""
import numpy as np
from scipy.stats import qmc


def inv_cot(x):
    return x / np.sqrt(1.0 + x * x)


def cot(z):
    return z / np.sqrt(1.0 - z * z)


def conditional_integral(h, exponent=19):
    """Integrate over the uniform angular simplex by scrambled Sobol quadrature."""
    q = qmc.Sobol(d=5, scramble=True, seed=201506).random_base2(exponent)
    root = np.sqrt(q[:, 0])
    b = np.column_stack((np.pi * (1 - root),
                         np.pi * root * q[:, 1],
                         np.pi * root * (1 - q[:, 1])))
    a = np.sin(b)
    u, v, w = q[:, 2], q[:, 3], q[:, 4]
    ones, twos = 0.0, 0.0
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        neg = a[:, i] * h * u / np.sqrt(1.0 - h*h*u*u)
        zmax = inv_cot(neg/a[:, j])
        zp = w * zmax
        remain = np.maximum(0.0, neg-a[:, j]*cot(zp))
        ones += h * np.mean(zmax * inv_cot(remain/a[:, k]))
        neg2 = neg + a[:, j]*h*v / np.sqrt(1.0 - h*h*v*v)
        twos += h*h * np.mean(inv_cot(neg2/a[:, k]))
    triple = h**3
    total = (ones + twos + triple)/(4*(1+h)**3)
    return total, (ones, twos, triple)


def cartesian_check(h, n=1_200_000, seed=2035):
    """Independent 3D vector and determinant test, batching memory usage."""
    rng = np.random.default_rng(seed)
    hits = [0, 0, 0, 0]
    for start in range(0,n,100000):
        k = min(100000, n-start)
        z = -h + (1+h)*rng.random((k,3))
        ph = 2*np.pi*rng.random((k,3))
        vx = np.sqrt(1-z*z)*np.cos(ph)
        vy = np.sqrt(1-z*z)*np.sin(ph)
        det0 = vx[:,1]*vy[:,2]-vy[:,1]*vx[:,2]
        det1 = vx[:,2]*vy[:,0]-vy[:,2]*vx[:,0]
        det2 = vx[:,0]*vy[:,1]-vy[:,0]*vx[:,1]
        allpos = (det0>0)&(det1>0)&(det2>0)
        allneg = (det0<0)&(det1<0)&(det2<0)
        wraps = allpos|allneg
        # If all determinants are negative, multiply by -1 to get positive barycentric weights.
        sign = np.where(allneg,-1.,1.)
        height = sign*(det0*z[:,0]+det1*z[:,1]+det2*z[:,2])
        bad = wraps & (height<0)
        count = np.sum(z[bad]<0,axis=1)
        hits[0] += int(bad.sum())
        hits[1] += int((count==1).sum())
        hits[2] += int((count==2).sum())
        hits[3] += int((count==3).sum())
    return np.array(hits)/n


def main():
    for h in [0.10, 0.05, 0.02, 0.0002, 0.00002]:
        val, parts=conditional_integral(h)
        print('quadrature h=',h,'loss=',val,'scaled=',val/h**3,
              'one/two=',parts[0]/(parts[0]+parts[1]))
        assert 0 < val < .25
    for h in [0.10, 0.05]:
        val, _=conditional_integral(h)
        counts=cartesian_check(h)
        se=np.sqrt(max(val,1e-12)/1_200_000)
        print('cartesian h=',h,'observed=',counts,'predicted=',val,'std=',se)
        assert abs(counts[0]-val)<5*se + 2e-5
        assert abs((counts[1]+counts[2]+counts[3])-counts[0])<1e-12
    print('SPHERICAL_CAP_POLE_CROSSOVER_CHECKS_OK')

if __name__=='__main__':
    main()
