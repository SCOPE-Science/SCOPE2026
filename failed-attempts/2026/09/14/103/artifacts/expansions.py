"""Root/unit expansions for simplest cubic + resonant ray (exact symbolic low orders)."""
import sympy as sp
n=sp.symbols('n')
# lam0 = n + 2/n + c2/n^2 + c3/n^3? solve
c2,c3,c4=sp.symbols('c2 c3 c4')
lam = n+2/n+c2/n**2+c3/n**3+c4/n**4
expr = sp.expand(lam**3-(n-1)*lam**2-(n+2)*lam-1)
for k in [2,3,4]:
    coeff = sp.expand(expr).coeff(n,-k) if False else None
# get series coefficients via expansion in t=1/n
t=sp.symbols('t')
exprt = sp.expand(expr.subs(n,1/t))
for k in range(0,7):
    print(f"t^{k}:", sp.expand(exprt).coeff(t,k))
