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

The standalone program `verify_bilinear_triangle.py` uses only the Python standard library. For the four inputs \((q,a,b)=(2,2,2),(2,2,3),(2,3,3),(3,2,2)\), it generates every vertex matrix, independently recognizes every rank-one increment by Gaussian row proportionality, constructs all graph adjacencies, enumerates each triangular face, and reduces the full triangular boundary columns over \(\mathbb F_2\). It asserts the exact closed formulas for vertex degree and triangle count, as well as first mod-two Betti number zero and second mod-two Betti number \(V-E+F-1\).

The recorded transcript in `verify_bilinear_triangle_output.txt` ends `BILINEAR_TRIANGLE_CHECKS_OK` and gives counts, ranks, and Betti numbers for all four cases. These are actual finite checks, not exhaustive verification of the infinite parameter set or of the integral homotopy equivalence. The latter follows from the edge-path presentation and Hurewicz–Whitehead argument in `RESULT.md`. The program checks prime fields of orders two and three, while the proof includes all finite-field extensions.
