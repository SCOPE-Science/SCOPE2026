#!/usr/bin/env python3
"""Independent quadrature and algebra checks for the synchronous-reset age-information law.

Scientific scope: finite computational tests support, but do not replace, the
analytic all-N monotonicity and asymptotic proof in RESULT.md.
"""
import math
from scipy.integrate import quad
from scipy.special import digamma, gammaln, kve

EULER = 0.5772156649015328606065120900824

def log_density(v, k):
    # This is the log of the exact density of log(A*G), A~Exp(1), G~Gamma(k,1).
    z = 2.0 * math.exp(v / 2.0)
    bessel_scaled = kve(k - 1.0, z)
    if not math.isfinite(bessel_scaled) or bessel_scaled <= 0.0:
        return -math.inf
    return (math.log(2.0) - gammaln(k) + (k + 1.0) * v / 2.0
            + math.log(bessel_scaled) - z)

def integrate_density(k, entropy=False):
    center = math.log(k)
    def integrand(v):
        lp = log_density(v, k)
        if lp <= -700.0:
            return 0.0
        density = math.exp(lp)
        return -density * lp if entropy else density
    return quad(integrand, center - 120.0, center + 12.0,
                points=[center-10.0, center, center+3.0],
                epsabs=2.0e-10, epsrel=2.0e-10, limit=600)[0]

def log_gamma_entropy(k):
    return gammaln(k) - k * digamma(k) + k

def information(n):
    k = n / 2.0
    return integrate_density(k, entropy=True) - log_gamma_entropy(k)

def large_n_approx(n):
    return (math.log(n) / 2.0 + 1.0 + EULER
            - math.log(4.0 * math.pi * math.e) / 2.0
            + 2.0 / (3.0 * n))

def posterior_density_t(t, z, k):
    # Unnormalized density of latent dimensionless age, expressed in log-age.
    # It integrates to 1 because p(t|z)dt = p(exp(v)|z)exp(v)dv.
    v = math.log(t)
    return math.exp((1.0-k)*v - t - z/t)

def main():
    checks=0
    for n in (1,2,3,4,6,10,20,40,80,160):
        k=n/2.0
        z=integrate_density(k)
        assert abs(z-1.0)<1e-6, (n,z)
        checks+=1
    values=[]
    for n in range(1,25):
        val=information(n)
        assert val>0.0
        if values: assert val > values[-1]
        values.append(val)
        checks+=2
    exact_one=(1.0+EULER-math.log(math.pi))/2.0
    assert abs(values[0]-exact_one)<3e-9, (values[0],exact_one)
    checks+=1
    for n,reference in [(2,0.38807484224635425),(10,1.0197271942710366),
                        (20,1.3398330917847792),(80,2.0108126721844832)]:
        assert abs(information(n)-reference)<2e-7
        checks+=1
    for n in (40,80,160):
        error=information(n)-large_n_approx(n)
        # This finite check compares with an analytic asymptotic, not an infinite proof.
        assert abs(error)<0.4 / n, (n,error)
        checks+=1
    # Check a posterior normalization independently in log-age coordinates.
    from scipy.special import kv
    for k in (0.5,1.0,2.0,6.0):
        for z in (0.2,1.0,3.0):
            normalizer=2.0*z**((1-k)/2.0)*kv(1-k,2*math.sqrt(z))
            got=quad(lambda w: math.exp((1.0-k)*w-math.exp(w)-z*math.exp(-w)),
                     -45,20,epsabs=1e-11,epsrel=1e-11,limit=250)[0]
            assert abs(got/normalizer-1.0)<2e-9, (k,z,got,normalizer)
            checks+=1
    print('PASS:',checks,'normalization, posterior, monotonicity, entropy and asymptotic tests')
    print('I_1=',values[0],'; I_2=',values[1],'; I_10=',information(10),'; I_80=',information(80))
    print('Large-N comparison (exact vs expansion):')
    for n in (40,80,160): print(n,information(n),large_n_approx(n))

if __name__=='__main__':
    main()
