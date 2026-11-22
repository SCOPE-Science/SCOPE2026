"""Numerical checks for annealed telegraph first passage (requires SciPy)."""
import math
from scipy.integrate import quad
from scipy.special import erfcx


def q0(L, v, lam):
    b = lam * L / v
    return (2 + b) / (2 * (1 + b))


def laplace(s, L=1., v=1., lam=1.):
    if s == 0:
        return q0(L, v, lam)
    c = L / (2 * v)
    h = math.sqrt(s * lam)

    def f(d):
        z = (d + 2 * s * (1 + c * lam)) / (2 * h)
        return math.exp(-d / lam) / lam * (1 + math.exp(-2 * c * d)) / 2 * (1 - c * math.sqrt(math.pi) * h * erfcx(z))

    return math.exp(-2 * c * s) * quad(f, 0, math.inf, epsabs=1e-13, epsrel=2e-12, limit=250)[0]


def independent_laplace(s, L=1., v=1., lam=1.):
    """Two independent exponential-rate integrals; no erfc formula used."""
    c = L / (2 * v)

    def f(d):
        def g(u):
            root = math.sqrt(d * d + 4 * s * (s + d + lam * u))
            return math.exp(-u - c * root)
        return math.exp(-d / lam) / lam * math.cosh(c * d) * quad(g, 0, 50, epsabs=3e-11, limit=120)[0]

    # cosh(c*d)*exp(-d/lam) can overflow at huge d, so integrate to finite
    # 55 lam; the positive tail is smaller than 2e-24 for these settings.
    return quad(f, 0, 50 * lam, epsabs=2e-10, limit=220)[0]


def run():
    checks=0
    for L,v,lam in ((1.,1.,1.),(2.,3.,.7),(.6,1.4,2.)):
        b=lam * L / v
        c=L / (2*v)
        p0=q0(L,v,lam)
        assert abs(p0-(2+b)/(2*(1+b)))<1e-14
        checks+=1
        for r in (.1,.7,2.):
            p=laplace(r,L,v,lam)
            q=independent_laplace(r,L,v,lam)
            assert abs(p-q) < 6e-9,(L,v,lam,r,p,q)
            assert 0<p<p0<1
            t=(1-p)/(r*p)
            assert t>0
            checks+=3
        ratio=(p0-laplace(lam*1e-7,L,v,lam))/(c*lam*1e-7*math.log(1e7))
        assert 0.975<ratio<1.06,(L,v,lam,ratio)
        checks+=1
        r=lam*200
        actual=laplace(r,L,v,lam)
        expected=math.exp(-r*L/v)/(1+b)
        if expected>1e-250:
            assert abs(actual/expected-1)<.035,(L,v,lam,actual/expected)
            checks+=1
    # One illustrative model: three widely separated rate choices.
    assert laplace(.00001) < q0(1.,1.,1.)
    vals=[(1-laplace(r))/(r*laplace(r)) for r in (.01,.6,10.)]
    assert vals[0]>vals[1] and vals[2]>vals[1]
    checks+=3
    print('PASS:',checks,'quadrature, limit, renewal and asymptotic checks')

if __name__=='__main__':run()
