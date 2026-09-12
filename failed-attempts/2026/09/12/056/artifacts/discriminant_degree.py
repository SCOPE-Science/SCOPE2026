import sympy as sp
t=sp.Symbol('t')
# Generic monodromy-free argument: discriminant of 4-dim complete-intersection-free family is a polynomial in t;
# here check special fibre t=1/100 smooth (done) + construct 16-dim bound via Bezout on singular eqs minus t.
# Instead: eliminate variables from singular system over Q(t) — check GB over QQ(t) contains 1 after clearing denominators.
x0,x1,x2=sp.symbols('x0 x1 x2')
F1 = x0 - x1*x2
F2 = x0**2+x1**2+x2**2+1 - x0 - x1*x2
G = x0**4+x1**4+x2**4+1
H = F1*F2 + t*G
eqs=[H,sp.diff(H,x0),sp.diff(H,x1),sp.diff(H,x2)]
Gb=sp.groebner(eqs,x0,x1,x2,t,order='lex')
print("num polys:", len(Gb.polys))
seen=False
for p in Gb.polys:
    s=str(p.as_expr())
    if 'x0' not in s and 'x1' not in s and 'x2' not in s:
        print("PURE-t poly:", p); seen=True
if not seen: print("no pure-t poly in first scan; last polys:")
for p in list(Gb.polys)[-5:]: print("  ", p)
