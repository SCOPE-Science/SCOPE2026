"""Numerical quadrature checks for stationary radial Fourier inversion.
Run with: python3 verify.py
Uses only Python's standard library. Tests are finite corroboration, not the proof.
"""
import math


def log_one_plus_exp(z):
    if z > 38:
        return z + math.log1p(math.exp(-z))
    if z < -38:
        return math.log1p(math.exp(z))
    return math.log1p(math.exp(z))


def radial_integral(dim, contraction, step=0.025):
    """Integral of k^(dim-1) times infinite-product characteristic function.
    Integrates on log k, truncating both frequency tails and product scales.
    """
    h = -math.log(contraction)
    upper = max(24.0, (dim / 2.0 + 4.0) * h + 15.0)
    lower = -24.0
    count = int(math.ceil((upper - lower) / step / 2)) * 2
    delta = (upper - lower) / count
    n_factors = max(35, int(math.ceil((upper + 15.0) / h)) + 5)
    def density_on_log_k(y):
        exponent = dim*y
        for j in range(n_factors):
            z = 2.0*(y - j*h)
            if z < -40:
                break
            exponent -= log_one_plus_exp(z)
        if exponent < -740:
            return 0.0
        return math.exp(exponent)
    total = density_on_log_k(lower) + density_on_log_k(upper)
    for j in range(1, count):
        total += (4 if j % 2 else 2) * density_on_log_k(lower + j*delta)
    return delta*total/3.0


def prefactor(dim):
    return math.exp(math.log(2) + (dim/2)*math.log(math.pi)
                    - math.lgamma(dim/2) - dim*math.log(2*math.pi))


def density_at_zero(dim, contraction, D=1., r=1.):
    return prefactor(dim) * (r/D)**(dim/2) * radial_integral(dim, contraction)


def close(actual, expected, tol, label):
    err = abs(actual/expected - 1)
    if err > tol:
        raise AssertionError('%s: got %.14g, expected %.14g, relative error %.5g > %.5g' %
                             (label, actual, expected, err, tol))
    return err


def main():
    checks = 0
    max_error = 0.
    for b in (0.1, 0.3, 0.65):
        measurements = {d: density_at_zero(d,b) for d in range(1,9)}
        exact_planar = -math.log(b)/(2*math.pi)
        max_error = max(max_error, close(measurements[2], exact_planar, 4e-7, 'planar b=%g'%b))
        checks += 1
        for d in range(1,7):
            predicted = ((b**(-d)-1)/(2*math.pi*d))*measurements[d]
            max_error = max(max_error, close(measurements[d+2], predicted, 4e-7,
                                             'dimension lift d=%d b=%g' % (d,b)))
            checks += 1
        for n in (2,3,4):
            even_formula = prefactor(2*n)*(-math.log(b))*math.prod(b**(-2*j)-1 for j in range(1,n))
            max_error = max(max_error, close(measurements[2*n], even_formula, 4e-7,
                                             'even closed form d=%d b=%g' % (2*n,b)))
            checks += 1
    for b in (0.01, 0.003):
        for d in (3,4,5,6):
            n = d//2
            asymptotic = prefactor(d) * (math.pi/2*b**(-n*n) if d%2
                                             else b**(-n*(n-1))*math.log(1/b))
            actual = density_at_zero(d,b)
            tolerance = 0.027 if b == 0.01 else 0.009
            max_error = max(max_error, close(actual, asymptotic, tolerance,
                                              'endpoint d=%d b=%g' % (d,b)))
            checks += 1
    print('PASS: %d deterministic quadrature identities/asymptotic comparisons.' % checks)
    print('Largest relative discrepancy including finite-b endpoint corrections: %.8g' % max_error)
    print('Quadrature checks do not constitute an infinite-dimensional proof.')

if __name__=='__main__':
    main()
