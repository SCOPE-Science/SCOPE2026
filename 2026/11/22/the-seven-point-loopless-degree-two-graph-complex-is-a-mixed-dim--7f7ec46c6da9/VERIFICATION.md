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

# Reproducibility

Run `python3 verify.py` and `python3 crosscheck.py`, standard library only. The former verifies all faces, matched Hasse incidences, acyclicity by full topological sort, integral elementary Morse reductions, and each of 131 unit-pivot attaching reductions. Expect `BOUNDED_DEGREE_LOOPLESS_7_OK`. The latter independently Gray-code enumerates every edge subset and expects `LOOPLESS_7_INDEPENDENT_CENSUS_OK`. Both scripts have deterministic assertions and fail rather than silently accepting a discrepancy. The derived Morse CW model has critical-cell counts 1 in dimension zero, 132 in dimension four, and 312 in dimension five. After unit cancellations it has 1, 1, and 181 in those dimensions. Algebraic cancellations determine actual homotopy attaching maps in this 4/5-dimensional simply connected setting. No general seven-plus parameter range or independent mathematical audit is certified.
