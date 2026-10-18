import math
import random

def run(lam, eta, zeta, x0, steps):
    x = x0
    gamma = zeta
    fvals = [0.5 * lam * x * x]
    for _ in range(steps):
        g = lam * x
        gamma += g * g
        x = x - eta * g / math.sqrt(gamma)
        fvals.append(0.5 * lam * x * x)
    return fvals

# Exact first-step frontier example.
lam = 3.0
zeta = 0.25
eta = 0.5
c = eta * lam / math.sqrt(zeta)
assert c == 3.0
radius = math.sqrt(eta * eta * lam * lam / 4.0 - zeta) / lam
inside = 0.5 * radius
outside = 2.0 * radius
fi = run(lam, eta, zeta, inside, 1)
fo = run(lam, eta, zeta, outside, 1)
assert fi[1] > fi[0]
assert fo[1] < fo[0]

# Random replay of the sufficient global monotonicity regime.
random.seed(7)
for _ in range(500):
    lam = 10 ** random.uniform(-2, 2)
    zeta = 10 ** random.uniform(-2, 2)
    eta = (2.0 * math.sqrt(zeta) / lam) * random.random()
    x0 = random.uniform(-30.0, 30.0)
    vals = run(lam, eta, zeta, x0, 200)
    assert all(vals[j + 1] <= vals[j] + 1e-12 * max(1.0, vals[j])
               for j in range(len(vals) - 1))

# Any prescribed finite ascent prefix can be obtained by taking x0 small enough.
lam = 1.0
zeta = 1.0
eta = 3.0
for N in (1, 2, 4, 8, 12):
    found = False
    for exponent in range(2, 80):
        x0 = 10.0 ** (-exponent)
        vals = run(lam, eta, zeta, x0, N)
        if all(vals[j + 1] > vals[j] for j in range(N)):
            found = True
            break
    assert found

# Local finite-horizon multiplier check for c=3.
x0 = 1e-10
vals = run(1.0, 3.0, 1.0, x0, 5)
for j in range(1, 6):
    expected = 4.0 ** j
    observed = vals[j] / vals[0]
    assert abs(observed / expected - 1.0) < 1e-5

print("VERIFY_OK")
