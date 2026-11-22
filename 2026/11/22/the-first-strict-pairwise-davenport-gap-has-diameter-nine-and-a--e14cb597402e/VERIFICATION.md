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

# Verification

The standalone \(\texttt{verify.py}\) checks all zero-sum multisets under the exact diameter and length reductions, rather than sampling numerical cases. The recorded zero-sum candidate counts by diameter \(2\) through \(9\) are \(1,3,9,25,79,245,809,2703\); the strict minimal-witness counts are \(0,0,0,0,0,0,0,2\). It verifies that the only critical sequences are negations, evaluates all bounded multiplicity vectors on the unique four-point support and tests all possible extra nonzero support points. The proof of the universal length bound and the completeness of the finite loop ranges appear in RESULT.md. Computation does not independently validate mathematical novelty or priority.
