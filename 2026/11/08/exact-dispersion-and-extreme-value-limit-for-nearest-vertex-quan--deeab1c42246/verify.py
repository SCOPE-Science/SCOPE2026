"""Exact checks for the nearest-vertex distortion theorem of a regular simplex.

Run: python3 verify.py
Uses only the Python standard library. Simulations are illustrative, not proofs.
"""
from fractions import Fraction as F
from math import factorial, isclose, log, pi, sqrt
from random import Random


def harmonic(m, power=1):
    return sum((F(1, k**power) for k in range(1, m + 1)), F(0))


def raw_moments(m):
    h, h2 = harmonic(m), harmonic(m, 2)
    e_m = h / m
    e_m2 = (h*h + h2) / (m*(m+1))
    e_s = F(2, m+1)
    e_s2 = F(4*(m+5), (m+1)*(m+2)*(m+3))
    e_ms = 2*h/(m*(m+2)) + (h*h + h2)/(m*(m+1)*(m+2))
    return e_m, e_m2, e_s, e_s2, e_ms


def independent_ordered_simplex_cubic(m):
    """Integrate max(lambda)*sum(lambda_i**2) over ordered barycentric chamber.

    On that chamber, sorted lambda_j=sum(z_l/l for l>=j),
    where z is uniform on the standard (m-1)-simplex.
    Dirichlet monomial integration is exact.
    """
    den = m*(m+1)*(m+2)
    value = F(0)
    for a in range(1, m+1):
        for b in range(1, m+1):
            for c in range(1, m+1):
                occurrences = {}
                for index in (a,b,c):
                    occurrences[index] = occurrences.get(index, 0) + 1
                value += F(min(b,c)*__import__('math').prod(factorial(v) for v in occurrences.values()), a*b*c*den)
    return value


def exact_distortion(m):
    em, em2, es, es2, ems = raw_moments(m)
    k = F(m, m-1)
    mean = k*(1+es-2*em)
    variance = k*k*((es2-es*es) + 4*(em2-em*em) - 4*(ems-em*es))
    covariance = ems-em*es
    return mean, variance, covariance


def simulate(m, trials, seed):
    rng = Random(seed)
    sumq, sumq2 = 0.0, 0.0
    for _ in range(trials):
        y = [rng.expovariate(1.) for i in range(m)]
        total = sum(y)
        s = sum((a/total)**2 for a in y)
        mx = max(y)/total
        q = m/(m-1)*(1+s-2*mx)
        sumq += q
        sumq2 += q*q
    mean = sumq/trials
    variance = sumq2/trials - mean*mean
    return mean, variance


def main():
    tested = 0
    for m in range(2, 17):
        cross = independent_ordered_simplex_cubic(m)
        assert cross == raw_moments(m)[4], ('mixed moment mismatch', m)
        mean, var, cov = exact_distortion(m)
        assert F(0) < mean < 1 and var > 0 and cov > 0
        assert cov == (harmonic(m)**2+harmonic(m,2)-2*harmonic(m))/(m*(m+1)*(m+2))
        tested += 1
    assert exact_distortion(2)[:2] == (F(1,3),F(4,45))
    assert exact_distortion(3)[:2] == (F(5,12),F(43,720))
    monte = 0
    for m, count in [(3,70000),(6,70000),(13,70000)]:
        actual_mean, actual_var = simulate(m,count,seed=9341+m)
        predicted_mean, predicted_var, _ = exact_distortion(m)
        assert abs(actual_mean-float(predicted_mean)) < .01
        assert abs(actual_var-float(predicted_var)) < .005
        monte += count
    print(f'VERIFY_OK ordered_simplex_exact_cases={tested} exact_dim1=1 exact_dim2=1 sampled_points={monte} strict_positive_covariance_cases={tested}')

if __name__=='__main__':
    main()
