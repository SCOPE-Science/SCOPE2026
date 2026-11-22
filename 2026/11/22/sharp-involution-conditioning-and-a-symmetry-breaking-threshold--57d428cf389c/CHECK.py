"""Numerical diagnostics for the three-step nilpotent involution norm law.
The accompanying written proof, not this finite diagnostic, covers the continuum.
"""
from math import sqrt
import numpy as np


def N(c):
    return np.array([[0, 1, c], [0, 0, 1], [0, 0, 0]], dtype=complex)


def J(x, z):
    return np.array([[1, x, -x*z/2], [0, -1, z], [0, 0, 1]], dtype=complex)


def formula(c):
    t = abs(c)
    p = 1+t*t/4 if t <= 2 else t
    return p + sqrt(p*p-1)


def optimal(c):
    t = abs(c)
    if t == 0:
        return [(0.0, 0.0)]
    v = c/t
    if t <= 2:
        return [(-c, -c)]
    d = sqrt(t*t-4)
    return [(-v*(t+d), -v*(t-d)), (-v*(t-d), -v*(t+d))]


def run():
    count = 0
    rng = np.random.default_rng(22054)
    for c in [0, 1e-3, .2, .7, 1, 1.99999, 2, 2.00001, 2.5, 4, 10,
              1+1j, -2+1j, 4j]:
        for x,z in optimal(c):
            m = N(c)
            a = J(x,z)
            for arr in [a@a-np.eye(3), a@m+m@a]:
                assert np.linalg.norm(arr) < 2e-12*max(1, abs(c)**2)
                count += 1
            assert abs(np.linalg.norm(a,2) - formula(c)) < 1e-11*max(1,abs(c))
            count += 1
        for k in range(400):
            x = rng.standard_normal()+1j*rng.standard_normal()
            x *= (abs(c)+.1)
            z = -2*c-x
            a = J(x,z)
            p = sqrt((1+abs(x)**2/4)*(1+abs(z)**2/4))
            theo = p+sqrt(p*p-1)
            assert abs(np.linalg.norm(a,2)-theo) < 1e-9*max(1,theo)
            assert np.linalg.norm(a@a-np.eye(3)) < 5e-11*max(1,theo**2)
            assert np.linalg.norm(a@N(c)+N(c)@a) < 5e-11*max(1,abs(c)*theo)
            assert theo >= formula(c)-1e-9*max(1,theo)
            count += 4
    # Integer thresholds and exact symbolic identities via Sympy.
    import sympy as s
    X,Z,C=s.symbols('X Z C',commutative=True)
    M=s.Matrix([[0,1,C],[0,0,1],[0,0,0]])
    Q=s.Matrix([[1,X,-X*Z/2],[0,-1,Z],[0,0,1]])
    assert Q**2==s.eye(3)
    assert s.simplify(Q*M+M*Q) == s.Matrix([[0,0,2*C+X+Z],[0,0,0],[0,0,0]])
    assert s.expand((1+s.symbols('r')**2)*(1+s.symbols('s')**2)-(s.symbols('r')+s.symbols('s'))**2-(s.symbols('r')*s.symbols('s')-1)**2)==0
    count+=3
    print('THREE_STEP_INVOLUTION_NORM_DIAGNOSTIC_OK',count)

if __name__ == '__main__':
    run()
