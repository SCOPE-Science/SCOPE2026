"""Finite-generation checks for a bisexual quadratic map's critical layer.

Run: python check.py    (requires NumPy)
These numerical tests do not replace the analytic limit proof.
"""
import numpy as np


def iterate(x, y, a, b):
    return x + a * (1 - x) * y, y * (x + b * (1 - x))


def layer(t):
    if abs(t) < 1e-7:
        return 1 - t/2 + t*t/12, 1 + t/2 + t*t/12
    f = t / np.expm1(t)
    return f, f + t


def integral_pair(n, a, b, K=4, nu=80, nt=161):
    q = 1 - b
    U = min(1, a / q)
    us = (np.arange(nu) + .5) * U / nu
    ts = (np.arange(nt) + .5) * (2*K/nt) - K
    u, t = np.meshgrid(us, ts, indexing='ij')
    d = t/(q*n)
    y = (q/a) * (u+d)
    valid = (y > 0) & (y < 1)
    x = 1 - u
    y = np.where(valid, y, 0.0)
    invariant = x + (a/q)*y - 1
    for _ in range(n):
        x, y = iterate(x, y, a, b)
    # Guard against floating-point cancellation in x ~ 1.
    p = q*n*(1-x)
    v = a*n*y
    assert np.max(np.abs(v-p-q*n*invariant)[valid]) < 1e-6
    out = np.maximum(0, 1 - np.maximum(p,v)/3)
    actual = np.mean(out*valid)*(2*K*U/a)
    expected = (U/a) * (2*K/nt) * sum(max(0, 1-max(layer(float(t0)))/3) for t0 in ts)
    return actual, expected


def test():
    for a,b in [(0.7,0.35),(0.2,0.1),(0.9,0.9)]:
        u = .3*min(1,a/(1-b))
        y = (1-b)/a*u
        x = 1-u
        initial = x+a/(1-b)*y-1
        for j in range(100):
            x,y = iterate(x,y,a,b)
            assert abs((x+a/(1-b)*y-1)-initial) < 1e-13
        n = 1200
        actual, expected = integral_pair(n,a,b)
        print('finite-layer',a,b,n,actual,'limit',expected)
        assert abs(actual-expected) < .15
        q=1-b
        z=1/(q*.25*min(1,a/q))
        offsets=[]
        for j in range(1,50002):
            z=z+1+1/(z-1)
            if j in (10000,50000): offsets.append(z-j-np.log(j))
        print('critical inverse corrections',offsets)
        assert abs(offsets[1]-offsets[0]) < .005
    print('BOXONOV_LAYER_CHECK_OK')


if __name__ == '__main__':
    test()
