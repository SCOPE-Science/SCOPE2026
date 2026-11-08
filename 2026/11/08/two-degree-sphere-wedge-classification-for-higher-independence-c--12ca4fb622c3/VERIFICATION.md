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

# Mathematical verification

The script `verify_subdivided_stars.py` is a standalone Python 3 program requiring only the standard library. Run `python3 verify_subdivided_stars.py` beside this document. It constructs the adjacency bitmasks directly from the definition, enumerates the permitted faces by induced connected components, and independently forms each augmented simplicial boundary over \(\mathbb F_2\). Bitset Gaussian elimination computes exact reduced homology ranks. It compares these ranks with the two binomial multiplicities (and the \(r=1\) and full-simplex boundary cases) for 117 parameter triples with \(1\leq a,b\leq4\), \(a+b\leq7\), and all \(1\leq r\leq a+b+3\). Recorded output:

```
ALL_VERIFY_OK cases=117 total_face_instances=36352
```

This is a finite consistency check, not a proof of infinite-parameter homotopy or integral torsion-freeness. The latter follow from the explicit contractible-base double-star attachment, the star skeleton calculation, the exact link identity after middle-vertex deletion, and the nullhomotopic cofiber decomposition documented in `RESULT.md`. Those arguments include \(r=1\), \(r=2\), vanishing binomial multiplicities, and \(r\geq a+b+3\).
