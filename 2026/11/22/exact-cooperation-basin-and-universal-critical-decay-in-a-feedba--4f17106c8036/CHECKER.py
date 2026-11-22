"""Symbolic verification of the exact global-feedback replicator basin theorem.

Requires Python 3 and SymPy. Checks identities and one fully admissible example;
the all-parameter conclusions follow from the analytic proof in RESULT.md.
"""
import sympy as S

s = S.symbols('s', real=True, positive=True)
a,b,h,B,q = S.symbols('a b h B q', positive=True)
A = a-b
D = b+B-a-h
E = S.exp
M = E(-a*s)*(1-q+q*E(-h*s))
Q = q*E(-h*s)/(1-q+q*E(-h*s))
F = (1-q)*(b/a+(1-b/a)*E(-a*s)) + q*((b+B)/(a+h)+(1-(b+B)/(a+h))*E(-(a+h)*s))
assert S.simplify(S.diff(F,s) - (-(1-q)*A*E(-a*s)+q*D*E(-(a+h)*s))) == 0
assert S.simplify(S.diff(Q,s) + h*Q*(1-Q)) == 0
assert S.simplify(S.diff(M,s) + (a+h*Q)*M) == 0
assert S.simplify(S.diff(F,s) - M*(b+B*Q) - S.diff(M,s)) == 0
assert S.simplify(F.subs(s,0)-1) == 0

# For the critical turning point, use the stationary relation
# q*D*exp(-(a+h)*s*)=(1-q)*A*exp(-a*s*).
# This gives q(s*)=A/(A+D), K=h*A*D/[2(A+D)].
q_star = A/(A+D)
K = h*A*D/(2*(A+D))
assert S.simplify(h*q_star*(1-q_star)/K -2/(A+D)) == 0

# Exactly admissible rational data from the manuscript.
a0,b0,h0,B0=S.Rational(3,5),S.Rational(1,5),S.Rational(2,5),S.Rational(6,5)
q0=S.Rational(3,4)
A0=a0-b0;D0=b0+B0-a0-h0
ss=S.log(q0*D0/((1-q0)*A0))/h0
H=S.simplify(F.subs({a:a0,b:b0,h:h0,B:B0,q:q0,s:ss}))
assert S.simplify(H-(S.Rational(17,15)+1/(45*S.sqrt(3)))) == 0
assert S.Rational(10,9)<H<S.Rational(5,4) # p=0.9 cooperates, p=0.8 defects
assert S.simplify(K.subs({a:a0,b:b0,h:h0,B:B0})-S.Rational(1,25)) == 0
assert S.simplify((2/(A+D)).subs({a:a0,b:b0,h:h0,B:B0})-S.Rational(5,2)) == 0
assert S.simplify(S.diff(F,s,2).subs({a:a0,b:b0,h:h0,B:B0,q:q0,s:ss})+h0*(1-q0)*A0*S.exp(-a0*ss)) == 0
print('PASS: integrator, derivative, critical amplitude and exact rational example')
