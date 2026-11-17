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

# Reproduction and verified scope

The standalone `check_exact_basin.py` was executed on the included source code using Python and SymPy, returning `EXACT_QUADRATIC_BASIN_AND_ESCAPE_IDENTITIES_OK`. It checks the scalar map obtained after one iteration, the exact centered quadratic form, the two fixed points, the positive inverse branch, the inverse multiplier \(5/9\), the quadratic Taylor identity at the unstable fixed point, the full-basin area and the improvement over the certified square. It also evaluates successive inverse iterates at increased precision as a diagnostic, not an infinite certificate.

The mathematical proof in `RESULT.md` supplies the global monotonicity and divergence arguments, the positive-definite level-area formula, the invariant-probability deduction by recurrence, and the product/telescoping estimates for the exact first-exit law. None of these universal claims is inferred solely from finite script output.

To reproduce: with Python 3 and SymPy installed, run `python check_exact_basin.py` from the directory containing this document and the script. No original-source PDF is distributed in this package. An independent mathematical audit has not been performed.
