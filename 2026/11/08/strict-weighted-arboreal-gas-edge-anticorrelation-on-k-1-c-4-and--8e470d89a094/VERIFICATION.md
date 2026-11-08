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

# Verification record

Run `python3 check_wheel.py` with Python 3 and assertions enabled; no third-party packages are needed.

The checker enumerates all \(256\) edge masks and obtains \(134\) acyclic subsets, then verifies the entire sparse multivariate polynomial identities for the six distinct-edge orbits. Five have respectively \(172,90,240,149,93\) positive nonzero integer coefficients. The sixth, the nonincident spoke/rim orbit, satisfies the separately displayed exact polynomial equality and positive square decomposition. Finally, \(48\) sets of nonuniform positive rational weights are independently tested against all \(28\) edge-pair covariances, for \(1344\) exact rational sign checks.

The universal real-weight claim follows from the proved polynomial positivity and exact analytic series-contraction identities, **not** from finite rational trials. The subdivision theorem is an all-graph argument under nonbridge/bridgeless hypotheses; no finite enumeration of arbitrarily long subdivisions is claimed.

All scientific limitations are stated in `RESULT.md`. No independent audit or external certification has been performed.
