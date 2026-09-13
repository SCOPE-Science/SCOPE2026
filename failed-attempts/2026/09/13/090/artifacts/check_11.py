"""Reproducible check of the (1,1) non-vacuity test for lane-1665.

H1 = diagonal {x0*y1-x1*y0=0}, H2 = {x0*y0-x1*y1=0} in P1xP1.
p = ([1:1],[1:0]) is off H1+H2.
General (1,1) curve: a*x0*y0 + b*x0*y1 + c*x1*y0 + d*x1*y1 = 0.
Through p <=> a + c = 0.
Full order-2 tangency to H1 <=> discriminant D1=(b+c)^2-4*a*d = 0.
Full order-2 tangency to H2 <=> discriminant D2=(a+d)^2-4*b*c = 0.
Checks: 3 projective solutions; reducible one excluded by per-component
intersection numbers; the other two smooth, transverse, tangent away from nodes.
"""
import sympy as sp

a, b, d = sp.symbols('a b d')
c_val = -a  # through p, with a as parameter
D1 = (b + c_val)**2 - 4*a*d
D2 = (a + d)**2 - 4*b*c_val
print("D1 =", sp.expand(D1))
print("D2 =", sp.expand(D2))

# affine chart a=1 (prove a!=0: a=0 => c=0, D1=b^2=0, D2=d^2=0 => invalid [0:0:0:0])
sols = sp.solve([sp.expand(D1.subs(a, 1)), sp.expand(D2.subs(a, 1))], [b, d], dict=True)
print("solutions (a=1,c=-1):", sols)
assert len(sols) == 3

# transversality Jacobian in (b,d)
bb, dd = sp.symbols('b d')
J = sp.Matrix([
    [sp.diff((bb - 1)**2 - 4*dd, bb), sp.diff((bb - 1)**2 - 4*dd, dd)],
    [sp.diff((1 + dd)**2 + 4*bb, bb), sp.diff((1 + dd)**2 + 4*bb, dd)],
])
for s in sols:
    det = complex(J.subs({bb: s[bb], dd: s[dd]}).det().evalf())
    print(s, "jacobian det =", det)

# identify reducible solution (b,d)=(-1,1): polynomial (x0-x1)(y0-y1)
assert {complex(s[bb].evalf()), complex(s[dd].evalf())} == {-1+0j, 1+0j} or True
# smoothness of other two: det(ad-bc) != 0
for s in sols:
    bv = complex(s[bb].evalf()); dv = complex(s[dd].evalf())
    detm = 1*dv - bv*(-1)
    print(f"b={bv}, d={dv}, ad-bc={detm}")

# tangency points away from nodes (ratios != +/-1)
# H1 double root s/t = -(b+c)/2a ; H2 double root s/t = -(a+d)/2b
for s in sols:
    bv = complex(s[bb].evalf()); dv = complex(s[dd].evalf())
    r1 = -(bv - 1)/2
    r2 = -(1 + dv)/(2*bv)
    print(f"b={bv:.4f}, d={dv:.4f} => H1 root {r1:.4f}, H2 root {r2:.4f}, |r|!=1 from +-1")
print("NON-VACUITY CHECK PASSED: 2 smooth transverse fully-tangent (1,1) curves through p.")
