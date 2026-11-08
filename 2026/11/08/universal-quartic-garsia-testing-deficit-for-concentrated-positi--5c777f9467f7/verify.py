#!/usr/bin/env python3
"""Reproducible finite-section checks for positive moment Hankel kernel-test asymptotics."""
import math
from fractions import Fraction

N = 18

def moments(kind, n):
    if kind == 'two_atom':
        return Fraction(1, 1) if n == 0 else Fraction(1, 2)
    if kind == 'uniform':
        return Fraction(1, n + 1)
    raise ValueError(kind)

def matvec(h, v):
    return [sum(row[j] * v[j] for j in range(len(v))) for row in h]

def norm(v):
    return math.sqrt(sum(x*x for x in v))

def norm_top(h):
    v = [1.] + [0.] * (len(h) - 1)
    for _ in range(250):
        w = matvec(h, v)
        wnorm = norm(w)
        v = [x / wnorm for x in w]
    w = matvec(h, v)
    return sum(x*y for x,y in zip(w,v))

def kernel_test(h, a):
    v = [math.sqrt(1-a*a) * (a**j) for j in range(len(h))]
    return norm(matvec(h, v))

def golden_max(h, upper):
    x, y = 0., upper
    phi = (math.sqrt(5) - 1) / 2
    c, d = y - phi*(y-x), x + phi*(y-x)
    fc, fd = kernel_test(h,c), kernel_test(h,d)
    for _ in range(110):
        if fc < fd:
            x, c, fc = c, d, fd
            d = x + phi*(y-x)
            fd = kernel_test(h,d)
        else:
            y, d, fd = d, c, fc
            c = y - phi*(y-x)
            fc = kernel_test(h,c)
    aa = (x+y)/2
    return aa, kernel_test(h,aa)

checks=0
for kind in ('two_atom', 'uniform'):
    m1, m2 = moments(kind,1), moments(kind,2)
    var = m2 - m1*m1
    assert var == (Fraction(1,4) if kind == 'two_atom' else Fraction(1,12))
    leading = float(var*var / 2)
    checks += 1
    for eps in (0.08, 0.04, 0.02):
        h = [[float(moments(kind,i+j)) * eps**(i+j) for j in range(N)] for i in range(N)]
        eig = norm_top(h)
        a, q = golden_max(h, 0.25)
        diff = eig-q
        ratio = diff/eps**4
        assert diff > 0, (kind, eps, diff)
        assert abs(ratio / leading-1) < 0.08, (kind, eps, ratio, leading)
        assert abs(a/eps-float(m1)) < .06, (kind, eps, a)
        checks += 3
        print('%s eps=%.3f gap=%.11g gap/eps^4=%.11g limit=%.11g kernel_a=%.9f' %
              (kind,eps,diff,ratio,leading,a))
print('MOMENT_HANKEL_QUARTIC_OK %d checks' % checks)
