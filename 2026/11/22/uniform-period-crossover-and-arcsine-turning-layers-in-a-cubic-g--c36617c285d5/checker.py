"""Independent arithmetic and quadrature checks for an analytic period theorem.

Run with Python 3, no third-party dependencies. Numerical tests are not proofs
of uniformity or infinite-amplitude limits.
"""
import math
from fractions import Fraction


def norm_j(t, B, alpha, beta):
    """Exact-quadrature bracket J_A(t)/(1+alpha*A*A), A*A=B/beta."""
    m = 1.0 + alpha * B / beta
    c = alpha / (beta * m)
    u = -math.expm1(-t)
    if t < 0.0001:
        v = t * t * (0.5 - t / 3 + t * t / 8 - t ** 3 / 30)
    else:
        v = u - t * math.exp(-t)
    return u - c * v


def simpson(f, lo, hi, n=12000):
    assert n % 2 == 0
    step = (hi-lo) / n
    z = f(lo) + f(hi)
    for i in range(1, n):
        z += (4 if i % 2 else 2) * f(lo + i * step)
    return z * step / 3


def angle_kernel(theta, A, alpha, beta):
    B = beta * A * A
    if theta == 0:
        return 2.0 * math.sqrt(B)
    t = B * math.sin(theta)**2
    j = norm_j(t, B, alpha, beta)
    assert j > 0
    return 2 * B * math.sin(theta) * math.exp(-t / 2) / math.sqrt(j)


def I(A, alpha, beta, s=None):
    B = beta * A * A
    hi = math.pi / 2 if s is None else math.asin(math.sqrt(min(s, B) / B))
    return simpson(lambda th: angle_kernel(th, A, alpha, beta), 0, hi)


def T(A, alpha, beta):
    return 2 * I(A, alpha, beta) / (A * math.sqrt(beta) * math.sqrt(1+alpha*A*A))


def rational_energy_test():
    # Exact cancellation of Hdot/e^(beta*x*x) for the polynomial vector field.
    for xi in range(-4, 5):
        for yi in range(-3, 4):
            for a in (Fraction(0), Fraction(1,3), Fraction(5,2)):
                for b in (Fraction(1,4), Fraction(2)):
                    x, y = Fraction(xi,2), Fraction(yi,3)
                    yd = -x -a*x**3 - b*x*y*y
                    residual = b*x*y**3 + y*yd + x*(1+a*x*x)*y
                    assert residual == 0
                    # h'(q)=1+(beta+3alpha)*x*x+alpha*beta*x^4
                    left = (1+a*x*x)*(1+b*x*x) + 2*a*x*x
                    right = 1+(b+3*a)*x*x+a*b*x**4
                    assert left == right


def main():
    rational_energy_test()
    # Under z=sin(theta)^2 the beta(1/2,1/2) normalization is 2*dtheta.
    assert abs(simpson(lambda th: 2., 0., math.pi/2) - math.pi) < 1e-11
    for alpha in (0., 0.05, 1., 10., 10000.):
        t0 = T(.25,alpha,1)
        t1 = T(.5,alpha,1)
        t2 = T(1.,alpha,1)
        assert 0 < t2 < t1 < t0 < 2*math.pi
    for alpha in (0., .2, 1., 1e3):
        for A in (8., 12., 20.):
            ratio = I(A,alpha,1.) / math.pi
            assert 0.95 < ratio < 1.08, (alpha,A,ratio)
    for A in (8., 16.):
        for alpha in (0., 1., 1e3, 1/(A*A)):
            total = I(A,alpha,1.)
            for s in (.25,1.,2.,4.):
                observed = I(A,alpha,1.,s) / total
                predicted = 2 * math.asin(math.sqrt(-math.expm1(-s))) / math.pi
                assert abs(observed-predicted) < 0.045, (A,alpha,s,observed,predicted)
    # The crossover alpha=c/A^2 has normalized period A*sqrt(beta)*sqrt(1+c)*T -> 2pi.
    for c in (0., .3, 5., 100.):
        A=20.; a=c/(A*A)
        assert abs(A*math.sqrt(1+c)*T(A,a,1)/(2*math.pi)-1)<0.012
    print('CHECK_OK: exact algebra, finite-amplitude monotonic samples,')
    print('large-amplitude uniform grids, turning-layer CDF and crossover samples')

if __name__=='__main__':
    main()
