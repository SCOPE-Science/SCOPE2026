"""Symbolic identity and finite trajectory diagnostics for the herd-response map.

Run: python check.py
Requires: sympy (for exact symbolic checks); Python standard library.
Finite trajectories are diagnostics and are not proofs of asymptotic statements.
"""
import math
import sympy as sp

v, a, d, B = sp.symbols('v a d B', positive=True)
H = a*v + B*v*v
D = 1 - (1-H)*sp.exp(H - a*v/sp.sqrt(1-H))
V = v*sp.exp(d*(sp.sqrt(1-H)-1))
def coeff(expr, degree, order):
    return sp.factor(sp.series(expr, v, 0, order).removeO().expand().coeff(v, degree))
assert sp.simplify(coeff(D - (a*V+B*V**2), 2, 3) - (a*a*(d+1)-2*B)/2) == 0
B0 = a*a*(d+1)/2
Vs = V.subs(B, B0)
c = a*d/2
e = -a*a*d*(d+3)/8
assert sp.simplify(coeff(Vs,2,3) + c) == 0
assert sp.simplify(coeff(Vs,3,4) - e) == 0
assert sp.simplify((c*c-e)/c-3*a*(d+1)/4) == 0
print('exact symbolic checks: PASS')

for aa,dd,xx,yy in [(1.0,2.0,0.996,0.004),(0.7,0.9,0.999,0.003)]:
    cc=aa*dd/2
    gamma=3*aa*(dd+1)/4
    small=aa*aa*(dd+1)/2
    records={}
    for n in range(1,30001):
        nx=xx*math.exp(1-xx-aa*yy/math.sqrt(xx))
        ny=yy*math.exp(dd*(math.sqrt(xx)-1))
        xx,yy=nx,ny
        if n in (5000,30000):
            records[n]=(1/yy-cc*n-gamma*math.log(n),((1-xx)-aa*yy)/(yy*yy))
    assert abs(records[30000][0]-records[5000][0])<0.3,records
    assert abs(records[30000][1]-small)<0.002,records
    print('finite diagnostic',aa,dd,'clock',records[5000][0],records[30000][0],
          'slaving',records[30000][1])
print('finite trajectory diagnostics: PASS (not an infinite-time proof)')
