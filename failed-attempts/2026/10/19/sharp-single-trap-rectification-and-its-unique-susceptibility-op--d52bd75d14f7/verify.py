"""Exact finite-state verification for a four-site boundary-driven exclusion model.

Requires Python 3 and SymPy. The rates here are multiplied by 2 relative
 to physical time units where all reference waiting times equal one.
"""
from itertools import product
import sympy as sp

u = sp.symbols('u', positive=True)
states = list(product((0, 1), repeat=4))
index = {state: j for j, state in enumerate(states)}
rate = (sp.Integer(1), u, sp.Integer(1), sp.Integer(1))

def generator(left, right):
    """Column generator with both reservoir exchange and site departure hops."""
    M = sp.zeros(16)
    for j, state in enumerate(states):
        for i in range(3):
            if state[i] == 1 and state[i+1] == 0:
                other = list(state)
                other[i], other[i+1] = 0, 1
                q = rate[i]
                M[index[tuple(other)],j] += q
                M[j,j] -= q
            elif state[i] == 0 and state[i+1] == 1:
                other = list(state)
                other[i], other[i+1] = 1, 0
                q = rate[i+1]
                M[index[tuple(other)],j] += q
                M[j,j] -= q
        for i, density in ((0,left),(3,right)):
            other = list(state)
            other[i] = 1-state[i]
            q = density if state[i] == 0 else 1-density
            M[index[tuple(other)],j] += q
            M[j,j] -= q
    return M

P = (232560*u**8 + 4331572*u**7 + 33739658*u**6 +
     142316303*u**5 + 351379457*u**4 + 510425170*u**3 +
     411771380*u**2 + 155893675*u + 15612625)
Q = (2380*u**5 + 24584*u**4 + 90837*u**3 +
     149179*u**2 + 108535*u + 27685)
B = (238*u**4 + 2642*u**3 + 10365*u**2 + 17100*u + 9975)
linear = u*B/Q
curvature = u*(u-1)*P/((u+1)*Q**2)

# Detailed-balance product distribution at half-filled equal reservoirs.
occupation = (sp.Rational(1,2), 1/(1+u), sp.Rational(1,2), sp.Rational(1,2))
p0 = sp.Matrix([
    sp.prod(occupation[i] if state[i] else 1-occupation[i]
            for i in range(4))
    for state in states
])
M0 = generator(sp.Rational(1,2), sp.Rational(1,2))
M1 = generator(sp.Rational(3,4), sp.Rational(1,4))-M0
# That difference corresponds to density contrast 1/2, so multiply by 2.
M1 = 2*M1
assert all(sp.cancel(v)==0 for v in M0*p0)
assert sp.simplify(sum(p0)-1) == 0
A = M0.copy()
A[15,:] = sp.ones(1,16)
M1[15,:] = sp.zeros(1,16)
print('invert',flush=True)
AI = A.inv(method='DM')
p1 = AI*(-M1*p0)
print('p1',flush=True)
p2 = AI*(-M1*p1)
print('p2',flush=True)
current_vec = sp.Matrix([[(u if st[1] and not st[2] else
                          -1 if st[2] and not st[1] else 0)
                         for st in states]])
# Current uses physical per-neighbor hop rates of one half.
linear_computed=sp.factor((current_vec*p1)[0]/2)
print('computed first',flush=True)
assert sp.simplify(linear_computed-linear)==0
curvature_computed=sp.factor((current_vec*p2)[0]/2)
print('computed second',flush=True)
assert curvature_computed == curvature
print('Exact product measure, two perturbative stationarity equations, and two current coefficients: PASS')

# The first nonvanishing even-current coefficient is zero iff the defect vanishes.
assert all(c > 0 for c in sp.Poly(P,u).all_coeffs())
assert all(c > 0 for c in sp.Poly(Q,u).all_coeffs())
assert all(c > 0 for c in sp.Poly(B,u).all_coeffs())

# Unique optimum of absolute rectification curvature on the physical trap interval (0,1).
x = sp.symbols('x', positive=True)
N = sp.together(sp.diff(curvature,u)).as_numer_denom()[0]
poly = sp.Poly(sp.cancel(N.subs(u,x/(1+x))*(1+x)**15),x)
assert poly.degree() == 15
signs = [sp.sign(c) for c in poly.all_coeffs()[::-1]]  # constant term first
assert signs == [-1]*7+[1]*9
# Descartes' rule: one positive root at most; existence from opposite endpoint signs.
assert sp.sign(N.subs(u,0)) < 0 and sp.sign(N.subs(u,1)) > 0
opt = sp.nsolve(sp.diff(curvature,u),sp.Rational(1,3),prec=40)
assert 0<opt<1
assert abs(float(sp.diff(curvature,u).subs(u,opt)))<1e-25
print('One-sign-change transformed derivative; unique physical maximizer of magnitude: PASS')
print('u_* =',sp.N(opt,20),'a2(u_*) =',sp.N(curvature.subs(u,opt),20))
print('trap depth E/T =',sp.N(-sp.log(opt),20))

# Separate exact finite-bias stationary solutions cross-check the perturbative limit.
for a in [sp.Rational(1,5),sp.Rational(1,2),sp.Integer(2)]:
    for d in [sp.Rational(1,100),sp.Rational(1,200)]:
        W = generator((1+d)/2,(1-d)/2).subs(u,a)
        V = W.copy()
        V[15,:] = sp.ones(1,16)
        rhs = sp.zeros(16,1)
        rhs[15] = 1
        probs = V.inv(method='DM')*rhs
        flux = sp.Rational(1,2)*(current_vec.subs(u,a)*probs)[0]
        pred = linear.subs(u,a)*d+curvature.subs(u,a)*d*d
        # The omitted analytic term is cubic; this numerical bound only corroborates.
        assert abs(float(flux-pred)) < 2e-7
print('Independent exact finite-driving stationarity checks: PASS')
