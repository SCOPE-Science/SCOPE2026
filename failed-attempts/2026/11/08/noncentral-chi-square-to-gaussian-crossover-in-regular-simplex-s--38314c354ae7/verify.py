"""Reproducible checks for the noncentral regular-simplex section face law.

Python standard library only. The finite Monte Carlo checks are not proofs of
convergence; exact geometric identities and analytical limits are proved in RESULT.md.
"""
import itertools
import math
import random
from statistics import fmean

SEED = 20261101
rng = random.Random(SEED)
PHI0 = 1 / math.sqrt(2 * math.pi)
SIGMA0_SQ = 0.25 - PHI0 ** 2


def binom(n, k):
    return math.comb(n, k) if 0 <= k <= n else 0


def face_count(n, plus_count, dimension):
    r = dimension + 2
    return binom(n, r) - binom(plus_count, r) - binom(n - plus_count, r)


def direct_face_count(signs, dimension):
    # A section face corresponds to a simplex face spanning both halfspaces.
    return sum(any(signs[i] > 0 for i in inds) and
               any(signs[i] < 0 for i in inds)
               for inds in itertools.combinations(range(len(signs)), dimension + 2))


def projected_counts(n, t, rng):
    g = [rng.gauss(0, 1) for _ in range(n)]
    mean = sum(g) / n
    sd = math.sqrt(sum((x - mean) ** 2 for x in g) / n)
    # ||g-mean|| = sqrt(n) * sd; U is Haar on the zero-sum sphere.
    # Hyperplane <U,x-centroid> = t: U_i>t iff g_i>mean+t*sqrt(n)*sd.
    k = sum(x > mean + t * math.sqrt(n) * sd for x in g)
    return k


def empirical_stats(values):
    m = fmean(values)
    v = fmean([(x - m)**2 for x in values])
    return m, v


def variance(c):
    p = 0.5 * math.erfc(c / math.sqrt(2))
    phi = math.exp(-c*c/2) / math.sqrt(2*math.pi)
    return p*(1-p) - phi*phi*(1+c*c/2)


def run():
    assert abs(SIGMA0_SQ - 0.0908450569) < 1e-8
    # Exhaustive finite sign checks; this checks all face dimensions, not only vertices.
    for n in range(4, 9):
        for bits in itertools.product((-1, 1), repeat=n):
            k = sum(b > 0 for b in bits)
            for j in range(n-2):
                assert direct_face_count(bits, j) == face_count(n, k, j)
                assert face_count(n, k, j) <= face_count(n, n//2, j)
            assert face_count(n, k, 0) == k*(n-k)
    print('EXACT_FACE_COUNT_AND_BALANCE_CHECKS_PASSED')

    n, trials = 800, 3600
    # Check the critical near-centroid distribution at two distinct offsets.
    for h in (0.0, 1.5):
        vals = [(projected_counts(n, h/n, rng) - n/2) / math.sqrt(n)
                for _ in range(trials)]
        m, v = empirical_stats(vals)
        target = -PHI0 * h
        assert abs(m - target) < 0.043, (h, m, target)
        assert abs(v - SIGMA0_SQ) < 0.014, (h, v, SIGMA0_SQ)
        # The deficit is exactly the square of this normalized imbalance.
        deficits = [x*x for x in vals]
        assert abs(fmean(deficits) - (SIGMA0_SQ + target*target)) < 0.07
        print('CRITICAL_OFFSET', h, 'imbalance mean', round(m, 5),
              'variance', round(v, 5), 'deficit mean', round(fmean(deficits), 5))

    # Noncentral fixed-distance/sqrt(n) branch uses the variance after estimating
    # the Gaussian mean and standard deviation from the same sample.
    c = 0.85
    p = 0.5 * math.erfc(c/math.sqrt(2))
    vals = [(projected_counts(n, c/math.sqrt(n), rng) - n*p)/math.sqrt(n)
            for _ in range(trials)]
    m, v = empirical_stats(vals)
    assert abs(m) < 0.06, m
    assert abs(v - variance(c)) < 0.012, (v, variance(c))
    print('FIXED_SCALED_OFFSET', c, 'count mean', round(m, 5),
          'variance', round(v, 5), 'predicted', round(variance(c), 5))

    # Uniform asymptotic quadratic/linear coefficients of all fixed face ranks.
    for j in range(5):
        r = j + 2
        for n in (400, 900, 1800):
            center = face_count(n, n//2, j)
            k = n//2 + int(math.sqrt(n)*1.3)
            deficit = (center - face_count(n, k, j)) / n**(j+1)
            predicted = 1.3**2/(2**j*math.factorial(j))
            assert abs(deficit - predicted) < 0.12 + 2.0/math.sqrt(n), (j,n,deficit,predicted)
    print('ALL_NONCENTRAL_SIMPLEX_SECTION_CHECKS_PASSED')


if __name__ == '__main__':
    run()
