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

Run the three embedded `verification/check_*.py` scripts with Python 3 and no non-standard packages. `check_integral.py` independently enumerates all original faces, forms the signed orbit-cell boundaries, checks boundary composition, cancels 1,954 integral units, and checks the exact residual differentials. `check_modular.py` generates cells from row/column masks and independently reduces boundaries modulo two, three and five. `check_pi1.py` constructs the full one- and two-skeleton and eliminates all 244 non-tree fundamental-group generators by triangular relations. The execution must report all three success markers named in `RESULT.md`.

The resulting integral homology statement follows from the integer boundary reductions, not solely from modular ranks. The finite calculation is complete only for this order-three complex. No independent mathematical audit is represented.
