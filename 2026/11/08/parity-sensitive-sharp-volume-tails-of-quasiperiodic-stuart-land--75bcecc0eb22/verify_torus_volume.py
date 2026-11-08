#!/usr/bin/env python3
"""Self-contained numerical checks for intrinsic volumes of quasiperiodic product tori."""
import math
import random


def even_upper_constant(n):
    return (math.factorial(n - 1) / math.sqrt(n)
            * (2 / n) ** (n - 1)
            * math.pi ** ((n - 1) / 2)
            / math.gamma((n + 1) / 2))


def odd_upper_constant(n):
    return (math.gamma(n + .5) / math.sqrt(n)
            * (2 / n) ** (n - .5)
            * math.pi ** ((n - 1) / 2)
            / math.gamma(n / 2 + 1))


def exact_moment(n, odd, s):
    alpha = .5 if odd else 0.
    return math.exp(n*s/2*math.log(n) + math.lgamma(n+alpha)
                    + n*math.lgamma(1+s/2)
                    - math.lgamma(n+alpha+n*s/2))


def beta_product_moment(n, odd, s):
    bs = ([(k + .5)/n for k in range(n)] if odd else
          [k/n for k in range(1, n)])
    return math.exp(sum(math.lgamma(1+s) + math.lgamma(1+b)
                        -math.lgamma(1+b+s) for b in bs))


def sample_volume(n, odd, rng):
    # Chi-square(2) modal energies are Exponential(1).
    energies = [rng.expovariate(1) for _ in range(n)]
    if odd:
        energies.append(rng.gauss(0, 1)**2 / 2)
    total = sum(energies)
    return math.exp((n*math.log(n)+sum(math.log(v / total) for v in energies[:n]))/2)


def run():
    # N=2 even has the explicit exact law R=2 sqrt(U(1-U)).
    assert abs(even_upper_constant(2)-math.sqrt(2)) < 1e-12
    assert abs(odd_upper_constant(2)-3*math.pi*math.sqrt(2)/8) < 1e-12
    assert abs(even_upper_constant(3)-8*math.pi/(9*math.sqrt(3))) < 1e-12
    for n in (3, 4, 5):
        assert even_upper_constant(n) > 0
        assert odd_upper_constant(n) > 0
        for odd in (False, True):
            assert abs(exact_moment(n, odd, 0)-1) < 1e-12
            for s in (.2, .5, 1, 2, 3):
                # The gamma multiplication identity underlying the beta factorization.
                assert abs(exact_moment(n, odd, 2*s)-beta_product_moment(n, odd, s)) < 1e-12
            # The product-torus volume is a bounded normalized random variable.
            for s in (.5, 1, 2, 3):
                assert 0 < exact_moment(n, odd, s) < 1
    rng = random.Random(20090425)
    for n, odd in ((3,False),(3,True),(4,False),(4,True)):
        samples = [sample_volume(n, odd, rng) for _ in range(60000)]
        mean = sum(samples)/len(samples)
        predicted=exact_moment(n,odd,1)
        assert abs(mean-predicted) < .013, (n,odd,mean,predicted)
        t=.12
        empirical=sum(v>1-t for v in samples)/len(samples)
        upper_const=(odd_upper_constant(n) if odd else even_upper_constant(n))
        exponent=(n/2 if odd else (n-1)/2)
        approximation=upper_const*t**exponent
        # At a finite, not asymptotically small, t a relative discrepancy is expected.
        assert abs(empirical - approximation) < .08, (n,odd,empirical,approximation)
        print('TORUS_VOLUME_MOMENT_AND_ENDPOINT_SPOTCHECK_OK',n,'odd' if odd else 'even',
              f'mean={mean:.7f}', f'theory={predicted:.7f}',
              f'survival={empirical:.7f}',f'leading={approximation:.7f}')
    print('TORUS_VOLUME_CHECK_OK')

if __name__ == '__main__':
    run()
