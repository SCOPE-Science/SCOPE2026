"""Numerical corroboration of two-meridian pure spherical-harmonic sampling.
Run: python verify.py (requires NumPy and SciPy).
The exact statements are proved separately; floating-point ranks are not certificates.
"""
import math
import numpy as np
from scipy.special import lpmv

checks = 0
for degree in range(1, 9):
    n = degree + 1
    ss = np.array([math.pi * j / n for j in range(n)])
    A = np.array([[lpmv(m, degree, math.cos(s)) for m in range(n)] for s in ss])
    B = A[1:, 1:]
    assert np.linalg.matrix_rank(A, tol=1e-7) == n
    assert np.linalg.matrix_rank(B, tol=1e-7) == degree
    checks += 2
    for q in (2, 3, 4, 5, 9, 13):
        angle = math.pi / q
        # Columns: P_l^m(cos s) cos(m phi) for m=0..l, then
        # P_l^m(cos s) sin(m phi) for m=1..l.
        M1 = np.column_stack((A, np.zeros((n, degree))))
        evens = np.array([[lpmv(m, degree, math.cos(s))*math.cos(m*angle)
                           for m in range(n)] for s in ss[1:]])
        odds = B * np.sin(angle * np.arange(1, n))[None, :]
        M = np.vstack((M1, np.column_stack((evens, odds))))
        expected_rank = 2*degree+1-degree//q
        rank = np.linalg.matrix_rank(M, tol=1e-6)
        assert rank == expected_rank, (degree, q, rank, expected_rank)
        checks += 1
        if q > degree:
            rhs = np.linalg.det(A)*np.linalg.det(B)*np.prod(np.sin(angle*np.arange(1,n)))
            lhs = np.linalg.det(M)
            assert abs(lhs/rhs-1) < 2e-7, (degree, q, lhs, rhs)
            checks += 1
    # One irrational-angle test well away from low-degree rational resonances.
    angle = math.pi/math.sqrt(2)
    M1 = np.column_stack((A, np.zeros((n, degree))))
    even = np.array([[lpmv(m, degree, math.cos(s))*math.cos(m*angle)
                      for m in range(n)] for s in ss[1:]])
    odd = B*np.sin(angle*np.arange(1,n))[None, :]
    M = np.vstack((M1, np.column_stack((even, odd))))
    assert np.linalg.matrix_rank(M, tol=1e-6) == 2*degree+1
    checks += 1
print(f'TWO_MERIDIAN_TRACE_CHECK_PASS checks={checks} degrees=1..8')
