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

# Verification record

The exact model and all boundary hypotheses are in `RESULT.md`. The pure-Python `check.py` performs 963 independently recomputed finite numerical tests, including high-precision log-probability comparisons, derivative identity tests, cross-checks of the two-vs-one identity, uniqueness brackets for 25 ordered thresholds at each of six receptivity probabilities, and integer brute-force comparisons. Command: `python3 check.py`. The computational checks were passed after extracting the program to a local file.

The proof does not infer infinite or global conclusions from this finite suite. Its decisive analytic steps are the strict monotonicity of \((1-s)(1-x)+se^{-x}\), the resulting unique zero of \(x\ell_s'(x)-\ell_s(x)\), and the strict monotonicity of the adjacent-count comparison on each \((j\xi_s,(j+1)\xi_s)\). Exact algebra for the two-vs-one difference was also independently simplified symbolically. Reproducibility has no external package dependency. Priority against the full 1999 source and independent third-party verification are not established.
