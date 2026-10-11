from itertools import combinations
import sympy as sp

v = [0, 1, 2, 3]
xyz = [sp.symbols(f"x{i} y{i} z{i}") for i in range(1, 6)]
(x1,y1,z1),(x2,y2,z2),(x3,y3,z3),(x4,y4,z4),(x5,y5,z5)=xyz
cols = [
    sp.Matrix([x1,y1,z1,0]),
    sp.Matrix([x2,y2,z2,x2]),
    sp.Matrix([x3,y3,z3,2*x3]),
    sp.Matrix([x4,y4,z4,3*x4]),
    sp.Matrix([x5,0,y5,z5]),
]
M = sp.Matrix.hstack(*cols)

def D(rows, cols):
    return sp.expand(M.extract([r-1 for r in rows], [c-1 for c in cols]).det())

F = sp.expand(sp.Matrix([
    [0,    0,    z1, y1],
    [z2,   y2,   z2, y2],
    [2*z3, 2*y3, z3, y3],
    [3*z4, 3*y4, z4, y4],
]).det())

rhs_x = (
    7*y4*y5*D((1,2,3),(1,2,3))
    - 6*y3*y5*D((1,2,3),(1,2,4))
    + 4*(y3*z4-y4*z3)*D((1,2,3),(1,2,5))
    + 3*y2*y5*D((1,2,3),(1,3,4))
    + (y4*z2-y2*z4)*D((1,2,3),(1,3,5))
    - 3*y4*y5*D((2,3,4),(1,2,3))
    + 2*y3*y5*D((2,3,4),(1,2,4))
    - y2*y5*D((2,3,4),(1,3,4))
)
rhs_z = (
    6*y4*y5*D((1,2,3),(1,2,3))
    - 6*y3*y5*D((1,2,3),(1,2,4))
    + 6*y2*y5*D((1,2,3),(1,3,4))
    - 2*y4*y5*D((2,3,4),(1,2,3))
    + 2*y3*y5*D((2,3,4),(1,2,4))
    + 4*(y3*z4-y4*z3)*D((2,3,4),(1,2,5))
    - 2*y2*y5*D((2,3,4),(1,3,4))
    + (y4*z2-y2*z4)*D((2,3,4),(1,3,5))
)
assert sp.expand(rhs_x - x5*F) == 0
assert sp.expand(rhs_z - z5*F) == 0

subs = {
    x1:0,y1:1,z1:0,
    x2:0,y2:1,z2:1,
    x3:0,y3:1,z3:4,
    x4:0,y4:1,z4:9,
    x5:0,y5:1,z5:0,
}
Mw = M.subs(subs)
assert Mw.rank() == 2
for rows in combinations(range(1,5),3):
    for cs in combinations(range(1,6),3):
        assert sp.expand(D(rows,cs).subs(subs)) == 0
assert sp.expand(F.subs(subs)) == -12
print("VERIFY_OK")
print("F_witness=-12")
print("rank_M_witness=2")
