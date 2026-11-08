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

# Verification notes

Run `python verification/check.py` with Python 3 and only the standard library. The script calculates exact rational synchronous Markov transitions, independently reproduces the first opposite-hub infection time via a frozen binomial process and by set partitions, and tests the exact geometric first-hub activation from the large-side start. It checks 209 assertions over finite cases, plus finite-size convergence and a numerical evaluation of the infinite tail sum. All checks complete successfully in the supplied package.

A finite-state computation is not an infinite proof. The theorem's limits are justified by the coupled geometric waiting times, independent-update survival product, strong law, dominated convergence, uniform summable tail bound, and a geometric activation plus logarithmic completion-time envelope as written in `RESULT.md`.

The first public date in the metadata is the 2025-08-11 public repository record for the precursor thesis. Its full text was not accessed. The directly inspected full primary manuscript is arXiv:2602.16300v1, first submitted 2026-02-18. A definitive external priority search or independent proof review has not been performed.
