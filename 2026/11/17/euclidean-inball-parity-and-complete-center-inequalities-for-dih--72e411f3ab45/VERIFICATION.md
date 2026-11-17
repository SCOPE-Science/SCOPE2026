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

# Computational verification

Run `python verify.py` with Python 3, NumPy and SciPy available. No external files are used.

The program exhaustively enumerates the cube-section vertices in dimensions \(3\) through \(12\) using exact integer arithmetic, computes their cyclic difference energies, and checks the exact maximizing configurations and counts. It separately constructs the original \(2n\) orbit points in ambient Euclidean coordinates for dimensions \(3\) through \(8\), computes convex hulls, deduplicates triangulated facet planes, and checks the claimed distances, active-facet multiplicities and active-normal ranks. In even order it additionally constructs a small nonzero center offset orthogonal to active facet normals and checks every facet inequality.

Observed execution output:

```text
PASS: 4850 exact cube-section vertices and 305 independent Euclidean/facet checks
Verified n=3..12 for exact centered-cube optimization, n=3..8 for Euclidean hull facets and active-normal ranks.
```

These tests do not prove claims for unbounded dimensions. The written proof gives exact reductions, finite equality classification, and Fourier spanning argument for every \(n\ge3\). Floating-point convex-hull calculations are only corroboration, while the energy enumeration is exact but finite.

Independent audit: not performed.
