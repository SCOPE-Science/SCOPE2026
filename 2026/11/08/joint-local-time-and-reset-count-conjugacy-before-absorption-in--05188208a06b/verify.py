"""Independent finite-state resolvent checks of a local-time/reset-count theorem.

Uses absorption at site zero, a reflecting remote boundary, central-difference
Ornstein-Uhlenbeck jump rates and a lattice occupation-density penalty. The
finite-state identities test algebra, while their convergence alone does not
prove the continuum theorem (whose proof is in RESULT.md).
"""
import math
import numpy as np
from scipy.sparse import lil_matrix, diags, csc_matrix
from scipy.sparse.linalg import spsolve
from scipy.integrate import quad
from scipy.special import pbdv

ASSERTIONS = 0

def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)

def close(x, y, atol=1e-10, rtol=1e-10):
    return abs(x - y) <= atol + rtol * max(abs(x), abs(y))

def discrete_case(diffusivity, stiffness, reset_rate, spacing, count=70, reset_x=1.0):
    # Site i represents x=(i+1)*spacing. Absorption is the left missing site.
    aidx = int(round(reset_x / spacing)) - 1
    check(aidx >= 1 and aidx < count - 2, 'reset interior')
    Q = lil_matrix((count, count))
    absorption = np.zeros(count)
    for i in range(count):
        x = (i+1)*spacing
        down = diffusivity / spacing**2 + stiffness*x/(2*spacing)
        up = diffusivity / spacing**2 - stiffness*x/(2*spacing)
        check(down >= 0, 'nonnegative down rate')
        if i < count-1:
            check(up >= 0, 'nonnegative up rate')
        else:
            up = 0.0  # no transition beyond the remote reflecting wall
        Q[i, i] = -(up + down)
        if i < count-1:
            Q[i, i+1] = up
        if i > 0:
            Q[i, i-1] = down
        else:
            absorption[i] = down
    Q = Q.tocsc()
    A = diags(np.full(count, reset_rate), format='csc') - Q
    h = spsolve(A, absorption)[aidx]
    unit_a = np.zeros(count)
    unit_a[aidx] = 1.0
    green = spsolve(A, unit_a)[aidx] / spacing
    check(0 < h < 1, '0<h<1')
    check(green > 0, 'green positive')
    one = np.ones(count)
    for s in [0.0, .17, .71, 2.3, 4.0]:
        for z in [0.0, .19, .51, .84, 1.0]:
            # Backward problem: (r-Q+s delta_a-r z 1 tensor delta_a) F = absorption.
            # delta_a on grid is 1/spacing times site indicator.
            diag_penalty = np.zeros(count)
            diag_penalty[aidx] = s/spacing
            matrix = A + diags(diag_penalty, format='csc') - csc_matrix(reset_rate*z*np.outer(one, unit_a))
            direct = spsolve(matrix, absorption)[aidx]
            from_theorem = h/(1+s*green-(1-h)*z)
            check(close(direct, from_theorem, atol=2e-11), 'double transform discrepancy')
    # Coefficient-level checks follow by differentiation and total normalization.
    check(close(h/(1-(1-h)), 1), 'probabilities sum to one')
    check(close(math.sqrt(1-h)**2, 1-h), 'universal correlation')
    for n in range(10):
        check(close(h*(1-h)**n * (n+1)*green, (n+1)*green*h*(1-h)**n), 'gamma coefficient')
    return h, green

def killed_ou_green(stiffness, diffusivity, reset_rate, a):
    # Method of images is valid because OU drift is odd about the absorbing point.
    def kern(t):
        if t == 0: return 0.0
        expm = math.exp(-stiffness*t)
        variance = diffusivity / stiffness * (-math.expm1(-2*stiffness*t))
        scale = 1/math.sqrt(2*math.pi*variance)
        return math.exp(-reset_rate*t)*scale * (
            math.exp(-a*a*(1-expm)**2/(2*variance)) -
            math.exp(-a*a*(1+expm)**2/(2*variance)))
    return quad(kern, 0, 45, epsabs=2e-10, epsrel=2e-10, points=[.002, .05, .4, 3], limit=350)[0]

def killed_ou_h(stiffness, diffusivity, reset_rate, a):
    q = -reset_rate / stiffness
    v = a * math.sqrt(stiffness / diffusivity)
    return math.exp(v*v/4)*pbdv(q, v)[0]/pbdv(q, 0.0)[0]

for params in [(1., .9, .7, .125, 48, 1.), (.8, .3, 1.1, .125, 60, 1.),
               (1.1, .55, .4, .125, 60, 1.)]:
    discrete_case(*params)

kappa, D, rate, a = .9, 1., .7, 1.
h = killed_ou_h(kappa, D, rate, a)
green = killed_ou_green(kappa, D, rate, a)
check(close(h, .5998000825533482, atol=2e-7), 'OU absorption resolvent')
check(close(green, .5041468049193368, atol=2e-7), 'OU Green kernel')
check(close(math.sqrt(1-h), .6326135609095428, atol=2e-7), 'OU correlation')

# Brownian limit: killed half-line heat kernel and Laplace hitting transform.
for d, rate, a in [(1.0, .7, 1.), (.5, 1.5, 2.), (2., .3, .7)]:
    k = math.sqrt(rate/d)
    h_b = math.exp(-k*a)
    green_b = -math.expm1(-2*k*a)/(2*d*k)
    check(close(h_b + (1-h_b), 1.0), 'Brownian hitting identity')
    check(close((1-h_b)/green_b, 2*d*k/(1+h_b)), 'Brownian conditional Poisson intensity')

print(f'PASS {ASSERTIONS} direct finite-state/analytic diagnostic assertions')
print(f'OU example: h={h:.12g}, G={green:.12g}, conditional reset intensity={(1-h)/green:.12g}')
