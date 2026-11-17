"""Exact finite algebra checks and numerical corroboration of critical compositions."""
from fractions import Fraction as F
from math import log


def normalized_step(y, r):
    h = F(2*r-1, 2*r)
    v = [k*(1-k/2) for k in y[:r]] + [h*y[-1]*(1-y[-1]/2)]
    g = sum(v)
    return [t/g for t in v]


def exact_test(r):
    # Differently weighted resident coordinates, strictly positive rational data.
    numbers = [F(j+1, 1) for j in range(r+1)]
    y = [t/sum(numbers) for t in numbers]
    z = y[-1]
    S = 1-z
    u = [v/S for v in y[:r]]
    q = sum(v*v for v in u)
    E = q-F(1, r)
    h = F(2*r-1, 2*r)
    a0 = F(2*r+1, 4*r)
    c = a0/h
    g = sum(y[i]*(1-y[i]/2) for i in range(r))+h*z*(1-z/2)
    assert g == h+z/F(2*r,1)-a0*z*z-S*S*E/2
    yp = normalized_step(y,r)
    zp = yp[-1]
    assert zp-z == (-a0*z*z*S+z*S*S*E/2)/g
    eps = S*S*E/(2*h*z*(1-z/2))
    assert 1/zp-1/z == c*S/(1-z/2)-eps
    assert yp[-1] > 0 and sum(yp) == 1
    assert max(yp[:r])/sum(yp[:r])-min(yp[:r])/sum(yp[:r]) < max(u)-min(u)
    assert h/(1-F(1,2*r)) == 1


def numeric_test(r, nmax=50000):
    h = 1-1/(2*r)
    c = (2*r+1)/(2*(2*r-1))
    y = [0.1]*(r-1) + [0.8-0.1*(r-1),0.2]
    prev = None
    for n in range(1,nmax+1):
        v = [v*(1-v/2) for v in y[:r]]+[h*y[-1]*(1-y[-1]/2)]
        s = sum(v)
        y = [v/s for v in v]
        if n in (10000,50000):
            correction = 1/y[-1]-c*n+0.5*log(n)
            if prev is None:
                prev = correction
            else:
                assert abs(correction-prev)<0.01, (r, correction, prev)
            assert abs(n*y[-1]-1/c)<0.004
    resident = [v/(1-y[-1]) for v in y[:r]]
    assert max(abs(v-1/r) for v in resident) < 1e-8


if __name__ == '__main__':
    for r in (2,3,5):
        exact_test(r)
        numeric_test(r)
    print('MULTI_RESIDENT_CRITICAL_LOG_CLOCK_OK')
