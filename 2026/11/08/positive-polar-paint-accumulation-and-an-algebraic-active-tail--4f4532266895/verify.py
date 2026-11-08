"""Independent deterministic checks of the polar first-visit theorem.

Uses only Python standard-library floating arithmetic. No numerical result
is a substitute for the proof of monotonicity or the Tauberian limit.
"""
import math


def closed_transform(s, D, alpha, v):
    w = math.sqrt(s) + math.sqrt(s + alpha)
    return 2 * math.hypot(v, math.sqrt(D) * w) / (math.sqrt(s + alpha) * w)


def boundary_transform(s, D, alpha, v):
    # Independently solve the two-dimensional backward first-passage ODE
    # by its two decaying spatial modes.
    rate = alpha / 2
    b = 2 * D * (s + rate) + v * v
    discriminant = b * b - 4 * D * D * s * (s + alpha)
    assert discriminant > 0
    k1 = math.sqrt((b + math.sqrt(discriminant)) / (2 * D * D))
    k2 = math.sqrt(s * (s + alpha)) / (D * k1)
    def q(k):
        return -(D * k * k + v * k - s - rate) / rate
    q1, q2 = q(k1), q(k2)
    c1 = (-1 - q2) / (q1 - q2)
    c2 = (q1 + 1) / (q1 - q2)
    assert math.isclose(c1 + c2, 1.0, abs_tol=5e-11)
    assert math.isclose(c1*q1 + c2*q2, -1.0, abs_tol=5e-10)
    for k, qi in [(k1, q1), (k2, q2)]:
        assert abs(D*k*k + v*k - s-rate + rate*qi) <= 2e-8*max(1.0,k*k)
        assert abs(rate + (D*k*k-v*k-s-rate)*qi) <= 2e-8*max(1.0,k*k)
    return c1 * (1-q1) / k1 + c2 * (1-q2) / k2


def saturated(D, alpha, v):
    return 2 * math.hypot(v, math.sqrt(D * alpha)) / alpha


def square_root_coefficient(D, alpha, v):
    return 2*v*v / (alpha**1.5 * math.hypot(v, math.sqrt(D*alpha)))


def main():
    checks=0
    max_relative_error=0.0
    for D in (0.2, 1.0, 3.0):
        for a in (0.4, 1.5, 3.0):
            for v in (0.0, 0.35, 1.7, 4.0):
                for s in (0.002, 0.05, 0.7, 7.0, 35.0):
                    direct=boundary_transform(s,D,a,v)
                    formula=closed_transform(s,D,a,v)
                    re=abs(direct-formula)/max(1.0,abs(formula))
                    max_relative_error=max(max_relative_error,re)
                    assert re < 1.0e-9, (s,D,a,v,direct,formula)
                    checks+=1
                    if v==0:
                        passive=2*math.sqrt(D/(s+a))
                        assert math.isclose(formula,passive,rel_tol=1e-13)
                        checks+=1
                # High precision asymptotic checks are kept away from
                # catastrophic subtraction; O(s) errors vanish vs sqrt(s).
                for s in (1e-7, 1e-9):
                    f=closed_transform(s,D,a,v)
                    c=saturated(D,a,v)
                    k=square_root_coefficient(D,a,v)
                    if v>0:
                        assert abs((c-f)/math.sqrt(s) - k) < 0.04*k
                    else:
                        assert abs((c-f)/math.sqrt(s)) < 0.2
                    checks+=1
    print('PASS:',checks,'checks; maximum independent BVP error',max_relative_error)
    assert checks==297


if __name__ == '__main__':
    main()
