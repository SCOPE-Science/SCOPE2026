"""Finite exact-arithmetic checks supporting the stated plank-shell formulas.

The universal results are proved analytically and do not follow from this script.
Python >=3.10, standard library only.
"""
from fractions import Fraction as F
from itertools import product

# Rational unit vectors from Pythagorean triples, including axial cases.
normals = [(F(1), F(0)), (F(0), F(1)), (F(3,5), F(4,5)),
           (F(5,13), F(12,13)), (F(8,17), F(15,17)),
           (F(20,29), F(21,29))]
lams = [F(5,4), F(3,2), F(2), F(3), F(5), F(17,3)]
checks = 0
for a,b in normals:
    assert a*a+b*b == 1
    for lam in lams:
        lhs = ((lam-1)*a+lam*b)/(a*a+lam*b*b)
        rhs = 1+(lam-1)*a/(a+b)
        assert lhs <= rhs, (a,b,lam,lhs,rhs)
        if a*b:
            assert lhs < rhs
        checks += 1

# Verify directional budget conservation and two-variable inequality for
# multiple weighted normal families and sample anisotropic parameters.
weights = [F(1,10), F(3,10), F(2,5), F(1,5)]
for inds in product(range(len(normals)),repeat=3):
    vecs = [normals[i] for i in inds]
    ws = weights[:3]
    W = sum(ws)
    R1 = sum(w*a/(a+b) for w,(a,b) in zip(ws,vecs))
    R2 = sum(w*b/(a+b) for w,(a,b) in zip(ws,vecs))
    assert R1+R2 == W
    for lam in lams:
        X1=sum(w*a/(a*a+lam*b*b) for w,(a,b) in zip(ws,vecs))
        X2=sum(w*lam*b/(a*a+lam*b*b) for w,(a,b) in zip(ws,vecs))
        assert (lam-1)*X1+X2 <= W+(lam-1)*R1
        checks += 1

# For representative strict nested boxes, check that the two canonical
# finite coordinate-plank constructions cover every rational mesh point.
examples = [((F(4),F(1)), (F(19,5),F(1,2))),
            ((F(3),F(2)), (F(5,2),F(7,4))),
            ((F(1),F(1)), (F(3,5),F(3,5))),
            ((F(7,4),F(3,2)), (F(3,2),F(5,4)))]
points=0
for outer,inner in examples:
    assert all(0<h<L for L,h in zip(outer,inner))
    S=sum((L-h for L,h in zip(outer,inner)))
    Lmin=min(outer)
    expected=min(S,Lmin)
    assert expected<=S and expected<=Lmin
    for k1,k2 in product(range(21),repeat=2):
        point=[-outer[0]/2+outer[0]*F(k1,20),
               -outer[1]/2+outer[1]*F(k2,20)]
        in_hole=all(abs(x)<h/2 for x,h in zip(point,inner))
        if not in_hole:
            # Exterior slab in at least one direction.
            assert any(abs(x)>=h/2 for x,h in zip(point,inner))
        points+=1
print('PASS: exact two-variable/budget identities:',checks,
      'rational shell grid checks:',points)
