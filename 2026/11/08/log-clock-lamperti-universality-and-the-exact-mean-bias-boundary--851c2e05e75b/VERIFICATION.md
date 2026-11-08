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

# Verification performed

The result rests on analytic proofs of (a) the exact exponential-maximum/stable-subordinator representation, (b) conditional stable-ratio mean, (c) joint stable convergence via uniform harmonic expansion, (d) Stieltjes inversion, and (e) the bounded-moment Taylor correction. The included checker is standalone standard-library Python and performs exact-rational finite Laplace-recursion comparisons plus deterministic numerical density and boundary diagnostics. These checks do not replace the proof of any asymptotic or infinite assertion.

To reproduce: run `python3 checker.py` in the directory containing the extracted embedded files. No external package, network access or unpublished data is required. All arguments and edge cases are stated in `RESULT.md`.

Independent mathematical validation has not been performed. Known limits: physical-time occupation, dependent trials, and nonconstant fractional indices are outside scope.
