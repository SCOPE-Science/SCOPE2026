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

Run `python3 verify.py` with Python 3. The checker uses only the standard library. It evaluates exact rational squared Toeplitz shift weights for several degrees, compares analytic logarithmic heat maxima against their Stirling bounds, and checks the explicit polynomial-degree envelope. A successful run outputs `PASS: finite normalized-weight/heat-bound checks: 306`.

The proof's infinitely many terms are controlled analytically, not by finite tests. The center selection requires, for each fixed index, a finite list of Gaussian-polynomial norm, compact-supremum, and matrix-coefficient bounds; all tend to zero along sufficiently distant integer translations. Certified rational interval bounds therefore produce a terminating integer search, though the center sequence is not exhaustively printed or timed. The verification does not certify numerical realizability at enormous indices.

The critical noncomputational claims to inspect are: Gaussian moment normalization in step 1, exact heat convolution in step 2, finite-stage termination in step 3, the distinction between kernel admissibility and domain membership for the selected vectors in step 4, and matrix-coefficient cross-term estimates in step 5. No independent mathematical validation has been performed.
