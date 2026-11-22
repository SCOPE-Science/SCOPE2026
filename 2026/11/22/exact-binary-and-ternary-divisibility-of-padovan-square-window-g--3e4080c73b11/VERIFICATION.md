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

# Verification record

The direct arithmetic verifier `check.py` completed successfully and its stdout is preserved as `CHECKS.txt`. It verifies 400 exact instances of the order-six recurrence, the low-precision matrices and witnesses, all 720 local valuations for square-window GCDs with lengths from 1 through 360, and full minimal-period assertions at fourteen tested prime-power precisions.

The proof handles infinitely many lengths and precisions by integer-matrix lifting and the unit property of \(Q(1)=-1\). Computations do not purport to exhaust those infinite families. No third-party or independent validation has been performed. The claim is restricted to binary and ternary factors.
