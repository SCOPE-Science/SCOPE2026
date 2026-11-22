"""Finite consistency diagnostics for an explicit diagonal holomorphic symbol.

The general theorem is analytic; these tests are supplementary only.
Run: python check_diag.py
"""
import math

checks = 0
for p in (1.0, 1.5, 2.0, 3.0, 5.0):
    for t in (0.0, 0.1, 0.37, 0.75, 1.0):
        def b(j):
            return 1.0 if j == 2 else t

        # The scalar complex derivative supremum for b_j z^(j*j)/j^2 is b_j.
        for j in range(2, 40):
            m = j*j
            near = b(j) * (1.0 - 1.0 / (m*m))**(m - 1)
            assert near <= b(j) + 1e-12
            assert near >= b(j) * (1.0 - 1.0/m) - 1e-12
            checks += 2

        # Upper bounds on the image norm and tails, uniform on the open unit ball.
        total = sum((b(j) / (j*j))**p for j in range(2, 2500))
        assert total**(1/p) < 0.65
        checks += 1
        for N in (3, 7, 19, 59, 199):
            tail = sum((b(j) / (j*j))**p for j in range(N+1, 2500))
            assert tail <= sum(j**(-2*p) for j in range(N+1, 2500)) + 1e-12
            checks += 1
        assert max(b(j) for j in range(2, 30)) == 1.0
        checks += 1

# Show the exponential derivative recovery at a moving near-boundary point.
for j in (10, 20, 50, 100, 200):
    m = j*j
    recovered = (1.0 - 1.0/(m*m))**(m-1)
    assert 1.0 - 1.0/m <= recovered <= 1.0
    checks += 1
print('HOLO_LIPSCHITZ_DIAGONAL_DIAGNOSTIC_OK', checks)
