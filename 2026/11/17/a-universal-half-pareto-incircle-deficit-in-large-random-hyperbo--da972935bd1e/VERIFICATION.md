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

The result is proved analytically using the exact hyperbolic inradius half-angle identity and first-labeled-vertex anchoring of the cyclic gap sequence, fixed-angular-gap side asymptotics, a bounded-shortest-gap cutoff, and \(L^1\) convergence on each gap-boundary chart. The moment statement concerns the limiting variable only.

With `numpy>=1.24`, run `python check_hyperbolic_inradius.py`. This performs two separately implemented finite-triangle incircle computations, tests the fixed-configuration \(e^{2R}\) scaling, and simulates independent normalized exponential angular gaps for the tail and its marked conditional law. Fixed-seed output includes `HYPERBOLIC_INCIRCLE_PARETO_GEOMETRY_CHECK_OK`. In a run using \(1{,}600{,}000\) angular triples, the observed tail coefficient at threshold \(6000\) was \(1.55626153309\), compared with the exact \(1.55939360247\); the conditional successor-gap mean was \(0.50249493493\) versus \(0.5\). These tests are corroboration, not a proof of asymptotic or total-variation claims.

The archival literature date is the first arXiv version date for reference [1], not a later journal or revision date. Source comparison is finite, and priority is subject to additional historical review.
