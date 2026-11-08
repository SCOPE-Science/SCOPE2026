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

# Reproduction and limitations

`verify.py` uses only the Python standard library. Execute `python verify.py` in the same folder as the text files. It independently enumerates original distance-power independent sets of size \(k\) and every vertex subset as a candidate hitting set for 14 small parameter instances, comparing all coefficients with the closed polynomial. It also reconstructs the bounded-composition coefficient using a direct dynamic program, independently of the binomial inclusion-exclusion expression, for four larger cases.

Expected closing lines are `DIRECT_GRAPH_AND_TRANSVERSAL_EXHAUSTIVE_OK 14 293152`, `INDEPENDENT_COMPOSITION_DP_OK ...`, and `VERIFY_OK`. The finite experiments corroborate, but cannot establish, the universal theorem; its proof is in `RESULT.md`. No external independent mathematical assessment has been performed. The priority comparison remains provisional.
