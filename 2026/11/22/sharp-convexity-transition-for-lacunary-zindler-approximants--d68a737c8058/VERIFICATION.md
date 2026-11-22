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

The standalone `checker.py` was run with a standard Python interpreter against the complete finite-family formulas; the run returned `PASS: 20393 exact-arithmetic and floating-point assertions`. It tests three admissible odd frequencies and amplitudes, truncations one through three, exact rational critical radii and sum identities, independently formed derivative-vector determinants, and many sampled angular positions. A separate high-resolution local expansion comparison for the example \((\alpha,\beta)=(8,7)\) confirmed the predicted positive quadratic curvature coefficient for truncation orders one through three.

The universal all-integer theorem, global convexity criterion, uniqueness/count of flat points, and asymptotic conclusion follow from the analytic proof in `RESULT.md`. No finite test establishes their infinite quantifiers, and no external audit or formal proof certificate was obtained.
