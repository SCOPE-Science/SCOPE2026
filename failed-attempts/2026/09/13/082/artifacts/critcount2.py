from sympy import symbols, diff, together, Poly, solve, resultant, N

def count_crit(W, x, y, label):
    Wx = diff(W, x); Wy = diff(W, y)
    numx, denx = together(Wx).as_numer_denom()
    numy, deny = together(Wy).as_numer_denom()
    Fx = Poly(numx, x, y); Fy = Poly(numy, x, y)
    print("="*60)
    print(label, ": W =", W)
    ex = Fx.as_expr(); ey = Fy.as_expr()
    print("  Fx =", ex, " Fy =", ey)
    resx = resultant(ex, ey, y)
    rx = Poly(resx, x)
    print("  resultant_x degree:", rx.degree(), " roots:", len(rx.all_roots()))
    sols = solve([ex, ey], [x, y], dict=True)
    print("  nsols:", len(sols))
    for s in sols:
        print("   ", {str(k): complex(N(v)) for k,v in s.items()})

x, y = symbols('x y')
cands = {
 "P2-Clifford": x + y + 1/(x*y),
 "P1xP1": x + y + 1/x + 1/y,
 "Bl2-pent": x + y + 1/(x*y) + 1/x + 1/y,
 "guess-oct": x*y + x + x/y + y + 1/y + y/x + 1/x + 1/(x*y),
 "guess-dP4-A": x*y + x + y + 1/y + 1/x + 1/(x*y),
 "guess-dP4-B": x + y + 1/(x*y) + 2/x + 2/y,
}
for k,v in cands.items():
    count_crit(v, x, y, k)
