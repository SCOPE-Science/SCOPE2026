"""Standalone rational and numerical verification of three-node BV quadrature.

This program is only a finite consistency check; the theorem uses analytic arguments.
"""
from fractions import Fraction as F
from math import sqrt
import random


def p(d):
    return 12*d*d*(1-d)-1

lo, hi=F(3611758622,10**10),F(3611758623,10**10)
assert p(lo)<0<p(hi)
assert 1/sqrt(12)<float(lo)<float(hi)<.4
print('CUBIC_UNIQUE_ROOT_RATIONAL_BRACKET_PASS')

def coefficients(d):
    b=1/(24*d*d)
    a=.5-d
    return [a,.5,1-a],[b,1-2*b,b]


def discrep(d):
    xx,ww=coefficients(d)
    pref=0.
    arr=[]
    for x,w in zip(xx,ww):
        arr.extend([abs(pref-x),abs(pref+w-x)])
        pref+=w
    return max(arr)

root=(float(lo)+float(hi))/2
assert abs(discrep(root)-root/2)<2e-10
for d in [1/sqrt(12),.3,.33,root,.38,sqrt(3/20),.43,.5]:
    xx,ww=coefficients(d)
    for k in range(4):
        actual=sum(w*x**k for x,w in zip(xx,ww))
        target=1/(k+1)
        assert abs(actual-target)<1e-12,(d,k,actual,target)
    b=ww[0]
    a=xx[0]
    formula=max(b-a,.5-b)
    assert abs(discrep(d)-formula)<1e-12
print('MOMENT_EXACTNESS_AND_SHARP_DISCREPANCY_FORMULA_PASS')

# Exact endpoint comparisons, including the Gaussian and Simpson rules.
assert abs(discrep(sqrt(3/20))-2/9)<1e-12
assert abs(discrep(.5)-1/3)<1e-12
assert abs(discrep(1/sqrt(12))-1/sqrt(12))<1e-12
print('CLASSICAL_RULE_BENCHMARKS_PASS')

# Exhaustive scalar grid: numerical corroboration, not a proof of uniqueness.
for j in range(20001):
    d=1/sqrt(12)+(.5-1/sqrt(12))*j/20000
    assert discrep(d)+1e-10>=root/2
print('POSITIVE_RULE_PARAMETER_GRID_PASS 20001')

# Explicit extremal Jordan-variation-one step functions at the algebraic optimizer.
xx,ww=coefficients(root)
a=xx[0];b=ww[0]
# f=1_{[1/2,1]}: quadrature = 1-b; integral=1/2.
assert abs(((1-b)-.5)-root/2)<1e-10
# f=1_{(a,1]}: quadrature=1-b, integral=1-a.
assert abs(((1-b)-(1-a))+root/2)<1e-10
print('SHARP_DISCONTINUOUS_STEP_WITNESSES_PASS')

# Independent random finite-step BV upper bounds (arbitrary jump locations and values).
random.seed(47055)
for _ in range(2500):
    d=1/sqrt(12)+(.5-1/sqrt(12))*random.random()
    nodes,weights=coefficients(d)
    jumps=sorted([random.random() for i in range(random.randint(1,10))]+nodes)
    # Jump magnitudes may be signed; value at a jump is selected from either side.
    signed=[(random.random()*2-1) for t in jumps]
    chosen=[random.randint(0,1) for t in jumps]
    def fv(x):
        return sum(v for t,v,c in zip(jumps,signed,chosen) if t<x or (t==x and c==1))
    # Integral of step signal over [0,1]: each jump contributes v*(1-t).
    integ=sum(v*(1-t) for t,v in zip(jumps,signed))
    Q=sum(w*fv(x) for x,w in zip(nodes,weights))
    variation=sum(abs(v) for v in signed)
    assert abs(Q-integ)<=discrep(d)*variation+1e-12
print('INDEPENDENT_RANDOM_JUMP_FUNCTIONS_PASS 2500')
print('ALL_THREE_NODE_CUBIC_EXACT_BV_CHECKS_PASS')
