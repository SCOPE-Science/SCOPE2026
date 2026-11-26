"""Finite checks for the neutral-feedback sinusoidal map. Python 3, stdlib only."""
import math
import random


def step(x, y, z, a, b, d):
    return y, math.sin(z), a + b*x + (d-b)*y - d*math.sin(z) + z


def w(x, y, z, b, d):
    return z + b*x + d*y


def fiber(x, y, theta, b, d):
    return y, math.sin(theta - b*x - d*y)


def roots(b, d, cosine):
    # The Jacobian is [[0,1],[b*cosine,d*cosine]], not cosine times M.
    trace, negative_det = d*cosine, b*cosine
    discr_root = math.sqrt(trace*trace + 4*negative_det)
    return (trace + discr_root)/2, (trace - discr_root)/2


def positive_root(t):
    lo, hi = 1e-8, 1.0
    assert math.sin(t*lo) > lo and math.sin(t*hi) <= hi
    for _ in range(100):
        mid = (lo+hi)/2
        if math.sin(t*mid) > mid:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def main():
    rng = random.Random(202311)
    for _ in range(400):
        b = rng.uniform(0.01, 0.45)
        d = rng.uniform(b, 1.8)
        a = rng.uniform(-3, 3)
        p = tuple(rng.uniform(-4, 4) for _ in range(3))
        assert abs(w(*step(*p, a, b, d), b, d) - w(*p, b, d) - a) < 5e-14

    for _ in range(100):
        b = rng.uniform(.004, .30)
        d = rng.uniform(b, .95-b)
        s = b+d
        a = rng.uniform(-math.pi, math.pi)
        theta = rng.uniform(-5, 5)
        p = tuple(rng.uniform(-2, 2) for _ in range(2))
        q = tuple(rng.uniform(-2, 2) for _ in range(2))
        initial = max(abs(p[0]-q[0]), abs(p[1]-q[1]))
        for n in range(26):
            bound = s**(n//2) * initial
            assert max(abs(p[0]-q[0]), abs(p[1]-q[1])) <= bound + 2e-12
            p = fiber(*p, theta+n*a, b, d)
            q = fiber(*q, theta+n*a, b, d)

    for eps in (0.0001, 0.001, 0.005, 0.01, 0.025, 0.04):
        t = 1+eps
        b0, d0 = .28, .72
        b, d = t*b0, t*d0
        r = positive_root(t)
        assert abs(math.sin(t*r)-r) < 1e-14
        assert roots(b, d, 1)[0] > 1
        c = math.cos(t*r)
        lam, nu = roots(b, d, c)
        assert max(abs(lam), abs(nu)) < 1
        # Check the two Jacobian columns directly against the fiber map.
        h = 1e-5
        for dx, dy, xc, yc in ((h, 0, 0, b*c), (0, h, 1, d*c)):
            plus = fiber(r+dx, r+dy, math.pi, b, d)
            minus = fiber(r-dx, r-dy, math.pi, b, d)
            assert abs((plus[0]-minus[0])/(2*h)-xc) < 1e-8
            assert abs((plus[1]-minus[1])/(2*h)-yc) < 1e-8
        if eps <= .01:
            assert abs(r/math.sqrt(6*eps/t**3)-1) < .02
            assert abs(lam - (1-2*eps/(1+b0))) < 10*eps**2

    alpha = math.pi*(math.sqrt(5)-1)
    b, d = .015, .04
    x = y = theta = acc = 0.
    n = 180000
    for k in range(n+2000):
        x, y = fiber(x, y, theta, b, d)
        theta = (theta+alpha) % (2*math.pi)
        if k >= 2000:
            acc += y
    mean = acc/n
    lead = (b*math.sin(2*alpha)+d*math.sin(alpha))/2
    assert abs(mean-lead) < 1.5*(b+d)**2+2e-4
    print(f"PASS: drift, contraction, six pitchfork samples; mean={mean:.9f}, lead={lead:.9f}.")
    print("Finite samples are supplementary; uniform claims use the analytic proof.")


if __name__ == '__main__':
    main()
