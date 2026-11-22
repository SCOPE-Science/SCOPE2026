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

The mathematical proof is contained in RESULT.md. The reproducible numerical checker in `check.py` is a standalone standard-library Python program. Its observed result was 2,916 successful assertions, with the sharp limiting constant 0.36959616113943 and critical angular parameter 1.92644766031737.

The code tests finite-degree Parseval residual formulas against independently truncated Fourier tails, exact reflection symmetry, the degree-zero constant, and the location/rate trends of selected critical points. The Fourier tail tests use the upper bound \(2/(\pi^2 M)\) on uncomputed terms. These numerical checks are not an exhaustive finite-degree optimization or proof of the infinite-degree assertion. The latter is demonstrated analytically by the signed-derivative representation, Parseval, dominated Riemann sums, Abel summation, and the strict global extremum of the sine-integral profile.

All results use the normalized arcsine probability measure. External review and independent verification have not been performed.
