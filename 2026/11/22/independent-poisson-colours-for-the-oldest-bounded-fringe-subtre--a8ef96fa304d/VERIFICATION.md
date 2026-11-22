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

Run `python verify.py` using standard Python 3. The executed checker passed 1,336 assertions. It exhausts every recursive parent vector through eight vertices (there are \((n-1)!\) at size \(n\)), checks the exact root fringe-size law, tests uniformity of the conditioned descendant sets and the inside/outside reduced parent-vector distributions, and compares finite expected early counts to their square-root-scale asymptotic.

The probabilistic limit is established separately by the exact Pólya law, subtree-deletion conditional independence, nested-event estimates and convergence of mixed factorial moments; computational tests alone are not a proof of the infinite statement. No independent mathematical audit has been performed.
