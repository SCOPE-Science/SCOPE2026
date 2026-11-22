"""Exact finite cross-checks for uniform-marginal Brownian-bridge quadrature.

The infinite-dimensional optimality proof is the piecewise polynomial dual
inequality in RESULT.md; finite tests here are supplementary, not a replacement.
Run with Python >= 3.10: python verify.py
"""
from fractions import Fraction as Q


def loss12(x, y):
    a, b = sorted((x, y))
    return a**3 + (b - a)**3 + (1 - b)**3


def dual(x):
    if x <= Q(1, 2):
        return x**3 - Q(3, 4)*x + Q(1, 4)
    return (1-x)**3 + Q(3, 4)*x - Q(1, 2)


def bridge_cov(s, t):
    return min(s, t) - s*t


def fixed_node_conditional_variance(x, y):
    # Only called for distinct sites strictly in (0, 1).
    k11 = bridge_cov(x, x)
    k12 = bridge_cov(x, y)
    k22 = bridge_cov(y, y)
    den = k11*k22-k12*k12
    assert den > 0
    m1, m2 = x*(1-x)/2, y*(1-y)/2
    return Q(1,12)-(k22*m1*m1-2*k12*m1*m2+k11*m2*m2)/den


checks = 0
for n in range(2, 39):
    for i in range(n+1):
        x = Q(i,n)
        assert dual(x) == dual(1-x)
        checks += 1
        for j in range(n+1):
            y = Q(j,n)
            gap = loss12(x,y)-dual(x)-dual(y)
            assert gap >= 0, (n, i, j, gap)
            if gap == 0:
                assert abs(x-y) == Q(1,2)
            if abs(x-y) == Q(1,2):
                assert gap == 0
            checks += 1

for n in (7, 11, 17, 23):
    for i in range(1, n):
        for j in range(i+1,n):
            x,y = Q(i,n),Q(j,n)
            assert fixed_node_conditional_variance(x,y)==loss12(x,y)/12
            checks += 1

# Exact integrals of the cubic spacing loss for three joint laws.
# For iid uniforms, spacings are Dirichlet(1,1,1): E sum h_i^3=3/10.
assert Q(3,10)/12==Q(1,40)
checks += 1
# For a half-period cyclic shift, the sorted first point is uniform on [0,1/2].
# 2 integral_0^(1/2) [x^3+(1/2)^3+(1/2-x)^3] dx = 3/16.
assert 2*(Q(1,64)+Q(1,16)+Q(1,64))==Q(3,16)
assert Q(3,16)/12==Q(1,64)
checks += 2
# Central reflection: 2 integral_0^(1/2) [2x^3+(1-2x)^3]dx=5/16.
assert 2*(Q(1,32)+Q(1,8))==Q(5,16)
assert Q(5,16)/12==Q(5,192)
checks += 2
# Integral of the dual: 2 int_0^1/2 (x^3-3x/4+1/4) dx = 3/32.
assert 2*(Q(1,64)-Q(3,32)+Q(1,8))==Q(3,32)
assert 2*Q(3,32)==Q(3,16)
checks += 2
# Separate the universal dual inequality by subregions using exact rational points.
for n in (8, 24, 32):
    for i in range(n//2+1):
        for j in range(i,n//2+1):
            x,y=Q(i,n),Q(j,n)
            d=loss12(x,y)-dual(x)-dual(y)
            # The left/left expression grows with x, and its x=0 value is
            # (2-y)*(1/2-y)^2.
            assert d >= (2-y)*(Q(1,2)-y)**2
            checks += 1
            yy=Q(n-j,n)
            d2=loss12(x,yy)-dual(x)-dual(yy)
            assert d2==(yy-x-Q(1,2))**2*(yy-x+1)
            checks += 1
print(f'PASS: {checks} exact rational checks; analytic global proof in RESULT.md')
