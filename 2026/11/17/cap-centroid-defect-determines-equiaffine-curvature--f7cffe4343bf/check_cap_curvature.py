"""Numerical cross-checks for the local cap-centroid equiaffine curvature law.

All computations are evidence of sample consistency; the proof of the limit is analytic.
Run: python check_cap_curvature.py
"""
import math
import mpmath as mp
mp.mp.dps = 55
c = (mp.mpf(3) / 175) * (3 / (4 * mp.sqrt(2))) ** (mp.mpf(2) / 3)

# Exact conic chord widths, after taking tangent as the horizontal axis.
for sigma, k in [(-1, 1), (0, 0), (1, -1)]:
    vals = []
    for raw_h in ['0.10', '0.04', '0.015', '0.005']:
        h = mp.mpf(raw_h)
        width = lambda y: 2 * mp.sqrt(2 * y + sigma * y * y)
        area = mp.quad(width, [0, h])
        depth = mp.quad(lambda y: y * width(y), [0, h]) / area
        val = (mp.mpf(3) / 5 - depth / h) / area ** (mp.mpf(2) / 3)
        vals.append(abs(val - c * k))
        if sigma < 0:
            assert depth / h < mp.mpf(3) / 5
        elif sigma > 0:
            assert depth / h > mp.mpf(3) / 5
        else:
            assert abs(depth / h - mp.mpf(3) / 5) < mp.mpf('1e-50')
    if sigma != 0:
        assert vals[-1] < vals[0]
        assert vals[-1] < mp.mpf('3e-5')

# Asymmetric quartic branch, testing the mixed f'''^2 and f'''' terms.
b, q = mp.mpf('0.2'), mp.mpf('0.1')
f = lambda x: x*x + b*x**3 + q*x**4
fp2, fp3, fp4 = mp.mpf(2), 6*b, 24*q
k = (3*fp2*fp4 - 5*fp3**2) / (9*fp2**(mp.mpf(8)/3))
errors = []
for raw_h in ['0.08','0.03','0.01','0.003']:
    h = mp.mpf(raw_h)
    def root(y, sign):
        if y == 0: return mp.mpf('0')
        guess = sign*mp.sqrt(y)
        return mp.findroot(lambda x: f(x)-y, (guess*mp.mpf('0.8'),guess*mp.mpf('1.2')))
    width = lambda y: root(y,1)-root(y,-1)
    area = mp.quad(width, [0,h])
    depth = mp.quad(lambda y:y*width(y), [0,h]) / area
    val = (mp.mpf(3)/5-depth/h)/area**(mp.mpf(2)/3)
    errors.append(abs(val-c*k))
assert errors[-1] < errors[0]
assert errors[-1] < mp.mpf('3e-5')
print('CAP_CENTROID_AFFINE_CURVATURE_CHECKS_OK')
print('conic coefficient',mp.nstr(c,24))
print('quartic coefficient',mp.nstr(c*k,24),'last error',mp.nstr(errors[-1],12))
