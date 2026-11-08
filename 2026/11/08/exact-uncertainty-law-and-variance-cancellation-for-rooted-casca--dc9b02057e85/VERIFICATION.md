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

The universal theorem is proved in RESULT.md by conditioning on a single parent per node, deriving a weighted random-subtree representation, and using independent child subtrees for the moment-generating and variance recursions. The signed covariance formula follows by counting the shared resharing gates in two activation paths.

Reproduction: run `python3 verify.py` with Python 3 (standard library only). The verifier checks 360 independently generated exact-rational trees of sizes two through nine, using independent exhaustive cascade simulation and message-law convolution. It compares entire distributions, aggregate means and variances, the nonnegative gate decomposition, all node means, and all pairwise covariances, plus a four-vertex aggregate-cancellation example. Its observed output was:

`PASS: 360 independent exact-rational finite-tree instances (n=2..9), including all-pair covariances, full law and variance decomposition; cancellation case verified.`

Limits: finitely many tests cannot certify the all-tree theorem; the proof supplies that general argument. No stochastic simulations with approximate floating-point tests are relied on. No independent audit or external validation has occurred.
