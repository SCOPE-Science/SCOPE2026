"""Exact 16-state transfer determinant identity. Requires SymPy."""
import sympy as sym
z, t = sym.symbols('z t')
states=[(r,s,c,d) for r in (0,1) for s in (0,1) for c in (0,1) for d in (0,1)]
T = sym.zeros(16)
for i,(r,s,c,d) in enumerate(states):
    for j,(R,S,C,D) in enumerate(states):
        if C == (c+S if r else S) <= 1 and D == (d+R if S else R) <= 1:
            T[i,j] = z**(R+S)
q = 1-(1+4*z)*t+(2*z+4*z*z)*t*t-z*z*t**3
actual = (sym.eye(16)-t*T).det(method='berkowitz')
assert sym.expand(actual-q) == 0
print('det(I-tT)=',sym.factor(actual))
print('WHEEL_TRANSFER_DETERMINANT_PASS')
