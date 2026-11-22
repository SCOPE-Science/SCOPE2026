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

# Verification

The supplied `check.py` is a standalone Python 3 program requiring only the standard library. It enumerates every eligible weighted nonneighbor for both retained endpoints of every discordant matching edge, using exact `fractions.Fraction` arithmetic, for each integer \(3\le n\le34\). It verifies the finite generator formulas, strict ordering, exact rational limiting slopes and a two-class affinity calculation. Run `python3 check.py` alongside the included package files.

The mathematical infinite-size limit is **not** certified by this finite enumeration. The analytic proof separate from the finite enumeration is in `RESULT.md`: uniform \(O(1/N)\) per-target selection, maximum-degree control, uniform target-type approximation, bounded-jump martingale convergence and Gronwall for the typed-edge ODE, plus a stopped linear martingale argument for the two-type absorbing limit. Endpoint sampling and exclusion conventions are explicitly stated.

Scientific scope: finitely many fixed separated opinion classes, strictly positive homophilic affinities, average degree bounded, \(K_N/N\to\kappa\in(0,1)\), initial maximum degree \(o(N)\), and event rate \(N\). The obstruction is about the nonexistence of a common **exact** scalar closure, not empirical accuracy of an approximate graphon method.

Historical priority remains literature-bounded. Related fixed-state models whose full texts were not accessible are documented in the review and audit. No independent audit or external validation has been performed.
