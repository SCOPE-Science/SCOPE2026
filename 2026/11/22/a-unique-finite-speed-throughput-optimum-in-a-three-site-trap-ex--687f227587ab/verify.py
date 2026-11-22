"""Exact eight-state stationary-generator check for a three-site site-trap SEP.

Requires SymPy. Run: python verify.py
The proof of uniqueness additionally uses Descartes' rule and the elementary
bounds documented in RESULT.md; finite samples are not substituted for proof.
"""
from itertools import product
import sympy as sp

rho, delta, t = sp.symbols('rho delta t', real=True)
q = sp.Rational(1, 2)
states = list(product((0, 1), repeat=3))
index = {state: k for k, state in enumerate(states)}
Q = sp.zeros(8)

def add_edge(state, target, rate):
    i, j = index[state], index[target]
    Q[j, i] += rate
    Q[i, i] -= rate

for x in states:
    # A contact with density a flips the boundary site at rate a/2 if
    # vacant and (1-a)/2 if occupied.
    for k, a in ((0, rho + q*delta), (2, rho - q*delta)):
        y = list(x)
        y[k] ^= 1
        add_edge(x, tuple(y), q*(a if x[k] == 0 else 1-a))
    # Site departure rates for boundary, centre, boundary: 1/2, 1/(2t), 1/2.
    for k in (0, 1):
        if x[k] != x[k+1]:
            y = list(x)
            y[k], y[k+1] = y[k+1], y[k]
            # Determine the occupied origin rather than inferring direction.
            origin = k if x[k] else k+1
            departure = t if origin == 1 else 1
            add_edge(x, tuple(y), q/departure)

assert all(sp.expand(z) == 0 for z in list(sp.ones(1, 8)*Q))
A = Q.copy()
A[7, :] = sp.ones(1, 8)
b = sp.zeros(8, 1)
b[7] = 1
pi = A.inv() * b
assert all(sp.cancel(z) == 0 for z in Q*pi)
assert sp.cancel(sum(pi)-1) == 0

I_left = sp.Matrix([[q*x[0]*(1-x[1]) - q*x[1]*(1-x[0])/t for x in states]])
I_right = sp.Matrix([[q*x[1]*(1-x[2])/t - q*x[2]*(1-x[1]) for x in states]])
I_contact = sp.Matrix([[q*((rho+q*delta)*(1-x[0]) - (1-rho-q*delta)*x[0]) for x in states]])
J_exact = sp.factor((I_left*pi)[0])
B = delta**2*t*(t-1)**2 + 8*(t+1)*(2*t+1)*(1+rho*(t-1))
formula = delta*(2*t+1)*(t+1+rho*(t-1))/B
assert sp.cancel(J_exact-formula) == 0
assert sp.cancel((I_right*pi)[0]-formula) == 0
assert sp.cancel((I_contact*pi)[0]-formula) == 0
assert sp.cancel(formula.subs(t, 1)-delta/8) == 0
assert sp.cancel(sp.limit(formula, t, 0, dir='+')-delta/8) == 0
assert sp.limit(formula, t, sp.oo) == 0

P = (2*(1+rho)*(delta**2+16*rho)*t**4
    +2*(3-rho)*(delta**2+16*rho)*t**3
    +(8*rho*(5-3*rho)-(3*rho+5)*delta**2)*t**2
    -4*(1-rho)*(delta**2+4*rho)*t
    +(1-rho)*(delta**2-8*rho))
assert sp.cancel(sp.diff(formula,t) + delta*P/B**2) == 0
assert sp.cancel(P.subs(t,1)-144*rho) == 0
assert sp.cancel(formula-delta/8 + delta*t*(t-1)*(delta**2*(t-1)+8*rho*(2*t+1))/(8*B)) == 0
assert sp.factor(P.subs({rho:q,delta:1})) == sp.Rational(3,2)*(3*t+1)**2*(2*t**2+2*t-1)
root = (sp.sqrt(3)-1)/2
assert sp.simplify(formula.subs({rho:q,delta:1,t:root})-(3*sp.sqrt(3)-2)/23) == 0

# Independent rational CTMC solve and checks across the admissible domain.
for density in (sp.Rational(1,4), sp.Rational(1,2), sp.Rational(3,4)):
    for contrast in (sp.Rational(1,4), sp.Rational(1,2), 1):
        if contrast > 2*min(density, 1-density):
            continue
        for dwell in (sp.Rational(1,5), sp.Rational(1,3), 1, 2, 7):
            M = A.subs({rho:density,delta:contrast,t:dwell})
            numer = b
            p = M.LUsolve(numer)
            assert all(z >= 0 for z in p)
            v = (I_left.subs(t,dwell)*p)[0]
            expected = formula.subs({rho:density,delta:contrast,t:dwell})
            assert sp.cancel(v-expected)==0
print('PASS: symbolic generator/three current equalities, exact derivative, limits, factorization, 45 rational sample checks.')
