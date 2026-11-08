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

The derivation is exact for every finite poset. It reduces ellipsoid containment to a family of chain-sum inequalities, checks a width-sensitive feasible diagonal ellipsoid, and proves global roundness by a chain partition plus AM--GM. The comparison volume is computed directly from the squared coordinate semiaxes and the binary relative entropy identity. The layered equality cases follow from exact concave maximization.

The accompanying self-contained `verify.py` was run with Python 3. It enumerated 1,099 acyclic presentations on up to five elements, including 89 cases with \(n=hw\), and checked the rational feasibility and chain-partition implications. It separately checked nine layered examples. This finite testing is corroborative and does not prove the universal assertions. No independent mathematical audit has been performed.
