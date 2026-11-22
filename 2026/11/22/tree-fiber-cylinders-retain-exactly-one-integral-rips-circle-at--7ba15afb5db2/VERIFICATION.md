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

From this directory run `python3 verify_tree_cylinders.py` (only the Python standard library is required). Compare stdout to `verify_output.txt`; the script emits twenty `PASS` lines and the final `VERIFY_OK` line. For each instance the script enumerates every flag simplex directly from the Cartesian shortest-path metric, checks complete three-column carrier coverage, dismantles all three possible strip widths by finding dominated graph-power vertices, computes mod-two chain ranks in every dimension and checks mod-two linear independence of all product square boundaries.

The exact integral and infinite-family claims require the written induction, nerve-lemma argument and cellular chain argument in `RESULT.md`. The finite tests do not establish integral torsion-freeness or infinite-range assertions by themselves. The graph's radius-one face complex is triangle-free and the product-square subgroup is an integral cellular boundary image, so its primitivity follows from the contractible-tree product, not from the mod-two certificate. There is no independent audit.
