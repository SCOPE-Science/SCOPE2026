"""Independent numerical checks for a normalized Laplace-kernel Markov operator.
Uses only Python's standard library. Numerical experiments supplement an analytic proof.
"""
from math import exp, expm1, isclose


def kernel_mean(x, length, rate):
    left, right = x, length - x
    def e1(u):
        z = rate * u
        return -expm1(-z) / rate
    def e2(u):
        z = rate * u
        return (1 - (1 + z) * exp(-z)) / (rate * rate)
    return x + (e2(right) - e2(left)) / (e1(left) + e1(right))


def local_gain(x, length, rate):
    a, b = x, length - x
    L = -expm1(-rate * a)
    R = -expm1(-rate * b)
    if not L or not R:
        return 0.0
    def trunc_mean(d):
        return 1 / rate - d / expm1(rate * d)
    return 2 * rate * L * R / ((L + R)**2) * (trunc_mean(a) + trunc_mean(b))


def optimal_gain(length, rate):
    z = rate * length / 2
    return 1 - z / expm1(z)


def mean_quad(x, length, rate, N=10000):
    # Composite midpoint quadrature, independent of analytic integral expressions.
    step = length / N
    total = weighted = 0.0
    for j in range(N):
        y = (j + 0.5) * step
        w = exp(-rate * abs(x - y))
        total += w
        weighted += y * w
    return weighted / total


def run():
    count = 0
    for length in (0.4, 1.0, 2.5):
        for rate in (0.2, 0.7, 2.1, 5.5):
            q = optimal_gain(length, rate)
            assert 0 < q < 1
            assert abs(local_gain(length/2, length, rate) - q) < 3e-13
            count += 2
            for j in range(1,100):
                x=length*j/100
                g=local_gain(x,length,rate)
                assert 0 <= g <= q+2e-13, (length,rate,x,g,q)
                assert abs(g - local_gain(length-x,length,rate)) < 3e-13
                count += 2
            # independent finite differences from directly summed kernel quadrature
            for j in (10,30,50,70,90):
                x = length*j/100
                h = length*0.0001
                numeric = (mean_quad(x+h,length,rate,5000)-mean_quad(x-h,length,rate,5000))/(2*h)
                assert abs(numeric-local_gain(x,length,rate)) < 0.0015, (numeric,local_gain(x,length,rate))
                count += 1
            for j in (0,20,40,60,80,100):
                x = length*j/100
                assert abs(kernel_mean(x,length,rate)-mean_quad(x,length,rate,5000))<8e-7
                count += 1
    print(f'PASS {count} direct numerical and symmetry/bound assertions')

if __name__=='__main__':
    run()
