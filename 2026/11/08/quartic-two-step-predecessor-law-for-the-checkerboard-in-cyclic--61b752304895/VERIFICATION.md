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

# Verification and reproducibility

From the directory containing this file, run `python3 check.py` with Python 3 and no third-party modules. The expected final line is `VERIFY_OK: all transfer rows, 4x4 determinant, 40 recurrence terms, 12 graph traces, exhaustive even rings 2..18`.

The checker constructs the two-iteration radius-two local rule directly from the Rule 50 rule table, builds both 16-state transition matrices, checks every nonzero entry of their two-letter product against the proof's table, computes the characteristic determinant by the 24-term permutation definition (not an external symbolic package), and compares transfer counts with the four-state quotient. It directly enumerates every binary initial condition on each even indexed ring of lengths 2, 4, ..., 18, independently simulates two updates, and compares the counts for all-zero, all-one, and both checkerboard targets.

These finite runs are not proofs of the infinite-length recurrence. The proof rests on the exact finite transfer-table identity, unique lifting of class walks, and Cayley–Hamilton / determinant trace identities valid for all positive integer half-lengths. No computational assertion establishes optimizer status among arbitrary output configurations.
