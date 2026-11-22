"""Exact algebraic check of the two-by-two erased-frame block invariants."""
import sympy as sp

d = sp.symbols('d', positive=True)
L = (d + 1) * (d + 2) / d**3
H = (d + 1) * (d + 2) / d**2
c = (d + 2) / (2*d)
alpha = 2 / (d*(d-1))
trace = sp.factor(L+H-c)
det = sp.factor(L*H-c*(L*(1-alpha)+H*alpha))
disc = sp.factor(trace**2-4*det)
assert sp.simplify(trace - (d+2)*(d*d+4*d+2)/(2*d**3)) == 0
assert sp.simplify(det - (d+1)*(d+2)**2/(2*d**4)) == 0
assert sp.simplify(disc - (d+2)**2*(d**4+12*d*d+16*d+4)/(4*d**6)) == 0
assert sp.simplify(disc - ((d+2)/(2*d**3))**2*(d**4+12*d*d+16*d+4)) == 0
print('SYMBOLIC_IDENTITIES_PASS')
