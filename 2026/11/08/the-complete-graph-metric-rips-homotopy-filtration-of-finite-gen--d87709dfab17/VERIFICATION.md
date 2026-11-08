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

# Verification of the all-orders incidence-graph theorem

The unrestricted proof is in `RESULT.md`. `verify.py` is a standalone finite stress test, requiring only Python 3's standard library. Run `python3 verify.py` from the directory containing both files. Its output should equal `verify_output.txt`. It independently constructs symplectic generalized quadrangles of orders 2 and 3, verifies incidence-graph shortest-path distances, enumerates maximal cliques, tests every proposed elementary collapse against all remaining cofaces, and reduces the factor boundary matrices over the field with two elements.

Both examples pass. The smaller has 15 points and 15 lines, 120 radius-two relative collapse pairs, and first Betti rank 16 in each radius-three join factor, predicting 256 free third-homology generators. The larger has 40 points and 40 lines, 880 radius-two pairs, and first Betti rank 81 in each factor, predicting 6,561 third-homology generators. The rank prediction for the complete join follows from the proved join formula, not a brute-force full-join homology calculation.

The computations are finite corroborations, not an exhaustive classification of parameter pairs or an independent external review. In particular they cannot establish a theorem for every finite generalized quadrangle without the incidence-axiom argument. They do not test torsion directly; the all-orders integral torsion-free conclusion is proved by the explicit collapses and sphere-wedge homotopy equivalence.
