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

# Verification

From a directory containing `verify_petersen_robust_puncture.py` and `verify_expected.txt`, run:

```
python3 verify_petersen_robust_puncture.py > actual.txt
cmp actual.txt verify_expected.txt
```

The program enumerates all nonempty faces from the definition of the graph complex, builds all full Hasse incidences, constructs deterministic coreduction pairs, independently checks the complete oriented Hasse graph for directed acyclicity, and calculates independent simplicial mod-two ranks. It is a complete finite certificate for the stated homotopy types, rather than a sample or a numerical extrapolation. The comparison with the expected output must exit successfully.

The integral inclusion statement follows from the long exact sequence of the pair consisting of the full complex and its induced vertex deletion, using the verified vertex-link wedge type. The symmetric-group action on two-element subsets of five symbols proves the claimed uniformity across all ten vertices. The checker is independent of the earlier total-cut calculation, while the known ambient rank agrees with it.

The proof does not compute higher puncture profiles or a canonical equivariant splitting. Publication novelty has not undergone independent exhaustive audit.
