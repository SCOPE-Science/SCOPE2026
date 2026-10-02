"""Exact checks for the repaired SCOPE-20260913-009 claim."""
import json
import sympy as sp

# Mayer--Vietoris H_1 map for the double of a genus-two handlebody.
# Columns: a1,b1,a2,b2. Rows: x1,x2,y1,y2. Meridians b_i die.
Phi = sp.Matrix([[1,0,0,0],[0,0,1,0],[-1,0,0,0],[0,0,-1,0]])
rank = Phi.rank()
assert rank == 2
betti = [1, 4-rank, 4-rank, 1]
assert betti == [1,2,2,1]

# Goldman form: symplectic intersection form on H^1(Sigma_2) tensor a
# nondegenerate invariant form on sl_2.  The span of a1,a2 is isotropic.
J2 = sp.Matrix([[0,1],[-1,0]])
J4 = sp.diag(1,1,1,1)
J4[:2,:2] = J2
J4[2:4,2:4] = J2
K = sp.diag(2,2,2)
Goldman = sp.kronecker_product(J4, K)
assert Goldman.det() != 0
idx = list(range(0,3)) + list(range(6,9))
assert Goldman.extract(idx, idx) == sp.zeros(6)

gdim = 3
tangent = {'minus1':gdim*betti[0], '0':gdim*betti[1], '1':gdim*betti[2], '2':gdim*betti[3]}
assert tangent == {'minus1':3,'0':6,'1':6,'2':3}
vdim = -tangent['minus1'] + tangent['0'] - tangent['1'] + tangent['2']
assert vdim == 0

out = {
  'Phi_rank': rank,
  'betti_M': betti,
  'goldman_det_nonzero': True,
  'restriction_image_dim': 6,
  'restriction_image_isotropic': True,
  'H_tan_W': tangent,
  'vdim': vdim,
  'duality_minus1_vs_2': tangent['minus1'] == tangent['2'],
  'duality_0_vs_1': tangent['0'] == tangent['1']
}
print(json.dumps(out, indent=2, sort_keys=True))
