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

# Reproducibility and scope

The analytical derivation in `RESULT.md` proves the uniform large-radius statement; no finite computation certifies an infinite range. `check.py` uses ordinary floating-point composite Simpson quadrature to inspect four sample fixed-area annuli and evaluates the exact normalization through a truncated positive summation with a conservative numerical tolerance. It prints `THIN_HERMITE_ANNULUS_PASS normalization=4 shoulder_cases=4` and the four observed signed-gap ratios close to one when run with Python 3's standard library.

The proof requires radial Hermite–Laguerre overlap, a two-term uniform Stirling expansion near the two modes, a uniform Poisson tail bound and the nondegenerate-grid maximization estimate. No exact finite onset radius, uniqueness of the top Hermite mode, or global higher-Hermite result is asserted. Historical priority remains subject to independent evaluation.
