"""Independent finite checks for exact bridge-barrier observation formulas.

Requires mpmath. All proofs and validity limits are in RESULT.md.
"""
import mpmath as mp
mp.mp.dps = 95


def phi_cdf(y):
    return mp.erfc(-y / mp.sqrt(2)) / 2


def second_moment(t, h):
    t, h = mp.mpf(t), mp.mpf(h)
    v = t * (1 - t)
    co = [(2*h/t, 1), (2*h/(1-t), 1), (2*h/v, -1)]
    ans = phi_cdf(-h/mp.sqrt(v))
    for c, s in co:
        for d, r in co:
            k = c+d
            ans += s*r*mp.exp(-k*h + k*k*v/2)*phi_cdf((h-k*v)/mp.sqrt(v))
    return ans


def posterior(y, t, h):
    if y >= h:
        return mp.mpf(1)
    l = mp.exp(-2*h*(h-y)/t)
    r = mp.exp(-2*h*(h-y)/(1-t))
    return l+r-l*r


def quadrature(t, h):
    t, h = mp.mpf(t), mp.mpf(h)
    v = t*(1-t)
    zden = lambda y: mp.exp(-y*y/(2*v))/mp.sqrt(2*mp.pi*v)
    return mp.quad(lambda y: zden(y)*posterior(y,t,h)**2,
                   [-mp.inf, 0, h, mp.inf])


def asymptotic(t, h):
    t, h = mp.mpf(t), mp.mpf(h)
    b, v = 1-t, t*(1-t)
    if t < mp.mpf('0.25'):
        return mp.exp(-4*h*h*(1-2*t)/b)
    if t == mp.mpf('0.25'):
        return mp.exp(-mp.mpf(8)*h*h/3)/2
    bracket = (mp.mpf(10)/3 + 1/(4*t-1) + 1/(4*b-1)
               - 2/(2*t+1) - 2/(2*b+1))
    return mp.sqrt(v)/(h*mp.sqrt(2*mp.pi))*bracket*mp.exp(-h*h/(2*v))


if __name__ == '__main__':
    cases = [(mp.mpf(t),mp.mpf(h)) for t in ['0.10','0.25','0.30','0.50'] for h in ['0.6','1.2']]
    for t, h in cases:
        exact = second_moment(t, h)
        integral = quadrature(t, h)
        assert mp.almosteq(exact, integral, rel_eps=mp.mpf('1e-65')),(t,h,exact,integral)
    print('8 exact-Gaussian-formula vs independent quadrature checks passed')

    for h in ['0.1','0.5','1.0','2.0','4.0']:
        h=mp.mpf(h)
        center = (5*phi_cdf(-2*h)-4*mp.exp(6*h*h)*phi_cdf(-4*h)
                  +mp.exp(16*h*h)*phi_cdf(-6*h))
        assert mp.almosteq(center,second_moment(mp.mpf('.5'),h),rel_eps=mp.mpf('1e-65'))
    print('5 exact midpoint identities passed')

    for t in ['0.10','0.25','0.30','0.45','0.50']:
        t=mp.mpf(t)
        r7=(second_moment(t,7)-mp.exp(-4*49))/asymptotic(t,7)
        r12=(second_moment(t,12)-mp.exp(-4*144))/asymptotic(t,12)
        assert abs(r12-1)<abs(r7-1)
        assert abs(r12-1)<mp.mpf('.10'),(t,r12)
        print('asymptotic',mp.nstr(t,4),'ratios',mp.nstr(r7,10),mp.nstr(r12,10))
    print('5 sharp rare-barrier asymptotic trend checks passed')
