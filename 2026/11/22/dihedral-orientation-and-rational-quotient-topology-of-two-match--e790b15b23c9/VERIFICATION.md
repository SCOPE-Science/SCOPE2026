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

The mathematical proof identifies all minimal nonfaces, constructs a complete acyclic matching on the invariant facet complement, and determines the top homology action from the orientation of the remaining rim simplex. The quotient's rational homology uses the finite-group invariants theorem, not an assumption that the action is free. The ordinary homotopy equivalence obtained by collapsing the contractible complement is not asserted equivariantly.

Reproduce the finite checks using `python3 verify.py` with Python 3.8 or later; no dependencies are required. The checker constructs face bitmasks, verifies all \(2\)-matching conditions through allowed pendant subsets, pairs every face other than the unique full rim facet, independently computes signed simplicial Lefschetz numbers for rotation and reflection, and confirms that the full-rotation invariant face supports are exactly the empty face, full rim face and full pendant face.

Observed output (run on the included file):

```
n=3: faces=45, pairs=22, one critical rim face, r=+1, s=-1, full-rotation fixed S^0
n=4: faces=161, pairs=80, one critical rim face, r=-1, s=+1, full-rotation fixed S^0
n=5: faces=573, pairs=286, one critical rim face, r=+1, s=+1, full-rotation fixed S^0
n=6: faces=2041, pairs=1020, one critical rim face, r=-1, s=-1, full-rotation fixed S^0
n=7: faces=7269, pairs=3634, one critical rim face, r=+1, s=-1, full-rotation fixed S^0
n=8: faces=25889, pairs=12944, one critical rim face, r=-1, s=+1, full-rotation fixed S^0
FINITE_CHECKS_PASS
```

Limits: finite examples verify signs but do not establish the arbitrary-length theorem; that conclusion follows from the general proof. Integral homology of the ordinary orbit spaces beyond the rational statement remains uncomputed. An independent audit has not been performed.
