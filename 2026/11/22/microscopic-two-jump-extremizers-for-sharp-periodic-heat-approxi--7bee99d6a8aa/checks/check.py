"""Reproducibility checks for the sharp periodic heat/BV residual theorem.

Standard-library only. Numerical checks corroborate, but do not replace,
the infinite-dimensional and uniform small-time arguments in RESULT.md.
"""
import math

PI = math.pi

def root_erfc():
    lo, hi = 0.7, 1.4
    def h(z):
        return math.erfc(z / math.sqrt(2.0)) - 2.0 * math.erfc(z)
    assert h(lo) < 0.0 < h(hi)
    for _ in range(80):
        mid = (lo + hi) / 2.0
        if h(mid) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2.0

def f_profile(z):
    return (z * (math.erfc(z)-0.5*math.erfc(z/math.sqrt(2.0))) +
            (1.0-math.exp(-z*z) - (1.0-math.exp(-z*z/2.0))/math.sqrt(2.0))/math.sqrt(PI))

def e_fast(t, d, k=None):
    """Exact identity with an exponentially decaying correction."""
    if k is None:
        k = int(math.ceil(12.0 / math.sqrt(t)))
    corr = math.fsum(math.exp(-4.0*PI*PI*t*n*n)
                     * (2.0-math.exp(-4.0*PI*PI*t*n*n))
                     * math.sin(PI*n*d)**2/(n*n)
                     for n in range(1, k+1))
    return d*(1.0-d)/4.0-corr/(2.0*PI*PI)

def e_direct(t,d,k=180000):
    return math.fsum((1.0-math.exp(-4.0*PI*PI*t*n*n))**2
                     * math.sin(PI*n*d)**2/n**2
                     for n in range(1,k+1))/(2.0*PI*PI)

def maximize_01(t):
    lo,hi=0.0,0.5
    phi=(math.sqrt(5.0)-1.0)/2.0
    p=hi-phi*(hi-lo);q=lo+phi*(hi-lo)
    for _ in range(85):
        if e_fast(t,p) < e_fast(t,q):
            lo=p
        else:
            hi=q
        p=hi-phi*(hi-lo);q=lo+phi*(hi-lo)
    return (lo+hi)/2.0

z = root_erfc()
fmax = f_profile(z)
finfty=(1.0-1.0/math.sqrt(2.0))/math.sqrt(PI)
assert 0.99 < z < 1.00
assert abs(math.erfc(z / math.sqrt(2.0)) - 2.0*math.erfc(z))<1e-14
assert fmax > finfty + 0.03
assert abs(fmax-0.19831349619700922)<1e-13
assert abs(finfty-0.16524730314632366)<1e-13
assert abs(f_profile(0.0))<1e-14

checks = 7
for t in (0.002,0.005,0.01,0.04):
    for d in (0.08,0.2,0.33,0.5):
        assert abs(e_direct(t,d)-e_fast(t,d)) < 5e-7
        assert abs(e_fast(t,d)-e_fast(t,1.0-d)) < 2e-14
        checks+=2

for t in (0.0001,0.0005,0.001,0.002):
    d=2.0*z*math.sqrt(t)
    assert d < 0.5
    assert abs(e_fast(t,d)/math.sqrt(t)-fmax)<2e-7
    checks+=1

for t in (0.0004, 0.001, 0.002):
    dmax=maximize_01(t)
    assert abs(dmax/(2.0*math.sqrt(t))-z)<2e-4
    assert e_fast(t,dmax) > e_fast(t,0.5)
    assert e_fast(t,dmax) > e_fast(t,0.25)
    checks+=3

print(f"PASS {checks} assertions; root z={z:.15f}, "
      f"F(z)={fmax:.15f}, F(infty)={finfty:.15f}, "
      f"sqrt(F(z))={math.sqrt(fmax):.15f}")
