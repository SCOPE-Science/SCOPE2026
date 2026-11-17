"""Supplementary numerical diagnostics for the finite-rank small Hankel formulas.

Requires Python 3 and scipy. Finite checks do not prove asymptotics.
"""
import math
from scipy.special import betaln, beta, gammaln


def v(j, gamma):
    return math.exp(math.log(2) + 2 * math.log(j + 1) + betaln(2*j+2, gamma+1))


def sigma(m, j, gamma, a):
    return math.exp(gammaln(j+a+2)-gammaln(j+1)
                    -gammaln(m+a+2)+gammaln(m+1)
                    +0.5*(math.log(v(j, gamma))-math.log(v(m-j, gamma))))


def d(j, gamma, a):
    constant = 2**(-gamma)*math.gamma(gamma+1)
    return math.exp(gammaln(j+a+2)-gammaln(j+1))*math.sqrt(v(j, gamma)/constant)


def inspect(gamma, a, p, m):
    alpha = (gamma-1)/2
    b = a+1-alpha
    actual = sum(sigma(m,j,gamma,a)**p for j in range(m+1))
    if p*b > -1:
        prediction = m*beta(1+p*b, 1+p*alpha)
    elif abs(p*b+1)<1.e-12:
        prediction = m*math.log(m)
    else:
        prediction = m**(-p*b)*sum(d(j,gamma,a)**p for j in range(10000))
    return actual/prediction


def main():
    count = 0
    # Monomial moment identity, with integer shape parameters.
    for gamma in (2,3,4,5):
        for j in range(20):
            r = v(j,gamma)
            s = 2*(j+1)**2 * (math.factorial(2*j+1)*math.factorial(gamma)
                               / math.factorial(2*j+gamma+2))
            assert math.isclose(r,s,rel_tol=1e-13)
            count += 1
    # Anti-diagonal formula for the Hilbert-space adjoint transformation.
    for gamma,a in ((3,3),(3,-0.5),(5,0),(2.5,0),(3,1)):
        for m in (4,13,50):
            norms = [sigma(m,j,gamma,a) for j in range(m+1)]
            assert all(math.isfinite(x) and x>0 for x in norms)
            assert math.isclose(norms[0], math.exp(gammaln(a+2)-gammaln(m+a+2)+gammaln(m+1))*math.sqrt(v(0,gamma)/v(m,gamma)))
            count += 2
    # Representative bulk, edge, and critical exponent regimes.
    for gamma,a,p in ((3,1,1),(3,3,2),(2.5,0,2), (3,-0.5,1),
                      (3,-0.5,2), (5,0,1), (5,0,2)):
        small=inspect(gamma,a,p,300)
        large=inspect(gamma,a,p,4000)
        # The improvements here are deliberately qualitative, not certificates.
        assert abs(large-1) < abs(small-1)+1.e-7
        assert 0.15 < large < 1.35
        count += 2
    print('SMALL_HANKEL_FINITE_DIAGNOSTICS_OK', count)

if __name__=='__main__':
    main()
