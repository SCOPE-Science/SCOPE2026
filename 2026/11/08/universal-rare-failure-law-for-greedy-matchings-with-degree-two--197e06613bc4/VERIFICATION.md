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

# Reproduction and verification

Execute `python check.py` with Python 3 (standard library only) from the directory containing the accompanying files. The successful run recorded `VERIFY_OK 28833 exact assertions`.

The code constructs the complete distribution of the last unmatched pair for random feasible-edge deletion via an exact rational recursion on subsets. Its cases include deleted matchings, paths, Hamiltonian cycles, disjoint triangles, quadrilaterals, and seeded degree-two forbidden graphs at orders 4, 6, 8, 10, and 12. Selected four-vertex examples are independently re-enumerated over every edge-priority permutation; the exact one-deleted-edge formula and the telescoping reference product are tested separately.

These finite tests cannot certify the infinite-order asymptotic error. The proof in RESULT.md establishes it by deriving uniform survival moments, bounding the perturbation at each even residual size, and summing the telescoping error. The restriction to maximum forbidden degree two is used in both the continuation property and the uniform error estimate. Source comparisons assess best-known coverage, not independent priority certification.
