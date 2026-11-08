"""Independent numerical checks for the sharp disphenoid central-section profile.
Run: python verify.py. Assumes NumPy; analytical theorem does not rely on this program.
"""
import math
import numpy as np


def f(x):
    if not 0 <= x <= 1:
        raise ValueError(x)
    return math.asin(math.sqrt(x))


def predicted_quad(p):
    return 3 - 4 / math.pi * sum(f(float(x)) for x in p)


def lower(t):
    return predicted_quad((t, (1-t)/2, (1-t)/2))


def upper(t):
    return predicted_quad((t,t,1-2*t)) if t < 0.5 else 1.0


def vertices(p):
    a,b,c = np.sqrt(p)
    return np.array([[a,b,c],[a,-b,-c],[-a,b,-c],[-a,-b,c]], dtype=float)


def polar_solid_angle_tri_probability(p):
    # For a vertex v of the polar tetrahedron, its spherical inner angle is
    # 2 atan2(|det(e1,e2,e3)|, 1 + e1.e2 + e2.e3 + e3.e1).
    reciprocals=1/np.asarray(p,dtype=float)
    w=vertices(reciprocals/reciprocals.sum())
    total=0.0
    for i in range(4):
        e=w[np.arange(4)!=i]-w[i]
        u=e/np.linalg.norm(e,axis=1)[:,None]
        z=abs(np.linalg.det(u))
        d=1+np.dot(u[0],u[1])+np.dot(u[0],u[2])+np.dot(u[1],u[2])
        total+=2*math.atan2(z,d)
    return total/(2*math.pi)


def sample_quad(p, count, rng):
    v=vertices(p)
    done=0
    batch=40000
    samples=0
    while samples < count:
        g=rng.normal(size=(min(batch,count-samples),3))
        s=(g@v.T)>0
        done+=int(np.count_nonzero(np.sum(s,axis=1)==2))
        samples+=len(g)
    return done/count


def run():
    rng=np.random.default_rng(20261104)
    checks=0
    max_polar_error=0.0
    max_violation=0.0
    for _ in range(18000):
        p=rng.dirichlet([0.72,0.72,0.72])
        t=max(p)
        q=predicted_quad(p)
        lo,hi=lower(t),upper(t)
        max_violation=max(max_violation,lo-q,q-hi)
        assert lo-2e-12<=q<=hi+2e-12,(p,q,lo,hi)
        checks+=1
    for t in [1/3,.36,.4,.499,.5,.55,.75,.95]:
        pp=[t,(1-t)/2,(1-t)/2]
        assert abs(predicted_quad(pp)-lower(t))<1e-13
        if t<.5:
            assert abs(predicted_quad([t,t,1-2*t])-upper(t))<1e-13
        else:
            assert abs(predicted_quad([t,1-t-1e-9,1e-9])-1)<.001
    for p in [[1/3]*3,[.6,.2,.2],[.8,.19,.01],[.49,.49,.02],[.34,.33,.33]]:
        q=predicted_quad(p)
        tri=polar_solid_angle_tri_probability(p)
        max_polar_error=max(max_polar_error,abs((1-q)-tri))
        assert abs((1-q)-tri)<5e-13,(p,tri,1-q)
    for p in [[1/3]*3,[.6,.2,.2],[.8,.19,.01]]:
        q=predicted_quad(p)
        sim=sample_quad(p,180000,rng)
        assert abs(q-sim)<.008,(p,q,sim)
    q0=lower(1/3)
    assert abs(q0-(3-12/math.pi*math.asin(1/math.sqrt(3))))<1e-13
    for eps in [1e-2,1e-3,1e-4]:
        p=np.array([1/3+eps,1/3-eps,1/3])
        rat=(predicted_quad(p)-q0)/np.sum((p-1/3)**2)
        assert abs(rat-9/(4*math.pi*math.sqrt(2)))<.012
    print('DISPHENOID_SECTION_OK random_profiles=',checks,
          'polar_checks=',5,'Haar_samples=',540000,
          'max_polar_error=',format(max_polar_error,'.3g'),
          'max_envelope_violation=',format(max_violation,'.3g'))

if __name__=='__main__':
    run()
