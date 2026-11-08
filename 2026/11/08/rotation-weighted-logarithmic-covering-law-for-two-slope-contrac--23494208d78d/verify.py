"""Finite corroboration of the analytic unequal-slope Sturmian atom bounds.

Only standard-library arithmetic; this does not prove infinite statements.
"""
import math


def check(la, mu, rho):
    assert 0 < la < 1 and 0 < la * mu < 1 and 0 < rho < 1
    chi = -(1-rho)*math.log(la)-rho*math.log(la*mu)
    assert chi > 0
    B = math.exp(abs(math.log(mu)))
    # The contraction factor depends on a block's number of high symbols.
    bits = [int(math.floor((j+1)*rho)-math.floor(j*rho)) for j in range(15000+25)]
    for n in range(1,17):
        words = {tuple(bits[j:j+n]) for j in range(15000)}
        assert len(words) == n+1, (n, len(words))
        for w in words:
            k = sum(w)
            assert abs(k-n*rho) < 1.00000001
            log_product = n*math.log(la)+k*math.log(mu)
            deviation = log_product+chi*n
            assert -abs(math.log(mu))-1.e-10 <= deviation <= abs(math.log(mu))+1.e-10
    # Canonical model f0(x)=la*x+delta, f1(x)=la*mu*(x-eta).
    # The delta formula comes from the cited two-interval rotation results.
    sigma = sum((math.floor((k+1)*rho)-math.floor(k*rho)) *
                (la**k)*(mu**math.floor(k*rho)) for k in range(1,300))
    delta = (1-la)*(1+mu*sigma)/(1+(mu-1)*sigma)
    eta = (1-delta)/la
    gap = delta-la*mu*(1-eta)
    assert 0 < eta < 1 and gap > 0
    print('PASS', 'slope0',la,'slope1',la*mu,'rho',round(rho,8),
          'chi',round(chi,8),'gap',round(gap,8))

if __name__ == '__main__':
    for la,mu in ((.8,.875),(.75,1.2)):
        for rho in ((math.sqrt(5)-1)/2, math.sqrt(2)-1):
            check(la,mu,rho)
    print('STURMIAN_TWO_SLOPE_LOG_COVERING_CHECKS_OK')
