---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible finite verification

Run `python3 verify.py` with Python 3.10 or later. The verifier uses only the standard library and no network connection. `verify-output.txt` records the exact expected output of one execution of the same bundled program. The program reconstructs all objects from the residue set \(\{1,3,4,5,9\}\) rather than reading any previous computation.

The code independently enumerates the complex by intersecting neighborhoods and by adding permitted vertices to directed triangle homomorphisms. Both produce exactly \(165\) zero-cells, \(495\) one-cells, \(330\) two-cells and no higher cells. All cellular product-orientation signs are generated directly; every two-cell has zero double boundary. A graph search verifies that the one-skeleton is connected. Each one-cell is contained in two or three two-cells, with multiplicities \(330\) and \(165\).

Using double-incidence rows of the integer matrix \(\partial_2\), a spanning forest in the induced graph on the \(330\) two-cells has five components of \(66\) vertices and \(325\) selected edges, producing integral unit relations. Its five remaining double-incidence rows reduce to zero. Each triple-incidence row reduces to the positive or negative of one of five stored-in-code matrix rows, and all five occur. The five-by-five determinant is \(33\) and a four-by-four minor is a unit. Thus the nonunit Smith invariant is exactly \(33\); importantly, the image is **not** primitive in the full one-chain lattice. A direct rank check over fields with \(2,3,5,11,13\) elements gives \((330,329,330,329,330)\), corroborating both prime factors and no extraneous factors.

Signed cellular traces of the involution \((A,B,C)\mapsto(-A,-C,-B)\) are \((5,-5,-10)\). They give Lefschetz number zero, hence trace one on the rational first-homology line. Affine automorphisms of the target and cyclic source permutations are also verified as cellular maps; because their orders are odd they act trivially on the free rank-one integral summand.

The code proves an **exact finite integral homology** statement only. It does not compute \(\pi_1\), a CW homotopy classification, an integral torsion symmetry character or the corresponding complexes for arbitrary prime powers. Field-only checks would not suffice; the integer five-generator presentation is the decisive certificate. The source manuscript's full independent assessment is not part of these computational checks.
