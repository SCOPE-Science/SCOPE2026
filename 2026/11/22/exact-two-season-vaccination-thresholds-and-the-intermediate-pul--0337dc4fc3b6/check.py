"""Independent arithmetic checks for an exact two-season vaccination allocation theorem.

All conclusions for arbitrary parameters are proved in RESULT.md; these calculations
check algebraic examples and finite-dimensional first-order optimality diagnostics.
Requires only the Python standard library.
"""
from fractions import Fraction as F
from math import exp, log, sqrt, isclose


def phases(H, L, delta, h, T):
    assert H > L > 0 and delta > 0 and 0 < h < T
    b = exp(-delta * (T - h))
    c = 1 - (L / H) * (1 - b)
    a0 = exp(-delta * h)
    x = H * (1 - c * a0) / (1 - b * a0)
    M0 = min(log(H / x), log(x / L))
    return b, c, a0, x, M0


def branch(H, L, delta, h, T, y):
    b, c, a0, x, M0 = phases(H, L, delta, h, T)
    a = exp(-delta * (h - y))
    p = log((1 - a * b) / (1 - a * c))
    eta = delta * a * (c - b) / ((1 - a * c) * (1 - a * b))
    return p, eta, p + eta * y


def criticals(H, L, delta, h, T):
    b, c, a0, x, M0 = phases(H, L, delta, h, T)
    assert x > sqrt(H * L)
    q = sqrt(H / L)
    a1 = (q - 1) / (q * c - b)
    y1 = h + log(a1) / delta
    assert 0 < y1 < h
    p1, eta1, M1 = branch(H, L, delta, h, T, y1)
    assert isclose(p1, log(q), abs_tol=1.e-12)
    return M0, y1, M1


def q_pure(M, H, L, delta, h, T, t):
    E = exp(-delta * T)
    z = exp(-M)
    A = (1 - z) / (1 - z * E)
    S = 1 - A * exp(-delta * t)
    W = (H * (1 - exp(-delta * min(t, h)))
         + L * max(0, exp(-delta * h) - exp(-delta * t))) / delta
    B = (H * (1 - exp(-delta * h))
         + L * (exp(-delta * h) - E)) / delta
    P0 = B / (1 - z * E)
    P = exp(delta * t) * (P0 - W)
    return S * P


def q_branch(H, L, delta, h, T, y, t):
    p, eta, M = branch(H, L, delta, h, T, y)
    k = delta + eta
    Sc = delta / k
    Pc = H / k
    if t <= y:
        return Sc * Pc
    S = 1 - (1 - Sc) * exp(-delta * (t - y))
    # compute P(t) backward from end-of-period condition P(T-)=e^-p P0+.
    PT = exp(-p) * Pc
    if t >= h:
        P = L / delta + (PT - L / delta) * exp(-delta * (T - t))
    else:
        Ph = L / delta + (PT - L / delta) * exp(-delta * (T - h))
        P = H / delta + (Ph - H / delta) * exp(-delta * (h - t))
    return S * P


# Fully rational crossing identities, with delta=log(2), T=2, h=1, H=4, L=1.
b = F(1, 2)
c = F(7, 8)
a0 = F(1, 2)
H, L = F(4), F(1)
x = H * (1 - c * a0) / (1 - b * a0)
assert x == F(3)
a1 = (F(2) - 1) / (F(2) * c - b)
assert a1 == F(4, 5)
assert (1 - a1 * b) / (1 - a1 * c) == F(2)
eta_over_delta = a1 * (c - b) / ((1 - a1 * c) * (1 - a1 * b))
assert eta_over_delta == F(5, 3)

# Independent floating-point evaluation of the two source-example thresholds.
H, L, delta, h, T = 7/4, 1/4, 1., .5, 1.
M0, y1, M1 = criticals(H, L, delta, h, T)
assert abs(M0 - .3909799575971128) < 1e-12
assert abs(y1 - .36135395666342635) < 1e-12
assert abs(M1 - 2.232928304349943) < 1e-11

# For the pure impulse, test the entire discretized first-order threshold
# on both sides, independently from the endpoint formula.
for M in [0.02, M0/2, M0, M0+0.05, M0+0.4]:
    q0 = q_pure(M, H, L, delta, h, T, 0.)
    differences = [q0-q_pure(M,H,L,delta,h,T,T*i/1000) for i in range(1,1000)]
    if M <= M0:
        assert min(differences) > -1.e-11
    else:
        assert min(differences) < -1.e-6

# Verify the exact pulse-plus-high-season-active family on its full
# analytic budget interval; Q=S*P is constant on the support and smaller elsewhere.
for fraction in [0., 0.001, .03, .1, .3, .6, .8, 1.]:
    y=y1*fraction
    p,eta,M = branch(H,L,delta,h,T,y)
    assert abs(M-(p+eta*y))<1.e-14
    qc=delta*H/(delta+eta)**2
    assert abs(q_branch(H,L,delta,h,T,y,0)-qc)<1.e-11
    assert abs(q_branch(H,L,delta,h,T,y,T)-qc)<1.e-11
    for i in range(1001):
        t=T*i/1000
        assert q_branch(H,L,delta,h,T,y,t)<=qc+1.e-10
        if t<=y:
            assert abs(q_branch(H,L,delta,h,T,y,t)-qc)<1.e-10

# Check monotonicity and the branch endpoint for further nondegenerate parameters.
for H,L,delta,h,T in [(5., 1., .25, .4, 2.), (9., 1., 3., 1., 3.),
                        (2.,1.,.75,.3,1.5), (10.,1.,.3,.2,1.)]:
    b,c,a0,x,M0=phases(H,L,delta,h,T)
    if x <= sqrt(H*L):
        continue
    M0,y1,M1=criticals(H,L,delta,h,T)
    Ms=[branch(H,L,delta,h,T,y1*i/100)[2] for i in range(101)]
    assert all(a < b for a,b in zip(Ms,Ms[1:]))
    for y in [0.,y1*.3,y1*.85,y1]:
        qc=delta*H/(delta+branch(H,L,delta,h,T,y)[1])**2
        assert all(q_branch(H,L,delta,h,T,y,T*i/200)<=qc+1e-10 for i in range(201))

print('PASS: exact rational identities, source-example thresholds, pure-pulse cutoff,')
print('       and first-variation inequalities for the mixed pulse–continuous branch')
