"""Exact symbolic checks of the limiting Fourier-symbol identities.
Requires SymPy. These checks supplement the analytic proof.
"""
import sympy as sp
r=2-sp.sqrt(3)
s=1/(4*sp.sqrt(3))
A=2*s
x=sp.symbols('x',real=True)
D=1-2*r**2*x+r**4
a=2*s-8*s**2*(1-r**4)/D
# |1+exp(i theta)|^2 = 2(1+cos(theta))
babs2=sp.expand(4*sp.sqrt(2)*s**2*(1-r)**2*(1-r**2))**2 * 2*(1+x)/D**2
assert sp.simplify(babs2-(A-a)*(A-2*a)) == 0
assert sp.simplify(a.subs(x,1)-A/3) == 0
assert sp.simplify(a.subs(x,-1)-A/2) == 0
assert sp.simplify(sp.diff(a,x) * D**2).is_negative  # monotonicity in cosine
print('Exact limiting determinant and endpoint identities verified.')
