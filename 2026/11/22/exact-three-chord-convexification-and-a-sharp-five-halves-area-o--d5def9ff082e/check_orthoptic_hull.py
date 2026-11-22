"""Reproducible numerical diagnostics for a threefold orthoptic hull-area law.

Requires Python 3 and mpmath; scipy/numpy are optional for hull cross-check.
Exact proof is in RESULT.md; these diagnostics are not a proof of convexity.
"""
import mpmath as mp
mp.mp.dps = 65
r = mp.sqrt(2)
e0 = r / 16
C = mp.mpf(3) * r**2 / 2 * (mp.mpf(32)/(5*r))**mp.mpf('2.5')
assert abs(C - mp.mpf('130.70243996332004023296596847345294')) < mp.mpf('1e-25')


def pocket_area(e):
    if e <= e0:
        return mp.mpf(0)
    s0 = mp.sqrt(32*(e-e0)/(5*r))
    s = mp.findroot(lambda t: 16*e*mp.cos(t)*mp.cos(2*t)-r,
                    (mp.mpf('.9')*s0, mp.mpf('1.1')*s0))
    assert 0 < s < mp.pi/6
    x = lambda t: r*mp.cos(t)-e*mp.cos(4*t)
    dy = lambda t: r*mp.cos(t)-4*e*mp.cos(4*t)
    return 6*mp.quad(lambda t: (x(s)-x(t))*dy(t), [0,s])

for d in ['0.0005', '0.0001', '0.00002', '0.000004']:
    d = mp.mpf(d)
    ratio = pocket_area(e0+d)/(C*d**mp.mpf('2.5'))
    assert abs(ratio-1) < 18*d

# Check a few exact sign and curvature boundaries, without claiming exhaustiveness.
for e in [e0/2, e0, (e0+mp.mpf('0.125'))/2]:
    kmin = r*r+64*e*e-20*r*e
    expect = (r-4*e)*(r-16*e)
    assert abs(kmin-expect) < mp.mpf('1e-55')
    assert (kmin >= 0) == (e <= e0)

try:
    import numpy as np
    from scipy.spatial import ConvexHull
    t = np.linspace(0,2*np.pi,60000,endpoint=False)
    for e in [float(e0)+0.003, float(e0)+0.012, 0.1249]:
        z = float(r)*np.exp(1j*t)-e*np.exp(4j*t)
        numerical = ConvexHull(np.column_stack([z.real,z.imag])).volume
        predicted = float(mp.pi*(r*r+4*mp.mpf(e)**2)+pocket_area(mp.mpf(e)))
        assert abs(numerical-predicted) < 6e-7
except ImportError:
    pass

print('THREEFOLD_ORTHOPTIC_HULL_AREA_CHECKS_OK')
