"""Independent symbolic reduction for two-particle activity on complete bicliques.

Run: python verify_bipartite_symbolic.py (requires SymPy).
The physical parameter range is integers r,s >=1 and r+s>=4.
"""
import sympy as sp

r, s = sp.symbols('r s', positive=True)
n = r+s
Q = sp.Matrix([[-2*s, 2*s, 0],
               [r-1, -(n-2), s-1],
               [0, 2*r, -2*r]])
lam = sp.Matrix([2*s, n-2, 2*r])
pi = sp.Matrix([r*(r-1), 2*r*s, s*(s-1)]) / (n*(n-1))
mu = sp.factor((pi.T*lam)[0])
u = sp.Matrix(sp.symbols('u0:3'))
# Fix the additive constant using the stationary mean.
conditions = [sp.expand(x) for x in Q*u+lam-sp.ones(3, 1)*mu]
conditions += [(pi.T*u)[0]]
solution = sp.solve(conditions, list(u), dict=True)
assert len(solution) == 1
h = u.subs(solution[0])
variance = mu + 2*sp.factor((pi.T*sp.diag(*list(lam-mu*sp.ones(3, 1)))*h)[0])
fano = sp.factor(variance/mu)
target = 1 + (n**2+(r-s)**2*(n**2-6*n+4))/(n**2*(n-1)**2)
assert sp.cancel(fano-target) == 0
assert sp.cancel(mu-4*r*s*(n-2)/(n*(n-1))) == 0
print('PASS: symbolic Poisson equation, stationary cumulants, and all-size formula')
print('F-1 =', sp.factor(fano-1))
