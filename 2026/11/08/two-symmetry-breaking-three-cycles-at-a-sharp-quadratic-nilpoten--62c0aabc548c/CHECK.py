"""Exact reproducibility checks for the quadratic nilpotent-map three-cycle classification.

Requires Python 3 and SymPy. Run: python CHECK.py
Symbolic identities are checked exactly; numerical root tests are supplementary.
"""
import sympy as sp

u, v, w, t, K, S, q, r = sp.symbols('u v w t K S q r')
g = lambda x: x * (x - 1)
res = [u - K*(g(v)-g(w))**2,
       v - K*(g(w)-g(u))**2,
       w - K*(g(u)-g(v))**2]
assert sp.expand(res[0]-res[1] -
    (u-v)*(1 + K*(u+v-1)*(g(u)+g(v)-2*g(w)))) == 0

Q = S**2 - 2*q
H = sp.expand((S-1-t)*(Q-S-3*t**2+3*t)+1/K)
q_of_S = -S**2 + 4*S - 3
r_of_S = -(S-1)**2*(S-2) - 1/(3*K)
assert sp.simplify(H.subs(q,q_of_S)/3 -(t**3-S*t**2 + q*t-r).subs({q:q_of_S,r:r_of_S})) == 0

sum_diff_sq = (2*S**4-4*S**3-8*S**2*q+2*S**2+14*S*q+12*S*r+
               2*q**2-6*q-18*r)
assert sp.expand(sum((g(b)-g(c))**2 for b,c in [(v,w),(w,u),(u,v)])-
    sum_diff_sq.subs({S:u+v+w,q:u*v+v*w+w*u,r:u*v*w})) == 0
assert sp.simplify((S-K*sum_diff_sq).subs({q:q_of_S,r:r_of_S})-(5*S-6)) == 0

C = sp.expand((t-sp.Rational(1,5))**2*(t-sp.Rational(4,5)) + 1/(3*K))
assert sp.factor(sp.discriminant(C,t)-3*(12*K-125)/(125*K**2)) == 0
assert sp.factor(C.subs(K,sp.Rational(125,12)) - t*(t-sp.Rational(3,5))**2)==0
assert sp.simplify((C.subs(t,sp.Rational(3,5))).subs(K,sp.Rational(125,12)))==0
assert sp.simplify(C.subs(t,0) + (12*K-125)/(375*K)) == 0
assert sp.simplify(C.subs(t,sp.Rational(3,5)) + (12*K-125)/(375*K)) == 0
# Both statements at 0 and 3/5 coincide due to the repeated-root onset.

# The converse uses only Vieta's constraints and each candidate root equation.
b, a = sp.symbols('b a')
otherdiff_sq = (sp.Rational(6,5)-t)**2 - 4*(sp.Rational(9,25)-t*(sp.Rational(6,5)-t))
assert sp.expand(otherdiff_sq-3*t*(sp.Rational(4,5)-t))==0
assert sp.factor(sp.together(3*K*(sp.Rational(4,5)-t)*(t-sp.Rational(1,5))**2 - 1 + 3*K*C))==0

# The repeated-coordinate branch: K*s(s-1)^2=1; its stationary points.
s=sp.symbols('s')
assert sp.factor(sp.diff(s*(s-1)**2,s)) == (s-1)*(3*s-1)
assert sp.Rational(27,4)*(sp.Rational(1,3))*(sp.Rational(1,3)-1)**2 == 1
assert sp.Rational(125,12)*(sp.Rational(3,5))*(sp.Rational(3,5)-1)**2 == 1

# Supplementary high-precision root-position and orbit tests; NOT the proof.
for kval in (sp.Rational(21,2), 12, 20, 100):
    roots = sorted(float(sp.re(x)) for x in sp.nroots(C.subs(K,kval),maxsteps=200))
    assert 0<roots[0]<.2<roots[1]<.6<roots[2]<.8
    for ordered in (roots, list(reversed(roots))):
        for i in range(3):
            x,y,z=[ordered[(i+j)%3] for j in range(3)]
            assert abs(x-float(kval)*(y*(y-1)-z*(z-1))**2)<1e-8
print('PASS: exact difference, cubic, symmetric, discriminant, converse and repeated-branch identities; 24 numerical cycle checks')
