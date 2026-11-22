"""Numerical cross-checks for the sharp radius-two weighted Fourier minimax law.

Only Python's standard library is required. Finite computations illustrate the
analytic extremal proof; they are not used to prove the all-order assertion.
"""
from math import log, exp, sqrt, isclose


def parameters(k):
    assert k > 0
    r = k / 2.0
    h_lower = (r + 2.0) / r
    def H(h):
        return (r + 1) * log(h) + log(r * h - r - 2) - log((r + 2) * h - r)
    lo = h_lower * (1 + 1e-12)
    hi = lo * 2.0
    while H(hi) < 0:
        hi *= 2.0
    for _ in range(180):
        mid = (lo + hi) / 2
        if H(mid) < 0: lo = mid
        else: hi = mid
    h = (lo + hi) / 2
    A = r * (1 + h) / ((r + 1) * h)
    B = r / ((r + 2) * h)
    C = ((r + 2) * h - r) / ((r + 1) * (r + 2) * h)
    def F(z): return z**r * (1 - A * z + B * z * z) - C
    lo = h
    hi = max(2*h, 10.0)
    while F(hi) < 0: hi *= 2.0
    for _ in range(180):
        mid = (lo + hi) / 2
        if F(mid) < 0: lo = mid
        else: hi = mid
    z = (lo + hi)/2
    a, b = A*z, B*z*z
    u0 = 1 - a/2 + 3*b/8
    u1 = (a-b)/4
    u2 = b/16
    M = 2**k * C / z**r
    return r, h, z, A, B, C, a, b, M, (u0, u1, u2)


def test(k):
    r,h,z,A,B,C,a,b,M,weights = parameters(k)
    t, v = 1/z, h/z
    q = lambda y: 1-a*y+b*y*y
    W = lambda y: 2**k * y**r * q(y) if y>0 else 0.0
    assert 0 < t < v < 1
    assert C > 0 and q(t)>0 and q(v)<0 and q(1)>0
    assert isclose(q(t), C, rel_tol=1e-11)
    assert isclose(W(t), M, rel_tol=2e-11)
    assert isclose(W(v), -M, rel_tol=2e-11)
    assert isclose(W(1), M, rel_tol=2e-11)
    assert isclose(weights[0]+2*weights[1]+2*weights[2],1.,rel_tol=1e-12,abs_tol=1e-12)
    for j in range(2001):
        y = j/2000
        assert abs(W(y)) <= M*(1+3e-10)
    # Perturb coefficients in two independent directions and independently
    # maximize their weighted multiplier by the stationary-point equation.
    for da,db in [(0.0002,0),(0,-0.0002),(.0001,-.0001),(-.0001,.0001),(.002,.002),(-.002,-.002)]:
        aa, bb = a+da,b+db
        # Stationary equation: r-(r+1)aa*y+(r+2)bb*y^2=0
        disc=((r+1)*aa)**2-4*r*(r+2)*bb
        critical=[1.]
        if disc>=0 and bb!=0:
            for e in [-1.,1.]:
                y=((r+1)*aa+e*sqrt(disc))/(2*(r+2)*bb)
                if 0<y<1: critical.append(y)
        test_M=max(abs(2**k * y**r * (1-aa*y+bb*y*y)) for y in critical)
        assert test_M > M*(1+1e-10)
    return {"order": k, "h": h, "z": z, "sharp_norm": M, "coefficients": weights,
            "alternation": (t,v,1.)}


if __name__ == "__main__":
    results = [test(k) for k in (0.5, 1, 2, 3, 4, 5, 6, 8, 12, 20, 30)]
    for result in results:
        print("order={order:g} norm={sharp_norm:.12f} h={h:.9f} z={z:.9f}".format(**result))
    print("FIFTH_ORDER",results[5])
    print("CHECK_OK: 11 orders, 3 exact ripple relations/order, 2001 mesh inequalities/order, 6 perturbations/order")
