"""Exact-arithmetic checks for the fixed-point facet-pedal simplex recurrence.

This is a finite computational cross-check of an independent analytic proof.
Run: python3 verify.py (standard library only).
"""
from fractions import Fraction as Q


def step(d, q, t):
    k = d - 1
    den = k*k*t + (1+t)*q
    return Q(k*k*q, den*den), Q(q, t*(k*k+q))


def multiply(A, B):
    return tuple(tuple(sum(A[i][m]*B[m][j] for m in range(2))
                       for j in range(2)) for i in range(2))


def jacobian(d):
    return ((Q(d-2,d), -Q(2*(d-1)*d*d,(d+1)**2)),
            (Q((d+1)**2,d**3), Q(-1)))


def derive_jacobian_from_difference(d):
    q0, t0 = Q(d-1,d+1), Q(1,d)
    k = d-1
    D = k*k*t0 + (1+t0)*q0
    # Differentiation of k^2 q / D^2 and q / [t(k^2+q)].
    fq = k*k*(D - 2*q0*(1+t0))/D**3
    ft = -2*k*k*q0*(k*k+q0)/D**3
    gq = k*k/(t0*(k*k+q0)**2)
    gt = -q0/(t0*t0*(k*k+q0))
    return ((fq, ft), (gq, gt))


checks = 0
for d in range(2, 16):
    k = d-1
    fixed = (Q(d-1,d+1), Q(1,d))
    assert step(d, *fixed) == fixed
    J = jacobian(d)
    assert J == derive_jacobian_from_difference(d)
    assert J[0][0]+J[1][1] == Q(-2,d)
    assert J[0][0]*J[1][1]-J[0][1]*J[1][0] == 1
    checks += 4
    P = ((Q(1),Q(0)), (Q(0),Q(1)))
    # Powers of J satisfy the Chebyshev recurrence.
    trace = Q(-2,d)
    b_prev, b_curr = Q(0), J[0][1]
    for N in range(1, 26):
        P = multiply(P,J)
        assert P[0][1] == b_curr
        if d >= 3:
            assert b_curr != 0
        b_prev, b_curr = b_curr, trace*b_curr - b_prev
        checks += 1

# Match the published regular tetrahedron four-step example exactly.
q,t = Q(1,2),Q(1,9)
expected = [(Q(2),Q(1)), (Q(1,8),Q(1,3)),
            (Q(2,9),Q(1,11)), (Q(121,50),Q(11,19))]
for item in expected:
    q,t = step(3,q,t)
    assert (q,t)==item
    checks += 1
squared_lateral_over_base = Q(1,3)*(1+1/q)
assert squared_lateral_over_base == Q(57,121)
checks += 1
print(f'PASS: {checks} exact arithmetic checks; benchmark 57/121')
