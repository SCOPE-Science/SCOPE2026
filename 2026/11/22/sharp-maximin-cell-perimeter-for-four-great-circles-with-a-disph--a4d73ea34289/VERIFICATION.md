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

The mathematical claim and its hypotheses are specified in `RESULT.md`; the actual standalone code is `check_perimeter.py`. Run `python3 check_perimeter.py` using Python 3 with no third-party packages. The program reconstructs vertices as intersections of every pair of great-circle planes, selects each cell by four signed hemispheres, orders polygon vertices and sums shortest great-circle arcs. It does not use the area/dual formula to compute those arcs.

Observed output:

```text
PASS: 900 nondegenerate configurations; 14-cell polygon reconstructions, triangular sum, min bound, disphenoid equality and exact 3-quadrilateral formulas
```

The 500 disphenoid cases verify the exact formulas numerically, and 400 generic positive-dependent cases test the eight-triangle upper bound. The exact infinite proof is by incidence combinatorics, polar spherical geometry, a solved Gram system, and a rectangle solid-angle integral. Floating-point tests do not certify the theorem, uniqueness or historical novelty; those require the analytic proof and literature comparison in `RESULT.md` and `REVIEW.md`. Independent audit has not been performed.
