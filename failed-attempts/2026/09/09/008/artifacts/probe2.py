from sympy import symbols, QQ, Poly, factor_list
x, y = symbols('x y')
fi = x**2 + y + 1
fj = y**2 + y + 1
Ix = Poly(fi, x, y).resultant(Poly(fj, x, y), x)[0]
Iy = Poly(fi, x, y).resultant(Poly(fj, x, y), y)[0]
print('Ix=', Ix, Ix.gens)
print('Iy=', Iy, Iy.gens)
print('fac y:', factor_list(Ix, domain=QQ))
print('fac x:', factor_list(Iy, domain=QQ))
for (q, e) in factor_list(Iy, domain=QQ)[1]:
    print('qtype=', type(q), repr(q)[:120])
    print('  gens=', q.gens if isinstance(q, Poly) else None)
