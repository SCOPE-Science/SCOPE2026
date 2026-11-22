"""Formal algebra certificate for the three-defect balancing identity.

Requires sympy; run python3 verify_symbolic.py. The exact all-parameter
positivity is proved in the accompanying mathematics, not by sampling.
"""
import sympy as s
A,B,C,q,u,c=s.symbols('A B C q u c')
X=A+B*C
Y=B+A*C
Z=C+A*B
Xnew=q*A+B*C/q
Ynew=B/q+q*A*C
S=(X**2+Y**2+Z**2)
Snew=(Xnew**2+Ynew**2+Z**2)
T=X*Y*Z
Tnew=Xnew*Ynew*Z
H=(1-q**2)*(q**2*A**2-B**2)/q**2
assert s.cancel(S-Snew - H*(1+C**2)) == 0
assert s.cancel(T-Tnew - H*C*(A*B+C)) == 0
r=1+A*B*C
lhs=s.expand((1+u*c*r)*(S-Snew)-2*u*c*(T-Tnew))
rhs=H*((1+C**2)+u*c*(1-C**2)*(1-A*B*C))
assert s.cancel(lhs-rhs)==0
print('SYMBOLIC_VERIFY_OK: both exact finite-difference factors and the final determinant inequality certificate')
