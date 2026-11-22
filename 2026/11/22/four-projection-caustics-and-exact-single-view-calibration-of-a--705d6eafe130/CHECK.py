"""Reproducibility checks for projected Beta-convolution caustics.
Requires Python 3 and mpmath. Run: python CHECK.py
The proof is analytic; quadrature checks are finite diagnostics only.
"""
import mpmath as mp
mp.mp.dps = 55

def projected_density(z, a, b, beta):
    z, a, b, t = map(mp.mpf, (z, a, b, beta))
    assert a > b > 0 and t > 0
    lo = max(-1, (z-b)/a)
    hi = min(1, (z+b)/a)
    if lo >= hi:
        return mp.mpf('0')
    norm = b * mp.beta(mp.mpf('0.5'), t)**2
    def integrand(u):
        v = (z-a*u)/b
        prod = max(mp.mpf(0), 1-u*u)*max(mp.mpf(0), 1-v*v)
        return (prod**(t-1)/norm) if prod > 0 else mp.mpf(0)
    return mp.quad(integrand, [lo, (lo+hi)/2, hi], method='tanh-sinh')

def coefficients(a,b,t):
    scale = 2**(2*t-2)/(a*b)**t/mp.beta(mp.mpf('.5'),t)**2
    return scale*mp.beta(t,t), scale*mp.beta(t,1-2*t)

checks = 0
for a,b,t in [(mp.mpf('.8'),mp.mpf('.6'),mp.mpf('.25')),
              (mp.mpf('.9'),mp.mpf('.2'),mp.mpf('.3')),
              (mp.mpf('.7'),mp.mpf('.4'),mp.mpf('.25'))]:
    outer, inner = coefficients(a,b,t)
    assert mp.almosteq(inner/outer,1/(2*mp.cos(mp.pi*t)))
    checks += 1
    eps = mp.mpf('.0001')
    for z,c in [(a+b-eps,outer),(a-b+eps,inner),(a-b-eps,inner),
                (-a+b+eps,inner),(-a-b+eps,outer)]:
        val = projected_density(z,a,b,t)*eps**(1-2*t)/c
        assert abs(val-1) < mp.mpf('.075'), (a,b,t,z,float(val))
        checks += 1

# At the logarithmic threshold the increment per decimal scale tends to K log 10.
a,b,t = mp.mpf('.8'),mp.mpf('.6'),mp.mpf('.5')
h = a-b
K = 1/(2*mp.pi**2*mp.sqrt(a*b))
p1=projected_density(h+mp.mpf('.0001'),a,b,t)
p2=projected_density(h+mp.mpf('.00001'),a,b,t)
assert abs((p2-p1)/(K*mp.log(10))-1) < mp.mpf('.015')
checks += 1

# The four singular locations algebraically determine scale and absolute view angle.
for aa,bb in [(mp.mpf('.8'),mp.mpf('.6')),(mp.mpf('.9'),mp.mpf('.1'))]:
    outer, inner = aa+bb,aa-bb
    ra, rb = (outer+inner)/2,(outer-inner)/2
    assert mp.almosteq(ra,aa) and mp.almosteq(rb,bb)
    assert mp.almosteq(mp.sqrt((outer**2+inner**2)/2),mp.sqrt(aa**2+bb**2))
    checks += 2
print('PASS:', checks, 'local-asymptotic, logarithmic, Beta-identity, and geometry assertions')
