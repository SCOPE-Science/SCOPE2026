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
Run `python3 check_cluster_inball.py` using only the Python standard library. The checker represents distances and heights as exact `fractions.Fraction` objects, enumerates signed spanning trees of the complete constraint graph independently of the theorem's predicted vertices for fifteen small parameter cases, and compares all recovered vertices against the proposed subset-height classification. It then validates every centered squared Euclidean normal, the contact multiplicity, the minimizing-integer rule, and the rational rank of the active contact-normal matrix.

Expected final success lines:

```
SIGNED_SPANNING_TREE_COMPLETE_VERTEX_ENUMERATION_PASS cases= 15 total_vertices= 450
PARITY_STAIRCASE_AND_EXACT_CENTER_RANK_PASS
SINGLE_CLUSTER_ULTRAMETRIC_INBALL_ALL_CHECKS_PASS
```

The signed-tree census covers rational parameter samples and cluster sizes three through five; additional exact-rational subset/rank tests cover sizes three through eight and several tie boundaries. Neither test range is an infinite certificate. The universal assertion rests on the proof by full vertex classification, exact quadratic optimization and contact-normal spanning. Independent audit and external certification have not been performed.
