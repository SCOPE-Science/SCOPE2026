"""Numerical cross-checks for sharp concentration of homogeneous Fock bidiscs.

Requires Python 3 and mpmath. Analytic arguments in RESULT.md prove the general theorem;
finite-precision testing is not a substitute for proof.
"""
import mpmath as mp
mp.mp.dps = 70

def tail(j, x):
    return mp.gammainc(j + 1, 0, x) / mp.factorial(j)

def ratio(j, x):
    return tail(j + 1, x) / tail(j, x)

def spec(m, a, b):
    return [tail(k, a) * tail(m-k, b) for k in range(m+1)]

def root(k, m, b):
    target = ratio(m-k-1, b)
    lo, hi = mp.mpf('0'), mp.mpf('1')
    while ratio(k, hi) <= target:
        hi *= 2
    for _ in range(230):
        med = (lo + hi)/2
        if ratio(k, med) < target:
            lo = med
        else:
            hi = med
    return (lo + hi)/2

def expected_asymptotic(m, a, b):
    h, v = min(a,b), max(a,b)
    p, q = h/(h+v), v/(h+v)
    c = v/(mp.exp(v)-1) / (mp.sqrt(2*mp.pi)*(p*q)**mp.mpf('1.5'))
    return c * m**(-mp.mpf('1.5')) * ((h+v)/h)**m

for a,b in [('0.4','1.7'),('1.2','1.2'),('2.6','1.3'),('0.9','3.1')]:
    a,b=mp.mpf(a),mp.mpf(b)
    for m in range(1,10):
        L=spec(m,a,b)
        assert all(x>0 for x in L)
        for k in range(1,m):
            assert L[k]**2 > L[k-1]*L[k+1]
        expected_min = min(L[0], L[-1]); assert min(L)==expected_min
        if a<b: assert L[-1]<L[0]
        if a>b: assert L[0]<L[-1]
        if a==b: assert mp.almosteq(L[0],L[-1])
        for k in range(m):
            assert mp.almosteq(L[k+1]/L[k],ratio(k,a)/ratio(m-k-1,b),rel_eps=mp.mpf('1e-58'))
print('EXACT_GAMMA_TAIL_RATIOS_LOG_CONCAVITY_ENDPOINT_MIN_PASS')

m,b=5,mp.mpf('2')
T=[root(k,m,b) for k in range(m)]
assert all(T[k]<T[k+1] for k in range(m-1))
for k,t in enumerate(T):
    L=spec(m,t,b)
    assert mp.almosteq(L[k],L[k+1],rel_eps=mp.mpf('1e-60'))
    assert all(L[j] < L[k] for j in range(m+1) if j not in (k,k+1))
checks = [T[0]/2]+[(T[k-1]+T[k])/2 for k in range(1,m)]+[2*T[-1]]
for k,a in enumerate(checks):
    L=spec(m,a,b)
    assert max(range(m+1),key=lambda j:L[j])==k
print('STRICT_FIVE_STEP_MODE_STAIRCASE_AND_NO_TRIPLE_CROSSING_PASS')

for aa,bb in [('1','1'),('0.5','2'),('1.2','3.4')]:
    a,b=mp.mpf(aa),mp.mpf(bb)
    err=[]
    for m in (60,120,220):
        L=spec(m,a,b)
        K=max(L)/min(L)
        E=expected_asymptotic(m,a,b)
        err.append(abs(K/E-1))
    assert err[-1] < err[0]
    assert err[-1] < mp.mpf('.025')
print('SHARP_EXPONENTIAL_STABILITY_RATE_AND_M_MINUS_THREE_HALVES_PREFACTOR_PASS')

for a,j in [(mp.mpf('.4'),0),(mp.mpf('2.7'),2),(mp.mpf('1.1'),5)]:
    integrated = mp.quad(lambda t: t**j*mp.exp(-t)/mp.factorial(j),[0,a])
    assert mp.almosteq(integrated,tail(j,a),rel_eps=mp.mpf('1e-62'))
print('GAUSSIAN_RADIAL_INTEGRAL_NORMALIZATION_PASS')
print('BIDISC_HOMOGENEOUS_FOCK_CONCENTRATION_CHECKS_PASS')
