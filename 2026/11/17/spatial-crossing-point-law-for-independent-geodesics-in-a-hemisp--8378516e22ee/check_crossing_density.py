"""Independent numerical diagnostics for the spherical-geodesic crossing-location law.
Run: python check_crossing_density.py (requires numpy and scipy).
The continuum identity is proved analytically, not by these finite tests.
"""
import math
import numpy as np
from scipy.integrate import quad

PI = math.pi

def subprobability_disk(R):
    if R <= 0:
        return 0.0
    return quad(lambda t: 4 / PI**2 * math.log1p(t*t) /
                (t*(1+t*t)**1.5), 0, R, epsabs=1e-11, epsrel=1e-11)[0]

def density_2d(r):
    if r == 0:
        return 2 / PI**3
    return (2 / PI**3)*math.log1p(r*r)/(r*r*(1+r*r)**1.5)

# Independently evaluate the angular double integral defining the flux density.
def angular_integral(r):
    angles = (np.arange(2400)+0.5)*PI/2400
    ww = 1/(1+(r*np.sin(angles))**2)
    kernel = np.abs(np.sin(angles[:,None]-angles[None,:]))
    return float(ww @ kernel @ ww)*(PI/2400)**2

for r in (0.0, 0.4, 1.0, 2.0):
    s = math.hypot(1,r)
    expr = 2*PI if not r else (4*PI*math.log(s)/(r*r*s))
    got = angular_integral(r)
    assert abs(got-expr) < 2.5e-6, (r, got, expr)
    assert abs(density_2d(r) - expr/(PI**4*s*s)) < 1e-12

expected = 1-8/PI**2
assert abs(subprobability_disk(1e4)-expected) < 2e-9
radii = (0.25,0.5,1.0,2.0,4.0)
cutprob = [subprobability_disk(R) for R in radii]
assert all(0<p<expected for p in cutprob)

rng = np.random.default_rng(20261109)
N = 600_000
counts = np.zeros(len(radii)+1,dtype=np.int64)
for _ in range(12):
    n = N//12
    height = rng.random((n,4))
    azimuth = rng.uniform(0,2*PI,(n,4))
    radius = np.sqrt(1-height**2)/height
    sample = np.stack((radius*np.cos(azimuth),radius*np.sin(azimuth)),axis=2)
    A,B,C,D = np.moveaxis(sample,1,0)
    u,v,w = B-A,D-C,C-A
    det = lambda x,y:x[:,0]*y[:,1]-x[:,1]*y[:,0]
    cross_uv = det(u,v)
    line1 = det(w,v)/cross_uv
    line2 = det(w,u)/cross_uv
    intersects = (line1>0)&(line1<1)&(line2>0)&(line2<1)
    counts[-1] += intersects.sum()
    point = A + u*line1[:,None]
    point_radius = np.hypot(point[intersects,0],point[intersects,1])
    for k,R in enumerate(radii):
        counts[k] += (point_radius <= R).sum()

for observed,target in zip(counts/N,cutprob+[expected]):
    standard_error = math.sqrt(target*(1-target)/N)
    assert abs(observed-target) < 5*standard_error + 1/N, (observed,target)
print('HEMISPHERE_GEODESIC_CROSSING_LOCATION_LAW_OK', N, 'tuples')
print('conditional crossing probability', counts[-1]/N, 'exact', expected)
for R,observed,exact in zip(radii,counts[:-1]/N,cutprob):
    print('subprobability radius',R,'observed',observed,'exact',exact)
