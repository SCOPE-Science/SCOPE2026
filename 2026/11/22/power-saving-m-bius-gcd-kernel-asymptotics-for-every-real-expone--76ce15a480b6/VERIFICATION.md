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

The provided `verify.py` performs the following finite diagnostics with no external packages:

1. Verify the original double sum against the exact Jordan-square decomposition over rational numbers for integer \(s=2,3,4\), for all cutoffs \(1\le N\le35\) (105 comparisons).
2. Numerically compute the local constants and finite \(A_{q,s}\) for \(1\le q\le65\), and compare independent normalized values at \(N=35,120\) for six real exponents \(s=1.25,1.5,2,2.5,3,4\) (12 comparisons). The finite constant truncations are not rigorous enclosures for the infinite series.

Expected terminal line: `MOBIUS_GCD_POWER_DIAGNOSTICS_OK 105 12`.

The uniform Euler-product bounds, convergence, power-saving errors, and large-exponent limit rely on the written infinite argument in `RESULT.md`. The finite diagnostics cannot independently establish any infinite assertion. No independent mathematical audit has been performed.
