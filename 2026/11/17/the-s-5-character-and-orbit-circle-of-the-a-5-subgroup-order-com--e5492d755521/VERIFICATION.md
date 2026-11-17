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

Run `python3 verify.py` in the same directory as this file with Python 3.9 or newer; no external packages or data files are needed. The code enumerates all \(59\) subgroups of \(A_5\), of which \(57\) belong to the proper nontrivial subgroup poset, and all \(203\) nonempty faces. It verifies that all \(15\) triangles admit distinct free edges of subtype \((2,4)\), proves connectivity of the remaining \(57\)-vertex, \(116\)-edge graph, and checks the consequent integral rank \(60\). Boundary ranks are also recomputed over six finite fields as an independent finite check.

For each of all \(120\) conjugation automorphisms, `verify.py` computes exact counts of fixed vertices, edges and triangles and checks the Lefschetz trace. It computes the seven \(S_5\) irreducible characters by the Jacobi–Trudi formula, verifies integral multiplicities and dimension, and tests the face-orbit counts \((7,8,1)\) and the quotient collapse to a circle. The expected terminal line is `face_orbits: 7 8 1; quotient_homotopy_type=S1`, following `A5_SUBGROUP_COMPLEX_PASS`.

The derivation and exhaustive checker prove the precise finite theorem; there is no inference from partial sampling or a computation timeout. There is no assertion of integral representation-lattice uniqueness, independent review, or equivariant homotopy equivalence.
