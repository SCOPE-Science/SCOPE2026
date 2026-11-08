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

Run `python verification/verify_hollow_monge.py` with Python 3, NumPy, and SciPy available.

The check independently forms the entire normalized rectangle-vertex coordinate matrix and inverts it numerically, rather than using the finite-difference inverse in the proof. For each \(n=3,\ldots,10\), it compares all restricted Frobenius gradient norms, the summed inverse norm radius, the LP-optimized simplex inball radius, the normalized center, all Toeplitz entries, and all strict superadditive inequalities across ordered index triples. The largest tested intrinsic dimension is 44. Further displayed asymptotic checks use dimensions 20, 40, 80, 160, 320 and 640.

On the checked environment, the script exited successfully and printed `HOLLOW_SYMMETRIC_MONGE_INBALL_CHECKS_PASSED`. The LP radius comparisons were within \(2\cdot10^{-10}\), and independent gradient norms were within \(5\cdot10^{-9}\). The exact all-dimensional proof is given in `RESULT.md`; finite checks, floating-point tolerances, and asymptotic samples cannot independently certify infinite claims. No external independent mathematical audit was performed.
