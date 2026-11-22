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

# Reproduction and limits

Run the two standard-library-only scripts directly beside `certificate.json`:

```
python3 verify.py
python3 burnside_check.py
```

The first reconstructs the exact graph, \(24\) symmetries, all \(162\) nonempty faces and \(3342\) barycentric flags. It forms all \(146\) orbit cells, checks \(60\) regular-cell elementary collapses against explicit ordered pairs, verifies the five-edge spanning tree, eight oriented attaching words and seven homotopy-preserving generator/relator cancellations, leaving one zero-cell and one two-cell. It prints `TRUNCATED_TETRA_ORBIT_SPHERE_OK`. The second independently computes the orbit-cell vector \((11,42,63,30)\) by Burnside counting and prints `BURNSIDE_OK`.

The checker is a complete finite certificate for this particular graph, not a formalized proof in a proof assistant. The mathematical passage from verified finite cell moves to the integral homotopy equivalence uses standard regular CW elementary collapses, contractible-tree contraction and elementary two-cell/one-cell cancellation. No independent mathematical audit is asserted.
