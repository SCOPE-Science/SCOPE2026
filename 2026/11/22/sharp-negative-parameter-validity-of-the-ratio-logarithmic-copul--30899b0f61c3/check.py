"""Reproducible high-precision diagnostics for the ratio-logarithmic copula theorem.
Run: python check.py  (dependency: mpmath, version 1.3 or later).
The continuum-wide inequalities are proved analytically in RESULT.md; grids are diagnostic only.
"""
import mpmath as mp
mp.mp.dps = 70
N = 0

def check(cond, msg):
    global N
    N += 1
    if not cond:
        raise AssertionError(msg)

def a(w):
    return mp.expm1(w) / w if w else mp.mpf(1)

def aprime(w):
    return ((w - 1) * mp.exp(w) + 1) / (w * w) if w else mp.mpf('0.5')

def h(w):
    return mp.expm1(w) * aprime(w)

w_star = mp.findroot(lambda w: h(w) - 1, (mp.mpf('0.7'),mp.mpf('0.9')))
t_star = -mp.expm1(-w_star)
check(mp.mpf('0.53981499794399050') < t_star < mp.mpf('0.53981499794399053'), 'critical t bracket')
check(h(mp.log(2)) < 1 < h(mp.log(mp.mpf(5)/2)), 'half-range and upper bracket')
check(abs(h(w_star)-1) < mp.mpf('1e-65'), 'critical equation')


def C(alpha,x,y):
    if x == 0 or y == 0:
        return mp.mpf(0)
    if alpha == 0:
        return x*y
    # stable at small alpha via analytic log1p; all test values nonzero and in real domain
    return x*y*mp.log1p(alpha*x)*mp.log1p(alpha*y)/(mp.log1p(alpha)*mp.log1p(alpha*x*y))

def g_and_qgp(alpha,z):
    # d/dz log( log(1+alpha*z)/(alpha*z) ) * z
    # stable for the nonzero diagnostic nodes used below
    u=alpha*z
    L=mp.log1p(u)
    ratio=u/((1+u)*L)
    g=ratio-1
    # derivative of u / ((1+u)*log(1+u)) with respect to u
    ugp=u*(L-u)/((1+u)**2*L**2)
    return g,ugp

def closed_density(alpha,x,y):
    if alpha == 0:
        return mp.mpf(1)
    q=x*y
    gx,_=g_and_qgp(alpha,x)
    gy,_=g_and_qgp(alpha,y)
    gq,qgp=g_and_qgp(alpha,q)
    return C(alpha,x,y)/(x*y)*((1+gx-gq)*(1+gy-gq)-qgp)

for alpha in [-mp.mpf('.2'), -mp.mpf('.5'), -t_star, -mp.mpf('.54'), -mp.mpf('.7'), mp.mpf('.4'),mp.mpf('2')]:
    for x,y in [(mp.mpf('0.13'),mp.mpf('0.29')), (mp.mpf('.5'),mp.mpf('.6')),(mp.mpf('.83'),mp.mpf('.91')), (mp.mpf('.99'),mp.mpf('.995'))]:
        check(abs(C(alpha,x,1)-x) < mp.mpf('1e-60'), 'first margin')
        check(abs(C(alpha,1,y)-y) < mp.mpf('1e-60'), 'second margin')
        # Derivative computed two ways: symbolic log differentiation vs independent numerical differentiation
        d=mp.diff(lambda xx,yy:C(alpha,xx,yy), (x,y), (1,1))
        check(abs(d-closed_density(alpha,x,y)) < mp.mpf('1e-55'), 'density identity')
        if alpha >= -t_star:
            check(closed_density(alpha,x,y)>0, 'admissible interior density')

for t in [mp.mpf('.50'), t_star,mp.mpf('.54'),mp.mpf('.60')]:
    alpha=-t
    _,g1=g_and_qgp(alpha,mp.mpf(1))
    d=closed_density(alpha,mp.mpf(1),mp.mpf(1))
    check(abs(d-(1-g1))<mp.mpf('1e-60'),'corner criterion')
    check(abs(d-(1-h(-mp.log1p(-t))))<mp.mpf('1e-60'),'corner exponential formula')
    if t>t_star:
        check(d<0,'failure beyond threshold')

for t in [mp.mpf('.5'),t_star, mp.mpf('.6')]:
    for x,y in [(mp.mpf('.25'),mp.mpf('.9')),(mp.mpf('.8'),mp.mpf('.9')),(mp.mpf('.99'),mp.mpf('.99'))]:
        gx,_=g_and_qgp(-t,x); gy,_=g_and_qgp(-t,y); gq,qgp=g_and_qgp(-t,x*y)
        check(gx>=gq and gy>=gq, 'increasing log-derivative')
        check(qgp<=h(-mp.log1p(-t)), 'sharp uniform control')

print('PASS:',N,'high-precision checks')
print('critical s:',mp.nstr(w_star,55))
print('critical t:',mp.nstr(t_star,55))
print('critical alpha:',mp.nstr(-t_star,55))
print('h(log 2):',mp.nstr(h(mp.log(2)),40))
