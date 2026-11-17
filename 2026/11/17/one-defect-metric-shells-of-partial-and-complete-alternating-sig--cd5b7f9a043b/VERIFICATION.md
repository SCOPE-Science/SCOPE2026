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

# Verification of the metric-shell theorem

The following commands were executed using the embedded scripts (in the same directory) with Python 3:

`python scripts/verify_one_defect.py`

`ONE_DEFECT_CERTIFICATES_PASS full_orders=48 partial_rectangles=36 partial_one_defect=2117 partial_shells=[((1, 1), 1164), ((1, 2), 266), ((2, 1), 526), ((2, 2), 161)] enumerated_ASM=478 full_one_defect=217`

`python scripts/independent_qp.py`

`ONE_DEFECT_INDEPENDENT_QP_PASS full_orders=7 partial_cases=14 max_coordinate_error=2.75e-15`

The first program checks exact rational row and column sums, entrywise nonnegativity, the canonical KKT potential identities, exact distances for orders three through fifty, and direct transfers of one-defect partial matrices. It independently enumerates all one-negative partial alternating-sign matrices in seven small rectangular shapes and complete alternating-sign matrices in orders three through five, checking canonical decomposition, distance shells, and the predicted multiplicities.

The optional second program requires NumPy and SciPy. It solves equality-constrained Birkhoff projection quadratic programs with a linearly independent equality system, and separately solves inequality-constrained partial-permutation projection programs, comparing optimization outputs to the exact values. These finite computations corroborate the analytical identities; they are not proofs of the unrestricted statements or evidence of historical uniqueness.

Independent mathematical audit has not been performed.
