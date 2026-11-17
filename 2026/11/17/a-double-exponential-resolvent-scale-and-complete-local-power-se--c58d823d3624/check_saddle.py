"""Finite diagnostic for the saddle-point model, not an infinite proof."""
from math import exp, log, e

def saddle(t, a):
    cap = int(exp(t + 2))
    f = 0.0
    best = float('-inf')
    for k in range(cap + 1):
        if k:
            f += log(log(k + e))
        z = k * log(t) - f - a*k/log(k + e)
        best = max(best, z)
    return best

if __name__ == '__main__':
    for t in (5.0, 6.0, 7.0, 8.0):
        base = saddle(t, 0.0)
        assert base > 0
        assert .6 < base / (exp(t)/t) < 1.4
        for a in (.5, 1., 2.):
            z = saddle(t, a)
            assert z >= 0
            # Loose diagnostics; convergence is slow on these short finite ranges.
            assert abs(z/base - exp(-a)) < .2
        print('sample t=',t,'baseline=',round(base,5))
    print('FINITE_SADDLE_DIAGNOSTICS_OK')
