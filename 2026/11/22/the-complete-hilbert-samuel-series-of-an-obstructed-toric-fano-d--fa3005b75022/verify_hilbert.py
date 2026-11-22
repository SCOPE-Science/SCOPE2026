#!/usr/bin/env python3
"""Exact rational Groebner and Hilbert-series verification for the octagonal-cone deformation base.

Requires sympy; all arithmetic is in QQ and all calculations are finite identities.
"""
import itertools
import math
import collections
import sympy as S

x = S.symbols('x1:6')
t = S.symbols('t')
p = x[0] + 2*x[1] + x[2] - 2*x[4]
q = x[1] + 2*x[2] + x[3] - x[4]
relations = []
for k in range(2,7):
    relations.append(S.expand(p**k-x[0]**k-2*x[1]**k-x[2]**k+2*x[4]**k))
    relations.append(S.expand(q**k-x[1]**k-2*x[2]**k-x[3]**k+x[4]**k))

G = S.groebner(relations, *x, order='grevlex', domain=S.QQ)
lms = [tuple(a.LM(order='grevlex')) for a in G.polys]
expected = [
 (0,0,2,3,0), (0,2,0,1,2), (0,0,1,2,2), (2,0,2,0,0),
 (0,2,0,2,0), (0,1,0,3,0), (1,0,1,0,2), (0,3,0,0,0),
 (0,0,3,0,0), (1,0,1,1,0), (1,1,0,0,0), (0,1,1,0,0)
]
assert sorted(lms) == sorted(expected), (lms, expected)

# Recheck Buchberger's criterion on the displayed leading-monomial certificate.
# The original generators must also reduce to zero.
basis_expressions = [a.as_expr() for a in G.polys]
for rel in relations:
    _, remainder = S.reduced(rel, basis_expressions, *x, order='grevlex', domain=S.QQ)
    assert S.expand(remainder) == 0

def monomial(exponents):
    return math.prod(z**k for z,k in zip(x,exponents))

for i,j in itertools.combinations(range(len(G.polys)), 2):
    a,b = G.polys[i], G.polys[j]
    e,f = lms[i], lms[j]
    L = tuple(max(e[k],f[k]) for k in range(5))
    sa = monomial(tuple(L[k]-e[k] for k in range(5)))*a.as_expr()/a.LC(order='grevlex')
    sb = monomial(tuple(L[k]-f[k] for k in range(5)))*b.as_expr()/b.LC(order='grevlex')
    _, remainder = S.reduced(S.expand(sa-sb), basis_expressions, *x,
                              order='grevlex', domain=S.QQ)
    assert S.expand(remainder) == 0, (i,j,remainder)

# LCM inclusion-exclusion gives the Hilbert numerator of the monomial ideal.
coefficient = collections.defaultdict(int, {0:1})
for count in range(1,len(lms)+1):
    for group in itertools.combinations(lms, count):
        degree = sum(max(ex[k] for ex in group) for k in range(5))
        coefficient[degree] += (-1)**count
N = S.expand(sum(c*t**d for d,c in coefficient.items()))
h = 1+2*t+t**2-2*t**3-5*t**4+5*t**6-t**8
assert S.cancel(N/(1-t)**5-h/(1-t)**3) == 0
H = h/(1-t)**3
Hred = 1/(1-t)**3 + 1/(1-t) - 1
Hnil = (t+5*t**2+6*t**3+2*t**4-2*t**5-t**6)/(1-t)
assert S.cancel(H-Hred-Hnil) == 0
Hglobal = h**2/(1-t)**12
assert S.expand(h**2) == S.expand((1+2*t+t*t-2*t**3-5*t**4+5*t**6-t**8)**2)
assert S.simplify(Hglobal - H**2/(1-t)**6) == 0
assert h.subs(t,1) == 1

# Independent direct standard-monomial enumeration for degrees 0 through 10.
for d in range(11):
    standard = 0
    for aa in range(d+1):
      for bb in range(d-aa+1):
       for cc in range(d-aa-bb+1):
        for dd in range(d-aa-bb-cc+1):
         ee=d-aa-bb-cc-dd
         ex=(aa,bb,cc,dd,ee)
         if not any(all(ex[k] >= v[k] for k in range(5)) for v in lms):
             standard += 1
    hseries_coefficient = S.series(H,t,0,d+1).removeO().expand().coeff(t,d)
    assert standard == hseries_coefficient, (d,standard,hseries_coefficient)
print('PASS: 12 leading monomials, 66 exact S-pairs, 10 source generators, degrees 0..10')
print('Affine factor:', S.factor(H))
print('Nilpotent excess:', S.factor(Hnil))
print('Full miniversal base:', S.factor(Hglobal))
