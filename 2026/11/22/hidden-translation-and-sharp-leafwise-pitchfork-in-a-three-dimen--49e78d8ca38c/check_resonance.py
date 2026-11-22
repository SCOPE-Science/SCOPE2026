"""Reproducible finite checks for the neutral-feedback sinusoidal map theorem.

These tests supplement, rather than replace, the analytic proof.
Run: python3 check_resonance.py
"""
import math
import random

R = random.Random(202311)


def step(x, y, z, a, b, d):
    g = d - b
    return y, math.sin(z), a + b*x + g*y - d*math.sin(z) + z


def w(x, y, z, b, d):
    return z + b*x + d*y


def eigen_radius_nonnegative(b, d):
    return (d + math.sqrt(d*d + 4*b))/2


def positive_root(s):
    assert s > 1
    l, u = 1e-8, 1.0
    assert math.sin(s*l) - l > 0
    assert math.sin(s*u) - u <= 1e-14
    for _ in range(100):
        m = (l+u)/2
        if math.sin(s*m) - m > 0:
            l = m
        else:
            u = m
    return (l+u)/2

identity_tests = 0
for _ in range(400):
    b = R.uniform(0.01, 0.45)
    d = R.uniform(b, 1.8)
    a = R.uniform(-3, 3)
    x, y, z = (R.uniform(-4, 4) for _ in range(3))
    x1, y1, z1 = step(x, y, z, a, b, d)
    assert abs((w(x1, y1, z1, b, d)-w(x, y, z, b, d))-a) < 5e-14
    identity_tests += 1

contraction_tests = 0
for _ in range(100):
    b = R.uniform(.004, .30)
    d = R.uniform(b, .95-b)
    s = b+d
    a = R.uniform(-math.pi, math.pi)
    W = R.uniform(-5, 5)
    x1, y1 = R.uniform(-2, 2), R.uniform(-2, 2)
    x2, y2 = R.uniform(-2, 2), R.uniform(-2, 2)
    initial_distance = max(abs(x1-x2), abs(y1-y2))
    for n in range(26):
        bound = s**(n//2) * initial_distance
        assert max(abs(x1-x2),abs(y1-y2)) <= bound + 2e-12
        th = W + n*a
        x1,y1 = y1,math.sin(th-b*x1-d*y1)
        x2,y2 = y2,math.sin(th-b*x2-d*y2)
    contraction_tests += 1

pitchfork_tests = 0
for eps in [0.0001, 0.001, 0.005, 0.01, 0.025, 0.04]:
    s = 1 + eps
    b0, d0 = .28, .72
    b, d = s*b0, s*d0
    root = positive_root(s)
    assert abs(math.sin(s*root)-root) < 1e-14
    assert eigen_radius_nonnegative(b,d) > 1
    assert abs(math.cos(s*root))*eigen_radius_nonnegative(b,d) < 1
    if eps <= .01:
        approx = math.sqrt(6*eps/s**3)
        assert abs(root/approx-1) < .02
    pitchfork_tests += 1

# Numerical ergodic means are diagnostics only, not proofs of unique ergodicity.
alpha = 2*math.pi*(math.sqrt(5)-1)/2
b,d = .015, .04
x,y,theta = 0.,0.,0.
n = 180000
acc = 0.
for k in range(n + 2000):
    x,y = y,math.sin(theta-b*x-d*y)
    theta = (theta+alpha) % (2*math.pi)
    if k >= 2000:
        acc += y
mean = acc/n
first_order = (b*math.sin(2*alpha)+d*math.sin(alpha))/2
# Analytic remainder bound 3s^2/2; small numerical discrepancy allowed.
assert abs(mean-first_order) < 1.5*(b+d)**2+2e-4

print(f"PASS: {identity_tests} drift identities; {contraction_tests} uniform contraction cases;")
print(f"      {pitchfork_tests} bifurcation/stability cases; mean={mean:.9f}, first-order={first_order:.9f}.")
print("Limit: finite tests are supplementary; infinite statements use analytic arguments.")
