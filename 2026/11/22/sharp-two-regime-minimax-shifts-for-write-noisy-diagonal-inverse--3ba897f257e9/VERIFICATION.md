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

The proof and definitions are self-contained in `RESULT.md`. Running `python3 verify.py` with Python's standard library produced `VERIFY_OK 1056 exact moment identities and numerical root/inequality checks`.

The checker enumerates all independent signs for up to three-by-three symmetric two-point programming-error matrices, with two-copy enumeration for two-by-two examples; it compares exact rational second moments to the analytic formula and checks the rational counterexample. Its further floating-point checks test representative crossing roots, stationary roots, convex spectral endpoints, and perturbed shifts. These are diagnostic finite tests only; they cannot certify the universal quantifiers, uniqueness, or the positive-root classification, which are established by the analytic proof.

The result excludes read noise, clipping, quantization, nonlinear programming effects, non-diagonal eigenvector orientations and outer iterative-solver dynamics. No independent mathematical audit or external verification has been performed.
