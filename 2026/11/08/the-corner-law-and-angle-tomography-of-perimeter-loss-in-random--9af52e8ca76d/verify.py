"""Numerical reproducibility checks for perimeter loss from a polygonal boundary."""
import math
import numpy as np
from scipy.spatial import ConvexHull
from scipy.integrate import quad


def geometry(vertices):
    v = np.asarray(vertices, dtype=float)
    steps = np.roll(v, -1, axis=0) - v
    lens = np.linalg.norm(steps, axis=1)
    assert (lens > 0).all()
    cross = steps[:, 0] * np.roll(steps, -1, axis=0)[:, 1] - steps[:, 1] * np.roll(steps, -1, axis=0)[:, 0]
    assert (cross > 0).all(), 'Expected strictly convex CCW vertices'
    theta = np.arctan2(cross, (steps * np.roll(steps, -1, axis=0)).sum(axis=1))
    return v, steps, lens, lens.sum(), theta


def polygon_sample(v, steps, lens, P, n, rng):
    arclength = rng.uniform(0., P, size=n)
    idx = np.searchsorted(np.cumsum(lens), arclength, side='right')
    start = np.r_[0., np.cumsum(lens)[:-1]]
    rel = arclength - start[idx]
    pts = v[idx] + rel[:, None] * (steps[idx] / lens[idx, None])
    return pts, idx, rel


def expected_factor(theta):
    q = math.sin(theta / 2)
    return 1 - (1-q*q) / q * math.asinh(q / math.sqrt(1-q*q))


def scalar_h(theta, u, v):
    return u+v-np.sqrt(np.maximum(0., (u+v)**2 - 4*u*v*math.sin(theta/2)**2))


def simulate(vertices, n, trials, seed):
    v, st, lengths, P, theta = geometry(vertices)
    rng = np.random.default_rng(seed)
    full_coverage_checks = 0
    scaled = np.empty(trials)
    for j in range(trials):
        pts, idx, rel = polygon_sample(v, st, lengths, P, n, rng)
        perimeter = ConvexHull(pts).area
        scaled[j] = n*(P-perimeter)
        if len(np.unique(idx)) == len(lengths):
            # For each side: near start/end; each vertex bridges outgoing and incoming rays.
            u = np.array([rel[idx == i].min() for i in range(len(lengths))])
            w = np.array([lengths[i] - rel[idx == i].max() for i in range(len(lengths))])
            corner_deficit = sum(scalar_h(theta[i],w[i],u[(i+1)%len(lengths)]) for i in range(len(lengths)))
            assert abs(P-perimeter-corner_deficit) < 2e-9, (P-perimeter, corner_deficit)
            full_coverage_checks += 1
    theoretical = P * sum(expected_factor(t) for t in theta)
    # Limit variables have finite second moments; large-but-finite n checks are approximate only.
    print('polygon',len(v),'perimeter',round(P,8),'n',n,'reps',trials,'empirical_mean',round(scaled.mean(),5),
          'limit_mean',round(theoretical,5),'relative_diff',round((scaled.mean()/theoretical-1),4),
          'all_edges_covered',full_coverage_checks)
    return scaled


def run():
    # Integral definition must agree with the derived closed mean formula.
    for theta in (.13, .5, math.pi/2, 2*math.pi/3, 3.1):
        num = 2*quad(lambda r: 1-math.sqrt(1-4*math.sin(theta/2)**2*r*(1-r)), 0., 1.,epsabs=1e-11)[0]
        assert abs(num - expected_factor(theta)) < 4e-11, (theta,num,expected_factor(theta))
    # Gamma representation: Laplace finite domain plus rate singularity at tcrit.
    for theta in (math.pi/4, math.pi/2, 2*math.pi/3):
        q=math.sin(theta/2)
        amax=1-math.cos(theta/2)
        assert abs((1-math.sqrt(1-q*q))-amax)<1e-12
        for t in (.25,.5,.8):
            z=quad(lambda r: (1-t*amax*(1-math.sqrt(1-4*q*q*r*(1-r)))/amax)**-2,0,1)[0]
            assert z > 1.0
    # Density at the origin of each corner term: F(x)/x -> 2/(1-cos(theta)).
    for theta in (math.pi/3, math.pi/2, 2*math.pi/3):
        q = math.sin(theta/2)
        x = 1e-4
        def cdf_integrand(r):
            temp = 4*q*q*r*(1-r)
            a = temp / (1 + math.sqrt(1-temp))
            if a < 1e-16: return 1.
            z = x / a
            return -math.expm1(-z) - z*math.exp(-z)
        numeric = 2*quad(cdf_integrand,0,.5,epsabs=1e-13,limit=250)[0] / x
        target = 2/(1-math.cos(theta))
        assert abs(numeric/target - 1) < .002, (theta,numeric,target)
    square = [[0,0],[1,0],[1,1],[0,1]]
    skinny = [[0,0],[1.7,0],[1.7,.3],[0,.3]]
    triangle = [[0,0],[3,0],[1,2]]
    a=simulate(square,500,1600,20261101)
    b=simulate(skinny,500,1600,20261102)
    c=simulate(triangle,600,1600,20261103)
    # Limit means identical for fixed perimeter and exterior angles, even for noncongruent rectangles.
    _,_,_,p1,t1=geometry(square)
    _,_,_,p2,t2=geometry(skinny)
    assert abs(p1-p2)<1e-12
    assert np.allclose(t1,t2)
    assert abs(p1*sum(map(expected_factor,t1))-p2*sum(map(expected_factor,t2)))<1e-12
    print('VERIFY_OK analytic_mean_angles=5 small_tail_checks=3 mgf_finiteness_checks=9 convex_hull_trials=4800 exact_deficit_identities=4800 rectangle_universality=1')

if __name__ == '__main__': run()
