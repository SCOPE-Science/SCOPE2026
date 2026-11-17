"""Standalone supplementary checks for the two-species double-Allee map.

Run: python3 verify.py
Only the Python standard library is required. Finite tests are diagnostic;
the statements for all trajectories are justified by the analytic proof.
"""
from fractions import Fraction
from math import exp, isfinite


def prey_growth(x, s, w):
    return (x - s) * (1 - x) / (x + w)


def iterate(x, y, s, w, alpha, beta, theta):
    return (x * exp(prey_growth(x, s, w) - y / (1 + alpha * x)),
            y * exp(beta * x / (1 + alpha * x) - theta))


def rational_checks():
    count = 0
    for s in [Fraction(1, 7), Fraction(1, 4), Fraction(3, 5)]:
        for w in [Fraction(1, 5), Fraction(2, 3)]:
            for alpha in [Fraction(1, 2), Fraction(3, 2)]:
                theta = Fraction(2, 5)
                a = (1 - s) / (1 + w)
                b = 1 / (1 + alpha)
                k = theta / (1 + alpha)
                h = b / a
                assert h * (a * (1 + alpha) ** 2 / theta) == (1 + alpha) / theta
                assert k * h * (a * (1 + alpha) ** 2 / theta) == 1
                for x in [Fraction(1, 10), Fraction(2, 5), Fraction(4, 5)]:
                    # Exact derivative of the prey exponent.
                    dg = -1 + (s + w) * (1 + w) / (x + w) ** 2
                    num = (1 + s - 2*x)*(x + w) - (x - s)*(1 - x)
                    assert dg == num/(x+w)**2
                    assert 1 + x * dg > 0
                    count += 1
    return count


def critical_cases():
    cases = [(0.2, 0.5, 1.0, 0.4), (0.1, 0.2, 2.0, 0.8), (0.6, 3.0, 0.3, 0.25)]
    for s, w, alpha, theta in cases:
        beta = theta * (1 + alpha)
        x, y = 0.95, 0.02
        for n in range(1, 250001):
            x, y = iterate(x, y, s, w, alpha, beta, theta)
            assert 0 < x <= 1 and 0 < y and isfinite(x+y)
        target_x = (1 + alpha) / theta
        target_y = (1 - s) * (1 + alpha)**2 / ((1 + w) * theta)
        assert abs(n * (1-x)/target_x-1) < 0.003, (s,w,n*(1-x),target_x)
        assert abs(n*y/target_y-1) < 0.003, (s,w,n*y,target_y)
        print(f'critical s={s} w={w}: n(1-x)={n*(1-x):.8f} target={target_x:.8f}; '
              f'ny={n*y:.8f} target={target_y:.8f}')
    return len(cases)


def sharpness_cases():
    count = 0
    for s, w, alpha, theta in [(0.2,0.5,1.0,0.4),(0.6,3.0,0.3,0.25)]:
        for d in [0.002, 0.005, 0.01]:
            beta = theta * (1 + alpha) + d
            x = theta/(theta+d)
            y = (1 + alpha*x) * prey_growth(x,s,w)
            assert s < x < 1 and y > 0
            xx, yy = iterate(x,y,s,w,alpha,beta,theta)
            assert abs(xx - x)<1e-12 and abs(yy-y)<1e-12
            count+=1
    return count

if __name__=='__main__':
    print('rational derivative and asymptotic coefficient checks:', rational_checks())
    print('critical trajectory tests:', critical_cases())
    print('near-threshold positive equilibria:', sharpness_cases())
    print('PASS: finite supplemental checks')
