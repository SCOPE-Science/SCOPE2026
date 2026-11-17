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

# Verification and boundaries

The analytic proof derives every asserted claim for all segment lengths. The standalone file `verify_horocycle_steiner.py` uses the Python standard library and may be run with `python verify_horocycle_steiner.py`. It checks independent integrations of the complete probability, exact normalization constants, the two sharp threshold coefficients, directly computed hyperbolic cosine-law angles, and fixed-seed Monte Carlo trials of independently uniform horocyclic triples. The script has a successful terminal message `HOROCYCLE_STEINER_TWO_THRESHOLDS_CHECKS_OK`. No finite simulation constitutes an infinite proof.

The total-variation mark convergence requires the two-edge event, which has positive probability at each finite segment length; its exact density is stated in the proof. Complete curvature -1 and uniform arclength are essential hypotheses. The result has undergone self-review only; no independent audit or certification has been performed. Historical priority remains qualified by inaccessible deterministic sources.
