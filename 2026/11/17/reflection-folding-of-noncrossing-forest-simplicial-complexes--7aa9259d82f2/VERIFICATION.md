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

# Reproducibility and scope

Execute `python3 verify_folding.py` in a clean Python 3 environment. The script needs only the Python standard library and emits `NONCROSSING_FOREST_REFLECTION_FOLDING_PASS` on success.

It checks admissible edge-orbit completeness and the equivalence of all pairwise crossing relations for \(m=2,\ldots,12\). It also enumerates **all** subsets of the smaller complete graph for \(m=2,\ldots,6\), compares forest status of every subset with that of its reflected lift, and constructs complete noncrossing-forest face vectors for small polygons up to eight vertices. The count formula is checked exactly by integer arithmetic. `verification_output.txt` is the captured actual script output.

No finite test certifies the universal PL claim; that claim rests on the explicit orbit bijection, crossing test, forest-lift characterization and barycentric fixed-coordinate argument in `RESULT.md`. No independent audit or automated formal theorem proving was performed.
