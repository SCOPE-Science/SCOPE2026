"""Exact-rational diagnostic for a sharp four-knot natural cubic spline theorem.

Run: python3 verify_natural4_monotone.py
Python 3 standard library only. Finite checks do not replace the analytic proof.
"""
from fractions import Fraction as Q
from itertools import product


def derivative(s, slopes, interval, z):
    """Derivative of the natural interpolant at normalized local position z."""
    a, b, c = slopes
    D = (s+2)*(3*s+2)
    m1 = 6*((2+3*s)*b-2*(1+s)*a-s*c)/D
    m2 = 6*((2+2*s)*c+s*a-(2+3*s)*b)/D
    M = (Q(0), m1, m2, Q(0))
    lengths = (Q(1),s,Q(1))
    h = lengths[interval]
    t = h*z
    return (slopes[interval] - h*(2*M[interval]+M[interval+1])/6
            + M[interval]*t + (M[interval+1]-M[interval])*t*t/(2*h))


def coefficients(s, interval, z):
    return tuple(derivative(s, tuple(Q(int(k==j)) for k in range(3)), interval, z)
                 for j in range(3))


def middle_formula(s,z):
    D=(s+2)*(3*s+2)
    pa=s*((9*s+6)*z*z-12*(s+1)*z+3*s+4)/D
    pb=2*(1+3*s*z*(1-z))/(s+2)
    pc=s*((9*s+6)*z*z-6*s*z-2)/D
    return pa,pb,pc


def risk_threshold(s):
    return min(s+3, Q(3)+Q(4)/s)


def check():
    tests=0
    meshes=[Q(1,8),Q(1,3),Q(1,2),Q(1),Q(3,2),Q(2),Q(7,3),Q(3),Q(6),Q(13)]
    for s in meshes:
        R=risk_threshold(s)
        for j in range(3):
            for k in range(21):
                z=Q(k,20)
                v=coefficients(s,j,z)
                assert sum(v)==1
                if j==1:
                    assert v==middle_formula(s,z)
                if j==0:
                    f=3*z*z-1
                    D=(s+2)*(3*s+2)
                    assert v==(1-2*(1+s)*f/D, (2+3*s)*f/D,-s*f/D)
                N=sum(-p for p in v if p<0)
                assert N<=max(1/(s+2),s/(2*(s+2)))
                for bits in product((Q(1),R),repeat=3):
                    out=derivative(s,bits,j,z)
                    assert out>=0, (s,j,z,bits,out)
                    tests+=1
        # Explicit sharpness at an endpoint or at the central midpoint.
        above=R+Q(1,17)
        if s<=2:
            d=derivative(s,(Q(1),above,Q(1)),0,Q(0))
        else:
            d=derivative(s,(above,Q(1),above),1,Q(1,2))
        assert d<0
        tests+=1
    assert derivative(Q(2),(Q(1),Q(5),Q(1)),0,Q(0))==0
    assert derivative(Q(2),(Q(5),Q(1),Q(5)),1,Q(1,2))==0
    print('PASS:',tests,'exact-rational derivative checks; all middle coefficient identities; sharp boundary witnesses')


if __name__=='__main__':
    check()
