"""Numerical checks of an analytic global transverse contraction lemma.
The theorem uses analytic inequalities; these finite checks are not a proof.
"""
import math

CASES = [
    (3.0, 0.9, 0.2, 9.0),
    (3.0, 0.9, 4.0, 0.07),
    (2.5, 0.8, 0.04, 3.0),
    (1.5, 0.1, 9.0, 0.25),
    (0.5, 0.5, 0.001, 0.9),
]
for h, c, x, y in CASES:
    L = 2 * math.exp(h - 1)
    assert 0 < c < 1 and (1 - c) * math.exp(h - 1) < 2
    u_last = None
    for n in range(1000):
        T = x+y
        if n >= 1:
            assert T <= L * (1+1e-12), (h,c,n,T,L)
        if x != y:
            u = math.log(x/y)
            if n >= 2 and u_last is not None and abs(u) > 1e-9:
                assert abs(u) <= abs(u_last) + 1e-10, (n,u,u_last)
            u_last = u
        nx = x * math.exp(h-x-c*y)
        ny = y * math.exp(h-c*x-y)
        x,y=nx,ny
    assert abs(x-y) < 1e-8, (h,c,x,y)
    assert x>0 and y>0
# Exact derivative along the diagonal at fixed point follows by hand:
# lambda_parallel = 1-h, lambda_transverse = 1-h*(1-c)/(1+c).
h,c=3.0,0.9
assert abs(1-h) > 1 and (1-c)*math.exp(h-1) < 2
print('VERIFY_OK positive_parameter_cases=5 iterations_per_case=1000 unstable_diagonal_fixed_point=1')
