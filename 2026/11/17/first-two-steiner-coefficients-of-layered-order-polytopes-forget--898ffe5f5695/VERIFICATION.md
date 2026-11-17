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

The standalone `verify_layered_order.py` needs Python with NumPy and SciPy. Run:

```bash
python verify_layered_order.py
```

Expected output from the supplied checker:

```text
LAYERED_STEINER_PASS profiles=16 ridges=1356 max_layers=5
```

The program constructs all vertices as binary order filters, enumerates every facet, tests every pair's common intersection for exact expected affine rank (with numerical tolerance), projects the face into its affine span, computes its Euclidean measure using convex hulls, and weights ridge measures by exterior normal angles. It independently sums all facet measures and compares them with the closed formulas. Profiles include unequal layer sizes and two through five layers.

The mathematical proof, rather than this finite experiment, establishes the statement for all integer layer sizes at least two. Floating-point affine ranks and convex-hull volumes should not be treated as formal certificates or as exhaustive infinite checks. The complete proof and exact Jacobian/multiplicity calculations are in `RESULT.md`.
