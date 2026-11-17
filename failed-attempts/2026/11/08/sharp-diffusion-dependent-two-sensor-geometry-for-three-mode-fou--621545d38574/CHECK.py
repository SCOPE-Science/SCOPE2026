"""Numerical checks of a four-sample, three-Fourier-mode heat observation frame.

Requires Python 3 and numpy. Every check is finite and supplements an analytic proof.
"""
import math
import numpy as np

count = 0


def assert_close(x, y, *, atol=1e-10, rtol=1e-9):
    global count
    if not np.allclose(x, y, atol=atol, rtol=rtol):
        raise AssertionError((x, y))
    count += 1


def measurement(q, theta):
    x = [-theta/2, theta/2]
    return np.asarray([[(decay if k else 1.0)*complex(math.cos(k*y),math.sin(k*y))
                        for k in (-1,0,1)]
                       for decay in (1.0,q)
                       for y in x
                       ], dtype=complex) * np.asarray([1,1,1], dtype=float)


def spectral(q, theta):
    u = math.cos(theta/2)**2
    h = 1+q*q
    b = 1+q
    even = np.array([[4*h*u,2*math.sqrt(2)*b*math.sqrt(u)],
                     [2*math.sqrt(2)*b*math.sqrt(u),4]], float)
    return np.sort(np.r_[np.linalg.eigvalsh(even),4*h*(1-u)])


def optimum(q):
    h = 1+q*q
    d = 1-q
    A=4*h*h+2*h*q*q-d*d
    discriminant = A*A-32*h*h*h*q*q
    assert discriminant > 0
    u=(A+math.sqrt(discriminant))/(8*h*h)
    return u,4*h*(1-u)

for q in [0.0,0.02,0.1,0.25,0.4,0.65,0.85,0.95,0.985]:
    for theta in np.linspace(0.0, math.pi, 61):
        direct=np.linalg.eigvalsh(measurement(q,float(theta)).conj().T @ measurement(q,float(theta)))
        assert_close(direct,spectral(q,float(theta)))
    u,v=optimum(q)
    assert_close(4*(1+q*q)*(1-u), v)
    assert_close(np.min(spectral(q,2*math.acos(math.sqrt(u)))),v)
    if q < 1:
        assert 0.5 < u < 1
        count+=1
    for angle in np.linspace(0.0, math.pi, 120):
        assert np.min(spectral(q,float(angle))) <= v+1e-9
        count+=1

# At distinct non-antipodal sensors, both Fourier parities are observable for every positive time separation.
for q in [0,0.03,0.35,0.9]:
    for angle in [0.02,0.2,math.pi/3, 2.7,math.pi-0.01]:
        assert min(spectral(q,angle)) > 0
        count += 1
    assert_close(min(spectral(q,0)),0)
    assert_close(min(spectral(q,math.pi)),0)

# Limiting design at distant times.
assert_close(optimum(0.0)[0],0.75)
assert_close(optimum(0.0)[1],1.0)
# Near-coincident times: quadratic lower-frame collapse and linearly collapsing sensor angle.
for delta in [0.01,0.005,0.002]:
    q=1-delta
    u,lower=optimum(q)
    assert_close((1-u)/(delta*delta),1/12,atol=1e-3,rtol=0.04)
    assert_close(lower/(delta*delta),2/3,atol=1e-2,rtol=0.04)
    assert_close(2*math.acos(math.sqrt(u))/delta,1/math.sqrt(3),atol=0.02,rtol=0.05)

print('HEAT_TWO_SENSOR_CHECKS_PASS',count)
