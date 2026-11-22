#!/usr/bin/env python3
"""Reproduce symbolic identities and supplementary finite tests for weighted path gossip."""
import itertools
import numpy as np
import sympy as sp

p, q, r = sp.symbols('p q r', real=True)
lam = sp.symbols('lam', real=True)
J = sp.ones(4) / 4
P = []
for k, rate in enumerate((p, q, r)):
    v = sp.zeros(4, 1)
    v[k] = 1
    v[k+1] = -1
    P.append(sp.eye(4) - rate * v * v.T)

def transfer(order):
    result = sp.eye(4)
    for edge in order:
        result = P[edge] * result
    return result

def gram(order):
    E = transfer(order) - J
    return sp.expand(E.T * E)

def invariants(order):
    G = gram(order)
    c1 = sp.factor(sp.trace(G))
    c2 = sp.factor((c1**2 - sp.trace(G*G)) / 2)
    c3 = sp.factor(sp.det(G+J))
    return (c1, c2, c3)

serial = (0, 1, 2)
batched = (0, 2, 1)
a = invariants(serial)
b = invariants(batched)
delta = 4*p*q**2*r*(1-p)*(1-r)
assert sp.factor(a[0]-b[0]-delta) == 0
assert sp.factor(a[1]-b[1]-delta) == 0
assert sp.factor(a[2]-b[2]) == 0
assert sp.factor(a[2]-(1-2*p)**2*(1-2*q)**2*(1-2*r)**2) == 0
chi_s = lam**3-a[0]*lam**2+a[1]*lam-a[2]
chi_b = lam**3-b[0]*lam**2+b[1]*lam-b[2]
assert sp.factor(chi_s-chi_b-delta*lam*(1-lam)) == 0

for order in itertools.permutations(range(3)):
    expected = a if order in ((0,1,2), (2,1,0)) else b
    actual = invariants(order)
    assert all(sp.factor(x-y)==0 for x,y in zip(actual,expected))

# Every transfer has the same characteristic polynomial, not merely the same determinant.
base_poly = transfer(serial).charpoly(lam).as_expr()
for order in itertools.permutations(range(3)):
    assert sp.factor(transfer(order).charpoly(lam).as_expr()-base_poly) == 0

half = {p:sp.Rational(1,2),q:sp.Rational(1,2),r:sp.Rational(1,2)}
assert a[0].subs(half) == sp.Rational(9,16)
assert b[0].subs(half) == sp.Rational(1,2)
assert sp.factor(chi_s.subs(half) - lam*(lam**2-sp.Rational(9,16)*lam+sp.Rational(1,16))) == 0
assert sp.factor(chi_b.subs(half) - lam**2*(lam-sp.Rational(1,2))) == 0

# Numerical tests do not prove the theorem; the symbolic identities and root sign argument do.
rates = (0.1, 0.25, 0.5, 0.7, 0.9)
count = 0
for pv, qv, rv in itertools.product(rates, repeat=3):
    if count >= 100:
        break
    matrices=[]
    for k, x in enumerate((pv,qv,rv)):
        v = np.zeros(4);v[k]=1.;v[k+1]=-1.
        matrices.append(np.eye(4)-x*np.outer(v,v))
    def empirical(order):
        T=np.eye(4)
        for edge in order: T=matrices[edge]@T
        E=T-np.ones((4,4))/4
        return np.linalg.norm(E, 'fro')**2, np.linalg.norm(E,2)**2, np.linalg.eigvals(T)
    f_s,w_s,e_s=empirical(serial)
    f_b,w_b,e_b=empirical(batched)
    d = 4*pv*qv*qv*rv*(1-pv)*(1-rv)
    assert abs((f_s-f_b)-d)<1e-10
    assert f_b < f_s and w_s < w_b
    assert np.allclose(np.poly(e_s),np.poly(e_b),atol=1e-10)
    count+=1
print('PASS: 6 symbolic schedule classes, characteristic invariance, five exact identities, 100 numerical parameter triples')
