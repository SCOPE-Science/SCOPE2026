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

Exact arithmetic was implemented in `verify.py` without third-party dependencies. Run `python verify.py` and compare stdout with `samples.csv`. The script constructs finite fields via irreducible monic polynomials, independently counts affine solutions for both models, enumerates points on the normalization boundary using tangent labels, and asserts the predicted counts for small odd prime powers. Formal infinite-degree arguments, not finite sampling, prove the theorem. The genus and degree-four inputs are from the cited work; no independent audit has been performed.
