"""Independent finite-dimensional covariance checks for the stated contact identities.

Requires numpy. The unrestricted proof is analytic and is given in RESULT.md.
"""
import math
import numpy as np

PI = math.pi


def coefficients(s):
    a, b = math.sqrt(1 - s), math.sqrt(s)
    root2, root6 = math.sqrt(2), math.sqrt(6)
    F = np.array([a, b, 0, 0], dtype=complex)
    Fx = math.sqrt(PI) * np.array([-b, a, root2 * b, 0], dtype=complex)
    Fy = -1j * math.sqrt(PI) * np.array([b, a, root2 * b, 0], dtype=complex)
    Fxx = PI * np.array([-a, -3*b, root2*a, root6*b], dtype=complex)
    Fyy = -PI * np.array([a, 3*b, root2*a, root6*b], dtype=complex)
    return F, Fx, Fy, Fxx, Fyy


def contact_from_gram(s, axis):
    F, Fx, Fy, Fxx, Fyy = coefficients(s)
    if axis == 'time':
        Du, Dv, Duu = Fx, Fy, Fxx
    else:
        Du, Dv, Duu = Fy, -Fx, Fyy
    M = np.column_stack([F, Du])
    G = M.conj().T @ M
    P = np.eye(4) - M @ np.linalg.solve(G, M.conj().T)
    A, B = Duu, Dv
    va = (A.conj() @ P @ A).real
    vb = (B.conj() @ P @ B).real
    c = A.conj() @ P @ B
    # E[Im(conj(A) B)^2] for jointly circular complex Gaussian A,B.
    moment = (va * vb + abs(c)**2 - 2 * (c*c).real) / 2
    return (moment / (4 * PI**2 * np.linalg.det(G).real))


def closed(s, axis):
    if axis == 'time':
        return 2*s**3*(4+7*s-8*s*s)/(1+2*s)**2
    return 6*s**4/(1-2*s+4*s*s)**2


def main():
    for s in [0, .0001, .01, .1, .25, .5, .75, .9, 1.]:
        for axis in ('time', 'frequency'):
            computed = contact_from_gram(s, 'time' if axis == 'time' else 'frequency')
            expected = closed(s, 'time' if axis == 'time' else 'frequency')
            assert abs(computed-expected) <= 2e-10 * max(1., abs(expected)), (s,axis,computed,expected)
    assert abs(closed(1,'time')-2/3)<1e-14
    assert abs(closed(1,'frequency')-2/3)<1e-14
    assert abs(closed(0,'time'))<1e-14
    assert abs(closed(0,'frequency'))<1e-14
    assert abs(closed(1e-5,'time')/(8e-15)-1)<.0001
    assert abs(closed(1e-4,'frequency')/(6e-16)-1)<.001
    print('MIXED_HERMITE_DIRECTIONAL_CONTACT_CHECKS_PASSED')


if __name__=='__main__':
    main()
