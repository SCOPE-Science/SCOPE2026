import sympy as sp
u,J,NmA,Q,B = sp.symbols("u J NmA Q B")
DE = J**2/sp.Integer(3)
p = u**3 - J*u**2 + DE*u + NmA
D1 = J**2 - 3*DE
Delta2 = (3*D1*(-J) - (-J)**3 + 27*NmA)**2 - 4*D1**3
assert sp.simplify(D1) == 0
assert sp.expand(sp.diff(p,u) - 3*(u-J/3)**2) == 0
assert sp.factor(Delta2 - (J**3 + 27*NmA)**2) == 0
triple_nmA = -J**3/sp.Integer(27)
assert sp.expand(p.subs(NmA,triple_nmA) - (u-J/3)**3) == 0
assert sp.simplify(Delta2.subs(NmA,triple_nmA)) == 0
assert Q not in p.free_symbols
assert Q not in sp.diff(p,u).free_symbols
print("VERIFY_OK")
