"""Direct facet and metric checks for K_(2,q) symmetric-edge polytopes.

Usage: python verify_surface.py
Dependencies: numpy, scipy, sympy. Standard Cartesian Euclidean metric.
"""
from itertools import product
from math import comb, factorial, sqrt
import numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull
from sympy import Matrix, eye, ones, Rational


def exact_gram_checks(q):
    basis_difference = Matrix.vstack(eye(q-1), -ones(1,q-1))
    for signs in product((-1, 1), repeat=q):
        v = Matrix(signs)
        gram = eye(q) + Rational(1,2) * v*v.T
        squared_simplex = (basis_difference.T * gram * basis_difference).det()
        r = sum(x == 1 for x in signs)
        assert squared_simplex == q + 2*r*(q-r)
    gram_cross = eye(q) + Rational(1,2)*ones(q,q)
    assert gram_cross.det() == 1 + Rational(q,2)


def geometry_checks(q):
    n=q+2
    eye_n=np.eye(n)
    vertices=np.array([sgn*(eye_n[i]-eye_n[j])
                       for i in (0,1) for j in range(2,n)
                       for sgn in (-1,1)])
    intrinsic=null_space(np.ones((1,n)))
    hull=ConvexHull(vertices@intrinsic)

    def key(normal):
        centered = normal - normal.mean()
        scale=np.linalg.norm(centered)
        unit=np.r_[centered@intrinsic/scale, -1/scale]
        return tuple(np.round(unit,7))

    candidates=[]
    all_expected={}
    for signs in product((-1,1),repeat=q):
        normal=np.r_[0.,0.,np.array(signs,dtype=float)]
        r=sum(x==1 for x in signs)
        expected=sqrt(2*(q+2*r*(q-r)))/factorial(q-1)
        all_expected[key(normal)]=expected
        candidates.append((normal,expected))
    for signs in ((1.,-1.),(-1.,1.)):
        normal=np.r_[signs,np.zeros(q)]
        expected=2**q/factorial(q)*sqrt(1+q/2)
        all_expected[key(normal)]=expected
        candidates.append((normal,expected))

    # Qhull supplies independent supporting planes, possibly triangulated.
    independent_facets={tuple(np.round(eq,7)) for eq in hull.equations}
    assert independent_facets==set(all_expected),(
        q,len(independent_facets),len(all_expected),
        list(independent_facets-set(all_expected))[:2])
    assert len(all_expected)==2**q+2

    measured=[]
    for normal, expected in candidates:
        on=vertices[np.abs(vertices@normal-1)<1e-9]
        tangent=null_space(np.vstack((normal,np.ones(n))))
        assert tangent.shape==(n,q)
        coords=on@tangent
        actual=ConvexHull(coords).volume
        assert abs(actual-expected)<2e-7,(q,normal,actual,expected)
        measured.append(actual)
    predicted_total=(2**(q+1)/factorial(q)*sqrt(1+q/2)
                     +sum(comb(q,r)*sqrt(2*(q+2*r*(q-r)))
                          for r in range(q+1))/factorial(q-1))
    assert abs(sum(measured)-predicted_total)<3e-7
    sum_sq_A=4**q*(q+2)/factorial(q)**2
    sum_sq_B=2**q*q*(q+1)/factorial(q-1)**2
    assert abs(sum(v*v for v in measured)-(sum_sq_A+sum_sq_B))<1e-6
    print('q=%d facets=%d area=%.12f squared_A=%.12f squared_B=%.12f'
          % (q,len(candidates),predicted_total,sum_sq_A,sum_sq_B))


def threshold_checks():
    def ratio(q): return 2**q*(q+2)/(q**3*(q+1))
    assert all(ratio(q)<1 for q in range(2,10))
    assert all(ratio(q)>1 for q in range(10,101))
    for q in range(5,101): assert ratio(q+1)>ratio(q)


if __name__=='__main__':
    for q in range(2,7):
        exact_gram_checks(q)
        geometry_checks(q)
    threshold_checks()
    print('K2Q_SURFACE_PASS q=2..6 exact_gram and independent_hull; squared_area_threshold=10')
