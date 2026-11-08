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

# Reproduction and scope

Execute `python3 verify_bridge.py` with Python 3.9 or newer, using only the standard library. The exact-rational script verifies the discrete kernel matrix against the integral \(K(s,t)=\min(s,t)-st\), enumerates all binary slope-budget assignments on uniform quantile partitions for mesh sizes \(2\) through \(10\), verifies 135 exact second-moment identities for balanced barbells, and checks 16,200 rational admissible edgewise-affine functions on sampled connected metric graphs. A successful run terminates with `ALL_BRIDGE_BUDGET_VARIANCE_CHECKS_OK`.

The empirical mesh comparisons do not optimize over continuous quantiles, and the finite graph tests do not exhaust all graph geometries or non-piecewise-affine functions. The analytical theorem depends on the level-crossing bridge-budget lemma, the quantile inverse-density relation, and a strictly concave first-variation argument, all proved in `RESULT.md`. No independent mathematical audit has been performed.
