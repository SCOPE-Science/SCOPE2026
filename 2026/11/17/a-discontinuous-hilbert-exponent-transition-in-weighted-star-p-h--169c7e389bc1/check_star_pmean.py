"""Standalone numerical and rational checks for star p-energy extension constants."""
from fractions import Fraction
from itertools import product
from math import isclose


def center(values, weights, p):
    """Unique minimizer of sum_i weights_i * abs(values_i - c)**p."""
    lo, hi = min(values), max(values)
    if lo == hi:
        return lo
    for _ in range(180):
        mid = (lo + hi) / 2
        eq = sum(w * (1 if mid > x else -1) * abs(mid - x)**(p-1)
                 for w, x in zip(weights, values))
        if eq > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def graph_lip_difference(f, g, w, p):
    c1 = center(f, w, p)
    c2 = center(g, w, p)
    h = [x-y for x, y in zip(f, g)]
    d = c1-c2
    return max(abs(x-d) for x in h) / ((max(h)-min(h))/2)


def tests():
    count = 0
    for m in range(2, 7):
        for weights in [list(range(1, m+1)), [1]*m, [2**i for i in range(m)]]:
            W = sum(weights)
            exact = Fraction(2)*(1-Fraction(min(weights), W))
            signs = list(product([-1, 1], repeat=m))
            best = max(
                max(abs(Fraction(h[i]) - sum(Fraction(weights[j], W)*h[j] for j in range(m)))
                    for i in range(m))
                for h in signs if len(set(h)) > 1
            )
            assert best == exact, (m, weights, best, exact)
            count += 1
    print('EXACT_WEIGHTED_HILBERT_CENTER_CASES_PASSED', count)

    count = 0
    for m in range(2, 7):
        for p in [1.5, 2.0, 3.0, 4.0]:
            w = [i+1 for i in range(m)]
            for k in range(12):
                f = [(i*7+k*3)%11 - 5 for i in range(m)]
                g = [(i*2+k*5)%13 - 6 for i in range(m)]
                h = [a-b for a,b in zip(f,g)]
                if max(h)==min(h):
                    continue
                ratio = graph_lip_difference(f,g,w,p)
                assert ratio <= 2 + 1e-11, (ratio,m,p)
                count += 1
    print('NONLINEAR_TWO_INPUT_GLOBAL_CAP_CHECKS_PASSED', count)

    count = 0
    for p in [1.5,2.0,3.0,4.0]:
        for w1,w2 in [(1,1),(1,2),(3,7)]:
            k1, k2 = w1**(1/(p-1)), w2**(1/(p-1))
            exact = 2*max(k1,k2)/(k1+k2)
            f = [1.2, -2.7]
            g = [-0.4, 0.9]
            predicted_c = lambda a: (k1*a[0]+k2*a[1])/(k1+k2)
            assert abs(center(f,[w1,w2],p) - predicted_c(f)) < 1e-12
            assert abs(center(g,[w1,w2],p) - predicted_c(g)) < 1e-12
            ratio = graph_lip_difference(f,g,[w1,w2],p)
            assert abs(ratio-exact) < 1e-11, (ratio,exact,p)
            count += 1
    print('TWO_LEAF_WEIGHTED_POWER_MEAN_CASES_PASSED', count)

    for p in [2.5,3.0,4.0]:
        f = [0,1,-1]
        assert abs(center(f,[1,1,1],p)) < 1e-12
        h = [1,-1,-1]
        vals = []
        for eps in [1e-2,1e-3,1e-4,1e-5]:
            g = [x+eps*y for x,y in zip(f,h)]
            vals.append(graph_lip_difference(g,f,[1,1,1],p))
        assert vals[-1] > 1.98 and vals[-1] > vals[0],(p,vals)
    print('SUPERHILBERT_SHARP_SMALL_PERTURBATIONS_PASSED', 3)

    for q in [10, 30, 100, 300, 1000]:
        # All displayed derivative weights are exact rational for p = 3/2.
        epsilon = Fraction(1,q*q)
        f = [Fraction(1), -(Fraction(1)+Fraction(1,q))**2, epsilon]
        assert Fraction(1) - (1+Fraction(1,q)) + Fraction(1,q) == 0
        vals = [Fraction(1), Fraction(q,q+1), Fraction(q)]
        a1 = vals[0]/sum(vals)
        tangent_lip = 2*(1-a1)
        assert tangent_lip < 2 and tangent_lip > Fraction(2)*(1-Fraction(2,q))
        assert f[0] > 0 > f[1] and f[2]>0
    print('SUBHILBERT_EXACT_RATIONAL_TANGENT_WITNESSES_PASSED', 5)

    for q in [100,1000]:
        p = 1.5
        e = 1/(q*q)
        f = [1,-(1+1/q)**2,e]
        h = [1,-1,-1]
        dt = 1e-8
        g = [x+dt*y for x,y in zip(f,h)]
        obs=graph_lip_difference(g,f,[1,1,1],p)
        theoretical = 2*(1-1/(1+q/(q+1)+q))
        assert abs(obs-theoretical) < 0.002, (q,obs,theoretical)
    print('SUBHILBERT_FINITE_DIFFERENCE_WITNESSES_PASSED', 2)
    print('ALL_WEIGHTED_STAR_P_HARMONIC_STABILITY_CHECKS_PASSED')

if __name__ == '__main__':
    tests()
