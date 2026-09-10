"""Derive + verify vertical-ray rank-one spherical wall equation and
Hodge-index/Mukai-square exclusion data. Target-directed (Step 1-3)."""
import sympy as sp

# Symbols
x, Q, N, M, sa, sv, r = sp.symbols('x Q N M s_a s_v r', real=True)
y = sp.symbols('y', real=True)

# Central charges at beta=0, omega=xH:
# Za = -sa + x^2 Q/2 + i x M ; Zv = -sv + r x^2 Q/2 + i x N
# Wall: Im(Za conj(Zv)) = Aa*Bv - Ba*Av = 0
Aa = -sa + x**2*Q/2
Ba = x*M
Av = -sv + r*x**2*Q/2
Bv = x*N
wall = sp.expand(Aa*Bv - Ba*Av)
print("wall numerator /x =", sp.factor(wall/x))

# Solve for y=x^2: wall/x = (-sa + yQ/2)N - M(-sv + r yQ/2) = 0
yy = sp.symbols('yy')
eq = (-sa + yy*Q/2)*N - M*(-sv + r*yy*Q/2)
sol = sp.solve(eq, yy)
print("y solution:", sol)
# spherical specialization sa=(D2+2)/2
D2, S = sp.symbols('D2 S')
sol_sph = sp.simplify(sol[0].subs(sa, (D2+2)/2).subs(sv, S))
print("y spherical:", sol_sph)

# b^2 expansion check: b=(r-1, C-D, S-sa), b^2=(C-D)^2-2(r-1)(S-sa)
# with C2 = v2+2rS, expand in D2, CDOT
v2, C2, CDOT = sp.symbols('v2 C2 CDOT')
b2 = (C2 - 2*CDOT + D2) - 2*(r-1)*(S - (D2+2)/2)
b2s = sp.expand(b2.subs(C2, v2+2*r*S))
print("b^2 =", b2s)
# expected: r*D2 - 2*CDOT + (v2+2S+2r-2)
print("b^2 - expected =", sp.expand(b2s - (r*D2 - 2*CDOT + (v2+2*S+2*r-2))))

# Hodge-defect upper envelope derivation (r>=2): maximize over t=sqrt(defect)
# bracket(t) = -r t^2 + 2 t K, K=sqrt(-Cperp2); max = K^2/r
t, K, rr = sp.symbols('t K rr', positive=True)
br = -rr*t**2 + 2*t*K
print("max of bracket:", sp.factor(br.subs(t, K/rr)), " at t=K/r")
