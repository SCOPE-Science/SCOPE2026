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

The deterministic Python 3 script `verify.py` was executed against the package contents. Its last run reported:

`PASS 110337 exact arithmetic assertions; 29 exhaustive finite sample spaces`

The finite checks enumerate the complete collection of fixed-edge hypergraphs for the listed small parameter cases and compare direct expectations and covariance with independently evaluated closed forms. Large integer-rational checks verify the sign boundary over 25 different ranks, all positive overlap sizes below each rank, and 45 orders from the nondegenerate starting order for each overlap size. The analytic proof is in RESULT.md and is not replaced by tests.

To reproduce, run `python verify.py` using Python 3 from the extracted package directory. It requires no third-party dependencies. No independent audit has been performed, and the computations do not establish novelty.
