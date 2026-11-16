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

# Verification of the exact finite classification

The supplied `orbit_check.py`, `tree_walsh_check.py`, `cross_check.py` and `orbits.csv` are complete, standalone Python 3 files requiring only the standard library. They were run directly on the included files, giving the three success markers named in `RESULT.md`.

The first method enumerates all 65,536 sign patterns through 192 symmetries, uses exact Bareiss determinants of reduced signed Laplacians, verifies the 192 certificate rows and counts multiplier occurrences. The second method enumerates every seven-edge graph, tests connectedness and acyclicity by disjoint sets, and independently performs a 16-variable integer Walsh–Hadamard transform. The third checks pointwise agreement for all 65,536 frequencies. The projector kernel is computed as the unnormalized Walsh transform of the nonzero-spectrum indicator; its absolute sum equals 2,950,060, before division by 65,536.

The programs are exhaustive over this finite graph, but they do not prove an analogous statement for all complete bipartite graphs. No external independent mathematical audit is recorded.
