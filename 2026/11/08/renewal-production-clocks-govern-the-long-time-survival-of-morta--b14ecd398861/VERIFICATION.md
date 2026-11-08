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

# Reproducible checks

Run `python verify_renewal.py` with Python 3 and no third-party dependencies. The program numerically solves the strict positive exponential-moment root for five success probabilities, compares deterministic, symmetric two-point, and Poisson clocks, solves the exact delayed-success renewal equation on half-unit grids in log space for multiple finite completion rates, and checks the Poisson exact survival formula. The actual executable in this package completed without an exception and printed `PASS 125 independent exponential/deterministic/two-point delay checks`. The rate approximations are checked at a finite horizon and are not used as the infinite-time proof.

The analytic proof independently establishes the change-of-measure identity for the stopped renewal epoch, the support-dependent overshoot bounds, a two-sided delayed-success comparison, the endpoint passage in the exponential root, and the Jensen/convex-order equality cases. No certificate for more general unbounded exponential-moment waiting laws or an exact finite-time survival ordering is claimed.
