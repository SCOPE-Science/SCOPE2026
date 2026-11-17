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

# Verification record

The analytical verification independently checks the input/output variation normalization, line-graph wedge multiplicity, graph coarea, boundary-neighbor equality condition, and matching bridge-cut tree extremizers. The first nontrivial dimension is five, where a five-vertex star and a complete graph both have sharp amplification \(3/2\); the universal ceiling rules out smaller strict amplification.

The included `verify.py` script uses only Python 3's standard library and computes exact rational values. Its completed run produced:

```
CONNECTED_GRAPHS_N 2 PASS
CONNECTED_GRAPHS_N 3 PASS
CONNECTED_GRAPHS_N 4 PASS
CONNECTED_GRAPHS_N 5 PASS
EXACT_CUT_WEDGE_AND_RIGIDITY_PASS 771 11199
TREE_DEGREE_FORMULA_PASS 145
PATH_STAR_COMPLETE_CYCLE_CROSSCHECK_PASS
ALL_MIDPOINT_LIFT_EXACT_CHECKS_PASS
```

The script checks 771 connected labeled graphs and 11,199 complement-identified nonempty cut cases on orders two through five; checks 145 labeled trees; and tests the explicit path, star, cycle, and complete-graph values through order twelve. Computation is finite, not proof of the unrestricted theorem. The analytical proof in `RESULT.md` supplies the all-dimensional justification. Independent mathematical audit has not been performed.
