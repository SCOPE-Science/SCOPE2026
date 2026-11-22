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

# Reproducibility notes

The analytical proof in `RESULT.md` establishes the complete three-dimensional matrix exponential, trigonometric entrywise sign envelope, strict-concavity cell count, monotonic parameter threshold, and dimension-two exclusion without numerical assumptions.

The auxiliary `check.py` uses only Python's standard library; run `python3 check.py`. It constructs the generator and matrix exponential using a scaling-and-squaring Taylor algorithm separate from the analytic Fourier formula. It tests the formulas, integer failure counts, root bracketing, and endpoint behavior across multiple finite samples. The actual run passed 1,276 finite-precision assertions. This finite testing is not an exhaustive proof, and rounding near critical thresholds can affect raw sign tests unless tolerances are used.

Independent mathematical auditing and validation have not been performed. Historical priority remains subject to further literature discovery.
