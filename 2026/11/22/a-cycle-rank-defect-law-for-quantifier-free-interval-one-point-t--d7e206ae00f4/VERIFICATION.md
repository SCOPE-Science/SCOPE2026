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

Run `python verify.py` using standard Python 3 (no external dependencies). The deterministic checker independently enumerates all interval witnesses on a half-integer endpoint grid for each proper base representation, compares the full trace-size polynomial with its predicted edge-span correction, and checks that every observed neighborhood is a contiguous index block. It covers all distinct-endpoint interval matchings with at most five base intervals and reproducible pseudorandom proper configurations on six to nine base intervals. Expected output: `VERIFY_OK 544`.

The finite checks cannot certify the universal theorem and do not establish historical originality. The all-size proof rests instead on ordered-endpoint inequalities, the missing-block versus long-edge bijection, and the equality \(|\{\text{consecutive edges}\}|=m-c\) for proper interval graphs. The model-theoretic interpretation counts new interval vertices only and uses rank-zero adjacency formulas with named parameters.
