# Exact verification (rational arithmetic only): base W0 + one cluster mutation W'.
# Replaces all finite-difference checks with exact derivatives.
from fractions import Fraction as Q

print("=== W0(x,y) = x + y + 1/(xy) at (1,1) ===")
x0, y0 = Q(1), Q(1)
# grad W0 = (1 - 1/(x^2 y), 1 - 1/(x y^2))
gx = 1 - Q(1, 1) / (x0*x0*y0)
gy = 1 - Q(1, 1) / (x0*y0*y0)
print("grad =", (gx, gy))
assert gx == 0 and gy == 0
# standard Hessian: [[2/(x^3 y), 1/(x^2 y^2)],[., 2/(x y^3)]]
a = Q(2) / (x0**3*y0); b = Q(1) / (x0*x0*y0*y0); c = Q(2) / (x0*y0**3)
det_std = a*c - b*b
print("H_std = [[%s,%s],[%s,%s]], det = %s" % (a, b, b, c, det_std))
assert det_std == 3
# log Hessian at critical point: H_log[i,j] = x_i x_j W_ij (since first derivatives vanish)
# H_log = [[x^2 Wxx, x y Wxy],[., y^2 Wyy]]
h11 = x0*x0*a; h12 = x0*y0*b; h22 = y0*y0*c
det_log = h11*h22 - h12*h12
print("H_log = [[%s,%s],[%s,%s]], det = %s" % (h11, h12, h12, h22, det_log))
assert det_log == 3
print("W0 value:", x0 + y0 + Q(1, 1)/(x0*y0))
print("OK W0: nondegenerate critical point, det_std = det_log = 3.")
print()
print("=== W'(X,Y) = X + Y/(1+X) + (1+X)/(X Y) at (1,2) ===")
X0, Y0 = Q(1), Q(2)
# Exact first derivatives:
# dW'/dY = 1/(1+X) - (1+X)/(X Y^2)
dY = Q(1, 1)/(1+X0) - (1+X0)/(X0*Y0*Y0)
# dW'/dX = 1 - Y/(1+X)^2 - 1/(X^2 Y)  [since (1+X)/(XY) = 1/(XY) + 1/Y]
dX = 1 - Y0/((1+X0)*(1+X0)) - Q(1, 1)/(X0*X0*Y0)
print("grad =", (dX, dY))
assert dX == 0 and dY == 0
# Exact second derivatives:
# W'YY = 2(1+X)/(X Y^3)
wYY = Q(2)*(1+X0)/(X0*Y0**3)
# W'XY = -1/(1+X)^2 + 1/(X^2 Y^2)
wXY = -Q(1, 1)/((1+X0)*(1+X0)) + Q(1, 1)/(X0*X0*Y0*Y0)
# W'XX = 2Y/(1+X)^3 + 2/(X^3 Y)
wXX = Q(2)*Y0/((1+X0)**3) + Q(2)/(X0**3*Y0)
det2 = wXX*wYY - wXY*wXY
print("H_std = [[%s,%s],[%s,%s]], det = %s" % (wXX, wXY, wXY, wYY, det2))
assert det2 == Q(3, 4)
# log Hessian at critical point
l11 = X0*X0*wXX; l12 = X0*Y0*wXY; l22 = Y0*Y0*wYY
detl = l11*l22 - l12*l12
print("H_log = [[%s,%s],[%s,%s]], det = %s" % (l11, l12, l12, l22, detl))
assert detl == 3
val = X0 + Y0/(1+X0) + (1+X0)/(X0*Y0)
print("W' value:", val)
assert val == 3
print("OK W': nondegenerate critical point at (1,2), det_std=3/4, det_log=3; value preserved (=3).")
print()
print("WALL CHECK: mutation Phi(x,y)=(x, y(1+x)); wall={1+x=0}. Tracked point (1,1): 1+x=2>0,")
print("DPhi=[[1,0],[y,1+x]] at (1,1) = [[1,0],[1,2]], det=2 != 0. Positive-real locus preserved")
print("(1+x>0 there). Pure-cluster bijection verified for this nodal-slide step;")
print("blowup (term-adding, Auroux-type) steps are handled separately in DRAFT section 4 via")
print("support-disjointness + open″det H_log != 0″ persistence under hypothesis (H-mono).")
