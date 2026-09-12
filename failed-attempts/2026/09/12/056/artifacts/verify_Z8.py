import sympy as sp
s,t=sp.symbols('s t')
b=(s**2+1)*(t**2+1)-2*s*t
# discriminant in t
Dt=sp.expand(sp.Poly(b,t).discriminant())
print("Disc_t =", sp.factor(Dt))
Ds=sp.expand(sp.Poly(b,s).discriminant())
print("Disc_s =", sp.factor(Ds))
# s-roots: s^4+1=0
roots_s=[sp.exp(sp.I*sp.pi/4+k*sp.I*sp.pi/2) for k in range(4)]
pts=set()
for r in roots_s:
    A=r**2
    # solve (A+1)t^2 -2 r t + (A+1)=0
    disc=sp.simplify(4*r**2-4*(A+1)**2)
    sq=sp.sqrt(disc)
    for sgn in [1,-1]:
        tv=sp.simplify((2*r+sgn*sq)/(2*(A+1)))
        pts.add(sp.simplify((r,tv)))
print("num pts s-chart:", len(pts))
for p in pts:
    print(sp.simplify(p[0]), sp.simplify(p[1]), "t^4+1=", sp.simplify(p[1]**4+1), "b=", sp.simplify(b.subs({s:p[0],t:p[1]})))
# check distinctness and t^4+1=0 exact: use minimal polys
print("s^4+1 all:", [sp.simplify(r**4+1) for r in roots_s])
