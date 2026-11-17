"""Independent diagnostics for the near-concurrent uniform-cevian area law.

Requires Python 3, NumPy, and SciPy. These calculations are finite diagnostics,
not substitutes for the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import dblquad


def area_ratio(u, v, w):
    numerator = 2*u*v*w-u*v-u*w+u-v*w+v+w-1
    denominator = (1-u+u*v)*(1-w+u*w)*(1-v+v*w)
    return numerator*numerator/denominator


def geometry_ratio(u, v, w):
    a = np.array([0., 0.]); b = np.array([1., 0.]); c = np.array([0., 1.])
    d = np.array([u, 1-u]); e = np.array([0., v]); f = np.array([1-w, 0.])
    def intersection(p, q, r, s):
        k = np.linalg.solve(np.column_stack((q-p, -(s-r))), r-p)[0]
        return p+k*(q-p)
    p = intersection(a,d,b,e)
    q = intersection(b,e,c,f)
    r = intersection(c,f,a,d)
    return abs(np.linalg.det(np.column_stack((q-p,r-p))))


def leading_integrand(v, u):
    h = u*v+(1-u)*(1-v)
    if h == 0.: return 0.
    return 2*math.sqrt(u*(1-v))*(1-u+u*v)**1.5/h**2


def run():
    rng = np.random.default_rng(20261110)
    for u,v,w in rng.uniform(.025,.975,size=(120,3)):
        assert abs(area_ratio(u,v,w)-geometry_ratio(u,v,w)) < 2e-11
    integral, err = dblquad(leading_integrand, 0., 1., lambda u:0.,
                           lambda u:1.,epsabs=8e-8,epsrel=8e-8)
    assert abs(integral-3*math.pi/4) < 5e-6,(integral,err)
    assert abs(3*math.pi/4-2.356194490192345) < 1e-13
    for t in (.01,.001,.0001):
        m=1_800_000
        uvw=rng.random((m,3))
        u,v,w=uvw.T
        ratio=area_ratio(u,v,w)
        p=np.mean(ratio<t)
        lead=(3*math.pi/4)*math.sqrt(t)
        # First-order asymptotics; convergence is not expected to be exact at finite t.
        if t==.0001:
            assert abs(p/lead-1)<.08,(t,p,lead)
            sel=ratio<t
            # The auxiliary triangle opposite sides are (a+b),(b+c),(c+a).
            x=u[sel]/(1-u[sel]); y=v[sel]/(1-v[sel])
            raw_a=1/y;raw_b=x;norm=raw_a+raw_b+1.
            a=raw_a/norm;b=raw_b/norm;c=1./norm
            sides=np.stack((a+b,b+c,c+a),axis=1)
            # An angle is obtuse iff opposite squared side exceeds sum of other two.
            acute=np.all(2*sides*sides < np.sum(sides*sides,axis=1)[:,None],axis=1)
            frac=np.mean(acute)
            assert abs(frac-1/math.pi)<.027,(frac,1/math.pi)
        print('threshold',t,'empirical',round(p,9),'leading',round(lead,9),'ratio',round(p/lead,7))
    print('ROUTH_CEVA_SQRT_AND_ANGLES_CHECK_OK')

if __name__=='__main__':run()
