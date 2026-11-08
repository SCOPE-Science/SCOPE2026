"""Reproducibility checks for the stated causal wavelet scale-frame theorem.

These are finite numerical checks, not a replacement for the analytical proof.
Requires mpmath; no external data or network.
"""
import mpmath as mp

mp.mp.dps = 75
CHECKS = 0


def assert_close(actual, expected, rtol=mp.mpf('1e-38'), atol=mp.mpf('1e-42')):
    global CHECKS
    CHECKS += 1
    if abs(actual-expected) > atol + rtol * max(abs(actual), abs(expected)):
        raise AssertionError((mp.nstr(actual, 25), mp.nstr(expected, 25)))


def p(h, t):
    # With finite tails, the omitted sech-squared terms are below 1e-45.
    m = max(120, int(80 / float(h)) + 20)
    return mp.fsum(mp.sech(t - j*h)**2 for j in range(-m,m+1)) / 4


def p_fourier(h, t):
    return 1/(2*h) + mp.pi**2/h**2 * mp.fsum(
        n*mp.cos(2*mp.pi*n*t/h)/mp.sinh(mp.pi**2*n/h)
        for n in range(1, 140))


def elliptic_modulus(h):
    # Unique elliptic modulus for K(k')/K(k)=pi/h.
    lo=mp.mpf('1e-70'); hi=1-mp.mpf('1e-70')
    for _ in range(255):
        k=(lo+hi)/2
        ratio=mp.ellipk(1-k*k)/mp.ellipk(k*k)
        if ratio > mp.pi/h: lo=k
        else: hi=k
    return (lo+hi)/2


def p_elliptic(h,t):
    k=elliptic_modulus(h)
    K=mp.ellipk(k*k); E=mp.ellipe(k*k)
    dn=mp.ellipfun('dn',2*K*t/h,k*k)
    return 1/(2*h)-K*E/h**2 + K**2 * dn**2/h**2


# Window derivative and its exact frequency response.
for a in [mp.mpf('0.7'),mp.mpf('1.3'),mp.mpf('3.5')]:
    for w in [mp.mpf('0.4'),mp.mpf('1.1'),mp.mpf('2.8')]:
        F = mp.quad(lambda t: a*mp.exp(-a*t)*(1-a*t)*mp.exp(-1j*w*t),[0, mp.inf])
        closed=1j*a*w/(a+1j*w)**2
        assert_close(F,closed)
        assert_close(abs(closed)**2,mp.sech(mp.log(w/a))**2/4)

# Poisson and elliptic identities, including nontrivial interior points.
for h_str in ['0.55','0.9','1.5','2.7','4','7.2']:
    h=mp.mpf(h_str)
    for alpha in ['0','0.07','0.17','0.31','0.5','0.73','1']:
        t=h*mp.mpf(alpha)
        assert_close(p(h,t),p_fourier(h,t),rtol=mp.mpf('1e-29'))
        assert_close(p(h,t),p_elliptic(h,t),rtol=mp.mpf('1e-28'))
    for j in range(1,50):
        t=h*j/100
        if p(h,t)<=p(h,t+h/200):
            raise AssertionError(('not decreasing',h,t))
        CHECKS+=1

# Exact strict global-bound comparisons have explicit pointwise witnesses.
for h_str in ['0.6','1','2','3.5','6','10']:
    h=mp.mpf(h_str)
    L=h/2
    amin=p(L,L/2); bmax=p(L,0)
    assert_close(amin,2*p(h,h/4))
    assert_close(bmax,p(h,0)+p(h,h/2))
    for theta_str in ['0','0.03','0.125','0.25','0.375','0.49']:
        theta=mp.mpf(theta_str)
        lower_probe=2*p(h,(1-theta)*h/2)
        upper_probe=p(h,0)+p(h,theta*h)
        if lower_probe>=amin or upper_probe<=bmax:
            raise AssertionError(('stagger witness failure',h,theta,lower_probe,amin,upper_probe,bmax))
        CHECKS += 2

# Wide-scale asymptotic (sparse geometric scales).
for h_str in ['11','14','17']:
    h=mp.mpf(h_str); L=h/2
    r=p(L,0)/p(L,L/2)
    rel=r/(mp.exp(h/2)/8)
    if abs(rel-1)>mp.mpf('0.04'):
        raise AssertionError(('sparse ratio',h,rel))
    CHECKS+=1

# High-density asymptotic (the first exponentially small Fourier harmonic).
for h_str in ['0.9','0.75','0.65']:
    h=mp.mpf(h_str); L=h/2
    r=p(L,0)/p(L,L/2)
    lead=(16*mp.pi**2/h)*mp.exp(-2*mp.pi**2/h)
    if abs((r-1)/lead-1)>mp.mpf('0.0001'):
        raise AssertionError(('dense ratio',h,mp.nstr((r-1)/lead,20)))
    CHECKS+=1

print('CAUSAL_STAGGERED_WAVELET_CHECKS_PASSED',CHECKS)
