"""Reproduce the exact one-bit occupation quadrature identities (Python 3 + mpmath)."""
import random
import mpmath as mp

mp.mp.dps = 40

def kval(a):
    a = mp.mpf(a)
    if abs(a) < mp.mpf('1e-8'):
        return (mp.mpf(4)/3 - 2*a*a/5 - a**4/14 - a**6/36)
    return (mp.asin(a)-a*(1-2*a*a)*mp.sqrt(1-a*a))/(2*a**3)

def opt(a):
    k = kval(a)
    return 1/(a*a+k*k)

def fclosed(x, a):
    k = kval(a)
    return (mp.asin(a*mp.sqrt(x))
            + a*mp.sqrt(x*(1-a*a*x))
            - a*k*x)

def fdirect(x, a):
    left = mp.quad(lambda t: mp.asin(a*mp.sqrt(t/x)), [0,x])
    right = mp.quad(lambda t: mp.asin(a*mp.sqrt(x/t)), [x,1])
    return left+right

def risk(x, a):
    return mp.mpf(1)/8-(fclosed(x,a)/mp.pi)**2

rng = random.Random(170603418)
alphas = [mp.mpf(s) for s in ('0.005','0.03','0.1','0.25','0.5','0.75','0.93','1')]
maxdiff = mp.mpf(0)
for a in alphas:
    k = kval(a)
    x = opt(a)
    assert 0 < x < 1
    assert k > 0
    assert a*mp.sqrt(1-a*a) < a*k  # derivative at right endpoint negative
    fstar = mp.atan(a/k)
    assert abs(fclosed(x,a)-fstar) < mp.mpf('1e-35')
    d = mp.diff(lambda y:fclosed(y,a),x)
    assert abs(d) < mp.mpf('1e-34')
    for yy in [x,mp.mpf('0.15'),mp.mpf('0.5'),mp.mpf('0.9')]:
        e = abs(fdirect(yy,a)-fclosed(yy,a))
        maxdiff = max(maxdiff,e)
        assert e < mp.mpf('1e-32'), (a,yy,e)
    for _ in range(300):
        yy = mp.mpf(rng.random())
        assert risk(yy,a) >= risk(x,a)-mp.mpf('1e-35')

xzero = mp.mpf(16)/(16+mp.pi**2)
rzero = mp.mpf(1)/8 - (mp.atan(4/mp.pi)/mp.pi)**2
assert abs(opt(mp.mpf(1))-xzero)<mp.mpf('1e-38')
assert abs(risk(xzero,1)-rzero)<mp.mpf('1e-38')
assert abs(opt(mp.mpf('1e-5'))-mp.mpf(9)/16)<mp.mpf('3e-12')
assert abs(risk(opt(mp.mpf('1e-5')),mp.mpf('1e-5'))-mp.mpf(1)/8)<mp.mpf('1e-11')
print('PASS: exact optimizing times, endpoint signs, closed/direct covariance integrals')
print('PASS: 2400 random global-risk comparisons; 8 parameter values; 32 direct integrals')
print('max integral residual:', mp.nstr(maxdiff,9))
print('noiseless optimum:',mp.nstr(xzero,25))
print('noiseless Bayes risk:',mp.nstr(rzero,25))
print('noiseless explained variance:',mp.nstr(1-rzero/(mp.mpf(1)/8),18))
