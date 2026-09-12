import sympy as sp
x0,x1,x2=sp.symbols('x0 x1 x2')
F1 = x0 - x1*x2
F2 = x0**2+x1**2+x2**2+1 - x0 - x1*x2
G = x0**4+x1**4+x2**4+1
tval = sp.Rational(1,100)
H = F1*F2 + tval*G
eqs = [H, sp.diff(H,x0), sp.diff(H,x1), sp.diff(H,x2)]
# Groebner to test emptiness in this chart (eliminate): if GB contains nonzero const -> no singular pts in chart
Gb = sp.groebner(eqs, x0,x1,x2, order='lex')
print("GB len:", len(Gb.polys))
for p in Gb.polys[:20]:
    print(p)
