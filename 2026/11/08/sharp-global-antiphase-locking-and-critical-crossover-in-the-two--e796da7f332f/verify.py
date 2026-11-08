"""Symbolic and numerical corroboration of the two-clock sine-map theorem.

Requires Python 3 and SymPy.  Numerical tests are not infinite-time proofs.
"""
import math
import sympy as sp

v = sp.symbols('v', positive=True)
g = 2*sp.sin(v)-v
series = sp.series(1/g**2-1/v**2, v, 0, 5).removeO().expand()
assert sp.simplify(series.coeff(v,0)-sp.Rational(2,3)) == 0
assert sp.simplify(series.coeff(v,2)-sp.Rational(3,10)) == 0
assert sp.simplify(sp.Rational(3,10)/sp.Rational(2,3)-sp.Rational(9,20)) == 0

# Global monotonicity corroboration over a broad, deterministic phase mesh.
monotonic_checks=0
for h in (0.01, 0.25, 0.5, 0.9, 1.0):
    for j in range(1,1000):
        u = j*math.pi/1000
        assert abs(u-2*h*math.sin(u)) < u
        monotonic_checks+=1

# Critical inverse-square corrected values approach an initial-data-dependent constant.
critical_cases=0
for v0 in (.45,.8,1.2,1.5):
    val=v0
    record={}
    for n in range(1,160001):
        val=abs(val-2*math.sin(val))
        if n in (40000,80000,160000):
            record[n] = 1/val**2-sp.Rational(2,3).__float__()*n-.45*math.log(n)
    assert abs(record[160000]-record[80000])<0.003
    critical_cases+=1

# Subcritical universal crossover with decreasing steps.
t=.75
exact=(math.exp(4*t)-1)/6
values=[]
for eps in (.02,.01,.005,.0025):
    val=.8
    for k in range(int(t/eps)):
        val=2*(1-eps)*math.sin(val)-val
        assert val>0
    values.append(eps/(val*val))
assert abs(values[-1]-exact)<0.2
assert abs(values[-1]-exact)<abs(values[0]-exact)
assert all(values[k]>values[k+1] for k in range(len(values)-1))
print('VERIFY_OK exact_critical_coefficients=3 global_mesh_checks=%s critical_orbits=%s crossover_sequences=%s' % (monotonic_checks,critical_cases,len(values)))
