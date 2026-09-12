"""Verify single nodal-slide wall-crossing in monotone dP1.

Checks:
 1. Exact Laurent identity  We(X,Y) = W0(X, 1/(X*Y)).
 2. Exponent-level GL(2,Z) equivalence of Newton polytopes.
 3. Exact Groebner bases of both log-critical schemes.
 4. Numerical critical values + log-Hessian determinants for both potentials.
Writes verification_output.txt next to this script.
"""
import numpy as np
import sympy as sp

out = []

x, y, X, Y = sp.symbols('x y X Y')
W0 = x + y + 1/(x*y) + 1/y
We = X + Y + X*Y + 1/(X*Y)

# 1. exact identity under Phi:(X,Y)->(x=X, y=1/(X*Y))
diff = sp.expand(We - W0.subs({x: X, y: 1/(X*Y)}))
out.append(f"identity We - Phi^*W0 = {diff}")
assert diff == 0

# 2. exponent map (a,b) -> (a-b,-b); matrix M=[[1,-1],[0,-1]], det=-1
M = sp.Matrix([[1, -1], [0, -1]])
out.append(f"exponent matrix det = {M.det()}")
assert M.det() in (1, -1)
W0exp = [(1, 0), (0, 1), (-1, -1), (0, -1)]
mapped = sorted(tuple(M*sp.Matrix([a, b])) for a, b in W0exp)
Weexp = sorted([(1, 0), (0, 1), (1, 1), (-1, -1)])
out.append(f"mapped exponents = {mapped}")
assert mapped == Weexp

# 3. Groebner bases of log-critical systems (exact)
xs, ys = sp.symbols('xs ys')
f1 = sp.simplify((xs*sp.diff(
    xs + ys + 1/(xs*ys) + 1/ys, xs)).as_numer_denom()[0])
f2 = sp.simplify((ys*sp.diff(
    xs + ys + 1/(xs*ys) + 1/ys, ys)).as_numer_denom()[0])
g1 = sp.simplify((xs*sp.diff(
    xs + ys + xs*ys + 1/(xs*ys), xs)).as_numer_denom()[0])
g2 = sp.simplify((ys*sp.diff(
    xs + ys + xs*ys + 1/(xs*ys), ys)).as_numer_denom()[0])
G0 = sp.groebner([f1, f2], xs, ys, order='lex')
Ge = sp.groebner([g1, g2], xs, ys, order='lex')
out.append(f"W0 log-crit GB = {G0}")
out.append(f"We log-crit GB = {Ge}")

# 4. numerics
def loghess_det_W0(xv, yv):
    M11 = xv + 1/(xv*yv); M12 = 1/(xv*yv)
    M21 = 1/(xv*yv); M22 = yv + 1/yv + 1/(xv*yv)
    return M11*M22 - M12*M21

def loghess_det_We(Xv, Yv):
    a = Xv + Xv*Yv + 1/(Xv*Yv); b = Xv*Yv + 1/(Xv*Yv)
    # M = [[x*df1/dx, y*df1/dy],[x*df2/dx, y*df2/dy]] computed directly
    # f1 = X + XY + 1/(XY) over X? use finite formula:
    M11 = Xv + Xv*Yv + 1/(Xv*Yv)
    M12 = Xv*Yv + 1/(Xv*Yv)
    M21 = Xv*Yv + 1/(Xv*Yv)
    M22 = Yv + Xv*Yv + 1/(Xv*Yv)
    return M11*M22 - M12*M21

yr = np.roots([1, 0, -2, -1, 1])      # y^4-2y^2-y+1
tr = np.roots([1, 1, 0, 0, -1])       # t^4+t^3-1
W0vals, Wevals = [], []
for yv in yr:
    xv = yv**3 - yv - 1
    assert abs(xv**2*yv - 1) < 1e-8
    W0vals.append(complex(xv + yv + 1/(xv*yv) + 1/yv))
    out.append(f"W0 x={xv:.6f} y={yv:.6f} W={W0vals[-1]:.6f} "
               f"det={loghess_det_W0(xv, yv):.6f}")
for tv in tr:
    Wevals.append(complex(tv + tv + tv*tv + 1/(tv*tv)))
    out.append(f"We t={tv:.6f} W={Wevals[-1]:.6f} "
               f"det={loghess_det_We(tv, tv):.6f}")
W0s = sorted(W0vals, key=lambda z: (z.real, z.imag))
Wes = sorted(Wevals, key=lambda z: (z.real, z.imag))
maxdev = max(abs(a - b) for a, b in zip(W0s, Wes))
out.append(f"max |W0crit - Wecrit| paired deviation = {maxdev:.3e}")
assert maxdev < 1e-6

text = "\n".join(out) + "\n"
with open("verification_output.txt", "w") as fh:
    fh.write(text)
print(text)
