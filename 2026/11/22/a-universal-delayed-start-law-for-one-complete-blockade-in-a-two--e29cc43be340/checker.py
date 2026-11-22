"""Reproducibility checks for a fixed-duration single-edge transmission blockade.

Requires Python 3.10+ (standard library only). Finite computations supplement,
not replace, the analytical uniqueness and duration-monotonicity proof.
"""
import math
import random
from fractions import Fraction

ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def integral_exp(a, length):
    """Integral from 0 to length of exp(a*u) du."""
    if abs(a * length) < 1e-7:
        z = a * length
        return length * (1 + z / 2 + z*z / 6 + z**3 / 24 + z**4 / 120)
    return math.expm1(a * length) / a


def m_weight(alpha, gamma, length):
    return gamma * math.exp(-gamma * length) * integral_exp(gamma-alpha, length) / (-math.expm1(-gamma*length))


def optimal_start(alpha, beta, gamma, length):
    rate = beta + gamma
    gap = rate-alpha
    m = m_weight(alpha, gamma, length)
    if abs(gap) < 1e-9 * max(rate, alpha):
        return m / rate
    return -math.log1p(-gap*m/rate) / gap


def infectious_at_start(alpha, rate, time):
    gap = rate-alpha
    if abs(gap) < 1e-8 * max(rate, alpha):
        return alpha*time*math.exp(-alpha*time)
    return alpha*math.exp(-alpha*time)*(-math.expm1(-gap*time))/gap


def saved_probability(alpha, beta, gamma, length, start):
    rate = beta+gamma
    A = -math.expm1(-gamma*length)
    K = math.exp(-gamma*length)*integral_exp(gamma-alpha, length)
    M = (A-gamma*K)/alpha
    return (beta/rate)*(A*infectious_at_start(alpha, rate, start)+alpha*math.exp(-alpha*start)*M)


def rk4_step(state, step, alpha, beta, gamma, on):
    def deriv(x):
        e,i,p=x
        return (-alpha*e, alpha*e-(gamma+on*beta)*i, on*beta*i)
    k1=deriv(state)
    k2=deriv(tuple(state[j]+step*k1[j]/2 for j in range(3)))
    k3=deriv(tuple(state[j]+step*k2[j]/2 for j in range(3)))
    k4=deriv(tuple(state[j]+step*k3[j] for j in range(3)))
    return tuple(state[j]+step*(k1[j]+2*k2[j]+2*k3[j]+k4[j])/6 for j in range(3))


def independently_integrated_target(alpha, beta, gamma, length, start):
    state = (1.0, 0.0, 0.0)
    segments = [(start,1.0),(length,0.0), (70/min(alpha, gamma),1.0)]
    for duration, on in segments:
        n=max(1, math.ceil(duration/0.012))
        dt=duration/n
        for _ in range(n):
            state = rk4_step(state,dt,alpha,beta,gamma,on)
    return state[2]


def run_checks():
    # All components of the exact example can be evaluated rationally.
    alpha,beta,gamma=2.0,2.0,1.0
    length=math.log(2)
    start=math.log(Fraction(6,5))
    check(abs(m_weight(alpha,gamma,length)-0.5)<1e-13, 'exact weight')
    check(abs(optimal_start(alpha,beta,gamma,length)-start)<1e-13, 'exact optimum')
    check(Fraction(2,3)-Fraction(125,648)==Fraction(307,648),'exact risk')
    check(Fraction(125,648)-Fraction(1,6)==Fraction(17,648),'exact strict gain')
    check(abs(saved_probability(alpha,beta,gamma,length,start)-125/648)<1e-13,'exact optimum probability')
    check(abs(saved_probability(alpha,beta,gamma,length,0)-1/6)<1e-13,'exact initial protection')
    check(abs(independently_integrated_target(alpha,beta,gamma,length,start)-307/648)<1e-8, 'ODE replay')
    rng=random.Random(101230)
    for j in range(68):
        alpha=rng.uniform(0.45,3)
        beta=rng.uniform(0.4,2.5)
        gamma=rng.uniform(0.45,2.8)
        length=rng.uniform(0.12,2.8)
        if j%9==0: alpha=beta+gamma  # Degenerate repeated-rate case.
        s=optimal_start(alpha,beta,gamma,length)
        check(s>0, 'strict delay')
        m=m_weight(alpha,gamma,length)
        check(0<m<1, 'proper weighted expectation')
        baseline=beta/(beta+gamma)
        maxsaved=saved_probability(alpha,beta,gamma,length,s)
        check(0<maxsaved<baseline, 'nontrivial prevention')
        for candidate in (0,0.25*s,0.75*s,s,s+0.5,s+2):
            actual=independently_integrated_target(alpha,beta,gamma,length,candidate)
            predicted=baseline-saved_probability(alpha,beta,gamma,length,candidate)
            check(abs(actual-predicted)<3e-7,'ODE versus conditioning')
            check(saved_probability(alpha,beta,gamma,length,candidate)<=maxsaved+1e-11, 'global optimum samples')
        lengths=[0.02,0.1,0.4,0.9,1.8,4,10]
        starts=[optimal_start(alpha,beta,gamma,L) for L in lengths]
        check(all(starts[i]>starts[i+1] for i in range(len(starts)-1)),'longer protection starts earlier')
        gap=beta+gamma-alpha
        peak=(math.log((beta+gamma)/alpha)/gap if abs(gap)>1e-9 else 1/alpha)
        check(abs(optimal_start(alpha,beta,gamma,1e-6)-peak)<3e-6,'short limit peak')
        check(optimal_start(alpha,beta,gamma,100)<1e-7,'long limit zero')
    print('All', ASSERTIONS, 'checks passed (including independent piecewise-ODE integration).')


if __name__=='__main__':
    run_checks()
