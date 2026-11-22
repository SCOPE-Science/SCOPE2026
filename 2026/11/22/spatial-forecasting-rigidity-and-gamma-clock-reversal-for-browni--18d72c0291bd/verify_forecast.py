"""Reproducible numerical checks for renewal-reset Brownian forward-time laws.

Requirements: Python 3, NumPy, SciPy. Run: python verify_forecast.py
Analytic proofs of all-parameter statements are in RESULT.md.
"""
import math
from scipy.integrate import quad
from scipy.special import gammaincc


def survival(b, k, rate):
    return gammaincc(k, rate * b)


def kernel(b, x, D):
    if b <= 0:
        return 0.0
    return math.exp(-x*x/(4*D*b))/math.sqrt(4*math.pi*D*b)


def conditional_tail(x, u, k, rate, D):
    # Two independent integrations from the equilibrium renewal occupation law.
    numerator = quad(lambda b: survival(b+u,k,rate)*kernel(b,x,D),
                     0, math.inf, epsabs=2e-12, epsrel=2e-11, limit=350)[0]
    denominator = quad(lambda b: survival(b,k,rate)*kernel(b,x,D),
                       0, math.inf, epsabs=2e-12, epsrel=2e-11, limit=350)[0]
    return numerator / denominator


def erlang2_formula(x, u, rate, D):
    a = abs(x)*math.sqrt(rate/D)
    return math.exp(-rate*u) * (1+2*rate*u/(3+a))


def erlang3_formula(x, u, rate, D):
    a = abs(x)*math.sqrt(rate/D)
    den = a*a+7*a+15
    return math.exp(-rate*u) * (1+4*rate*u*(a+3)/den + 4*(rate*u)**2/den)


def check_close(a,b,tol=3e-8):
    assert abs(a-b) <= tol * max(1,abs(a),abs(b)), (a,b)


def main():
    n = 0
    for rate,D in [(1.3,0.8), (0.7,1.4)]:
        for shape in [0.55,0.8,1.0,2.0,3.0,4.5]:
            for u in [0.2,0.9,1.7]:
                values = [conditional_tail(x,u,shape,rate,D) for x in [0,0.5,2.,5.]]
                for v in values:
                    assert 0<v<1
                    n += 1
                if shape>1:
                    assert all(v>w for v,w in zip(values,values[1:])), (shape,u,values)
                elif shape<1:
                    assert all(v<w for v,w in zip(values,values[1:])), (shape,u,values)
                else:
                    for v in values:
                        check_close(v, math.exp(-rate*u))
                        n += 1
                n += 1
                if shape in (2,3):
                    for x,v in zip([0,0.5,2.,5.],values):
                        form = erlang2_formula if shape==2 else erlang3_formula
                        check_close(v, form(x,u,rate,D))
                        n += 1
    # Exact first correction from the independent Erlang-2 and Erlang-3 formulas.
    rate,D,u = 1.1,1.9,0.7
    coefficient = 2*u*math.sqrt(D*rate)
    for shape,form in [(2,erlang2_formula),(3,erlang3_formula)]:
        for x in [100.,200.,400.,800.]:
            ratio = form(x,u,rate,D)/math.exp(-rate*u)
            observed = x*(ratio-1)
            target = (shape-1)*coefficient
            assert abs(observed-target) < 0.13*target, (shape,x,observed,target)
            n += 1
    # k=2 exact mean residual and its strictly negative spatial derivative.
    for x in [0.1,1.,4.,16.]:
        a=x*math.sqrt(rate/D)
        val=(1+2/(3+a))/rate
        deriv=-2*math.sqrt(rate/D)/(rate*(3+a)**2)
        assert val>1/rate and deriv<0
        n += 1
    print('PASS',n,'deterministic analytic/quadrature assertions')


if __name__ == '__main__':
    main()
