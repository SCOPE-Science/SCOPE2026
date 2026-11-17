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

# Reproduction

Run `python verify_cyclic_fixed_not3.py` with Python 3.9+; no external packages are required. The script reads no input files and independently constructs the circulant adjacency graph for each distance subset, testing connectivity after deleting one and two vertices. It checks 6,117 nonempty distance subsets at orders 4 through 22, including antipodal cases. It checks 327 prime-subfamily simplex intersections at graph orders 4 through 120, then the first mixed-dimensional case at order 30. The actual output is embedded in `verifier_output.txt`.

The verifier asserts actual graph connectivity, not merely matching Euler characteristics, but it is a **finite** test. The proof of all-parameter three-connectivity uses the pre-existing vertex-transitive connectivity theorem, not computational induction. The arithmetic nerve and isolated-vertex decomposition are proved in `RESULT.md`. No external auditor has verified the claim.
