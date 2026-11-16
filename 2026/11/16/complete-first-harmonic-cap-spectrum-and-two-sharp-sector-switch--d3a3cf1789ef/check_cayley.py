"""Exact, standard-library verification for Cayley-plane cap spectra.

This verifies polynomial identities by coefficient-independent exact integration
and 17 evaluations, sufficient for polynomials of degree <= 13.
It does not replace the geometric group-representation argument.
"""
from fractions import Fraction as F
from math import comb

# Coefficients, in increasing powers of x, of beta density up to normalization.
density = [F(0)] * 3 + [F((-1)**k * comb(7,k)) for k in range(8)]
weights = {
    'axial': [F(1,9), F(-2,3), F(1)],
    'spin': [F(0), F(1), F(-1)],
    'vector': [F(1), F(-2), F(1)],
}

def convolution(a,b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def evalpoly(a,t):
    s=F(0)
    for c in reversed(a):s=s*t+c
    return s

def integral_tail(coeffs,t):
    return sum((c * (1-t**(i+1))/F(i+1) for i,c in enumerate(coeffs)),F(0))

def exact_eigen(name,t):
    a=convolution(density,weights[name])
    return integral_tail(a,t)/integral_tail(a,F(0))

def closed(name,t):
    w=1-t
    if name=='axial':return w**8*(1+8*t+36*t**2+120*t**3-1815*t**4+5940*t**5)
    if name=='spin':return w**9*(1+9*t+45*t**2+165*t**3+495*t**4)
    if name=='vector':return w**10*(1+10*t+55*t**2+220*t**3)
    raise KeyError(name)

def volume(t):return (1-t)**8*(1+8*t+36*t*t+120*t**3)

for i in range(17):
    t=F(i,16)
    v={k:exact_eigen(k,t) for k in weights}
    for k in weights:assert v[k]==closed(k,t),(k,t,v[k],closed(k,t))
    assert v['axial']-v['spin']==2145*t**4*(1-t)**8*(3*t-1)
    assert v['axial']-v['vector']==1430*t**4*(1-t)**8*(4*t-1)
    assert v['spin']-v['vector']==715*t**4*(1-t)**9
    assert v['axial']+16*v['spin']+9*v['vector']==26*volume(t)

# For all six displayed expressions, the integral construction and closed
# factorization are polynomials of degree at most 13. Therefore equality at
# seventeen distinct rational t proves coefficient identity globally.
for t in [F(0),F(1,4),F(1,3),F(1,2),F(1)]:
    axial=F(3,2)*(t-F(1,3))**2
    spin=2*t*(1-t)
    vector=(1-t)**2/F(2)
    assert axial+spin+vector==F(2,3)
assert exact_eigen('axial',F(1,4))==exact_eigen('vector',F(1,4))
assert exact_eigen('axial',F(1,3))==exact_eigen('spin',F(1,3))
for t in [F(1,10),F(3,10),F(1,2),F(9,10)]:
    v={k:exact_eigen(k,t) for k in weights}
    assert all(F(0)<x<F(1) for x in v.values())
    if t<F(1,4):assert v['spin']>v['vector']>v['axial']
    elif t<F(1,3):assert v['spin']>v['axial']>v['vector']
    else:assert v['axial']>v['spin']>v['vector']
# Leading coefficients of the t->1 tails yield the sharp ratio 4290/286 =15.
assert F(5940-1815+120+36+8+1,220+55+10+1)==15
print('CAYLEY_26_THREE_BRANCHES_EXACT_POLYNOMIAL_PASS 17-point degree-13 identities')
print('CAYLEY_SPIN9_PEIRCE_NORM_IDENTITY_PASS')
print('CAYLEY_TWO_CROSSINGS_TRACE_ORDER_AND_ASYMPTOTIC_PASS')
