---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For U=X_1² with Beta(1/2,(d+1)/2), conditioning on U splits Π₂ into even 2×2, axial linear, transverse linear, mixed x_1Y, and centered transverse quadratic sectors of dimensions 2,1,d−1,d−1,d(d−1)/2. Conditional moments yield the stated four scalar beta-CDFs and generalized even eigenvalues. Strict beta stochastic orders and min-max on u and 1−u place λ− and λ+ outside the four scalar levels. Determinant/first-moment expansions produce λ+/λ−~405 a^(−4)/(8(d+1)(d+4)). Direct independent symbolic constant check and the actual verify_exact.py source corroborate arithmetic; finite tests do not prove the infinite family.

## originality

PASS

No located prior result implies the six strictly ordered degree-two central-ball-slab levels and sharp fixed-dimensional thin-width prefactor. Existing polynomial-ball asymptotic theory, half-ball parity, and radial-mask classification differ geometrically and in conclusion. Best-of-knowledge only.

## value

PASS

Complete strict spectrum and unique extremizers quantify a natural finite-bandwidth localization problem; the exact small-aperture a^(−4) instability and dimension prefactor are significant sharp quantitative consequences not just normalization tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
