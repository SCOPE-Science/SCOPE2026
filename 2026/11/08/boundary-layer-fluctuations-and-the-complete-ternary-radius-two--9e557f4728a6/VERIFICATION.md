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

# Reproduction and proof boundaries

With Python 3.10 or later, run `python3 checker.py`. The script has no nonstandard dependencies. It independently generates the full multiset simplex, compares the actual radius-\(r\) ball found using half the \(\ell_1\) distance against the ideal-difference-vector sum for 4,451 centers in small dimensions, recomputes exact ordered-pair second moments, and verifies the complete ternary radius-two frequency law for \(6\le n\le40\), using integer and rational arithmetic. The expected result comprises three `PASS` lines.

These computations check finite cases only. The unrestricted claims require the explicit argument in `RESULT.md`: simultaneous lower-bound stars-and-bars counting, strict interior criterion, the single-deficient-coordinate count, and control of multiple deficient coordinates at order \(n^{-2}\). The exact six-bin ternary classification is proved by enumerating the possible small-coordinate patterns; it is not inferred from numerical extrapolation.

A reader may directly reproduce the general moment expressions by constructing the finite set \(\mathcal Z_{q,r}\), summing the binomial terms in equations (2) and (3), and subtracting the squared mean. No outside source code or datasets are required. The result is a scientific self-review only; no independent audit has been performed.
