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

# Verification of the mathematical claim

Run `python3 checker.py` with Python 3.8 or newer in the directory containing the files. No third-party packages or network access are needed. The checker returns a nonzero exit status if any exact check fails.

The checker verifies the normalized four-species probability vectors, recomputes the three large integer scaled differences at sample sizes 2, 5 and 12, and independently computes expected species richness from a weighted distribution of actual *sets of detected species*. It also checks the rational perturbation margins supporting arbitrarily many additional positive species.

As supplemental finite evidence, the checker exhaustively compares distinct sorted three-species rational profiles with shared denominators from 3 through 14 for sample sizes 2 through 18, using exact integers. There are 391 such profile pairs. This finite test does **not** prove the real-parameter zero bound or the sharp all-size threshold: those are proved analytically in `RESULT.md` using majorization, a self-contained exponential sign-variation lemma, and explicit rational inequalities.

The proof does not assert a sharp maximum number of crossings for all larger supports and does not address sampling without replacement or noisy observed curves. Historical priority remains provisional; independent audit and external scientific validation have not been performed.
