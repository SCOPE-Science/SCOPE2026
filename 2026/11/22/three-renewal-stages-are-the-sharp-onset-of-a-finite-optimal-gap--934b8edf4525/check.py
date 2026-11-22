#!/usr/bin/env python3
"""Independent finite-state probability calculations for a two-window renewal model.

All numerical tests support, but do not replace, the algebraic proof.
The phase generator is a directed n-cycle with rate one; a call is emitted
only on the final-to-first transition. Time is dimensionless.
"""
import math


def rowmul(v, M):
    return [sum(v[j] * M[j][i] for j in range(len(v))) for i in range(len(v))]


def no_call_matrix(n, t):
    out = [[0.0] * n for _ in range(n)]
    e = math.exp(-t)
    for i in range(n):
        for j in range(i, n):
            out[i][j] = e * t ** (j - i) / math.factorial(j - i)
    return out


def cycle_matrix(n, t):
    # P(N(t) mod n=r) for Poisson(t), via a rigorously bounded positive sum.
    probs = [0.0] * n
    term = math.exp(-t)
    for k in range(500):
        probs[k % n] += term
        term *= t / (k + 1)
        if k > t + 35 and term < 1e-17:
            break
    assert abs(sum(probs) - 1.0) < 3e-14
    return [[probs[(j - i) % n] for j in range(n)] for i in range(n)]


def exact_matrix_both(n, w, g):
    pi = [1.0/n] * n
    z = no_call_matrix(n, w)
    p = cycle_matrix(n, g)
    v = rowmul(rowmul(rowmul(pi, z), p), z)
    joint_no_call = sum(v)
    single_no_call = sum(rowmul(pi, z))
    return 1.0 - 2.0 * single_no_call + joint_no_call


def formula_both(n, w, g):
    if n == 1:
        return (1.0 - math.exp(-w))**2
    if n == 2:
        s = math.exp(-w) * (1 + w/2)
        return (1-s)**2 - math.exp(-2*w-2*g)*w*w/4
    if n == 3:
        s = math.exp(-w) * (1 + 2*w/3 + w*w/6)
        a = -w*w*(w*w+8*w+4)/36
        b = math.sqrt(3)*w*w*(w*w-4)/36
        return (1-s)**2 + math.exp(-2*w-1.5*g)*(a*math.cos(math.sqrt(3)*g/2) + b*math.sin(math.sqrt(3)*g/2))
    raise ValueError('n must be 1, 2 or 3')


def optimal_gap3(w):
    c = w**3*(w+4)/12
    d = -math.sqrt(3)*w*w*(w*w-4*w-8)/36
    return 2/math.sqrt(3)*(math.pi/2 + math.atan2(d, c))


def run():
    checks = 0
    ws = [0.02, 0.1, 0.3, 0.5, 1., 1.5, 2., 3., 5.]
    gs = [0., 0.01, 0.1, 0.5, 1., 1.8, 2., 2.5, 3.5, 4., 5., 7., 10., 12.]
    for n in (1,2,3):
        for w in ws:
            for g in gs:
                p = exact_matrix_both(n, w, g)
                f = formula_both(n, w, g)
                assert abs(p-f) < 6e-13, (n,w,g,p,f)
                checks += 1
    last_g = math.inf
    for w in [0.02, 0.1, 0.5, 1., 2., 3., 5., 10.]:
        g = optimal_gap3(w)
        assert 2*math.pi/(3*math.sqrt(3)) < g < 2*math.pi/math.sqrt(3)
        assert g < last_g
        last_g = g
        f = formula_both(3,w,g)
        for shift in [1e-3, 0.1, .5, 1., 2., 3., 5., 7., 10., 15.]:
            if shift < g:
                assert f > formula_both(3,w,g-shift)
                checks += 1
            assert f > formula_both(3,w,g+shift)
            checks += 1
        checks += 2
    for w in ws:
        assert formula_both(2,w,1) > formula_both(2,w,0)
        assert formula_both(2,w,2) > formula_both(2,w,1)
        checks += 2
    print('PASS',checks,'checks')
    w = 1.0
    print('w=1 lambda=1: optimal gap',format(optimal_gap3(w),'.12f'))
    print('w=1: P(both; gap=0)',format(formula_both(3,w,0),'.12f'))
    print('w=1: P(both; optimal)',format(formula_both(3,w,optimal_gap3(w)),'.12f'))
    print('w=1: P(both; infinite gap)',format((1-math.exp(-w)*(1+2*w/3+w*w/6))**2,'.12f'))


if __name__ == '__main__':
    run()
