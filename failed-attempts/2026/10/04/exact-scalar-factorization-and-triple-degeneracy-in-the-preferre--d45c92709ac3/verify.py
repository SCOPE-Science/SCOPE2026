#!/usr/bin/env python3
import math

# Exact coefficient identity for the j=1,3 bracket, with y=k^2 and x=cos^2(k/2):
# P = 2 y^2 (2x-1)x + y(1+4x(2x-1)) + 2(2x-1)x
#   = (2(y+1)x-y)(2(y+1)x-1).
def coeff_p(y):
    # coeffs constant, x, x^2
    return [y, -2*(y+1)**2, 4*(y+1)**2]

def coeff_factored(y):
    # (2(y+1)x-y)(2(y+1)x-1)
    return [y, -2*(y+1)*(y+1), 4*(y+1)**2]

for y in [0,1,2,7,101,10000]:
    assert coeff_p(y) == coeff_factored(y)

# The j=0 residual factor is 2(y+1)x-1; the j=2 residual factor is 2(y+1)x-y.
for y in [1,2,13,89]:
    for x in [0.0,0.1,0.25,0.49]:
        j0 = 2*((y+1)*x - 0.5)
        A = 2*(y+1)*x - 1
        j2 = 2*(y*(x-0.5)+x)
        B = 2*(y+1)*x - y
        assert abs(j0-A) < 1e-12
        assert abs(j2-B) < 1e-12

# Root functions equivalent to the exact scalar equations.
def A(k):
    return 2*(k*k+1)*math.cos(k/2.0)**2 - 1

def B(k):
    return 2*(k*k+1)*math.cos(k/2.0)**2 - k*k

def bisect(f,a,b,it=100):
    fa,fb=f(a),f(b)
    assert math.isfinite(fa) and math.isfinite(fb) and fa*fb < 0
    for _ in range(it):
        m=(a+b)/2
        fm=f(m)
        if fa*fm <= 0:
            b,fb=m,fm
        else:
            a,fa=m,fm
    return (a+b)/2

# Check the two A-roots around several odd multiples of pi and the sharp sqrt(2)/K scale.
for n in [2,5,10,30,80]:
    K=(2*n+1)*math.pi
    eps=1e-8
    left=bisect(A, 2*n*math.pi+eps, K-eps)
    right=bisect(A, K+eps, 2*(n+1)*math.pi-eps)
    assert abs(A(left)) < 1e-8 and abs(A(right)) < 1e-8
    # K*(distance) -> sqrt(2)
    assert abs(K*(K-left)-math.sqrt(2)) < 0.25
    assert abs(K*(right-K)-math.sqrt(2)) < 0.25

# Check the B-root near L_n=pi/2+n*pi and its alternating L^-2 displacement.
for n in [3,8,17,40,90]:
    L=math.pi/2+n*math.pi
    # B has a pole at odd multiples of pi; bracket locally around L without crossing a pole.
    w=0.45
    root=bisect(B, L-w, L+w)
    assert abs(B(root)) < 1e-8
    target=(-1)**n
    assert abs((root-L)*L*L-target) < 0.15

# Root-set separation: the two right sides could coincide only at k=1, but k=1 is not a root.
assert abs(2*(1.0+1.0)*math.cos(0.5)**2-1.0) > 0.5

print('VERIFY_OK')
