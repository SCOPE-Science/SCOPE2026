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

# Reproducible checks and limits

Run `python3 mixed_polygon_verify.py` with Python 3. The script uses only the Python standard library and constructs regular polygons, convex hulls of vertex pair sums, and membership witnesses. It also samples nonsimilar, finite-faceted, rotationally symmetric convexifiers made as Minkowski sums of rotated regular polygons. Locally observed output:

```text
MIXED_REGULAR_POLYGON_TESTS_OK 61438
N_FOLD_SYMMETRIC_CONVEXIFIER_TESTS_OK 82508
```

The supplementary checks include conditions at the proposed threshold, strict violations of the face or center obstruction below threshold, and loss of facet alignment. All mathematical statements for arbitrary real dilation and all compact symmetric convex bodies rely on the exact exposed-face/radial argument in `RESULT.md` rather than any finite numerical tests. The tests are floating-point, so the verification output alone is not a formal or exhaustive certificate. No independent audit has been performed.
