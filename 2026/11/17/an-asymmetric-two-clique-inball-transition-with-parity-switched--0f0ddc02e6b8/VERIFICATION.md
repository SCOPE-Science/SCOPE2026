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

From the directory containing the standalone checker, run:

```sh
python3 verify.py
```

No packages beyond the Python 3 standard library are needed. The checker independently enumerates all nonempty signed binary patterns per blade and evaluates the integer numerator of every squared polar-vertex norm. It compares exact maximum norms, maximizing-support descriptions, binomial tangent-facet counts, and center-span ranks to the theorem. For small cases, a separate ternary exhaustive inequality enumeration and tight-edge graph connectivity test reproduce the complete vertex set rather than assuming the product description; exact rational row reduction verifies rank. The 1,485 additional parameter checks evaluate the strict and tied integer quadratics directly.

Expected complete output:

```text
EXACT_POLAR_PRODUCT_MAX_CONTACT_PASS cases=17 checked_vertices=2176596
INDEPENDENT_TIGHT_EDGE_GRAPH_AND_CENTER_RANK_PASS
INTEGER_QUADRATIC_THRESHOLD_EXACT_PASS profiles=1485
TWO_CLIQUE_INBALL_AND_INCENTER_ALL_CHECKS_PASS
```

These are finite rational checks, not a proof of all integer sizes or a demonstration of historical originality. The general proof in `RESULT.md` supplies the all-parameter argument. The statuses in this file do not assert independent validation.
