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

The self-contained `verification.py` uses only the Python standard library. Execute `python3 verification.py` from the directory containing the extracted files.

The executed checks reported 20 exact-root and independent bisection comparisons, nine direct logit integral comparisons, and nine small-noise correction/reflection checks, followed by `ALL CHECKS PASS`. High-precision decimal arithmetic is used in the closed-form tests, and an independent composite Simpson integration is used at moderate noise. The finite tests are not a substitute for the analytic limiting proof in `RESULT.md`.

The source model is a nonatomic fixed-point game with uniform types, two resources, a linear popularity subsidy, independent Gumbel perturbations, and a single vanishing offset. No results are asserted for dynamic learning or finite-player stochastic selection. Independent scientific validation has not been carried out.
