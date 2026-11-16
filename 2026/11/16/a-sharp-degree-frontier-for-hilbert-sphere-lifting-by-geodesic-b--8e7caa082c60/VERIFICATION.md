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

# Verification evidence and limits

Run `python3 check.py` from the extracted package directory. The checker requires Python 3 standard library only. It uses exact fractions to verify the low-degree Legendre evaluations, the integrated degree-eight Laplace majorant, the cubic arcsine coefficient-ratio identity through twenty-one terms, the cubic Bernstein expansion over fifty exact sample points, and the explicit negative witnesses.

The actual packaged checker produced:

`CHECK_OK exact_legendre_low=8 integral_bound=1 asin_cubic_ratios=21 cubic_identity_grid=50 negative_witnesses=3`

The proof is not an extrapolation from these finite tests. The bound for all higher Legendre degrees follows from the integral with a pointwise monotonic power; the coefficient ratio at all orders follows from a differential-equation recurrence and an odd-square reciprocal series; the infinite families of negative witnesses follow from strict monotonicity of \(\cos(\pi/n)^n\). For all input dimensions the Gegenbauer-to-Legendre convexity reduction follows from restriction to an embedded sphere and uniqueness of Schoenberg coefficients. The exact boundary cases of each parameter are in `RESULT.md`.

The linked August 2026 motivating article was inspected in its full available HTML representation. Some other similar published research items were available only via short public summaries, so no whole-document noncoverage claim is made for them. Publication priority remains subject to independent literature assessment.
