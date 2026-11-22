"""Standalone exact and numerical checks for the Poisson--Mirra modal theorem.

Uses only the Python standard library. These tests support, but do not replace,
the mathematical proof of the assertions quantified over infinite domains.
"""
from fractions import Fraction as Q
import math

checks = 0

def check(condition, msg):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(msg)


def v(k):
    return (k + 1) * (k + 2)


def parameters(theta):
    q = Q(1, 1) / (1 + theta)
    return q


def mode_threshold(theta):
    """Exact finite comparison for positive rational theta strictly below 2."""
    assert Q(0) < theta < Q(2)
    q = parameters(theta)
    choices = []
    k = 1
    # v(k)q**k is unimodal: its ratio is q(k+3)/(k+1).
    while v(k) * q ** k > 2:
        ak = (1 - q**k) / (v(k)*q**k - 2)
        choices.append((k, ak))
        k += 1
    return min(a for _, a in choices), [k for k, a in choices if a == min(v for _, v in choices)], len(choices)


def shape(k, q, b):
    return q**k * (1 + b*v(k))


def adjacency_sign(k, theta, b):
    return b * (k+2) * (2 - theta*(k+1)) - theta


theta = Q(1,5)
q = parameters(theta)
b = Q(31031,781688)
alpha = Q(279279,2442775)
check(alpha == 2*(1+theta)**2*b, 'Parameter conversion')
check(b == (1-q**6)/(v(6)*q**6-2), 'Zero-six matching value')
threshold, winners, n_candidates = mode_threshold(theta)
check(threshold == b and winners == [6], 'Unique exact threshold at six')
check(n_candidates == 35, 'Finite exact comparison count')
check(shape(0,q,b) == shape(6,q,b), 'Exact equal maxima')
for k in range(75):
    s = shape(k,q,b)
    if k not in (0,6):
        check(s < shape(0,q,b), f'Other index below global maxima: {k}')
    if k < 2 or k >= 6:
        check(adjacency_sign(k,theta,b) < 0, f'Decrease at {k}')
    if 2 <= k <= 5:
        check(adjacency_sign(k,theta,b) > 0, f'Increase at {k}')
# Establish the tail by exact polynomial, not finite testing.
check(b * 24 < 1, 'Tail threshold: (k+2)(9-k)<=24 for k>=6')
check(b * 24 < 1 and b * 28 > 1, 'Strict sign pattern')
# Normalization: sum v(k)q^k = 2/(1-q)^3, exactly.
K = theta**3 / ((theta**2+alpha)*(1+theta))
check(K * (1/(1-q) + 2*b/(1-q)**3) == 1, 'Exact normalization')
for f in [Q(99,100),Q(101,100)]:
    bb = b*f
    mm = max(range(200), key=lambda j:shape(j,q,bb))
    check(mm == (0 if f<1 else 6), 'Mode changes across exact boundary')
# Check finite-threshold classification on a collection of rational parameters.
for den in [2,3,4,5,6,8,10,20,25,50]:
    for num in range(1,2*den):
        theta1=Q(num,den)
        if theta1>=2:continue
        qq=parameters(theta1)
        th, _, size=mode_threshold(theta1)
        check(size>=1, 'Threshold set nonempty')
        for mult in [Q(1,2),Q(1),Q(2)]:
            bb=th*mult
            p0=shape(0,qq,bb)
            # The infinite-tail bound is analytic; this tests a generous finite range.
            maxj=max(range(1000), key=lambda j:float(shape(j,qq,bb)))
            check((maxj==0)==(mult<=1), 'Numerical global threshold side')
# Asymptotic benchmark: finite scans are diagnostics only.
for theta1 in [0.1, 0.05, 0.02, 0.01, 0.005]:
    qq=1/(1+theta1)
    vals=[]
    k=1
    while (k+1)*(k+2)*qq**k>2:
        vals.append(( (1-qq**k)/(qq**k*(k+1)*(k+2)-2),k))
        k+=1
    aa,kk=min(vals)
    check(abs(kk*theta1-1.59362426004004)<0.8, 'Scaling of competing index')
    check(abs(aa/theta1**2-1.54413865237087)<0.8, 'Scaling of threshold')
print(f'PASS: {checks} assertions; exact rational tie, infinite-tail polynomial witness, normalization, threshold finite comparisons, and asymptotic diagnostics')
print(f'Exact parameters: theta={theta}, alpha={alpha}, b={b}; competing modes {{0,6}}')
