#!/usr/bin/env python3
"""Reproducible exact polynomial and numerical checks for the RK3 shear theorem.

Requires only the Python standard library. The universal conclusions require the
analytic proof in RESULT.md; finite checks are supplementary.
"""
from fractions import Fraction as Q
from math import sqrt, exp
from decimal import Decimal, getcontext


def add(a, b):
    n = max(len(a), len(b))
    return [((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)) for i in range(n)]


def mult(a, b):
    o = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] += x * y
    return o


def scale(a, c):
    return [c * x for x in a]


def diff(a):
    return [i * a[i] for i in range(1, len(a))]


def same(a, b):
    n = max(len(a), len(b))
    assert all((a[i] if i < len(a) else 0) == (b[i] if i < len(b) else 0) for i in range(n)), (a, b)


def evalp(a, x):
    ans = Q(0)
    for c in reversed(a):
        ans = ans * x + c
    return ans

r = [Q(1), Q(-1), Q(1, 2), Q(-1, 6)]
p = [Q(1), Q(-1), Q(1, 2)]
F = [Q(-48), Q(150), Q(-132), Q(67), Q(-20), Q(3)]
N = add([Q(1)], scale(mult(r, r), -1))
D = mult([Q(0), Q(1)], p)
# The h^3 F /72 identity for the derivative of G=(1-r^2)/(hp).
same(add(mult(diff(N), D), scale(mult(N, diff(D)), -1)), scale([Q(0)] * 3 + F, -Q(1, 72)))
# Explicit closed form for G(h).
A = [Q(6), Q(-3), Q(1)]
B = [Q(-12), Q(6), Q(-3), Q(1)]
C = [Q(2), Q(-2), Q(1)]
same(scale(mult(N, C), 18), scale(mult(D, mult(A, B)), -1))
# The claimed strictly positive decomposition of F'(h).
square = mult([Q(2), -Q(8, 3), Q(1)], [Q(2), -Q(8, 3), Q(1)])
quad = [Q(90), Q(-104), Q(103, 3)]
same(diff(F), add(scale(square, Q(15)), quad))
# Quadratic has negative discriminant; F'(h) > 0 for all real h.
assert quad[1]**2 - 4*quad[0]*quad[2] == -1544
assert evalp(F, Q(0)) == -48 and evalp(F, Q(1)) == 20
# Difference G-2 = -h^2 (h^3 - 6h^2 + 21h - 12)/(18(h^2-2h+2)).
H = [Q(-12), Q(21), Q(-6), Q(1)]
same(scale(add(N, scale(D, -2)), 36), scale(mult([Q(0),Q(0),Q(0),Q(1)], H), -1))


def r3(h):
    return 1.0 - h + h*h/2.0 - h*h*h/6.0


def p2(h):
    return 1.0 - h + h*h/2.0


def G(h):
    return (1.0 - r3(h)**2)/(h*p2(h))


def Fv(h):
    return (((((3*h-20)*h+67)*h-132)*h+150)*h-48)


def bisect(f, lo, hi, count=160):
    flo, fhi = f(lo), f(hi)
    assert flo * fhi < 0
    for _ in range(count):
        mid = (lo+hi)/2
        fm = f(mid)
        if fm == 0: return mid
        if flo*fm <=0: hi=mid
        else: lo=mid; flo=fm
    return (lo+hi)/2

hc = bisect(Fv, 0.0, 1.0)
beta = bisect(lambda h: r3(h)+1, 2.0, 3.0)
gc = G(hc)
assert 0.47981117 < hc < 0.47981119
assert 2.03215928 < gc < 2.03215931
assert 2.51274532 < beta < 2.51274534
h2 = bisect(lambda h: G(h)-2, .6, .8)
assert .69269427 < h2 < .69269430

# Exact evaluation of a three-stage order-three polynomial on Jordan-block matrices.
# Full 2x2 polynomial multiplication avoids invoking the derivative formula.
def mm(A, B):
    return ((A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3],
             A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3]))

def ma(A, B): return tuple(a+b for a,b in zip(A, B))
def ms(A, c): return tuple(a*c for a in A)
I = (Q(1), Q(0), Q(0), Q(1))
exact_checks = 0
for num in range(1, 26):
    h = Q(num, 19)
    for j in range(0, 21):
        gamma = Q(j, 7)
        A = (-h, gamma*h, Q(0), -h)
        A2 = mm(A, A)
        A3 = mm(A2, A)
        T = ma(ma(ma(I, A), ms(A2, Q(1,2))), ms(A3, Q(1,6)))
        expected = (evalp(r, h), gamma*h*evalp(p, h), Q(0), evalp(r, h))
        assert T == expected
        exact_checks += 1

# Independent 2x2 singular-norm test versus the analytic criterion, away from equality.
float_checks = 0
for i in range(1, 140):
    h = i * 0.0231
    for j in range(0, 83):
        gamma = j*0.0517
        a, d = r3(h), gamma*h*p2(h)
        norm = (sqrt(4*a*a+d*d)+abs(d))/2
        predicate = a*a+abs(d) <= 1
        assert predicate == (norm <= 1), (h,gamma,norm)
        float_checks += 1

# Demonstrate detached positive step for a nondissipative generator and its loss above cutoff.
for gamma in (2.001, 2.01, 2.02, 2.03):
    assert 2 < gamma < gc
    assert r3(hc)**2 + gamma*hc*p2(hc) < 1
for gamma in (gc+0.001, 2.1, 3.0, 10.0):
    assert r3(hc)**2 + gamma*hc*p2(hc) > 1
# For this choice of non-dissipative gamma the exact semigroup initially expands,
# even though the finite-step numerical map contracts.
gamma = 2.02
assert (exp(-1e-4)*(sqrt(4+(gamma*1e-4)**2)+gamma*1e-4)/2) > 1
assert (sqrt(4*r3(hc)**2+(gamma*hc*p2(hc))**2)+gamma*hc*p2(hc))/2 < 1
print('VERIFIED: exact polynomial identities and positive decomposition')
print('exact Jordan polynomial cases:', exact_checks)
print('independent singular-norm comparisons:', float_checks)
print('critical step: %.15f' % hc)
print('critical shear: %.15f' % gc)
print('scalar endpoint: %.15f' % beta)
print('shear-two endpoint: %.15f' % h2)
