"""Finite exact checks and numerical asymptotics for a two-defect zero-range ring.

Run: python3 verify.py. Requires Python 3.10+ standard library only.
The asymptotic checks do not constitute an infinite-size proof.
"""
import itertools
import math
from fractions import Fraction


def compositions(m, n):
    if n == 1:
        yield (m,)
    else:
        for v in range(m + 1):
            for t in compositions(m - v, n - 1):
                yield (v,) + t


def exact_ring_check(L, M):
    rates = (Fraction(3, 7), Fraction(1, 2)) + (Fraction(1),) * L
    states = tuple(compositions(M, len(rates)))
    weights = {state: math.prod(r ** (-k) for r, k in zip(rates, state)) for state in states}
    Z = sum(weights.values())
    if M:
        zm = sum(math.prod(r ** (-k) for r, k in zip(rates, state))
                 for state in compositions(M - 1, len(rates)))
    for state in states:
        out = sum((rates[i] for i, v in enumerate(state) if v), Fraction(0)) * weights[state]
        incoming = Fraction(0)
        for i in range(len(rates)):
            j = (i + 1) % len(rates)
            if state[j]:
                predecessor = list(state)
                predecessor[i] += 1
                predecessor[j] -= 1
                incoming += rates[i] * weights[tuple(predecessor)]
        assert out == incoming, ('stationary balance', L, M, state)
    if M:
        for i in range(len(rates)):
            flux = sum(weights[state] * rates[i] for state in states if state[i]) / Z
            assert flux == zm / Z, ('flux', L, M, i)
        q = float(rates[1]); a = math.log(float(rates[1] / rates[0]))
        by_defect = {}
        for state in states:
            pair = state[:2]
            by_defect[pair] = by_defect.get(pair, Fraction(0)) + weights[state] / Z
        for (j, k), prob in by_defect.items():
            # The negative-binomial representation has the same unnormalised ratio.
            t = M - j - k
            predicted = math.exp(a*j) * math.comb(t + L - 1, L - 1) * q ** (-j-k)
            direct = float(prob) * float(Z)
            assert math.isclose(predicted, direct, rel_tol=2e-12), ('joint', L, M, j, k)


def geom_sum_prob(L, max_s, q):
    """The law of sum of L independent geom(q) (support 0,1,..)."""
    mode = max(0, math.floor((L-1)*q/(1-q)))
    p_mode = math.exp(math.lgamma(mode + L) - math.lgamma(L) - math.lgamma(mode + 1)
                      + L * math.log1p(-q) + mode * math.log(q))
    p = [0.0] * (max_s + 1)
    if mode <= max_s:
        p[mode] = p_mode
        for s in range(mode, max_s):
            p[s+1] = p[s] * q * (s + L)/(s+1)
    v = p_mode
    for s in range(mode, 0, -1):
        v *= s / (q * (s + L-1))
        if s-1 <= max_s:
            p[s-1] = v
    return p


def finite_metrics(L, M, q, a):
    p = geom_sum_prob(L, M, q)
    H = [1.0] * (M+1)
    H1 = [0.0] * (M+1)
    v = 1.0
    for t in range(1, M+1):
        v *= math.exp(a)
        H[t] = H[t-1] + v
        H1[t] = H1[t-1] + t*v
    D = s_t = s_x = s_gt = n = 0.0
    for s, prob in enumerate(p):
        t = M-s
        d = prob*H[t]
        D += d
        s_t += d*t
        s_x += prob*H1[t]
        s_gt += prob*(H[t]-H[t//2])
        n += prob*math.exp(a*t)
    return {'mean_t':s_t/D,'mean_x':s_x/D,
            'p_x_gt_y':s_gt/D,'current':q*(1-n/D), 'norm':D}


def simpson(f, endpoint=35.0, steps=14000):
    h = endpoint/steps
    s = f(0.0)+f(endpoint)
    for i in range(1,steps):
        s += (4 if i%2 else 2) * f(i*h)
    return s*h/3


def I(t,theta):
    return t if theta == 0 else math.expm1(theta*t)/theta


def I1(t,theta):
    return t*t/2 if theta == 0 else ((theta*t-1)*math.exp(theta*t)+1)/theta**2


def limit_critical(h,theta,q):
    sigma=math.sqrt(q)/(1-q)
    g=lambda t: math.exp(-((h-t)**2)/(2*sigma*sigma))
    d=simpson(lambda t: I(t,theta)*g(t))
    n=simpson(lambda t: math.exp(theta*t)*g(t))
    mx=simpson(lambda t: I1(t,theta)*g(t))/d
    gt=simpson(lambda t: (I(t,theta)-I(t/2,theta))*g(t))/d
    return {'current_correction':n/d,'mean_x':mx,'p_x_gt_y':gt}


def limit_supercritical(alpha, theta):
    if theta == 0:
        return {'current_correction':1/alpha,'mean_x':alpha/2}
    E=math.exp(theta*alpha)
    return {'current_correction':E*theta/(E-1),
            'mean_x':alpha*E/(E-1)-1/theta}


def main():
    nchecks=0
    for L in range(2,6):
        for M in range(0,7):
            exact_ring_check(L,M)
            nchecks += 1
    print('PASS: exact stationary balances, joint probabilities, and fluxes for',nchecks,'labeled-state models')
    q=0.5
    for theta in (-2.,0.,2.):
        target=limit_critical(0.,theta,q)
        errors=[]
        for L in (200,800,3200):
            m=round(L*q/(1-q))
            exact=finite_metrics(L,m,q,theta/math.sqrt(L))
            values={'current_correction':math.sqrt(L)*(1-exact['current']/q),
                    'mean_x':exact['mean_x']/math.sqrt(L),
                    'p_x_gt_y':exact['p_x_gt_y']}
            err=max(abs(values[k]-target[k]) for k in target)
            errors.append(err)
        assert errors[2] < 0.25 and errors[2] < errors[0], ('critical',theta,errors)
        print('PASS: critical limit convergence',theta, 'max errors=',[round(e,5) for e in errors])
    for theta in (-2.,0.,2.):
        target=limit_supercritical(1.,theta)
        errors=[]
        for L in (200,800,3200):
            exact=finite_metrics(L,2*L,q,theta/L)
            values={'current_correction':L*(1-exact['current']/q),
                    'mean_x':exact['mean_x']/L}
            err=max(abs(values[k]-target[k]) for k in target)
            errors.append(err)
        assert errors[2] < 0.01 and errors[2] < errors[0], ('supercritical',theta,errors)
        print('PASS: supercritical limit convergence',theta,'max errors=',[round(e,5) for e in errors])
    print('All checks passed. Infinite-size statements require the analytic proof.')

if __name__=='__main__': main()
