"""Deterministic and randomized checks for rounded-orthotope Löwner ellipsoids.
Run with Python 3, NumPy and SciPy: python VERIFY.py
Numerical samples supplement but do not prove the all-dimensional theorem.
"""
import math
import numpy as np
from scipy.optimize import brentq, minimize


def outer_axes(a, r):
    a = np.asarray(a, dtype=float)
    assert a.ndim == 1 and len(a) >= 3 and np.min(a) > 0 and r > 0
    def v_of(c):
        return 2*c/(np.sqrt(a*a+4*r*c)+a)  # stable root
    upper = max(1.0, (np.max(a)+r)*10)
    while np.dot(v_of(upper), v_of(upper)) < 1:
        upper *= 2
    c=brentq(lambda k: np.dot(v_of(k),v_of(k))-1, 0,upper,xtol=1e-13)
    v=v_of(c)
    z=a+r*v
    return v,z,np.sqrt(len(a))*z,c


def run():
    rng=np.random.default_rng(20261030)
    cases=0
    for d in [3,4,5,8,12]:
        for rep in range(30):
            a=10**rng.uniform(-2,2,size=d)
            r=10**rng.uniform(-2,2)
            v,z,axes,c=outer_axes(a,r)
            assert np.max(np.abs(v*z-c)) < 1e-8*max(1,c)
            assert abs(np.dot(v,v)-1)<3e-12
            assert np.min(z*z-r*c)>0
            assert abs(np.sum((z/axes)**2)-1)<1e-12
            # Compare with independent concave optimization, not the root solver.
            from scipy.optimize import minimize
            res=minimize(lambda w:-np.sum(np.log(a+r*w)),
                    np.ones(d)/np.sqrt(d),method='SLSQP',
                    bounds=[(0,1)]*d,
                    constraints=[{'type':'ineq','fun':lambda w:1-np.dot(w,w)}],
                    options={'maxiter':300,'ftol':2e-12})
            assert res.success or np.linalg.norm(res.x-v)<2e-3
            assert abs(np.sum(np.log(a+r*res.x))-np.sum(np.log(z)))<1e-5
            # Signed vertices give an isotropic contact certificate.
            if d<=8:
                signs=np.array([[(1 if (mask>>i)&1 else -1) for i in range(d)] for mask in range(1<<d)],float)
                Y=signs/np.sqrt(d)
                assert np.max(np.abs(Y.mean(axis=0)))<1e-12
                assert np.max(np.abs((Y.T@Y)/len(Y)-np.eye(d)/d))<1e-12
            # Maximal ellipsoid gauge attained at the predicted signed contacts.
            for j in range(200):
                w=rng.normal(size=d); w/=np.linalg.norm(w)
                w*=rng.uniform(0,1)**(1/d)
                b=rng.uniform(-a,a)
                x=b+r*w
                gauge=np.sum((x/axes)**2)
                if gauge > 1+2e-12:
                    raise AssertionError((d,rep,gauge))
            cases+=1
    print(f"PASS: {cases} parameter instances; 30,000 independently sampled points; product KKT, contact isotropy, numerical optimization")

if __name__=='__main__':
    run()
