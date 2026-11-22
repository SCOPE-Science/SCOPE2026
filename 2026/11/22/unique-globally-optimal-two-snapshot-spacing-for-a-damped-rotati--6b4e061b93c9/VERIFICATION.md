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

# Reproducibility and verification

The proof is self-contained in `RESULT.md`. In particular, differentiation is with respect to \(t=2\omega h\), not the physical time directly. For each \(\alpha>0\), the diagnostic script uses bisection on \((0,\pi)\) and checks matrix eigenvalues from trace/determinant, monotonicity near the claimed maximum, strict global advantage over the first perpendicularization time, and the strong-damping expansion. Run `python3 check_oscillator.py` with a standard Python 3 installation. The script does not invoke a theorem prover or external numerical service and does not assert that finite tests prove the universal statement. The passed checker output is recorded in the packaged run and may be reproduced directly.

Actual scientific caveat: numerical floating point resolution deteriorates for very large damping; the proof of the limit uses the scaled analytic expression, not cancellation-prone floating-point eigenvalue differences.

Observed diagnostic output from the embedded script: `DAMPED_TWO_SNAPSHOT_CHECK_OK 8115`.
