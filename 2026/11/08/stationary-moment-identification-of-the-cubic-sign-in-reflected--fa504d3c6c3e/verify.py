"""Independent numerical spot checks of the stationary-moment identities.

Requires mpmath >= 1.3. Analytical claims are proved in RESULT.md; a
finite test is not a proof for all parameter values.
"""
import mpmath as mp

mp.mp.dps = 65
EPS = mp.mpf('1e-45')


def moments(mu, s, D, L, degrees=(0, 2, 4, 6, 8)):
    mu, s, D, L = map(mp.mpf, (mu, s, D, L))
    base = lambda x: mp.exp((mu*x*x + s*x**4/2)/D)
    z = mp.quad(base, [0, L])
    return {k: mp.quad(lambda x: x**k*base(x), [0, L])/z
            for k in degrees}


def reconstruct(mm, L):
    L = mp.mpf(L)
    A = L*L*mm[2] - mm[4]
    B = L*L*mm[4] - mm[6]
    C = L*L*mm[6] - mm[8]
    Delta = A*C - B*B
    Q = (3*mm[2] - L*L)/2
    R = (5*mm[4] - 3*L*L*mm[2])/2
    assert Delta > 0
    return (C*Q-B*R)/Delta, (A*R-B*Q)/Delta


def even_moment_alpha_beta(alpha, beta, L, degree):
    alpha, beta, L = map(mp.mpf, (alpha, beta, L))
    w = lambda x: mp.exp(alpha*x*x + beta*x**4)
    return mp.quad(lambda x: x**degree*w(x), [0, L]) / mp.quad(w, [0, L])


def baseline(u, L):
    # The root is uniquely determined because the variance is strictly
    # increasing with alpha for each fixed quartic tilt.
    a, b = mp.mpf('-100'), mp.mpf('100')
    for _ in range(200):
        mid = (a+b)/2
        if even_moment_alpha_beta(mid, 0, L, 2) < u:
            a = mid
        else:
            b = mid
    return even_moment_alpha_beta((a+b)/2, 0, L, 4)


cases = [
    ('-1', '-2', '0.5', '1'),
    ('-1', '2', '0.5', '1'),
    ('0.2', '-0.7', '0.9', '1.5'),
    ('1.3', '1.1', '3', '2'),
    ('-0.1', '0', '1', '1'),
    ('-4', '-3', '2', '0.75'),
    ('0', '1', '1', '1'),
    ('0.3', '0', '1.25', '0.8'),
]
passed = 0
for mu, s, D, L in cases:
    m = moments(mu, s, D, L)
    alpha, delta = reconstruct(m, L)
    assert abs(alpha - mp.mpf(mu)/mp.mpf(D)) < EPS
    assert abs(delta - mp.mpf(s)/mp.mpf(D)) < EPS
    passed += 2
    reference = baseline(m[2], L)
    if mp.mpf(s) > 0:
        assert m[4] > reference + EPS
    elif mp.mpf(s) < 0:
        assert m[4] < reference - EPS
    else:
        assert abs(m[4]-reference) < EPS
    passed += 1

# At the same second moment, different cubic signs are possible.
L = mp.mpf('1')
u = mp.mpf('0.3')
def alpha_at_variance(beta):
    a, b = mp.mpf('-100'), mp.mpf('100')
    for _ in range(200):
        mid = (a+b)/2
        if even_moment_alpha_beta(mid, beta, L, 2) < u:
            a = mid
        else:
            b = mid
    return (a+b)/2

b_minus, b_zero, b_plus = map(mp.mpf, ['-1', '0', '1'])
a_minus = alpha_at_variance(b_minus)
a_zero = alpha_at_variance(b_zero)
a_plus = alpha_at_variance(b_plus)
v_minus = even_moment_alpha_beta(a_minus, b_minus, L, 2)
v_zero = even_moment_alpha_beta(a_zero, b_zero, L, 2)
v_plus = even_moment_alpha_beta(a_plus, b_plus, L, 2)
assert max(abs(v-u) for v in (v_minus, v_zero, v_plus)) < EPS
r4 = [even_moment_alpha_beta(a,b,L,4) for a,b in
      ((a_minus,b_minus), (a_zero,b_zero), (a_plus,b_plus))]
assert r4[0] < r4[1] < r4[2]
passed += 2
print(f'PASS {passed} numerical checks; 8 parameter cases and same-variance sign separation')
