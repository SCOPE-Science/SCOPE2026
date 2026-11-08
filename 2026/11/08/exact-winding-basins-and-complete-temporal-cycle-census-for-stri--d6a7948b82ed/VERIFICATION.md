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

The supplementary `verify.py` uses only Python standard-library modules. It has been run from the file path supplied in the complete research package and reported `VERIFY_OK exhaustive_n=4..10 direct_2d_n=4..6 roots_unity_n=1..100 six_wall_L7=True`.

The script exhaustively visits every row word at each length from 4 through 10, independently checks exact two-dimensional Moore dynamics at lengths 4 through 6, reconstructs each eventual temporal cycle and winding sector, and compares all integer outputs to the claimed analytic formulas. Exact finite arithmetic also checks the length-seven six-wall example and roots-of-unity identity for lengths 1 through 100.

The all-length assertion depends on the mathematical proof in `RESULT.md`, not on finite enumeration. Prior-work access remains incomplete for certain older general cycle-count papers. Independent scientific validation has not been performed.
