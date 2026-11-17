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

# Verification and limits

The exact proof is contained in `RESULT.md`, including the face classification, the simplicial face-poset formula, the complete-graph incidence spine, the six-to-six barycentric triangle correspondence, exterior contraction over the integers, and rational invariants for each Young subgroup.

Run the standalone Python standard-library program `checks/kneser_equivariant_check.py` without command-line arguments. Its expected complete output is `checks/kneser_equivariant_check.out`. The output checks four finite point counts, including all four to seven-point cycle-type characters, and ends with `KNESER_TWO_SUBSET_EQUIVARIANT_CHECK_PASS`.

The checked finite cases are consistency tests and are not asserted to prove the universal case. The integral-module proof depends on the homotopy equivalence and the integer direct-summand decomposition, not on modular ranks alone. The assertion is not a full equivariant homotopy equivalence or an integral computation of quotient homology. A separate, independent mathematical audit has not been performed.
