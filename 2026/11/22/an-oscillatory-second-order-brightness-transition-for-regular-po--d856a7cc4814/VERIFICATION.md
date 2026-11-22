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

The analytic proof establishes the finite maximum formula, exact first transition, a sharp local upper-tail formula, and the full second-order accumulation interval. The executable `verify.py` uses only the Python standard library and is run by `python3 verify.py` from the extracted package.

The checker independently compares projected convex-hull polygon areas to Cauchy's facet formula in 2,800 random cases, exhaustively enumerates subsets for small polygons, and tests the asymptotic critical-height formula. Expected output starts with `PASS 2840 numerical checks`. Numeric tests are not infinite or formal verification and are not used to prove the irrationality argument. Rounded numerical constants are not interval-certified. The corresponding relevant preprint's full text was inaccessible at review time, which limits historical-priority certainty.
