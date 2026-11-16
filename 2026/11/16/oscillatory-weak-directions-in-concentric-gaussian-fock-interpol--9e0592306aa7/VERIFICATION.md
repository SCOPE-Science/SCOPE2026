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

# Reproducibility and limits

Run `python CHECK.py` with NumPy and mpmath. Actual execution returned: `PASS: 125 independent finite consistency assertions; analytic proof is separate.` The tests compare a full Gram matrix to its independently assembled Fourier-block spectrum and evaluate the collision coefficient from both conditional moments and a finite root-of-unity sum. They also check small-radius and large-radius sector predictions on selected finite examples.

The proof in RESULT.md establishes the unbounded subsequence result by an explicit asymptotic domination argument. No finite numeric collection constitutes an exhaustive proof of the infinite recurrence. The exact formulas are restricted to positive distinct radii and fixed polygon order; all collision coefficients are evaluated at positive base radius. The public-source comparisons establish only best-knowledge originality, not external or independent validation.
