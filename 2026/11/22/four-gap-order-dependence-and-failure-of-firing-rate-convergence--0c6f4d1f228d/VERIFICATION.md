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

The mathematical claim is proved in `RESULT.md`. This verification note specifies actual finite checks without substituting them for a proof of the infinite limiting statements.

Run `python3 verify.py` with an ordinary Python 3 interpreter. The script verifies the four clock gap lists exactly, tests the projected spike counts for all binary clock words through length eight over representative rational reset times including each transition endpoint, and independently checks greedy maximality and reflection invariance for finite windows of periodic three-gap examples.

The bounds on graininess and histogram discrepancy follow from one complete list of four gaps per cell and do not depend on experiments. Superexponential run concatenation and the interval of Cesàro limit points are analytic arguments, not extrapolations from finite simulations. The comparison with earlier literature cannot exclude every unindexed historical equivalent. Independent mathematical validation has not been performed.
