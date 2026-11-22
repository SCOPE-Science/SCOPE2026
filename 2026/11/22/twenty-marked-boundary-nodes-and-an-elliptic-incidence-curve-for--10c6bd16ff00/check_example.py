"""Exact characteristic-zero checks for one generic line--conic Hadamard witness.

Requires Python 3 and SymPy. This verifies nonempty Zariski-open conditions
used in the general geometric argument; the example is not itself a proof of
all generic statements.
"""
from itertools import combinations
import sympy as S

r, z, w = S.symbols('r z w')
k = [0, 1, 2, 4]
q = [z*z+z+2, z*z+3*z+3, 2*z*z+3*z+1, 3*z*z+z+4]
F = [(r+a)*b for a,b in zip(k,q)]

# Linear and quadratic independence: no plane or quadric contains the image.
for degree in (1, 2):
    polys = F if degree == 1 else [F[i]*F[j] for i in range(4) for j in range(i,4)]
    M = S.Matrix([[S.expand(f).coeff(r,a).coeff(z,b) for f in polys]
                  for a in range(degree+1) for b in range(2*degree+1)])
    assert M.rank() == len(polys)

# Distinct simple intersection points with each coordinate hyperplane.
for i in range(4):
    assert S.discriminant(q[i],z) != 0
    for j in range(i):
        assert S.resultant(q[i],q[j],z) != 0

# Distinct ruling lines meet where the 4x4 line-incidence determinant vanishes.
T = S.Matrix([[qi, ki*qi, qi.subs(z,w), ki*qi.subs(z,w)]
              for qi,ki in zip(q,k)])
D = S.factor(T.det()/(z-w)**2)
assert S.expand(D/4) == (17*z*z*w*w+5*z*z*w+5*z*w*w-40*z*w+5*z+5*w+27)
Q = S.expand(D/4)
assert S.expand(Q-Q.xreplace({z:w,w:z})) == 0
for inverted_z, inverted_w in [(False,False),(True,False),(False,True),(True,True)]:
    G = Q
    if inverted_z:
        G = S.expand(z*z*G.subs(z,1/z))
    if inverted_w:
        G = S.expand(w*w*G.subs(w,1/w))
    G = S.expand(G)
    basis = S.groebner([G,S.diff(G,z),S.diff(G,w)], z,w)
    assert list(basis) == [S.Integer(1)]
qd = S.factor(Q.subs(w,z))
assert qd == 17*z**4 + 10*z**3 - 40*z**2 + 10*z + 27
assert S.discriminant(qd,z) != 0

# For each coordinate plane: smooth conic, distinct ruling lines,
# simple conic/line intersections, and line crossing off the conic.
for i in range(4):
    J = [j for j in range(4) if j != i]
    C = S.Matrix([(k[j]-k[i])*q[j] for j in J])
    mon = [C[0]**2,C[0]*C[1],C[0]*C[2],C[1]**2,C[1]*C[2],C[2]**2]
    mat = S.Matrix([[S.expand(f).coeff(z,d) for f in mon] for d in range(5)])
    ns = mat.nullspace()
    assert len(ns) == 1
    a,b,c,d,e,f = ns[0]
    A = S.Matrix([[a,b/2,c/2],[b/2,d,e/2],[c/2,e/2,f]])
    assert A.det() != 0
    U = S.Matrix([q[j] for j in J]); V = S.Matrix([k[j]*q[j] for j in J])
    H = U.cross(V)
    assert S.resultant(q[i],S.factor(H.dot(C.diff(z))),z) != 0
    roots = S.solve(q[i],z)
    assert len(roots) == 2
    H1 = H.subs(z,roots[0]); H2 = H.subs(z,roots[1]); P = H1.cross(H2)
    assert P != S.zeros(3,1)
    assert S.simplify((P.T*A*P)[0]) != 0

# The double curve is nonplanar: four distinct incidence pairs give
# linearly independent points in P3, hence the rational cubic is twisted.
pairs = [(S.Integer(-14),S.Rational(-1,2)),
         (S.Integer(-14),S.Rational(43,1631)),
         (S.Integer(-1),S.Rational(-11,3)),
         (S.Integer(0),S.Rational(-27,5))]
pts=[]
for v1,v2 in pairs:
    assert S.simplify(Q.subs({z:v1,w:v2})) == 0
    MM = S.Matrix([[qi.subs(z,v1), ki*qi.subs(z,v1),
                    qi.subs(z,v2), ki*qi.subs(z,v2)] for qi,ki in zip(q,k)])
    assert MM.rank() == 3
    n = MM.nullspace()[0]
    pts.append(MM[:,:2]*n[:2,:])
assert S.Matrix.hstack(*pts).rank() == 4

# Nonimmersion values in an affine chart occur exactly at four simple
# diagonal ruling-incidence parameters.
Jac = S.Matrix.hstack(S.Matrix(F),S.Matrix([S.diff(f,r) for f in F]),
                        S.Matrix([S.diff(f,z) for f in F]))
minors = [Jac[list(I),:].det() for I in combinations(range(4),3)]
Gb = S.groebner(minors,r,z,order='lex')
assert S.Poly(Gb.polys[-1].as_expr(),z).monic().as_expr() == S.Poly(qd,z).monic().as_expr()
print('PASS: incidence genus-one witness, four simple diagonal contacts,')
print('      four 5-node coordinate plane sections, nonplanar double cubic.')
