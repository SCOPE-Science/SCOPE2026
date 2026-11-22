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

# Reproducible calculation

Run `python3 verify_gp_covers.py` using Python 3 and no external packages. The script exactly constructs both twenty-vertex generalized Petersen graphs, compares independent shortest-path computations, enumerates every geodesic-forbidden triple and admissible simplex, checks face closure and squared-zero boundaries, and computes exact mod-two ranks by independent row and column elimination. Both graph calculations and the quotient involution checks completed with `ALL CHECKS PASS`.

The complete face vectors are \((20,190,600,550,60)\) and \((20,190,420,370,60)\). Their ranks for \(\partial_1,\ldots,\partial_4\) are \((19,161,379,60)\) and \((19,131,289,60)\). The resulting reduced Betti vectors in dimensions zero through four are \((0,10,60,111,0)\) and \((0,40,0,21,0)\). These exact finite computations establish only mod-two homology; no integral or homotopy claim is supported by these certificates.
