"""Independent tests for the eight-normal two-square projection-zonotope theorem.

All exact determinant tests use rational arithmetic. Floating-point hull tests
provide a separate geometric implementation and do not replace the proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import pi, sqrt, cos, sin
import numpy as np
from scipy.spatial import ConvexHull


def normals_unscaled(c, s):
    U = [(1, 0, 1), (0, 1, 1), (-1, 0, 1), (0, -1, 1)]
    L = [(c, s, -1), (-s, c, -1), (-c, -s, -1), (s, -c, -1)]
    return U + L


def determinant(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))


def exact_sum(c, s):
    X = normals_unscaled(c,s)
    vals = [abs(determinant(X[i], X[j], X[k]))
            for i,j,k in combinations(range(8),3)]
    return sum(vals), len(vals)


def test_exact():
    tests = [(F(1),F(0)), (F(12,13),F(5,13)),
             (F(4,5),F(3,5)), (F(15,17),F(8,17))]
    for c,s in tests:
        assert c*c+s*s==1 and c>=s>=0
        val,count = exact_sum(c,s)
        assert count==56
        assert val == 32*(1+c+s), (c,s,val)
    print('Exact rational determinant identities passed:',len(tests)*56,'minors')


def test_design():
    # Moment identities for all 20 monomials of total degree <=3.
    for phi in (0,.13,.33,pi/4):
        x=[]
        for h,delta in ((1/sqrt(3),0),(-1/sqrt(3),phi)):
            for j in range(4):
                a=delta+j*pi/2
                x.append([sqrt(2/3)*cos(a),sqrt(2/3)*sin(a),h])
        x=np.array(x)
        for degree in range(4):
            for i in range(degree+1):
                for j in range(degree-i+1):
                    k=degree-i-j
                    actual=np.mean(x[:,0]**i*x[:,1]**j*x[:,2]**k)
                    target=1/3 if (degree==2 and max(i,j,k)==2) else (1 if degree==0 else 0)
                    assert abs(actual-target)<1e-12,(phi,i,j,k,actual,target)
    print('Spherical design moments checked at four twists')


def test_volume_hull():
    # Independent from determinant formula: enumerate segment endpoints and take hull.
    for phi in [0,.05,.2,pi/8,pi/4]:
        N=[]
        for h,delta in [(1/sqrt(3),0),(-1/sqrt(3),phi)]:
            for j in range(4):
                a=delta+j*pi/2
                N.append([sqrt(2/3)*cos(a),sqrt(2/3)*sin(a),h])
        N=np.asarray(N)
        endpoints=np.asarray(list(product([-1,1],repeat=8)),dtype=float)
        Z=(pi/4)*(endpoints@N)
        observed=ConvexHull(Z).volume
        expected=8*pi**3/(3*sqrt(3))*(1+cos(phi)+sin(phi))
        assert abs(observed/expected-1)<2e-12, (phi,observed,expected)
    print('Independent 256-endpoint 3D hull volume comparisons passed: 5')

if __name__=='__main__':
    test_exact()
    test_design()
    test_volume_hull()
    print('ALL CHECKS PASSED')
