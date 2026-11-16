"""Exact, reproducible checks for cube-edge harmonic-polynomial onset."""
from sympy import Matrix, Poly, symbols, diff, expand, factor, groebner
x, y, z = symbols('x y z')
u, v, w = symbols('u v w')
coords = (u, v, w)
B = [u*v, u*w, v*w, u*u*v, u*v*v, u*u*w, u*w*w,
     v*v*w, v*w*w, u*v*w]
R = [u*u, v*v, w*w, u*v, u*w, v*w, u, v, w]

def leps(Q, eps):
    return expand(sum(4*(t+1)*diff(Q,t,2) + (2+4*e)*diff(Q,t)
                      for t,e in zip(coords,eps)))

M = Matrix([[Poly(leps(q,(0,0,0)),*coords).coeff_monomial(t)
             for q in B] for t in R])
assert M.shape == (9, 10)
assert M.rank() == 9
assert M[:,[0,1,2,3,4,5,6,7,9]].det() == 110592
V = (u-v)*(u-w)*(v-w)
assert leps(V,(0,0,0)) == 0
assert all(not v0 for v0 in [leps(V,(0,0,0))])
for eps in ((1,0,0),(0,1,0),(0,0,1), (1,1,0),
            (1,0,1),(0,1,1)):
    L=Matrix([[Poly(leps(q,eps),*coords).coeff_monomial(t)
               for q in B[:3]] for t in coords])
    assert L.det() != 0
P = (x*x-y*y)*(x*x-z*z)*(y*y-z*z)
assert expand(sum(diff(P,t,2) for t in (x,y,z)))==0
for a in (x,y,z):
    q = [i for i in (x,y,z) if i != a]
    for s in (-1,1):
        for t in (-1,1):
            assert expand(P.subs({q[0]:s,q[1]:t})) == 0
assert [p.as_expr().as_poly(x,y,z).total_degree() for p in groebner(
       [(x*x-1)*(y*y-1),(x*x-1)*(z*z-1),(y*y-1)*(z*z-1)],
       x,y,z,order='grlex').polys] == [4,4,4]
print('PASS: exact matrix rank, nonzero minor, all six parity sectors, harmonicity, twelve edges, Groebner basis.')
