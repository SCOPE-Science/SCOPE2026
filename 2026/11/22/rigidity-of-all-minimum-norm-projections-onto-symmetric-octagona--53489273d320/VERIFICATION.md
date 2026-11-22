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

The full parameter statement follows from the analytic calculations in `RESULT.md`, specifically the four-coordinate inclusion, real Hahn–Banach extensions, symmetry averaging, unique equivariant optimizer, and the eight forced norm-saturation equations with determinant \(64\beta^4\). These steps cover all real parameters in the closed interval and both degenerate square endpoints.

`verify_octagonal.py` is a Python-standard-library executable. It checks the eight tight-pair constraints and full-rank determinant exactly, and also enumerates the extreme points of the actual source unit ball at rational test parameters, checks all four output supporting functionals, tests the explicit retraction and the dual certificate using exact fractions, and checks the algebraic endpoint factorization. The printed assertion count is a reproducibility aid, not an exhaustive continuum certification.

An additional unrestricted numerical linear-programming spot check (all eight real retraction coefficients; 16 source extreme points times four target supports) was performed for nine parameters. Such floating-point tests are not a substitute for the analytic proof and are not offered as an independent audit.

The entire numerical projection constant is treated as a known implication of the classical planar self-length identity, not as the originality basis. The new claim is full uniqueness of the canonical best retraction. Full older planar literature comparison remains bounded by accessible source text. Independent audit was not performed.
