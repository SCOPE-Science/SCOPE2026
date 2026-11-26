"""Finite checks of projection geometry and density asymptotics (Python 3, mpmath)."""
import mpmath as mp

mp.mp.dps = 65


def projection_geometry(R, c, s):
    assert mp.almosteq(c*c+s*s, 1)
    a, b = sorted((R*abs(c+s)/2, R*abs(c-s)/2), reverse=True)
    corners = sorted((R*c, -R*c, R*s, -R*s))
    low, high = a-b, a+b
    for u, v in zip(corners, (-high, -low, low, high)):
        assert mp.almosteq(u, v)
    assert mp.almosteq(mp.sqrt(low*low+high*high), R)
    return a, b


def density(z, a, b, beta):
    l, r = max(-1, (z-b)/a), min(1, (z+b)/a)
    if r <= l:
        return mp.mpf(0)

    def integrand(t):
        u = l+(r-l)*t
        v = (z-a*u)/b
        rad = (1-u*u)*(1-v*v)
        return rad**(beta-1) if rad > 0 and abs(u) < 1 and abs(v) < 1 else mp.mpf(0)

    return (r-l)*mp.quad(integrand, [0, mp.mpf('0.5'), 1])/(b*mp.beta(mp.mpf('0.5'), beta)**2)


if __name__ == '__main__':
    for R, c, s in [(mp.mpf(1), mp.mpf(4)/5, mp.mpf(3)/5),
                    (mp.mpf(3)/2, -mp.mpf(5)/13, mp.mpf(12)/13)]:
        a, b = projection_geometry(R, c, s)
        h, S = a-b, a+b
        eps = b*mp.mpf('1e-6')
        for beta in (mp.mpf('0.2'), mp.mpf('0.3')):
            scale = 2**(2*beta-2)/((a*b)**beta*mp.beta(mp.mpf('0.5'), beta)**2)
            co = scale*mp.beta(beta, beta)
            ci = scale*mp.beta(beta, 1-2*beta)
            assert mp.almosteq(ci/co, 1/(2*mp.cos(mp.pi*beta)))
            for z, coefficient in ((S-eps, co), (-S+eps, co),
                                   (h+eps, ci), (h-eps, ci),
                                   (-h+eps, ci), (-h-eps, ci)):
                numerical = density(z, a, b, beta)*eps**(1-2*beta)
                assert abs(numerical/coefficient-1) < mp.mpf('0.01')
        beta = mp.mpf('0.5')
        critical_outer = 1/(2*mp.pi*mp.sqrt(a*b))
        assert abs(density(S-eps,a,b,beta)/critical_outer-1) < mp.mpf('1e-5')
        for sign in (-1, 1):
            slope = (density(h+sign*eps/10,a,b,beta)-density(h+sign*eps,a,b,beta))/mp.log(10)
            assert abs(slope*2*mp.pi**2*mp.sqrt(a*b)-1) < mp.mpf('1e-4')
    print('PASS: two physical projection geometries, four Beta-ratio checks, 24 subcritical density checks, six critical checks')
